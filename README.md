# clash-academic-direct

> 校园网（机构 IP）认证型学术资源 → 强制直连的 Clash / mihomo 规则集。
> 一句话：**别让代理把你从"校内用户"变成"校外用户"。**

## 这个仓库解决什么问题

IEEE Xplore、ScienceDirect、Springer、Web of Science、ACM 这类库，授权依据不是账号，而是**你的来源 IP 是否属于订阅机构**。开着全局代理访问时，对方看到的是机房 IP，于是：

- 明明学校买了库，却提示要付费 / 要登录 / 无权限；
- 或者能进首页，下 PDF 时被拦。

主流模板（含 ACL4SSR、Aethersailor 等）把这类域名统一归到 `category-scholar-!cn` 走代理——这对 arXiv、Google Scholar 是对的（它们在国内本来就不通），但对 IP 认证的库是反向操作：**分类里混了两种需求相反的东西**。

这个仓库把"IP 认证型"单独捞出来，做成可以直接订阅的 rule-provider，插在学术分类之前。

## 订阅地址

```
https://raw.githubusercontent.com/Ergo042/clash-academic-direct/main/campus-licensed.yaml
https://cdn.jsdelivr.net/gh/Ergo042/clash-academic-direct@main/campus-licensed.yaml
```

国内拉 jsdelivr 更稳；jsdelivr 有 CDN 缓存，更新后最多延迟十几分钟。规则文件是纯文本，不需要 Pages。

## 用法

### 1. Clash / mihomo / Clash.Meta（含 Clash Verge、CMFA、ClashX Meta）

```yaml
rule-providers:
  campus-licensed:
    type: http
    behavior: classical
    format: yaml
    url: "https://cdn.jsdelivr.net/gh/Ergo042/clash-academic-direct@main/campus-licensed.yaml"
    path: ./ruleset/campus-licensed.yaml
    interval: 86400

rules:
  # 必须排在学术分类（category-scholar-!cn / GEOSITE 学术）之前
  - RULE-SET,campus-licensed,🎓 校园直连
  # ... 之后才是
  - GEOSITE,category-scholar-!cn,🚀 代理
```

顺便建议在 proxy-groups 里建一个**可切换**的组，而不是直接写 `DIRECT`：

```yaml
proxy-groups:
  - name: "🎓 校园直连"
    type: select
    proxies: [DIRECT, 🚀 节点选择]   # 默认 DIRECT；放假回家手动切到代理
```

好处是：在校外时不用改规则，点一下就能让这些库走代理，回家照常查文献。

### 2. OpenClash

把上面 `rule-providers` 与 `rules` 两段分别并进 `/etc/openclash/config/<你的配置>.yaml`。注意 OpenClash 启动时会重写 provider 的 `path`（强制进 `./rule_provider/`），所以 path 写什么都无所谓，**但规则位置很重要**：必须在学术分类之前。

### 3. 不想用 provider

`campus-licensed.yaml` 的 `payload:` 下面就是标准规则行，复制粘贴到你配置 `rules:` 的最前面即可。

## 收录标准

**收**：授权依赖来源 IP 的订阅型资源 —— 出版社全文库、文摘索引平台、学会期刊、电子书平台、法律/财经数据库、中文库。

**不收**：

| 类型 | 例子 | 原因 |
|---|---|---|
| 开放获取 | arXiv、bioRxiv、PLOS、MDPI、Frontiers、Zenodo | 不需要 IP 身份，直连没收益，反而可能更慢 |
| 被墙 / 不可达 | brill.com、galegroup.com、morganclaypool.com、jneurosci.org、westlawchina.com、lawdata.com.tw、t21.nikkei.co.jp、icsd.fiz-karlsruhe.de、myilibrary.com | 直连根本连不上，硬直连等于让它废掉 |
| 已废弃 / 无 A 记录 | springerlink.com、els-cdn.com、silverchair-cdn.com、aspbjournals.org 等 | 域名已不再服务 |
| 侵权镜像 | sci-hub、z-library | 不提供 |
| 校内网段 | `10.0.0.0/8` 之类 | 出校无意义，且泄露拓扑；校园网内用 `GEOIP,lan` 就够 |

## 实测

全部条目在上海科技大学校园网出口 `10.19.75.204` 上逐条验证，方法是：

1. 用**校内 DNS（10.15.44.11）** 解析，避免拿到代理软件的 fake-ip；
2. 连接时**绑定校园源地址**（配合 policy route 走教育网出口，绕开默认路由）；
3. TLS 握手后**比对证书 SAN 与域名** —— 这一步能识别 DNS 投毒：被投毒时证书必然不匹配。

结果：**候选 142 条 → 通过 121 条**，明细见 [`docs/resources.md`](docs/resources.md)（含每条实测状态与解析 IP）。剔除的 21 条及原因见上表。

这 121 条里：

- **109 条**原本落在 `category-scholar-!cn`，即正被模板送进代理——本仓库对它们真正起作用；
- 4 条（知网、万方、维普、北大法宝）本就在 `category-scholar-cn`，走直连，加进来只是显式化；
- 8 条（SpringerOpen、AIP、SPIE、ASCE、AMS 气象、JBC、Liebert、IMF）不在任何 scholar 分类里，属于补漏。

> 注意：能直连 ≠ 你有权限。学校买了哪些库、认不认你的 IP 段，因校而异；本仓库只保证"这些域名在校内网可以直连访问"。

## 和现有方案的区别

| 项目 | 规模 | 状态 | 可用性 |
|---|---|---|---|
| [shxiaj/Clash-paperRule](https://github.com/shxiaj/Clash-paperRule) | 18 条 | 2025-05 停更 | 规则写在 README，混入 `DOMAIN-KEYWORD,microsoft/office/docs` 等宽关键词 |
| [microa/Clash-rules-for-academic](https://github.com/microa/Clash-rules-for-academic) | 12 条 | 2023-05 停更 | 目标组写死为 `Domestic`，复制到自己配置里会因组名不存在而报错 |
| [SherlockChiang/direct2academic](https://github.com/SherlockChiang/direct2academic) | 21 条 | 2026-01 | v2rayN 路由 JSON，格式不通用于 Clash |
| **本仓库** | **121 条** | 维护中 | 可直接订阅的 `behavior: classical` provider，逐条实测 + 每周自动巡检 |

## 自动巡检

`.github/workflows/probe.yml` 每周一跑一次：在 GitHub runner 上解析 + TLS 验证每个域名，报告存为 artifact，出现失效域名则任务失败（会给我发邮件提醒）。

注意：runner 在国外，它验证的是"域名还活着、证书还对得上"，**不代表校内可达性**；校内可达性只能在校内网自己跑：

```bash
python3 scripts/probe.py --file campus-licensed.yaml --src 10.19.75.204 --dns 10.15.44.11
```

## 许可

MIT。规则数据来自公开的 GeoSite / ACL4SSR 分类线索，加上人工筛选与实测。
