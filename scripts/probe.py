#!/usr/bin/env python3
"""campus-licensed.yaml 探测脚本

对规则文件里的每个域名做真实 HTTP(S) 验证：
  1. 用指定 DNS 解析真 IP（绑定源地址，避免拿到代理的 fake-ip / 走错出口）
  2. curl --resolve 锁定该 IP 发请求，同时校验证书链（证书不匹配会失败）
  3. 记录 HTTP 状态码；000 视为不可达，会重试一次

为什么用 curl 而不是裸 TLS：Cloudflare 之类的 Bot 防护会掐掉缺少 ALPN/h2
的裸握手，只有真实 HTTP 客户端才能反映"浏览器能不能打开"。

用法：
  # 在校园网机器上跑（绑定校园出口地址 + 校内 DNS）
  python3 scripts/probe.py --src 10.19.75.204 --dns 10.15.44.11

  # 在任意机器上跑（只验证域名存活与证书）
  python3 scripts/probe.py
"""
import argparse
import concurrent.futures as cf
import json
import os
import re
import subprocess
import sys
import time

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
DEFAULT_RULES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "campus-licensed.yaml")


def load_rules(path):
    out = []
    for line in open(path, encoding="utf-8"):
        m = re.match(r"^-?\s*(DOMAIN-SUFFIX|DOMAIN)\s*,\s*([^,\s]+)", line.strip())
        if m:
            out.append((m.group(1), m.group(2)))
    return out


def resolve(host, dns, src):
    cmd = ["dig", "+short", "+time=3", "+tries=1", "A", host]
    if src:
        cmd[1:1] = ["-b", src]
    if dns:
        cmd.append("@" + dns)
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=10).stdout
    except Exception:
        return None
    ips = [l.strip() for l in out.splitlines()
           if l.strip() and not l.strip().endswith(".") and l.strip()[0].isdigit()]
    ips = [i for i in ips if not i.startswith("198.18.")]
    return ips[0] if ips else None


def http(host, ip, src, timeout):
    cmd = ["curl", "-sS", "-o", "/dev/null"]
    if src:
        cmd += ["--interface", src]
    cmd += ["-m", str(timeout), "-A", UA,
            "--resolve", "%s:443:%s" % (host, ip),
            "-w", "%{http_code} %{ssl_verify_result}",
            "https://%s/" % host]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 5)
    except subprocess.TimeoutExpired:
        return "000", 1
    parts = (p.stdout.strip() or "000 1").split()
    code = parts[0]
    verify = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 1
    return code, verify


def one(host, src, dns, timeout):
    ip = resolve(host, dns, src)
    if not ip:
        return host, "dns-fail", None
    code, verify = http(host, ip, src, timeout)
    if code == "000":
        code, verify = http(host, ip, src, timeout)      # 重试一次
    if code == "000":
        status = "unreachable"
    elif verify != 0:
        status = "cert-error"
    else:
        status = "HTTP " + code
    return host, status, ip


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", default=DEFAULT_RULES)
    ap.add_argument("--src", default="", help="绑定源地址（校园出口 IP）")
    ap.add_argument("--dns", default="", help="指定 DNS，如 10.15.44.11")
    ap.add_argument("--timeout", type=float, default=15)
    ap.add_argument("--jobs", type=int, default=8)
    ap.add_argument("--json", default="")
    args = ap.parse_args()

    hosts = sorted({d for _, d in load_rules(args.file)})
    if not hosts:
        sys.exit("没有从 %s 里解析到域名" % args.file)

    t0 = time.time()
    with cf.ThreadPoolExecutor(max_workers=args.jobs) as ex:
        rows = list(ex.map(lambda h: one(h, args.src, args.dns, args.timeout), hosts))
    bad = [r for r in rows if r[1] in ("unreachable", "dns-fail", "cert-error")]

    print("| 域名 | 结果 | IP |")
    print("|---|---|---|")
    for h, s, ip in rows:
        print("| `%s` | %s | `%s` |" % (h, s.replace("|", "\\|"), ip))
    print("\n共 %d 条：通过 %d，异常 %d，用时 %.0fs" % (len(rows), len(rows) - len(bad), len(bad), time.time() - t0))
    if bad:
        print("\n异常条目：")
        for h, s, ip in bad:
            print("  - %-40s %-12s %s" % (h, s, ip))
    if args.json:
        json.dump({"src": args.src, "dns": args.dns, "checked_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                   "results": {h: {"status": s, "ip": ip} for h, s, ip in rows}},
                  open(args.json, "w"), ensure_ascii=False, indent=1)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
