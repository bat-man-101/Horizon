---
layout: default
title: "Horizon Summary: 2026-06-30 (ZH)"
date: 2026-06-30
lang: zh
---

> 从 133 条内容中筛选出 11 条重要资讯。

---

1. [最高法院裁定地理围栏搜查令需受宪法保护](#item-1) ⭐️ 9.0/10
2. [谷歌 AI 同行评审系统在 ICML/STOC 处理约 1 万篇论文](#item-2) ⭐️ 9.0/10
3. [vLLM v0.24.0：支持 MiniMax-M3，深度优化 DeepSeek-V4](#item-3) ⭐️ 8.0/10
4. [Ornith-1.0：开源权重自支架编码大模型](#item-4) ⭐️ 8.0/10
5. [MiCA 截止日期或致 1000 万欧盟加密用户失去平台](#item-5) ⭐️ 8.0/10
6. [OpenAI 首席研究官警告：AGI 准备窗口很小](#item-6) ⭐️ 6.0/10
7. [私钥泄露导致 160 亿美元加密黑客损失中的 40%](#item-7) ⭐️ 6.0/10
8. [摩根大通扩大区块链结算网络](#item-8) ⭐️ 6.0/10
9. [纽约梅隆银行面向机构推出 USDC 稳定币服务](#item-9) ⭐️ 6.0/10
10. [Breez SDK 实现比特币到稳定币跨 30 多条链支付](#item-10) ⭐️ 6.0/10
11. [Vitalik：混淆技术可实现链上匿名投票](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [最高法院裁定地理围栏搜查令需受宪法保护](https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision) ⭐️ 9.0/10

美国最高法院裁定，地理围栏搜查令（要求谷歌等科技公司提供特定区域内所有设备的位置数据）需要根据第四修正案获得宪法保护。这一里程碑式的裁决限制了执法部门在没有个别嫌疑的情况下进行大规模位置监控的能力。 这一裁决为普遍监控时代的数字隐私设立了关键先例，可能影响数百万用户（其位置数据被谷歌等公司收集）。它还可能影响未来涉及其他形式的反向搜查令和批量数据请求的案件。 该案涉及一起银行抢劫案，谷歌提供了银行周围 150 米内 19 个账户的位置数据，从而识别出嫌疑人。法院强调，地理围栏搜查令本质上是宽泛的，需要基于可能原因签发搜查令，并附带具体限制以保护无辜第三方。

hackernews · cdrnsf · 6月29日 15:54 · [社区讨论](https://news.ycombinator.com/item?id=48720924)

**背景**: 地理围栏搜查令（又称反向位置搜查令）是一种允许执法部门在特定时间段内搜索特定地理区域内所有活跃移动设备数据库（如谷歌的 Sensorvault）的搜查令。与针对特定个人或设备的传统搜查令不同，地理围栏搜查令会收集许多无辜个人的数据，引发了关于不合理搜查的第四修正案重大关切。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Geofence_warrant">Geofence warrant</a></li>
<li><a href="https://www.npr.org/2026/06/29/nx-s1-5844697/supreme-court-restricts-use-of-geofence-warrants">Supreme Court restricts use of geofence warrants : NPR</a></li>

</ul>
</details>

**社区讨论**: 评论者对该裁决表示强烈支持，一些人引用了位置追踪的历史案例（如彼得雷乌斯事件），并质疑其他监控工具（如 Flock 车牌识别器）现在是否也需要搜查令。还有人注意到法院在意见书中引用了事实来源，同时批评持异议的大法官阿利托、托马斯和巴雷特倾向于政府权力。

**标签**: `#privacy`, `#supreme court`, `#surveillance`, `#law`, `#technology`

---

<a id="item-2"></a>
## [谷歌 AI 同行评审系统在 ICML/STOC 处理约 1 万篇论文](https://www.reddit.com/r/MachineLearning/comments/1uio9rb/googles_agentic_peerreviewer_handled_10k_papers/) ⭐️ 9.0/10

谷歌在 ICML 和 STOC 会议上部署了一个智能 AI 同行评审系统，以 30 分钟的处理时间评审了约 1 万篇论文，正式论文显示其比零样本提示多检测出 34%的数学错误。 这为在会议规模上实现 AI 自动化的科学评审开创了先例，可能加速同行评审过程并提高数学内容的错误检测能力，从而改变研究的评估方式。 该系统在检测数学错误方面比零样本提示提高了 34%，每篇论文处理时间约 30 分钟，展示了在大型会议中的实际可扩展性。

reddit · r/MachineLearning · /u/Justgototheeffinmoon · 6月29日 10:05

**背景**: 同行评审是学术出版中关键但耗时的环节，常导致延迟。零样本提示是指在不提供示例的情况下要求 AI 模型执行任务，这是一种常见的基线方法。智能 AI 系统能够自主规划并执行多步骤任务，因此适合复杂的评审工作流程。

**社区讨论**: Reddit 社区对 AI 减轻评审负担的潜力表示兴奋，但也提出了对公平性、准确性以及过度依赖自动化系统进行科学评估风险的担忧。

**标签**: `#AI`, `#peer review`, `#machine learning`, `#conference`, `#automation`

---

<a id="item-3"></a>
## [vLLM v0.24.0：支持 MiniMax-M3，深度优化 DeepSeek-V4](https://github.com/vllm-project/vllm/releases/tag/v0.24.0) ⭐️ 8.0/10

vLLM v0.24.0 新增了对 MiniMax-M3 模型的支持，并对 DeepSeek-V4 进行了重大优化，包括 FlashInfer 稀疏索引缓存（首 Token 延迟降低 2-4%）和预填充块规划（端到端吞吐量提升 4%）。该版本还引入了流式解析引擎、DiffusionGemma 支持以及用于专家并行的 DeepEP v2 集成。 此版本显著增强了 vLLM 服务前沿大语言模型（如 MiniMax-M3 和 DeepSeek-V4）的能力，这些模型是目前最先进的开源权重模型之一。性能优化和新功能（流式解析器、DiffusionGemma）扩展了 vLLM 在智能体工作流、长上下文推理和多模态任务中的适用性，惠及整个 LLM 推理生态系统。 该版本包含来自 256 位贡献者的 571 次提交，其中 77 位是首次贡献者。关键技术亮点包括：Model Runner V2 默认支持量化模型、新的流式解析引擎统一了跨模型的工具调用/推理解析、以及集成了 DeepEP v2 用于专家并行。此外，vLLM 不再内部设置 CUDA_VISIBLE_DEVICES，而是改用 device_ids 参数。

github · khluu · 6月29日 19:41

**背景**: vLLM 是一个开源的高吞吐量 LLM 推理引擎，使用 PagedAttention 高效管理 KV-cache 内存。MiniMax-M3 是一个多模态视觉语言模型，拥有 1M token 的上下文窗口，基于混合专家架构和 MiniMax 稀疏注意力（MSA）。DeepSeek-V4 是一个大型 MoE 模型，总参数高达 1.6T（激活参数 49B），专为高级推理和智能体任务设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.minimax.io/models/text/m3">MiniMax M 3 - Coding & Agentic Frontier, 1M Context, Multimodal</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro">deepseek-ai/DeepSeek-V4-Pro · Hugging Face</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#open source`, `#performance optimization`, `#model support`

---

<a id="item-4"></a>
## [Ornith-1.0：开源权重自支架编码大模型](https://simonwillison.net/2026/Jun/29/ornith/#atom-everything) ⭐️ 8.0/10

DeepReinforce 发布了 Ornith-1.0，这是一个基于 Gemma 4 和 Qwen 3.5 构建的开源权重（MIT 许可）编码智能体大模型系列，参数规模从 9B 到 397B 不等。在编码基准测试中，它在同等规模的开源模型中达到了最先进的性能。 此次发布提供了一个宽松许可、高性能的编码模型，可本地运行并处理复杂的智能体任务，有望加速 AI 辅助软件开发。其自支架能力使模型能在推理过程中自我改进推理过程，这是一种新颖的方法。 该模型系列包括 9B Dense、31B Dense、35B MoE 和 397B MoE 变体，均采用 MIT 许可。早期用户报告显示推理速度快（例如 103 tokens/秒）且工具使用有效，但部分用户指出在无工具聊天时存在幻觉倾向。

rss · Simon Willison · 6月29日 16:17

**背景**: 智能体编码是指使用 AI 智能体自主执行软件开发任务，如代码生成、调试和测试。自支架大语言模型能在推理过程中生成并优化自身的推理步骤或工具调用，从而无需外部提示即可提升性能。MoE（混合专家）架构每个 token 仅激活部分参数，使得更大规模的模型也能高效计算。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/29/ornith/">Ornith-1.0: Self - Scaffolding LLMs for Agentic Coding</a></li>
<li><a href="https://deep-reinforce.com/ornith_1_0.html">Ornith-1.0: Self - Scaffolding LLMs ... | DeepReinforce Blog | Jun. 2026</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agentic_coding">Agentic coding</a></li>

</ul>
</details>

**社区讨论**: 社区反应褒贬不一但总体积极：部分用户认为 Ornith-1.0 略优于 Qwen-3.6 35B，并赞赏其因更短的思维链而带来的更快推理速度。另一些用户质疑它是否只是“刷榜”微调，并对 DeepReinforce 缺乏透明度表示怀疑。少数用户报告在复杂编码任务上表现良好，但指出在纯聊天场景下性能不佳。

**标签**: `#LLM`, `#open-source`, `#coding`, `#agentic`, `#model release`

---

<a id="item-5"></a>
## [MiCA 截止日期或致 1000 万欧盟加密用户失去平台](https://www.coindesk.com/business/2026/06/29/mica-july-1-deadline-could-leave-10-million-crypto-users-searching-for-a-new-platform-in-the-eu) ⭐️ 8.0/10

《加密资产市场法案》（MiCA）的 2026 年 7 月 1 日截止日期可能迫使欧盟约 1000 万加密货币用户寻找新平台，因为许多现有交易所可能无法满足新规要求。 这一截止日期代表着重大监管转变，可能扰乱欧盟加密市场，导致数百万用户访问受限，并重塑交易所之间的竞争格局。 MiCA 于 2023 年 4 月通过，自 2024 年 12 月起全面适用，但过渡期将于 2026 年 7 月 1 日结束，此后所有加密资产服务提供商必须获得 MiCA 的全面授权。

rss · CoinDesk · 6月29日 15:03

**背景**: MiCA 是欧盟首个针对加密资产的全面监管框架，涵盖发行方、交易所和托管机构。其目标是在促进创新的同时保护投资者并确保市场诚信。该法规分两个阶段实施，最终阶段要求所有相关方在 2026 年 7 月 1 日前完全合规。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Markets_in_Crypto-Assets">Markets in Crypto-Assets - Wikipedia</a></li>
<li><a href="https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica">Markets in Crypto-Assets Regulation (MiCA)</a></li>
<li><a href="https://www.nortonrosefulbright.com/en/knowledge/publications/2cec201e/regulating-crypto-assets-in-europe-practical-guide-to-mica">Regulating crypto-assets in Europe: Practical guide to MiCA | Global law firm | Norton Rose Fulbright</a></li>

</ul>
</details>

**标签**: `#crypto`, `#regulation`, `#EU`, `#MiCA`, `#finance`

---

<a id="item-6"></a>
## [OpenAI 首席研究官警告：AGI 准备窗口很小](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&mid=2652710037&idx=2&sn=942dd7ab7358a3a8a5729c96860e9831) ⭐️ 6.0/10

OpenAI 首席研究官 Mark Chen 表示，人类为通用人工智能（AGI）做准备的时间窗口很小，并指出规模定律仍然有效，预训练、数据工程、推理训练和更长的任务链仍是通往 AGI 的主要路径。 来自 OpenAI 顶级研究人员的这一警告凸显了人工智能发展的加速步伐以及对安全与治理措施的迫切需求，将影响政策制定者、研究人员和公众。 该文章缺乏技术深度，被视为标题党，但 Chen 的言论证实了 OpenAI 对规模定律的持续信念以及推理时计算的重要性。

rss · 新智元 · 6月30日 04:32

**背景**: 通用人工智能（AGI）是一种假设的人工智能，能够在几乎所有认知任务上达到或超越人类能力。许多 AI 研究人员和预测市场估计 AGI 可能在未来十年内到来，一些时间线认为 2027-2030 年是一个可能的窗口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eu.36kr.com/en/p/3875321045217288">AGI Countdown: OpenAI's Chief Research Officer Warns Humanity ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Artificial_general_intelligence">Artificial general intelligence - Wikipedia</a></li>
<li><a href="https://aimultiple.com/artificial-general-intelligence-singularity-timing">AGI /Singularity: 9,800 Predictions Analyzed</a></li>

</ul>
</details>

**标签**: `#AGI`, `#OpenAI`, `#AI safety`

---

<a id="item-7"></a>
## [私钥泄露导致 160 亿美元加密黑客损失中的 40%](https://www.coindesk.com/tech/2026/06/29/private-keys-not-smart-contracts-caused-40-of-crypto-s-usd16-billion-hack-losses-here-s-whats-being-done) ⭐️ 6.0/10

一项新分析显示，160 亿美元加密黑客损失中的 40%源于私钥泄露，而非智能合约漏洞，这促使行业采用多方计算（MPC）和硬件安全模块（HSM）等新安全措施。 这一发现将安全焦点从智能合约审计转向密钥管理，这对保护用户资金和恢复加密生态系统信任至关重要。 私钥泄露通常通过钓鱼、恶意软件、社会工程或弱存储发生，一旦泄露，攻击者即可获得不可逆的访问权限，盗取钱包和协议资金。

rss · CoinDesk · 6月29日 15:45

**背景**: 在加密货币中，私钥是允许用户签署交易并证明资产所有权的秘密代码。与智能合约漏洞（代码错误）不同，私钥泄露直接针对用户对其资金的控制权。行业历来专注于审计智能合约，但这些数据凸显了改进密钥管理实践的必要性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.securview.com/ai-security-essentials/private-key-compromise">Private Key Compromise: Definition and Key Concepts</a></li>
<li><a href="https://www.guardrail.ai/common-attack-vectors/private-key-compromises">Guardrail – Protect Your Wallet from Private Key Compromises</a></li>
<li><a href="https://coinsprobe.com/zachxbt-flags-suspected-polymarket-exploit-as-658k-drained-from-uma-ctf-adapter/">Polymarket $520K Drain Was a Compromised Private Key — Not...</a></li>

</ul>
</details>

**标签**: `#cryptocurrency`, `#security`, `#private keys`, `#hacks`

---

<a id="item-8"></a>
## [摩根大通扩大区块链结算网络](https://www.coindesk.com/business/2026/06/29/j-p-morgan-broadens-blockchain-settlement-network-as-banks-modernize-cross-border-payments) ⭐️ 6.0/10

摩根大通扩大了其 Kinexys 区块链结算网络，该网络已处理超过 4 万亿美元的交易，以深化在亚太地区的覆盖，推动跨境支付现代化。 这一扩张标志着区块链在传统银行业中的采用日益增长，可能降低跨境支付的成本和结算时间，而传统跨境支付通常缓慢且昂贵。 Kinexys 是一个许可区块链平台，支持可编程支付、资产代币化和近乎实时的结算，摩根大通选择了以太坊二层网络 Base 用于可扩展的机构应用。

rss · CoinDesk · 6月29日 15:23

**背景**: 跨境支付传统上依赖代理银行网络，导致延迟和高费用。区块链技术通过实现直接、近乎实时的结算，提供了一种更高效的替代方案。摩根大通的 Kinexys 是领先的银行主导区块链项目之一，已处理超过 4 万亿美元的交易。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.jpmorgan.com/kinexys/index">Kinexys: Enterprise Bank-Led Blockchain Solutions</a></li>
<li><a href="https://www.coindesk.com/business/2026/06/29/j-p-morgan-broadens-blockchain-settlement-network-as-banks-modernize-cross-border-payments">J . P . Morgan broadens Kinexys blockchain settlement network as...</a></li>
<li><a href="https://www.binance.com/en/square/post/32457142769777">JPMorgan Ignites a New Era Where... | Decilizer on Binance Square</a></li>

</ul>
</details>

**标签**: `#blockchain`, `#finance`, `#cross-border payments`, `#J.P. Morgan`

---

<a id="item-9"></a>
## [纽约梅隆银行面向机构推出 USDC 稳定币服务](https://www.coindesk.com/business/2026/06/29/wall-street-s-bny-expands-stablecoin-services-for-institutions-starting-with-circle-s-usdc) ⭐️ 6.0/10

纽约梅隆银行扩大了与 Circle 的合作，通过其数字资产托管平台为机构客户提供 USDC 的托管、转账、铸造和赎回服务。 此举标志着机构对稳定币的采用日益增长，并连接了传统金融与基于区块链的数字资产，可能增加受监管稳定币服务的流动性和信任度。 纽约梅隆银行已是 USDC 储备的主要托管人；现在它增加了面向客户的稳定币功能，允许机构在其平台上直接铸造和赎回 USDC。

rss · CoinDesk · 6月29日 14:46

**背景**: 像 USDC 这样的稳定币是旨在保持稳定价值的加密货币，通常与美元等法定货币 1:1 挂钩。纽约梅隆银行是全球最大的托管银行之一，其进入稳定币服务领域代表着将数字资产整合到主流金融中的重要一步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cryptobriefing.com/bny-mellon-usdc-digital-asset-custody/">BNY adds USDC as first stablecoin on its institutional custody platform</a></li>
<li><a href="https://cryptopotato.com/circles-usdc-becomes-first-stablecoin-supported-by-bny-mellon-for-institutional-clients/">Circle's USDC Becomes First Stablecoin Supported by BNY Mellon for Institutional Clients</a></li>
<li><a href="https://crypto.news/bny-unlocks-usdc-minting-and-redemption-for-clients/">BNY unlocks USDC minting and redemption for institutional clients</a></li>

</ul>
</details>

**标签**: `#stablecoins`, `#institutional adoption`, `#crypto`, `#finance`

---

<a id="item-10"></a>
## [Breez SDK 实现比特币到稳定币跨 30 多条链支付](https://cointelegraph.com/news/breez-bitcoin-wallets-send-usdc-usdt-without-holding-stablecoins?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) ⭐️ 6.0/10

Breez 推出了新的 SDK 功能，允许开发者将比特币余额的支付路由到超过 30 条区块链网络上的 USDC 或 USDT 收款方，而无需用户持有稳定币。 这简化了比特币用户的稳定币支付，使他们无需管理单独的钱包或代币即可发送稳定币，可能推动基于比特币的支付解决方案的更广泛采用。 该功能基于 Spark 构建，Spark 是一个原生比特币 Layer 2，具有即时结算和多资产支持。超过 75 个应用（包括 Deblock、Cake Wallet 和 Klever）已集成 Breez SDK。

rss · CoinTelegraph · 6月29日 13:00

**背景**: USDC 和 USDT 等稳定币是与法定货币挂钩的数字资产，常用于支付和汇款。然而，用户通常需要单独获取并持有这些代币。Breez 的 SDK 通过利用其闪电网络集成和跨链路由，在支付时自动将比特币转换为稳定币，从而消除了这一要求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cryptobriefing.com/breez-bitcoin-stablecoin-payments-30-blockchains/">Breez launches Bitcoin - to - stablecoin payments across 30 blockchains</a></li>
<li><a href="https://breez.technology/sdk/">Breez SDK | Add Bitcoin to Any App or Service</a></li>
<li><a href="https://www.cointrust.com/market-news/breez-enables-bitcoin-to-stablecoin-payments-across-30-blockchains">Breez Enables Bitcoin-to-Stablecoin Payments Across 30 Blockchains</a></li>

</ul>
</details>

**标签**: `#Bitcoin`, `#stablecoins`, `#payments`, `#SDK`, `#blockchain`

---

<a id="item-11"></a>
## [Vitalik：混淆技术可实现链上匿名投票](https://cointelegraph.com/news/vitalik-buterin-private-onchain-voting-obfuscation?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) ⭐️ 6.0/10

Vitalik Buterin 表示，不可区分混淆（iO）最终可能实现无需可信委员会的私密、抗合谋链上投票，但目前该技术仍不实用。 如果实现，基于 iO 的投票将解决区块链治理中长期存在的透明与隐私之间的矛盾，允许在不泄露个人选择的情况下验证投票。这可能加强 DAO 及其他加密社区的去中心化决策。 不可区分混淆是一种密码学原语，能在保留功能的同时隐藏程序实现，但当前的候选方案极不实用——例如，混淆一个简单的 32 位 AND 函数会产生近 12GB 的程序。

rss · CoinTelegraph · 6月29日 10:53

**背景**: 链上投票是许多去中心化自治组织（DAO）的核心功能，但通常会暴露每个参与者的投票方式，从而可能引发贿赂或胁迫。不可区分混淆于 2001 年首次提出，是一种强大但尚处理论阶段的工具，可以在隐藏投票选择的同时允许公开验证结果。然而，由于巨大的体积和计算开销，已知的构造远未达到实用部署水平。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Indistinguishability_obfuscation">Indistinguishability obfuscation</a></li>
<li><a href="https://cointelegraph.com/news/vitalik-buterin-private-onchain-voting-obfuscation">Vitalik Details Cryptographic Path To Private Onchain Voting</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#voting`, `#privacy`, `#blockchain`

---