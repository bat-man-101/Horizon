---
layout: default
title: "Horizon Summary: 2026-06-30 (ZH)"
date: 2026-06-30
lang: zh
---

> 从 131 条内容中筛选出 9 条重要资讯。

---

1. [最高法院裁定地理围栏搜查令需受宪法保护](#item-1) ⭐️ 9.0/10
2. [vLLM v0.24.0 新增 MiniMax-M3 支持并深度优化 DeepSeek-V4](#item-2) ⭐️ 8.0/10
3. [提议的 .self 顶级域名旨在促进自托管](#item-3) ⭐️ 8.0/10
4. [纽约梅隆银行扩大 USDC 稳定币服务](#item-4) ⭐️ 7.0/10
5. [英国降低稳定币资本缓冲，削弱欧盟 MiCA 要求](#item-5) ⭐️ 6.0/10
6. [私钥泄露导致 160 亿美元加密黑客损失中的 40%](#item-6) ⭐️ 6.0/10
7. [MiCA 截止日期或迫使 1000 万欧盟加密用户离开平台](#item-7) ⭐️ 6.0/10
8. [Breez SDK 实现比特币到稳定币跨 30 多条链的支付](#item-8) ⭐️ 6.0/10
9. [Vitalik Buterin：混淆技术或可实现链上隐私投票](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [最高法院裁定地理围栏搜查令需受宪法保护](https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision) ⭐️ 9.0/10

美国最高法院裁定，允许执法部门获取特定区域内所有设备位置数据的地理围栏搜查令，需受第四修正案的宪法保护。这项里程碑式的裁决于 2026 年 6 月 29 日作出，为大规模监控背景下的数字隐私确立了先例。 这项裁决显著限制了执法部门进行无证数字拉网式搜查的能力，保护了数百万被谷歌等科技公司收集位置数据的个人隐私。它强化了第四修正案对现代监控技术的适用性，可能影响自动车牌识别器等其他数据收集实践。 该案涉及一起银行抢劫案，谷歌提供了银行周围 150 米范围内 19 台设备的位置数据。法院认为，获取如此全面的位置历史构成第四修正案下的搜查，需要基于可能原因获得搜查令。

hackernews · cdrnsf · 6月29日 15:54 · [社区讨论](https://news.ycombinator.com/item?id=48720924)

**背景**: 地理围栏搜查令，也称为反向位置搜查令，允许执法部门向科技公司请求虚拟边界内所有设备的位置数据。第四修正案保护公民免受不合理搜查和扣押，最高法院此前在 Carpenter 诉美国案等案件中裁定，访问历史手机位置数据需要搜查令。该裁决将这一推理延伸至地理围栏搜查令。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Geofence_warrant">Geofence warrant - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者对该裁决表示强烈支持，有人将其与彼得雷乌斯事件中保拉·布罗德韦尔的识别进行历史类比，作为无需搜查令即可使用位置数据的例子。其他人则对 Flock 摄像头等其他监控技术的影响表示担忧，并指出阿利托和托马斯大法官持异议，巴雷特大法官加入了少数派。

**标签**: `#privacy`, `#supreme court`, `#geofence warrants`, `#digital rights`, `#law enforcement`

---

<a id="item-2"></a>
## [vLLM v0.24.0 新增 MiniMax-M3 支持并深度优化 DeepSeek-V4](https://github.com/vllm-project/vllm/releases/tag/v0.24.0) ⭐️ 8.0/10

vLLM v0.24.0 版本由 256 位贡献者提交了 571 次代码，新增了对 MiniMax-M3 模型的支持，并对 DeepSeek-V4 进行了重大性能优化，包括 FlashInfer 稀疏索引缓存和集群协作 topK 内核。 此版本显著扩展了 vLLM 的模型生态系统并提升了推理效率，使 MiniMax-M3 和 DeepSeek-V4 等前沿模型的用户能够获得更高的吞吐量和更低的延迟。 值得注意的技术改进包括：新的流式解析引擎用于统一工具调用/推理解析、Model Runner V2 默认支持量化模型，以及集成 DeepEP v2 实现专家并行。

github · khluu · 6月29日 19:41

**背景**: vLLM 是一个高性能、内存高效的大语言模型推理引擎，通过优化 KV 缓存管理和批处理等关键操作来降低延迟和内存占用。DeepSeek-V4 是一个混合专家模型，总参数量达 1.6 万亿；MiniMax-M3 则是一个多模态混合专家模型，支持 100 万 token 的上下文窗口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/docs/inference-endpoints/engines/vllm">vLLM · Hugging Face</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro">deepseek-ai/DeepSeek-V4-Pro - Hugging Face</a></li>
<li><a href="https://huggingface.co/MiniMaxAI/MiniMax-M3">MiniMaxAI/ MiniMax - M 3 · Hugging Face</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#DeepSeek-V4`, `#MiniMax-M3`, `#performance optimization`

---

<a id="item-3"></a>
## [提议的 .self 顶级域名旨在促进自托管](https://hccf.onmy.cloud/2026/06/21/reclaiming-our-digital-selves-hccfs-vision-for-a-human-centered-top-level-domain/) ⭐️ 8.0/10

一项关于新顶级域名 .self 的提案已发布，旨在通过向个人提供免费子域名来支持自托管。该倡议由 HCCF 领导，设想了一个以人为中心、具有严格反滥用政策的域名空间。 如果实施，.self 可能降低自托管门槛并促进去中心化互联网，但其成功取决于解决滥用预防和资金挑战。该提案引发了社区关于可行性和声誉管理的辩论。 该提案包括“每人一个免费域名”的模式，但批评者指出，在没有身份验证的情况下执行这一点很困难。正在讨论滥用预防机制，例如事后域名撤销和对非活跃域名的挑战系统。

hackernews · HumanCCF · 6月29日 19:49 · [社区讨论](https://news.ycombinator.com/item?id=48724230)

**背景**: 顶级域名是域名名称的最后一部分，例如 .com 或 .org。自托管是指个人运行自己的服务器来提供网站、电子邮件或其他服务，而不是依赖第三方提供商。.self 顶级域名旨在为自托管服务创建一个专用命名空间，可能提高可发现性和信任度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tldz.com/2026-gtld-guide-how-to-get-your-own-top-level-domain/">2026 gTLD Guide: How to Get Your Own Top-Level Domain</a></li>
<li><a href="https://www.hawkdive.com/apple-self-tld-self-hosting-troubleshooting/">Apple Devices and the New .self TLD: Self-Hosting Issues Fixed</a></li>

</ul>
</details>

**社区讨论**: 社区评论强调了对滥用和声誉的担忧，并与被诈骗者泛滥的 .tk 免费顶级域名相提并论。一些人建议使用声誉系统和挑战机制来缓解域名抢注，而另一些人则质疑免费顶级域名的财务可持续性。

**标签**: `#DNS`, `#self-hosting`, `#TLD`, `#decentralization`, `#community`

---

<a id="item-4"></a>
## [纽约梅隆银行扩大 USDC 稳定币服务](https://www.coindesk.com/business/2026/06/29/wall-street-s-bny-expands-stablecoin-services-for-institutions-starting-with-circle-s-usdc) ⭐️ 7.0/10

纽约梅隆银行升级了其数字资产托管平台，允许机构客户在受监管的银行环境中直接铸造、存储、转账和赎回 Circle 的 USDC 稳定币。 此举标志着机构对稳定币的采用日益增长，并连接了传统金融与数字资产，可能加速 USDC 在支付和结算中的主流应用。 该服务包括通过存入美元铸造 USDC、托管、转账以及赎回为法币，全部在 BNY 现有的受监管托管基础设施内完成，深化了 BNY 与 Circle 的合作关系。

rss · CoinDesk · 6月29日 14:46

**背景**: USDC 是由 Circle 发行的与美元挂钩的稳定币，1:1 由储备支持并可随时赎回。纽约梅隆银行作为华尔街主要托管银行，此前已是 USDC 储备的主要托管人，随后扩展至为客户提供铸造和赎回服务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://finance.biggo.com/news/0ba2d465-1f22-4869-9395-079606d20a8e">BNY Mellon Lets Institutional Clients Mint and Redeem USDC, Deepening Stablecoin Integration — BigGo Finance</a></li>
<li><a href="https://cointelegraph.com/news/bny-adds-usdc-minting-and-redemption-to-institutional-custody-platform">BNY adds USDC minting and redemption to institutional custody ...</a></li>
<li><a href="https://www.bny.com/corporate/global/en/solutions/platforms/digital-assets/digital-assets-custody.html">Secure Digital Asset Custody for Institutional Investors</a></li>

</ul>
</details>

**标签**: `#stablecoins`, `#institutional adoption`, `#crypto`, `#finance`, `#BNY Mellon`

---

<a id="item-5"></a>
## [英国降低稳定币资本缓冲，削弱欧盟 MiCA 要求](https://www.coindesk.com/policy/2026/06/30/uk-to-lower-stablecoin-capital-buffers-undercutting-eu-s-mica-requirements) ⭐️ 6.0/10

英国金融行为监管局（FCA）最终确定了加密规则，将稳定币发行商所需资本缓冲从稳定币总价值的 2%降至 1%，与欧盟更严格的 MiCA 规定产生分歧。 此举使英国相比欧盟对稳定币发行商更具吸引力，可能改变稳定币活动的中心，并影响全球监管标准。 FCA 将加密公司的授权截止日期定为 2027 年 2 月，较低的资本缓冲适用于新框架下的稳定币发行商。

rss · CoinDesk · 6月30日 10:08

**背景**: 稳定币是旨在维持稳定价值的加密货币，通常与美元等法定货币挂钩。资本缓冲是发行商必须持有的资金，用于覆盖潜在损失并保护用户。欧盟的《加密资产市场法规》（MiCA）自 2024 年 12 月起全面适用，要求重要稳定币持有 2%的资本缓冲。英国降低这一要求的决定代表了旨在促进创新的监管分歧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.electronicpaymentsinternational.com/news/uk-fca-lowers-planned-stablecoin-capital-buffer/">UK FCA lowers planned stablecoin capital buffer in final crypto rules</a></li>
<li><a href="https://en.wikipedia.org/wiki/Markets_in_Crypto-Assets">Markets in Crypto-Assets - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Stablecoin">Stablecoin - Wikipedia</a></li>

</ul>
</details>

**标签**: `#crypto regulation`, `#stablecoins`, `#UK policy`, `#MiCA`

---

<a id="item-6"></a>
## [私钥泄露导致 160 亿美元加密黑客损失中的 40%](https://www.coindesk.com/tech/2026/06/29/private-keys-not-smart-contracts-caused-40-of-crypto-s-usd16-billion-hack-losses-here-s-whats-being-done) ⭐️ 6.0/10

一份新报告显示，在总计 160 亿美元的加密黑客损失中，40%源于私钥泄露而非智能合约漏洞，这促使行业采取措施改进密钥管理。 这一发现将安全焦点从智能合约审计转向私钥保护，突显了一个影响个人用户和协议的关键漏洞。 攻击者通过钓鱼、恶意软件、社会工程和弱存储窃取私钥；一旦泄露，他们可以立即清空钱包和协议金库。

rss · CoinDesk · 6月29日 15:45

**背景**: 私钥是授予加密货币资产所有权和控制权的加密代码，类似于密码。智能合约是区块链上的自执行代码，其漏洞一直是主要安全问题。这份报告强调密钥管理同样甚至更为关键。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.coindesk.com/tech/2026/06/29/private-keys-not-smart-contracts-caused-40-of-crypto-s-usd16-billion-hack-losses-here-s-whats-being-done">Private keys, not smart contracts, caused 40% of crypto's $16 ...</a></li>
<li><a href="https://www.guardrail.ai/common-attack-vectors/private-key-compromises">Guardrail – Protect Your Wallet from Private Key Compromises</a></li>
<li><a href="https://www.ccn.com/education/crypto/private-key-security-vs-smart-contract-audits/">Private Key Security vs. Smart Contract Audits: What Matters ...</a></li>

</ul>
</details>

**标签**: `#cryptocurrency`, `#security`, `#private keys`, `#hacks`

---

<a id="item-7"></a>
## [MiCA 截止日期或迫使 1000 万欧盟加密用户离开平台](https://www.coindesk.com/business/2026/06/29/mica-july-1-deadline-could-leave-10-million-crypto-users-searching-for-a-new-platform-in-the-eu) ⭐️ 6.0/10

欧洲证券和市场管理局（ESMA）警告称，在 2026 年 7 月 1 日 MiCA 法规截止日期后，欧盟加密客户必须通过 MiCA 授权的实体提供服务，这可能使 1000 万用户找不到合规平台。 这一截止日期可能扰乱数百万欧盟加密用户的访问，并迫使币安等主要交易所重组其在欧盟的业务，对欧洲加密市场产生重大影响。 MiCA（加密资产市场法规）自 2024 年 12 月起全面适用，但过渡期将于 2026 年 7 月 1 日结束，此后所有加密服务提供商必须获得 MiCA 的完全授权。

rss · CoinDesk · 6月29日 15:03

**背景**: MiCA 是欧盟首个针对加密资产的全面监管框架，涵盖发行、服务提供和防止市场滥用。它旨在保护投资者、确保金融稳定，同时促进创新。ESMA 是负责执行 MiCA 规则的欧盟机构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Markets_in_Crypto-Assets">Markets in Crypto-Assets - Wikipedia</a></li>
<li><a href="https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica">Markets in Crypto -Assets Regulation (MiCA)</a></li>

</ul>
</details>

**标签**: `#crypto`, `#regulation`, `#EU`, `#MiCA`

---

<a id="item-8"></a>
## [Breez SDK 实现比特币到稳定币跨 30 多条链的支付](https://cointelegraph.com/news/breez-bitcoin-wallets-send-usdc-usdt-without-holding-stablecoins?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) ⭐️ 6.0/10

Breez 推出了一项新的 SDK 功能，允许开发者将比特币余额的支付路由到超过 30 条区块链上的 USDC 和 USDT 接收方，而无需用户持有稳定币。 这一创新连接了比特币和稳定币生态系统，使比特币持有者无需转换 BTC 即可使用稳定币进行交易，可能提升比特币在日常支付和 DeFi 中的实用性。 该 SDK 构建于原生比特币二层网络 Spark 之上，支持即时结算且无最低限额。它是非托管的，并已被超过 75 个团队采用。

rss · CoinTelegraph · 6月29日 13:00

**背景**: USDC 和 USDT 等稳定币广泛用于支付和 DeFi，但比特币持有者通常需要出售 BTC 才能获得它们。Breez SDK 的路由功能消除了这一步骤，允许通过闪电网络和跨链交换直接进行比特币到稳定币的支付。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cryptobriefing.com/breez-bitcoin-stablecoin-payments-30-blockchains/">Breez launches Bitcoin - to - stablecoin payments across 30 blockchains</a></li>
<li><a href="https://breez.technology/sdk/">Breez SDK | Add Bitcoin to Any App or Service</a></li>
<li><a href="https://coincentral.com/breez-launches-bitcoin-to-stablecoin-payments-without-holding-usdc-or-usdt/">Breez Launches Bitcoin - to - Stablecoin Payments Without Holding ...</a></li>

</ul>
</details>

**标签**: `#Bitcoin`, `#stablecoins`, `#payments`, `#SDK`, `#blockchain`

---

<a id="item-9"></a>
## [Vitalik Buterin：混淆技术或可实现链上隐私投票](https://cointelegraph.com/news/vitalik-buterin-private-onchain-voting-obfuscation?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) ⭐️ 6.0/10

以太坊联合创始人 Vitalik Buterin 提出，不可区分混淆（iO）最终可能实现无需可信委员会的隐私、抗合谋链上投票。但他也承认，该技术目前仍极不实用。 如果实现，基于 iO 的投票可能彻底改变 DAO 和 DeFi 协议的治理方式，确保投票者隐私并防止合谋，解决当前链上投票系统的关键局限。这将增强去中心化决策中的信任和参与度。 不可区分混淆是一种密码学原语，能在保留程序功能的同时隐藏其实现，使等价程序的混淆版本无法区分。当前的 iO 候选方案极不实用；例如，混淆一个简单的 32 位 AND 函数会产生近 12GB 的程序。

rss · CoinTelegraph · 6月29日 10:53

**背景**: 不可区分混淆（iO）于 2001 年首次提出，被认为是一种强大的工具，理论上可以构建几乎所有密码学原语。然而，实用的 iO 仍然遥不可及；即使已知最高效的构造也过于庞大和缓慢，无法实际应用。当前的链上投票通常依赖可信委员会或公开投票，容易受到合谋或隐私泄露的影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Indistinguishability_obfuscation">Indistinguishability obfuscation</a></li>
<li><a href="https://coinfractal.com/vitalik-buterin-indistinguishability-obfuscation-private-onchain-voting/">Vitalik: Obfuscation Could Power Private Onchain Voting</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#blockchain`, `#voting`, `#privacy`

---