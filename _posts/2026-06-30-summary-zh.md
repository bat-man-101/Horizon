---
layout: default
title: "Horizon Summary: 2026-06-30 (ZH)"
date: 2026-06-30
lang: zh
---

> 从 150 条内容中筛选出 10 条重要资讯。

---

1. [最高法院：地理围栏搜查令需受宪法保护](#item-1) ⭐️ 9.0/10
2. [vLLM v0.24.0 新增 MiniMax-M3 支持与 DeepSeek-V4 优化](#item-2) ⭐️ 8.0/10
3. [Fil-C 实现内存安全的上下文切换](#item-3) ⭐️ 8.0/10
4. [MiCA 截止日或迫使 1000 万欧盟加密用户离开平台](#item-4) ⭐️ 7.0/10
5. [纽约梅隆银行为机构客户添加 USDC 铸造与赎回服务](#item-5) ⭐️ 7.0/10
6. [英国拟降低稳定币资本缓冲，与欧盟 MiCA 规则分歧](#item-6) ⭐️ 6.0/10
7. [摩根大通支持加密法案，呼吁加强保障措施](#item-7) ⭐️ 6.0/10
8. [私钥泄露导致 160 亿美元加密黑客损失中的 40%](#item-8) ⭐️ 6.0/10
9. [摩根大通扩大区块链结算网络，助力银行跨境支付](#item-9) ⭐️ 6.0/10
10. [Breez SDK 实现比特币到稳定币跨 30 多条链支付](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [最高法院：地理围栏搜查令需受宪法保护](https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision) ⭐️ 9.0/10

美国最高法院裁定，地理围栏搜查令（要求科技公司提供特定区域内所有设备的位置数据）需要第四修正案的保护，这意味着执法部门必须基于可能原因获得搜查令。 这项里程碑式的裁决极大地限制了执法部门在没有个别嫌疑的情况下进行大规模位置监控的能力，为移动追踪无处不在的时代中的数字隐私树立了关键先例。 该案涉及一起银行抢劫案，谷歌提供了银行周围 150 米内 19 个账户的位置数据；法院认为，此类搜查在没有搜查令的情况下推定不合理。卡根大法官撰写了多数意见，引用了 2014 年 Riley 诉 California 案的判决。

hackernews · cdrnsf · 6月29日 15:54 · [社区讨论](https://news.ycombinator.com/item?id=48720924)

**背景**: 地理围栏搜查令，也称为反向位置搜查令，允许执法部门在特定时间段内搜索公司数据库中特定地理区域内的所有移动设备。第四修正案保护免受不合理的搜查和扣押，但自最高法院 2018 年 Carpenter 案裁决以来，其对数字位置数据的应用一直存在争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Geofence_warrant">Geofence warrant - Wikipedia</a></li>
<li><a href="https://www.congress.gov/crs-product/LSB11274">Geofence Warrants and the Fourth Amendment | Congress.gov | Library of Congress</a></li>
<li><a href="https://www.brennancenter.org/our-work/policy-solutions/fourth-amendment-digital-age">The Fourth Amendment in the Digital Age | Brennan Center for Justice</a></li>

</ul>
</details>

**社区讨论**: 评论者提到了 Paula Broadwell 案的历史类比，其中未经搜查令使用了 IP 地理定位，并质疑该裁决是否扩展到 Flock 摄像头等其他监控工具。一些人对巴雷特大法官加入异议表示惊讶，而另一些人则赞扬法院在意见中引用了来源。

**标签**: `#privacy`, `#supreme court`, `#geofence warrants`, `#fourth amendment`, `#digital rights`

---

<a id="item-2"></a>
## [vLLM v0.24.0 新增 MiniMax-M3 支持与 DeepSeek-V4 优化](https://github.com/vllm-project/vllm/releases/tag/v0.24.0) ⭐️ 8.0/10

vLLM v0.24.0 引入了对 MiniMax-M3 模型的支持，并对 DeepSeek-V4 进行了重大优化，包括 FlashInfer 稀疏索引缓存和预填充块规划。该版本还扩展了 Model Runner V2，新增了流式解析引擎，并集成了 DeepEP v2 以支持专家并行。 此版本显著扩展了 vLLM 的模型支持和推理性能，通过支持 MiniMax-M3 和 DeepSeek-V4 等前沿模型的高效部署，使 AI 社区受益。优化降低了延迟并提高了吞吐量，使大规模 LLM 服务更加实用。 此版本包含来自 256 位贡献者的 571 次提交，其中 77 位是新贡献者。关键技术新增包括 MiniMax-M3 的 MXFP4 支持、DeepSeek-V4 的集群协作 topK 内核，以及统一跨模型工具调用和推理解析的新流式解析引擎。

github · khluu · 6月29日 19:41

**背景**: vLLM 是一个开源的高吞吐量 LLM 推理引擎，广泛应用于生产环境。MiniMax-M3 是一个 428B 参数的多模态模型，支持 1M 上下文窗口；DeepSeek-V4 是一个 1.6T 参数的混合专家模型。FlashInfer 是一个用于 LLM 服务的核函数库，支持稀疏注意力模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.minimax.io/models/text/m3">MiniMax M3 - Coding & Agentic Frontier, 1M Context ...</a></li>
<li><a href="https://deepseek.ai/deepseek-v4">DeepSeek AI: R1 Reasoning, API & Local Deployment 2026</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#model optimization`, `#open source`, `#AI infrastructure`

---

<a id="item-3"></a>
## [Fil-C 实现内存安全的上下文切换](https://fil-c.org/context_switches) ⭐️ 8.0/10

Fil-C（一种内存安全的 C 语言实现）现已为 setjmp/longjmp 和 ucontext API 提供内存安全支持，使得上下文切换不会导致内存损坏。这包括栈帧验证和胖指针等新特性，以防止误用。 这一进展使得以内存安全的方式使用危险的上下文切换机制成为可能，这对系统编程、协程和纤程实现至关重要。它减少了 C 代码库中的一大类漏洞。 该实现包括编译器强制控制流完整性和能力模型检查。对 ucontext API 的支持自 0.680 版本起新增，用户必须从源码构建才能使用 setcontext、getcontext、makecontext 和 swapcontext。

hackernews · modeless · 6月30日 00:38 · [社区讨论](https://news.ycombinator.com/item?id=48727177)

**背景**: setjmp/longjmp 和 ucontext 是用于非局部跳转和上下文切换的 C API，但它们以不安全著称，因为它们可能破坏栈或违反内存安全。Fil-C 是一个内存安全的 C 环境，它使用自定义编译器和运行时来强制执行内存安全，而无需修改现有 C 代码。这项工作将 Fil-C 的安全保证扩展到了这些传统上危险的 API。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fil-c.org/context_switches">Memory Safe Context Switching - fil-c.org</a></li>
<li><a href="https://micrologics.org/blog/memory-safe-context-switching-implementing-setjmp-and-longjmp-in-fil-c">Memory-Safe Context Switching: Implementing setjmp and ...</a></li>
<li><a href="https://lwn.net/Articles/1042938/">Fil - C : A memory - safe C implementation [LWN.net]</a></li>

</ul>
</details>

**社区讨论**: 评论者赞赏了深入的技术分析，有人表示希望自己几个月前就能读到这篇文章。另一位指出 Boost 纤程使用了比 ucontext 更高效的机制，还有一位强调 setjmp/longjmp 的风险远不止内存安全。有人对栈帧祖先关系的方向提出了小修正。

**标签**: `#memory safety`, `#context switching`, `#systems programming`, `#C language`, `#security`

---

<a id="item-4"></a>
## [MiCA 截止日或迫使 1000 万欧盟加密用户离开平台](https://www.coindesk.com/business/2026/06/29/mica-july-1-deadline-could-leave-10-million-crypto-users-searching-for-a-new-platform-in-the-eu) ⭐️ 7.0/10

欧洲证券和市场管理局（ESMA）警告称，欧盟加密客户必须在 2026 年 7 月 1 日前通过 MiCA 授权的实体提供服务，不合规交易所退出市场可能导致 1000 万用户失去可用平台。 这一截止日可能重塑欧盟加密格局，迫使数百万用户迁移至合规交易所或面临服务中断，并为全球加密监管树立先例。 MiCA 法规（EU 2023/1114）为加密资产服务提供商制定了统一规则，要求授权和监管。不合规交易所必须在截止日前停止为欧盟客户提供服务。

rss · CoinDesk · 6月29日 15:03

**背景**: MiCA（加密资产市场）是一项全面的欧盟法规，旨在协调各成员国的加密资产规则，涵盖透明度、授权和消费者保护。该法规于 2023 年通过并分阶段实施，7 月 1 日的截止日是服务提供商的关键执法里程碑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Markets_in_Crypto-Assets">Markets in Crypto-Assets - Wikipedia</a></li>
<li><a href="https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica">Markets in Crypto-Assets Regulation (MiCA)</a></li>
<li><a href="https://eur-lex.europa.eu/EN/legal-content/summary/european-crypto-assets-regulation-mica.html">European crypto-assets regulation (MiCA) - EUR-Lex</a></li>

</ul>
</details>

**标签**: `#crypto regulation`, `#MiCA`, `#EU policy`, `#crypto exchanges`

---

<a id="item-5"></a>
## [纽约梅隆银行为机构客户添加 USDC 铸造与赎回服务](https://www.coindesk.com/business/2026/06/29/wall-street-s-bny-expands-stablecoin-services-for-institutions-starting-with-circle-s-usdc) ⭐️ 7.0/10

纽约梅隆银行扩展其数字资产托管平台，支持 Circle 的 USDC 稳定币，使机构客户能够直接通过该银行铸造、赎回、存储和转移 USDC。 此举标志着传统金融对稳定币采纳的重要一步，一家华尔街大行将美元支持的稳定币整合到其机构托管服务中，可能为更广泛的机构数字资产使用铺平道路。 USDC 是纽约梅隆银行数字资产托管平台支持的首个稳定币，该平台于 2022 年 10 月推出，最初支持比特币和以太坊。该银行还担任 USDC 储备的主要托管人，深化了与 Circle 的合作关系。

rss · CoinDesk · 6月29日 14:46

**背景**: 稳定币是旨在保持价值稳定的加密货币，通常与美元等法定货币挂钩。USDC 是由 Circle 发行的广泛使用的美元支持稳定币，其储备存放在受监管的金融机构中。纽约梅隆银行的数字资产托管平台允许机构投资者在受监管环境中将数字资产与传统资产一起持有。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tokenmetrics.com/usdc/news/bny-usdc-minting-institutional-custody/">BNY Adds USDC Minting To Institutional Custody Platform</a></li>
<li><a href="https://cryptobriefing.com/bny-mellon-usdc-digital-asset-custody/">BNY Mellon integrates USDC as first stablecoin on Digital Asset...</a></li>
<li><a href="https://americatokenization.com/entities/bny-mellon-digital/">BNY Mellon Digital Assets — The... — AMERICA TOKENIZATION</a></li>

</ul>
</details>

**标签**: `#stablecoins`, `#institutional finance`, `#crypto adoption`, `#BNY Mellon`, `#USDC`

---

<a id="item-6"></a>
## [英国拟降低稳定币资本缓冲，与欧盟 MiCA 规则分歧](https://www.coindesk.com/policy/2026/06/30/uk-to-lower-stablecoin-capital-buffers-undercutting-eu-s-mica-requirements) ⭐️ 6.0/10

英国金融行为监管局（FCA）提议将稳定币资本缓冲降至 1%，低于欧盟 MiCA 要求的 2%。 这一监管分歧可能使英国成为更具吸引力的稳定币发行中心，可能改变市场格局，影响全球稳定币监管标准。 该提议是在英国央行放弃限制稳定币价值之后提出的，并设定了 2027 年 2 月为加密公司获得 FCA 授权的截止日期。

rss · CoinDesk · 6月30日 10:08

**背景**: 稳定币是旨在保持价值稳定的加密货币，通常与美元等法定货币挂钩。资本缓冲是发行方必须持有的储备金，用于覆盖潜在损失并确保赎回稳定性。欧盟的 MiCA 法规自 2024 年起生效，对重要稳定币要求 2%的资本缓冲，而英国 FCA 现提议较低的 1%缓冲以促进创新。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.coindesk.com/policy/2026/06/30/uk-to-lower-stablecoin-capital-buffers-undercutting-eu-s-mica-requirements">UK's FCA lowers stablecoin capital buffers to 1% ... - CoinDesk</a></li>
<li><a href="https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica">Markets in Crypto-Assets Regulation (MiCA)</a></li>

</ul>
</details>

**标签**: `#cryptocurrency`, `#regulation`, `#stablecoin`, `#UK`, `#EU`

---

<a id="item-7"></a>
## [摩根大通支持加密法案，呼吁加强保障措施](https://www.coindesk.com/policy/2026/06/29/jpmorgan-backs-u-s-crypto-bill-but-warns-repeatedly-of-risks-in-digital-asset-framework) ⭐️ 6.0/10

摩根大通公开表示支持美国加密市场结构立法，同时反复警告数字资产相关风险，并强调需要强有力的保障措施。 这标志着一家大型传统金融机构对加密监管的谨慎接纳，可能影响国会辩论，并为银行如何参与数字资产树立先例。 摩根大通的支持正值国会持续努力建立联邦加密市场结构框架之际，该框架旨在明确监管管辖权和投资者保护。

rss · CoinDesk · 6月29日 17:31

**背景**: 加密市场结构规则是指定义数字资产如何分类、交易和监管的立法。近年来多届国会提出了多项法案，但均未成为法律。摩根大通的立场反映了传统金融对加密领域日益开放的态度，同时伴随着对风险的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://xerogravity.com/blog/crypto-market-structure-regulation-guide">Crypto Market Structure: A Complete Regulatory Guide</a></li>
<li><a href="https://www.congress.gov/crs_external_products/R/PDF/R48963/R48963.2.pdf">Cryptocurrency: Regulatory and Legislative Policy Issues</a></li>
<li><a href="https://www.theblock.co/learn/403749/what-is-crypto-market-structure">What Is Crypto Market Structure? A Guide to How Crypto ...</a></li>

</ul>
</details>

**标签**: `#cryptocurrency`, `#regulation`, `#finance`, `#blockchain`

---

<a id="item-8"></a>
## [私钥泄露导致 160 亿美元加密黑客损失中的 40%](https://www.coindesk.com/tech/2026/06/29/private-keys-not-smart-contracts-caused-40-of-crypto-s-usd16-billion-hack-losses-here-s-whats-being-done) ⭐️ 6.0/10

一份新报告显示，160 亿美元加密黑客损失中的 40%是由私钥泄露而非智能合约漏洞造成的。业界正在努力改进密钥管理解决方案。 这凸显了加密领域最大的安全风险不是代码漏洞，而是糟糕的密钥管理，影响所有用户和平台。改进密钥管理可以防止数十亿美元的损失，并增强对生态系统的信任。 2024 年，私钥泄露占被盗加密货币的 43%，使其不符合竞争性审计竞赛的资格。黑客通常使用钓鱼或社会工程手段窃取密钥，从而立即获得钱包的完全访问权限。

rss · CoinDesk · 6月29日 15:45

**背景**: 私钥就像密码，可以完全控制加密钱包。如果被盗，资金可以立即被转出。密钥管理涉及安全地生成、存储和使用密钥，但许多用户和平台未能正确做到这一点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.trailofbits.com/2025/06/25/maturing-your-smart-contracts-beyond-private-key-risk/">Maturing your smart contracts beyond private key risk -The Trail of...</a></li>
<li><a href="https://www.ccn.com/education/crypto/private-key-theft-in-minutes-darkweb-business/">Hackers Can Now Steal Your Private Key in Minutes — Here’s How</a></li>
<li><a href="https://www.visualcapitalist.com/sp/in02-crypto-theft-top-ten-techniques/">Crypto Theft: The Top 10 Techniques Hackers Use | Visual Capitalist</a></li>

</ul>
</details>

**标签**: `#cryptocurrency`, `#security`, `#private keys`, `#hacks`

---

<a id="item-9"></a>
## [摩根大通扩大区块链结算网络，助力银行跨境支付](https://www.coindesk.com/business/2026/06/29/j-p-morgan-broadens-blockchain-settlement-network-as-banks-modernize-cross-border-payments) ⭐️ 6.0/10

摩根大通扩大了其 Kinexys 区块链结算网络，以推动银行跨境支付现代化，实现基于许可链的近乎实时结算。 此次扩张标志着机构对区块链在核心银行业务中的应用日益接受，有望将结算时间从数天缩短至数分钟，并降低跨境交易成本。 该网络使用摩根大通运营的许可链，JPM Coin（JPMD）将原生接入 Canton Network，以实现与公共区块链的互操作性。

rss · CoinDesk · 6月29日 15:23

**背景**: 传统跨境电汇可能需要 3-5 个工作日且费用高昂。基于区块链的结算网络可提供近乎即时、全天候的结算，且成本更低。摩根大通的 Kinexys 平台是一个银行主导的区块链解决方案，用于可编程支付和资产代币化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.coindesk.com/business/2026/06/29/j-p-morgan-broadens-blockchain-settlement-network-as-banks-modernize-cross-border-payments">J.P. Morgan broadens Kinexys blockchain settlement network as banks modernize cross-border payments</a></li>
<li><a href="https://www.jpmorgan.com/kinexys/index">Kinexys: Enterprise Bank-Led Blockchain Solutions</a></li>
<li><a href="https://blog.digitalasset.com/news/digital-asset-and-kinexys-by-j.p.-morgan-bring-usd-jpm-coin-jpmd-natively-to-canton">Digital Asset and Kinexys by J.P. Morgan announce intention to bring USD JPM Coin (JPMD) natively to the Canton Network</a></li>

</ul>
</details>

**标签**: `#blockchain`, `#banking`, `#cross-border payments`, `#J.P. Morgan`

---

<a id="item-10"></a>
## [Breez SDK 实现比特币到稳定币跨 30 多条链支付](https://cointelegraph.com/news/breez-bitcoin-wallets-send-usdc-usdt-without-holding-stablecoins?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) ⭐️ 6.0/10

Breez 推出了新的 SDK 功能，允许开发者将比特币支付路由到超过 30 条区块链上的 USDC 和 USDT 收款方，而无需用户持有稳定币。 这一创新通过让用户直接使用比特币进行支付，简化了稳定币支付流程，弥合了比特币与更广泛的多链稳定币生态系统之间的鸿沟。它可能推动比特币支付在去中心化金融和日常交易中的采用。 该 SDK 是非托管的，意味着用户在交易过程中始终保留对资金的控制权。Breez 以其闪电网络基础设施闻名，此功能可能利用跨链路由技术实时将比特币转换为稳定币。

rss · CoinTelegraph · 6月29日 13:00

**背景**: 比特币主要是一种价值储存和交换媒介，但其波动性使其不太适合日常支付。USDC 和 USDT 等稳定币与法定货币挂钩，提供价格稳定性。Breez 的 SDK 允许开发者集成自动转换为稳定币的比特币支付，从而实现稳定价值转移，而用户无需管理多种资产。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cryptobriefing.com/breez-bitcoin-stablecoin-payments-30-blockchains/">Breez launches Bitcoin -to- stablecoin payments across 30 blockchains</a></li>
<li><a href="https://breez.technology/sdk/">Breez SDK | Add Bitcoin to Any App or Service</a></li>
<li><a href="https://en.coin-turk.com/breez-launched-direct-usdc-and-usdt-transfers-from-bitcoin-balances-across-more-than-30-blockchains/">COINTURK NEWS - Bitcoin , Blockchain and Cryptocurrency News...</a></li>

</ul>
</details>

**标签**: `#Bitcoin`, `#stablecoins`, `#payments`, `#SDK`, `#blockchain`

---