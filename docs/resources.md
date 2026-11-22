# 条目明细（校园网实测）

采集于 2026-11-22，从上海科技大学校园网出口 `10.19.75.204` 发起：校内 DNS(10.15.44.11) 解析真 IP → `curl --resolve` 锁定该 IP → TLS 证书链校验 + HTTP 请求。

`HTTP 403` 属于正常（站点对非浏览器 UA 做 Bot 防护，能返回状态码就说明网络可达、证书正确）。

| # | 规则 | 所属 / 说明 | 校内侧实测 | 解析 IP |
|---:|---|---|---|---|
| 1 | `DOMAIN-SUFFIX,aacrjournals.org` | AACR | HTTP 403 | `104.18.12.179` |
| 2 | `DOMAIN-SUFFIX,acs.org` | ACS 美国化学会 | HTTP 301 | `45.60.77.135` |
| 3 | `DOMAIN-SUFFIX,agu.org` | AGU | HTTP 403 | `104.18.31.254` |
| 4 | `DOMAIN-SUFFIX,aiaa.org` | AIAA | HTTP 403 | `141.193.213.21` |
| 5 | `DOMAIN-SUFFIX,aip.org` | AIP 美国物理联合会 | HTTP 301 | `166.117.56.54` |
| 6 | `DOMAIN-SUFFIX,alexanderstreet.com` | Alexander Street | HTTP 301 | `34.202.128.153` |
| 7 | `DOMAIN-SUFFIX,amdigital.co.uk` | Adam Matthew Digital | HTTP 301 | `52.223.14.85` |
| 8 | `DOMAIN-SUFFIX,ametsoc.org` | AMS 美国气象学会 | HTTP 301 | `172.66.156.88` |
| 9 | `DOMAIN-SUFFIX,ams.org` | AMS 美国数学会 | HTTP 301 | `104.18.29.217` |
| 10 | `DOMAIN-SUFFIX,annualreviews.org` | Annual Reviews | HTTP 301 | `104.18.25.141` |
| 11 | `DOMAIN-SUFFIX,apa.org` | APA PsycNET | HTTP 301 | `45.60.44.114` |
| 12 | `DOMAIN-SUFFIX,aps.org` | APS 美国物理学会 | HTTP 301 | `149.28.6.76` |
| 13 | `DOMAIN-SUFFIX,artstor.org` | ARTstor | HTTP 301 | `151.101.128.152` |
| 14 | `DOMAIN-SUFFIX,asce.org` | ASCE | HTTP 301 | `104.20.35.91` |
| 15 | `DOMAIN-SUFFIX,ascelibrary.org` | ASCE Library | HTTP 403 | `104.16.248.101` |
| 16 | `DOMAIN-SUFFIX,asm.org` | ASM 美国微生物学会 | HTTP 200 | `20.119.16.57` |
| 17 | `DOMAIN-SUFFIX,asme.org` | ASME | HTTP 301 | `20.120.9.155` |
| 18 | `DOMAIN-SUFFIX,asmedigitalcollection.asme.org` | ASME Digital Collection | HTTP 403 | `104.18.12.179` |
| 19 | `DOMAIN-SUFFIX,asminternational.org` | ASM International | HTTP 301 | `172.66.170.30` |
| 20 | `DOMAIN-SUFFIX,astm.org` | ASTM | HTTP 301 | `18.164.174.106` |
| 21 | `DOMAIN-SUFFIX,biologists.com` | Company of Biologists | HTTP 301 | `192.124.249.18` |
| 22 | `DOMAIN-SUFFIX,biomedcentral.com` | BMC | HTTP 301 | `151.101.40.95` |
| 23 | `DOMAIN-SUFFIX,bioone.org` | BioOne | HTTP 200 | `107.154.251.12` |
| 24 | `DOMAIN-SUFFIX,bloomsburycollections.com` | Bloomsbury Collections | HTTP 301 | `63.184.11.22` |
| 25 | `DOMAIN-SUFFIX,bloomsburydesignlibrary.com` | Bloomsbury Design Library | HTTP 301 | `52.57.222.71` |
| 26 | `DOMAIN-SUFFIX,bmj.com` | BMJ | HTTP 301 | `18.65.14.5` |
| 27 | `DOMAIN-SUFFIX,brepolis.net` | Brepols | HTTP 301 | `20.101.249.219` |
| 28 | `DOMAIN-SUFFIX,bvdinfo.com` | Orbis / BvD | HTTP 301 | `104.18.34.217` |
| 29 | `DOMAIN-SUFFIX,cairn.info` | Cairn | HTTP 403 | `185.34.32.93` |
| 30 | `DOMAIN-SUFFIX,cambridge.org` | Cambridge Core | HTTP 301 | `104.17.110.190` |
| 31 | `DOMAIN-SUFFIX,capitaliq.com` | S&P Capital IQ | HTTP 301 | `23.200.143.69` |
| 32 | `DOMAIN-SUFFIX,cas.org` | CAS SciFinder | HTTP 301 | `45.60.106.242` |
| 33 | `DOMAIN-SUFFIX,ceicdata.com` | CEIC | HTTP 301 | `54.230.70.38` |
| 34 | `DOMAIN-SUFFIX,cell.com` | Cell Press | HTTP 403 | `172.66.0.112` |
| 35 | `DOMAIN-SUFFIX,chemnetbase.com` | CRC Handbook | HTTP 302 | `104.16.26.102` |
| 36 | `DOMAIN-SUFFIX,clarivate.com` | Clarivate | HTTP 403 | `23.185.0.4` |
| 37 | `DOMAIN-SUFFIX,clinicalkey.com` | ClinicalKey | HTTP 301 | `52.73.19.162` |
| 38 | `DOMAIN-SUFFIX,cnki.net` | 中国知网 | HTTP 301 | `115.31.65.10` |
| 39 | `DOMAIN-SUFFIX,cqvip.com` | 维普 | HTTP 301 | `120.55.187.212` |
| 40 | `DOMAIN-SUFFIX,degruyter.com` | De Gruyter | HTTP 301 | `63.180.139.66` |
| 41 | `DOMAIN-SUFFIX,ebsco.com` | EBSCO | HTTP 301 | `13.33.183.54` |
| 42 | `DOMAIN-SUFFIX,ebscohost.com` | EBSCOhost | HTTP 301 | `23.185.0.3` |
| 43 | `DOMAIN-SUFFIX,electrochem.org` | ECS 电化学学会 | HTTP 301 | `20.127.233.4` |
| 44 | `DOMAIN-SUFFIX,elgaronline.com` | Edward Elgar | HTTP 202 | `3.163.158.111` |
| 45 | `DOMAIN-SUFFIX,elsevier.com` | Elsevier | HTTP 301 | `34.243.46.252` |
| 46 | `DOMAIN-SUFFIX,embase.com` | Embase 医学文摘 | HTTP 301 | `18.65.14.32` |
| 47 | `DOMAIN-SUFFIX,emerald.com` | Emerald | HTTP 302 | `172.66.167.1` |
| 48 | `DOMAIN-SUFFIX,ems-ph.org` | EMS Press | HTTP 301 | `92.43.218.122` |
| 49 | `DOMAIN-SUFFIX,engineeringvillage.com` | Engineering Village / Ei | HTTP 301 | `203.22.241.2` |
| 50 | `DOMAIN-SUFFIX,gale.com` | Gale | HTTP 200 | `54.237.182.128` |
| 51 | `DOMAIN-SUFFIX,heinonline.org` | HeinOnline | HTTP 301 | `173.225.61.242` |
| 52 | `DOMAIN-SUFFIX,icevirtuallibrary.com` | ICE Virtual Library | HTTP 301 | `20.246.173.94` |
| 53 | `DOMAIN-SUFFIX,ieee.org` | IEEE Xplore | HTTP 301 | `140.98.193.152` |
| 54 | `DOMAIN-SUFFIX,igi-global.com` | IGI Global | HTTP 429 | `150.171.110.108` |
| 55 | `DOMAIN-SUFFIX,imf.org` | IMF eLibrary | HTTP 403 | `104.116.243.99` |
| 56 | `DOMAIN-SUFFIX,infolinker.com.tw` | 汉珍数位 | HTTP 526 | `172.67.141.47` |
| 57 | `DOMAIN-SUFFIX,informs.org` | INFORMS | HTTP 301 | `104.26.7.206` |
| 58 | `DOMAIN-SUFFIX,iop.org` | IOP 英国物理学会 | HTTP 301 | `23.185.0.4` |
| 59 | `DOMAIN-SUFFIX,jamanetwork.com` | JAMA Network | HTTP 403 | `104.18.12.179` |
| 60 | `DOMAIN-SUFFIX,japanknowledge.com` | JapanKnowledge | HTTP 200 | `34.36.88.177` |
| 61 | `DOMAIN-SUFFIX,jbc.org` | JBC / ASBMB | HTTP 403 | `172.66.0.112` |
| 62 | `DOMAIN-SUFFIX,jstor.org` | JSTOR | HTTP 301 | `151.101.0.152` |
| 63 | `DOMAIN-SUFFIX,karger.com` | Karger | HTTP 403 | `104.18.12.179` |
| 64 | `DOMAIN-SUFFIX,kuke.com` | KUKE 数字音乐图书馆 | HTTP 200 | `60.205.130.221` |
| 65 | `DOMAIN-SUFFIX,lexisnexis.com` | LexisNexis | HTTP 301 | `138.12.4.23` |
| 66 | `DOMAIN-SUFFIX,liebertpub.com` | Mary Ann Liebert | HTTP 301 | `104.18.43.204` |
| 67 | `DOMAIN-SUFFIX,literatumonline.com` | Wiley/Atypon 平台 | HTTP 403 | `104.18.138.72` |
| 68 | `DOMAIN-SUFFIX,nature.com` | Nature | HTTP 301 | `151.101.40.95` |
| 69 | `DOMAIN-SUFFIX,nejm.org` | NEJM | HTTP 301 | `52.45.66.44` |
| 70 | `DOMAIN-SUFFIX,oecd-ilibrary.org` | OECD iLibrary | HTTP 403 | `151.101.67.10` |
| 71 | `DOMAIN-SUFFIX,opg.optica.org` | Optica Publishing | HTTP 302 | `65.202.222.45` |
| 72 | `DOMAIN-SUFFIX,optica.org` | Optica / OSA | HTTP 307 | `65.202.222.44` |
| 73 | `DOMAIN-SUFFIX,osapublishing.org` | OSA 旧平台 | HTTP 301 | `89.106.200.1` |
| 74 | `DOMAIN-SUFFIX,oup.com` | Oxford University Press | HTTP 301 | `75.2.119.185` |
| 75 | `DOMAIN-SUFFIX,ovid.com` | Ovid | HTTP 301 | `104.18.10.162` |
| 76 | `DOMAIN-SUFFIX,oxfordartonline.com` | Oxford Art Online | HTTP 301 | `18.64.67.36` |
| 77 | `DOMAIN-SUFFIX,oxfordbibliographies.com` | Oxford Bibliographies | HTTP 301 | `52.224.90.245` |
| 78 | `DOMAIN-SUFFIX,oxfordmusiconline.com` | Oxford Music Online | HTTP 301 | `18.64.67.117` |
| 79 | `DOMAIN-SUFFIX,physiology.org` | APS 生理学会 | HTTP 202 | `98.87.72.28` |
| 80 | `DOMAIN-SUFFIX,pkulaw.com` | 北大法宝 | HTTP 301 | `101.72.227.62` |
| 81 | `DOMAIN-SUFFIX,pnas.org` | PNAS | HTTP 403 | `104.18.33.155` |
| 82 | `DOMAIN-SUFFIX,projecteuclid.org` | Project Euclid | HTTP 200 | `107.154.79.145` |
| 83 | `DOMAIN-SUFFIX,proquest.com` | ProQuest | HTTP 301 | `165.215.200.228` |
| 84 | `DOMAIN-SUFFIX,reaxys.com` | Reaxys 化学 | HTTP 301 | `13.226.69.127` |
| 85 | `DOMAIN-SUFFIX,routledgehandbooks.com` | Routledge Handbooks | HTTP 301 | `104.18.43.77` |
| 86 | `DOMAIN-SUFFIX,rsc.org` | RSC 英国皇家化学会 | HTTP 403 | `162.159.140.121` |
| 87 | `DOMAIN-SUFFIX,rupress.org` | Rockefeller University Press | HTTP 403 | `104.18.12.179` |
| 88 | `DOMAIN-SUFFIX,sae.org` | SAE | HTTP 302 | `206.160.145.240` |
| 89 | `DOMAIN-SUFFIX,sagepub.com` | SAGE | HTTP 301 | `104.18.3.100` |
| 90 | `DOMAIN-SUFFIX,science.org` | Science / AAAS | HTTP 301 | `52.8.62.150` |
| 91 | `DOMAIN-SUFFIX,sciencedirect.com` | Elsevier ScienceDirect | HTTP 301 | `203.22.241.8` |
| 92 | `DOMAIN-SUFFIX,sciencemag.org` | Science 旧域名 | HTTP 301 | `52.8.62.150` |
| 93 | `DOMAIN-SUFFIX,scitation.org` | AIP Scitation 平台 | HTTP 200 | `20.85.172.21` |
| 94 | `DOMAIN-SUFFIX,scopus.com` | Scopus 文摘库 | HTTP 307 | `203.22.241.5` |
| 95 | `DOMAIN-SUFFIX,siam.org` | SIAM | HTTP 403 | `172.66.168.112` |
| 96 | `DOMAIN-SUFFIX,spie.org` | SPIE | HTTP 200 | `192.230.66.233` |
| 97 | `DOMAIN-SUFFIX,spiedigitallibrary.org` | SPIE Digital Library | HTTP 301 | `107.154.251.12` |
| 98 | `DOMAIN-SUFFIX,springer.com` | Springer | HTTP 301 | `151.101.40.95` |
| 99 | `DOMAIN-SUFFIX,springeropen.com` | SpringerOpen | HTTP 301 | `151.101.40.95` |
| 100 | `DOMAIN-SUFFIX,tandfonline.com` | Taylor & Francis | HTTP 403 | `172.64.148.133` |
| 101 | `DOMAIN-SUFFIX,taylorandfrancis.com` | T&F 主站 | HTTP 200 | `104.19.253.95` |
| 102 | `DOMAIN-SUFFIX,thelancet.com` | The Lancet | HTTP 403 | `162.159.140.114` |
| 103 | `DOMAIN-SUFFIX,thieme-connect.com` | Thieme Connect | HTTP 302 | `141.66.193.71` |
| 104 | `DOMAIN-SUFFIX,thieme-connect.de` | Thieme Connect (de) | HTTP 302 | `141.66.193.70` |
| 105 | `DOMAIN-SUFFIX,thieme.de` | Thieme | HTTP 301 | `91.208.107.242` |
| 106 | `DOMAIN-SUFFIX,tickdata.com` | Tick Data | HTTP 301 | `18.65.14.72` |
| 107 | `DOMAIN-SUFFIX,totalmateria.com` | Total Materia | HTTP 301 | `172.212.179.64` |
| 108 | `DOMAIN-SUFFIX,wanfangdata.com.cn` | 万方数据 | HTTP 200 | `122.115.55.103` |
| 109 | `DOMAIN-SUFFIX,webofknowledge.com` | WoS 旧域名 | HTTP 301 | `44.239.44.122` |
| 110 | `DOMAIN-SUFFIX,webofscience.com` | Web of Science | HTTP 302 | `32.185.15.94` |
| 111 | `DOMAIN-SUFFIX,westlaw.com` | Westlaw | HTTP 301 | `155.46.172.255` |
| 112 | `DOMAIN-SUFFIX,wiley.com` | Wiley Online Library | HTTP 301 | `104.18.12.232` |
| 113 | `DOMAIN-SUFFIX,worldscientific.com` | World Scientific | HTTP 301 | `104.26.3.222` |
| 114 | `DOMAIN,beck-online.beck.de` | Beck-Online | HTTP 302 | `185.5.82.160` |
| 115 | `DOMAIN,databank.worldbank.org` | World Bank DataBank | HTTP 200 | `172.64.145.25` |
| 116 | `DOMAIN,dl.begellhouse.com` | Begell Digital Library | HTTP 301 | `169.48.244.201` |
| 117 | `DOMAIN,elib.maruzen.co.jp` | Maruzen e-Book Library | HTTP 302 | `140.245.93.241` |
| 118 | `DOMAIN,firstsearch.oclc.org` | OCLC FirstSearch | HTTP 200 | `132.174.0.24` |
| 119 | `DOMAIN,muse.jhu.edu` | Project MUSE | HTTP 200 | `130.102.46.11` |
| 120 | `DOMAIN,t21ipau.nikkei.co.jp` | 日经 TELECOM IPAU | HTTP 200 | `13.197.26.149` |
| 121 | `DOMAIN,wrds-www.wharton.upenn.edu` | WRDS 沃顿 | HTTP 200 | `165.123.60.122` |

剔除（校园网内直连不可用）：`brill.com`、`galegroup.com`、`morganclaypool.com`、`jneurosci.org`（被墙/SNI 重置）、`westlawchina.com`、`lawdata.com.tw`、`t21.nikkei.co.jp`、`icsd.fiz-karlsruhe.de`、`myilibrary.com`、`hanzhen.xmulib.org`（不可达），以及 `airiti.com`、`airitilibrary.com`、`aspbjournals.org`、`database.asahi.com`、`els-cdn.com`、`ggsrv.com`、`sciencedirectassets.com`、`silverchair-cdn.com`、`ulrichsweb.serialservicesolutions.com`（无 A 记录/已停用）、`angle.com.tw`（证书不匹配）。
