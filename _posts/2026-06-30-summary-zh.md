---
layout: default
title: "Horizon Summary: 2026-06-30 (ZH)"
date: 2026-06-30
lang: zh
---

> 从 130 条内容中筛选出 12 条重要资讯。

---

1. [最高法院：地理围栏搜查令需受宪法保护](#item-1) ⭐️ 9.0/10
2. [谷歌 AI 同行评审处理约 1 万篇论文，错误检测率提高 34%](#item-2) ⭐️ 9.0/10
3. [vLLM v0.24.0 新增 MiniMax-M3 支持与 DeepSeek-V4 优化](#item-3) ⭐️ 8.0/10
4. [Ornith-1.0：用于智能体编程的开源自搭建大语言模型](#item-4) ⭐️ 8.0/10
5. [OpenAI 首席研究官警告 AGI 窗口很小](#item-5) ⭐️ 6.0/10
6. [私钥泄露导致 160 亿美元加密黑客损失中的 40%](#item-6) ⭐️ 6.0/10
7. [摩根大通扩大区块链结算网络](#item-7) ⭐️ 6.0/10
8. [MiCA 截止日期或致 1000 万欧盟加密用户失去平台](#item-8) ⭐️ 6.0/10
9. [纽约梅隆银行为机构客户推出 USDC 铸造与赎回服务](#item-9) ⭐️ 6.0/10
10. [英国设定 2027 年 FCA 加密公司授权截止日期](#item-10) ⭐️ 6.0/10
11. [Breez SDK 实现比特币到稳定币跨链支付](#item-11) ⭐️ 6.0/10
12. [Vitalik：混淆技术或可实现链上隐私投票](#item-12) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [最高法院：地理围栏搜查令需受宪法保护](https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision) ⭐️ 9.0/10

美国最高法院以 6 比 3 裁定，地理围栏搜查令需要根据第四修正案获得宪法保护，限制了执法部门无证进行数字位置追踪的行为。 这项里程碑式的裁决加强了数字隐私权，要求执法部门在从谷歌等科技公司获取位置数据前，必须基于可能原因获得搜查令，影响了数百万智能手机用户。 该案涉及一起银行抢劫案，警方使用地理围栏搜查令从谷歌获取位置数据，识别出犯罪现场附近的 19 台设备；法院认为此类搜查受第四修正案搜查令要求的约束。

hackernews · cdrnsf · 6月29日 15:54 · [社区讨论](https://news.ycombinator.com/item?id=48720924)

**背景**: 地理围栏搜查令，也称为反向位置搜查令，允许执法部门请求特定地理区域在特定时间段内所有设备的位置数据。第四修正案保护公民免受不合理的搜查和扣押，最高法院此前已在 Riley 诉 California 案和 Carpenter 诉 United States 案等案件中将其保护范围扩展到数字位置数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Geofence_warrant">Geofence warrant - Wikipedia</a></li>
<li><a href="https://www.congress.gov/crs-product/LSB11274">Geofence Warrants and the Fourth Amendment | Congress.gov | Library of Congress</a></li>
<li><a href="https://www.nacdl.org/Content/Geofence-Warrants">NACDL - Geofence Warrants</a></li>

</ul>
</details>

**社区讨论**: 评论者对该裁决表示支持，一些人注意到法院在意见中使用了事实来源。其他人讨论了该裁决对 Flock 摄像头等其他监控技术的影响，并辩论了持异议的大法官的立场。

**标签**: `#privacy`, `#supreme court`, `#geofence warrants`, `#digital surveillance`, `#law`

---

<a id="item-2"></a>
## [谷歌 AI 同行评审处理约 1 万篇论文，错误检测率提高 34%](https://www.reddit.com/r/MachineLearning/comments/1uio9rb/googles_agentic_peerreviewer_handled_10k_papers/) ⭐️ 9.0/10

谷歌在 ICML 和 STOC 会议上部署了一个智能体 AI 同行评审系统，处理了约 1 万篇论文，每篇平均 30 分钟完成评审；正式研究论文显示，该系统比零样本提示多检测出 34%的数学错误。 这为会议规模的 AI 自动化科学评审开创了先例，可能通过提高错误检测率和减轻评审者工作量来改变同行评审流程。 该系统采用智能体方法，能够执行搜索参考文献或进行计算等操作，而不仅仅是生成文本。它已在顶级机器学习和理论会议的真实论文上进行了测试。

reddit · r/MachineLearning · /u/Justgototheeffinmoon · 6月29日 10:05

**背景**: 同行评审是专家在论文发表前评估其质量和正确性的过程。零样本提示要求 AI 在没有示例的情况下执行任务，这是 AI 性能的常见基线。智能体 AI 系统可以与工具和环境交互，从而能够执行验证数学证明等更复杂的任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zero-shot_prompting">Zero-shot prompting</a></li>

</ul>
</details>

**社区讨论**: Reddit 上的讨论总体积极，用户对处理规模和错误检测改进印象深刻。一些人担心 AI 取代人类评审者，而另一些人则认为它是有用的辅助工具。少数评论者质疑其泛化到计算机科学以外领域的能力。

**标签**: `#AI`, `#peer review`, `#machine learning`, `#scientific publishing`, `#Google`

---

<a id="item-3"></a>
## [vLLM v0.24.0 新增 MiniMax-M3 支持与 DeepSeek-V4 优化](https://github.com/vllm-project/vllm/releases/tag/v0.24.0) ⭐️ 8.0/10

vLLM v0.24.0 由 256 位贡献者提交了 571 次提交，新增了对 MiniMax-M3 模型的支持，并对 DeepSeek-V4 进行了重大优化，包括 FlashInfer 稀疏索引缓存和预填充分块规划改进。 此版本显著提升了两款前沿模型的推理性能，使大型语言模型在生产环境中能够更快、更高效地部署。 MiniMax-M3 支持包括通过 MSA 实现的 BF16/FP8 索引器、MXFP4 支持以及 FP8 稀疏 GQA；DeepSeek-V4 获得了 FlashInfer 稀疏索引缓存（TTFT 提升 2-4%）和预填充分块规划优化（端到端吞吐量提升 4%）。

github · khluu · 6月29日 19:41

**背景**: vLLM 是一个高吞吐量、内存高效的大型语言模型推理引擎。MiniMax-M3 使用新颖的稀疏注意力机制，需要专门的内核支持；而 DeepSeek-V4 采用复杂的多池 KV 缓存架构，受益于优化的稀疏索引。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://discuss.vllm.ai/t/minimax-m3-support/2689">Minimax m3 support - Model Support - vLLM Forums</a></li>
<li><a href="https://www.lmsys.org/blog/2026-04-25-deepseek-v4/">DeepSeek-V4 on Day 0: From Fast Inference to Verified RL with SGLang and Miles - LMSYS Org</a></li>

</ul>
</details>

**社区讨论**: vLLM 社区一直在积极讨论 MiniMax-M3 支持，指出 M3 从 MLA 风格的潜在压缩转向全注意力 GQA，这需要新的内核实现。该版本因其性能提升和广泛的模型支持而受到好评。

**标签**: `#vLLM`, `#LLM inference`, `#DeepSeek`, `#MiniMax`, `#performance optimization`

---

<a id="item-4"></a>
## [Ornith-1.0：用于智能体编程的开源自搭建大语言模型](https://simonwillison.net/2026/Jun/29/ornith/#atom-everything) ⭐️ 8.0/10

DeepReinforce 发布了 Ornith-1.0，这是一个基于 MIT 许可证的开源权重大语言模型系列，专为智能体编程设计，参数规模从 9B 到 397B 不等，基于 Gemma 4 和 Qwen 3.5 基座模型构建。在编程基准测试中，它在同等规模的开源模型中达到了最先进的性能。 Ornith-1.0 引入了一种新颖的自搭建训练框架，模型学习同时生成解决方案的 rollout 以及驱动这些 rollout 的脚手架，可能减少智能体编程任务中对外部编排的需求。其 MIT 许可证和强劲性能使其对开发者和研究人员高度可用。 该模型系列包括 9B Dense、31B Dense、35B MoE 和 397B MoE 变体，全部采用 MIT 许可证。底层基座模型（Gemma 4 和 Qwen 3.5）采用 Apache 2.0 许可证，确保了许可证兼容性。早期用户报告显示，由于思维链更短，推理速度比同类模型更快。

rss · Simon Willison · 6月29日 16:17

**背景**: 智能体编程是指 AI 智能体在最少人工干预下自主规划、编写、测试和修改代码。传统的基于大语言模型的编程助手需要外部脚手架（例如工具使用框架）来执行多步骤任务。Ornith-1.0 的自搭建方法旨在内化这种能力，使模型能够生成自己的执行计划和工具调用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/29/ornith/">Ornith-1.0: Self - Scaffolding LLMs for Agentic Coding</a></li>
<li><a href="https://deep-reinforce.com/ornith_1_0.html">Ornith - 1 . 0 : Self-Scaffolding LLMs... | DeepReinforce Blog | Jun. 2026</a></li>
<li><a href="https://ornith.site/">Ornith 1 . 0 — Open-Source Agentic Coding Models</a></li>

</ul>
</details>

**社区讨论**: 社区评价褒贬不一：一些用户报告了强劲的编程性能和更快的推理速度，而另一些用户则指出在无工具聊天中表现不佳且容易产生幻觉。一些评论者质疑 Ornith-1.0 是否只是 Qwen 或 Gemma 4 的微调版本，并对 DeepReinforce 团队的背景感到好奇。

**标签**: `#LLM`, `#open-source`, `#coding`, `#AI`, `#machine learning`

---

<a id="item-5"></a>
## [OpenAI 首席研究官警告 AGI 窗口很小](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&mid=2652710037&idx=2&sn=942dd7ab7358a3a8a5729c96860e9831) ⭐️ 6.0/10

OpenAI 首席研究官 Mark Chen 表示，人类为通用人工智能（AGI）做准备的窗口非常小，暗示 AGI 可能比许多人预期的更早到来。 OpenAI 关键人物的这一警告凸显了 AI 安全研究和政策制定的紧迫性，因为 AGI 可能对社会和全球经济产生变革性影响。 该声明没有给出具体时间表，但与其他预测一致，即 AGI 可能在未来几年内出现。这一评论反映了 OpenAI 内部对进展速度的持续担忧。

rss · 新智元 · 6月30日 04:32

**背景**: 通用人工智能（AGI）是一种假设的 AI 系统，能够执行人类能够完成的任何智力任务。与擅长特定任务的狭义 AI 不同，AGI 将具备通用认知能力。AGI 的时间表存在很大争议，一些专家预测它将在十年内出现，而另一些人则认为还很遥远。AI 安全是一个专注于确保先进 AI 系统与人类价值观一致且不造成伤害的领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Artificial_general_intelligence">Artificial general intelligence - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_safety">AI safety - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AGI`, `#OpenAI`, `#AI safety`, `#timeline`

---

<a id="item-6"></a>
## [私钥泄露导致 160 亿美元加密黑客损失中的 40%](https://www.coindesk.com/tech/2026/06/29/private-keys-not-smart-contracts-caused-40-of-crypto-s-usd16-billion-hack-losses-here-s-whats-being-done) ⭐️ 6.0/10

一份最新报告显示，在 160 亿美元的加密黑客损失中，40%是由私钥泄露而非智能合约漏洞造成的，这促使行业制定新的缓解策略。 这一发现将安全焦点从智能合约审计转向私钥管理，影响交易所、钱包和 DeFi 协议保护用户资产的方式。 报告估计，自 2022 年以来，约 49.6%的已实现加密损失来自私钥泄露、钓鱼和社会工程攻击，而非合约逻辑缺陷。

rss · CoinDesk · 6月29日 15:45

**背景**: 私钥是控制加密资产的加密秘密；一旦泄露，攻击者无需利用智能合约漏洞即可窃取资金。历史上，加密行业高度重视智能合约审计，但这一数据表明密钥管理是更大的风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.coindesk.com/tech/2026/06/29/private-keys-not-smart-contracts-caused-40-of-crypto-s-usd16-billion-hack-losses-here-s-whats-being-done">Private keys, not smart contracts, caused 40% of crypto's $16 billion ...</a></li>
<li><a href="https://cryptodaily.co.uk/2026/06/crypto-audit-gap-private-keys-phishing">The Crypto Audit Gap: Keys , Phishing, and Missed Risks</a></li>
<li><a href="https://blog.trailofbits.com/2025/06/25/maturing-your-smart-contracts-beyond-private-key-risk/">Maturing your smart contracts beyond private key risk - The Trail of Bits Blog</a></li>

</ul>
</details>

**标签**: `#cryptocurrency`, `#security`, `#private keys`, `#hacks`

---

<a id="item-7"></a>
## [摩根大通扩大区块链结算网络](https://www.coindesk.com/business/2026/06/29/j-p-morgan-broadens-blockchain-settlement-network-as-banks-modernize-cross-border-payments) ⭐️ 6.0/10

摩根大通扩大了其 Kinexys 区块链结算网络，使银行能够使用许可区块链实现近乎实时的跨境支付结算，从而推动支付现代化。 这一扩张标志着机构对区块链在核心银行业务中的应用日益接受，有望将结算时间从数天缩短至几分钟，并降低跨境交易成本。 该网络使用由摩根大通运营的许可区块链，其 JPM Coin（JPMD）正在与 Canton Network 集成，以实现公共区块链互操作性。

rss · CoinDesk · 6月29日 15:23

**背景**: 传统跨境支付依赖代理银行网络，可能需要数天且费用高昂。基于区块链的解决方案通过消除中介，提供更快、更便宜且全天候的结算。摩根大通的 Kinexys 平台是一个银行主导的区块链，用于可编程支付和资产代币化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.coindesk.com/business/2026/06/29/j-p-morgan-broadens-blockchain-settlement-network-as-banks-modernize-cross-border-payments">J.P. Morgan broadens Kinexys blockchain settlement network as banks modernize cross-border payments</a></li>
<li><a href="https://www.jpmorgan.com/kinexys/index">Kinexys: Enterprise Bank-Led Blockchain Solutions</a></li>
<li><a href="https://blog.digitalasset.com/news/digital-asset-and-kinexys-by-j.p.-morgan-bring-usd-jpm-coin-jpmd-natively-to-canton">Digital Asset and Kinexys by J.P. Morgan announce intention to bring USD JPM Coin (JPMD) natively to the Canton Network</a></li>

</ul>
</details>

**标签**: `#blockchain`, `#banking`, `#cross-border payments`, `#J.P. Morgan`

---

<a id="item-8"></a>
## [MiCA 截止日期或致 1000 万欧盟加密用户失去平台](https://www.coindesk.com/business/2026/06/29/mica-july-1-deadline-could-leave-10-million-crypto-users-searching-for-a-new-platform-in-the-eu) ⭐️ 6.0/10

这一截止日期标志着重大监管转变，可能扰乱数百万欧盟居民获取加密服务的渠道，或将用户推向未受监管的平台或降低市场参与度，同时为全球加密监管树立先例。 MiCA 法规于 2024 年全面通过，要求欧盟内所有加密资产服务商获得授权并遵守透明度、消费者保护和反洗钱的严格规定。不合规平台须在 2026 年 7 月 1 日前停止运营。

rss · CoinDesk · 6月29日 15:03

**背景**: MiCA 是全球首个针对数字资产的全面监管框架，旨在统一欧盟成员国的加密规则。它涵盖加密资产发行方、服务商和稳定币，旨在保护投资者并确保市场诚信。7 月 1 日截止日期是现有加密企业实现完全合规的过渡期结束日。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Markets_in_Crypto-Assets">Markets in Crypto -Assets - Wikipedia</a></li>
<li><a href="https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica">Markets in Crypto -Assets Regulation ( MiCA )</a></li>
<li><a href="https://ondato.com/blog/mica-regulation/">MiCA Regulation and its Impact on the Crypto Market | Ondato</a></li>

</ul>
</details>

**标签**: `#crypto`, `#regulation`, `#EU`, `#MiCA`

---

<a id="item-9"></a>
## [纽约梅隆银行为机构客户推出 USDC 铸造与赎回服务](https://www.coindesk.com/business/2026/06/29/wall-street-s-bny-expands-stablecoin-services-for-institutions-starting-with-circle-s-usdc) ⭐️ 6.0/10

纽约梅隆银行扩展其数字资产托管平台，支持 Circle 的 USDC，使机构客户能够直接通过该银行铸造、赎回、存储和转移该稳定币。这是 BNY 机构托管服务首次集成稳定币。 此举标志着机构对稳定币的采用日益增长，连接了传统金融与数字资产。通过提供 USDC 服务，纽约梅隆银行为机构获取稳定币流动性和结算提供了受监管的通道，可能加速主流加密整合。 纽约梅隆银行此前已是 USDC 储备的主要托管人；此次扩展增加了面向客户的铸造和赎回功能。USDC 是 BNY 数字资产托管平台支持的首个稳定币，该平台于 2022 年 10 月启动，最初支持比特币和以太坊。

rss · CoinDesk · 6月29日 14:46

**背景**: USDC 等稳定币是与稳定资产（通常是美元）挂钩的加密货币，为交易和结算提供价格稳定性。纽约梅隆银行的数字资产托管平台允许机构投资者在受监管环境中将数字资产与传统证券一同持有。此次集成加深了 BNY 与 USDC 发行方 Circle 的合作关系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://crypto.news/bny-unlocks-usdc-minting-and-redemption-for-clients/">BNY unlocks USDC minting and redemption for institutional clients</a></li>
<li><a href="https://cryptobriefing.com/bny-mellon-usdc-digital-asset-custody/">BNY Mellon integrates USDC as first stablecoin on Digital Asset...</a></li>
<li><a href="https://tokenmetrics.com/usdc/news/bny-usdc-minting-institutional-custody/">BNY Adds USDC Minting To Institutional Custody Platform</a></li>

</ul>
</details>

**标签**: `#stablecoins`, `#institutional finance`, `#crypto`, `#BNY Mellon`

---

<a id="item-10"></a>
## [英国设定 2027 年 FCA 加密公司授权截止日期](https://cointelegraph.com/news/uk-crypto-rules-2027-fca-authorization-deadline?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) ⭐️ 6.0/10

英国金融行为监管局（FCA）发布了最终的加密监管框架，要求所有加密公司在 2027 年 2 月前获得 FCA 授权。 该法规将加密公司置于与传统金融机构相同的监管之下，增强了消费者保护和市场诚信，并使英国成为领先的加密中心。 目前根据反洗钱法规注册的公司也必须申请全面授权。新制度预计将于 2027 年 10 月 25 日生效。

rss · CoinTelegraph · 6月29日 23:01

**背景**: 英国一直在制定全面的加密监管框架，以使数字资产与传统金融保持一致。FCA 是负责授权和监督公司的金融监管机构。此举旨在为在英国运营的加密企业提供清晰度和法律确定性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.grantthornton.co.uk/insights/crypto-firms--a-guide-to-fca-authorisation/">Crypto firms – a guide to FCA authorisation | Grant Thornton</a></li>
<li><a href="https://www.fca.org.uk/firms/new-regime-cryptoasset-regulation/authorisation-supervision-enforcement">Cryptoasset firms: Authorisation, supervision and enforcement | FCA</a></li>
<li><a href="https://www.edgen.tech/news/crypto/uk-targets-crypto-hub-status-with-2027-regulatory-framework">UK Targets Crypto Hub Status With 2027 Regulatory Framework</a></li>

</ul>
</details>

**标签**: `#cryptocurrency`, `#regulation`, `#UK`, `#FCA`

---

<a id="item-11"></a>
## [Breez SDK 实现比特币到稳定币跨链支付](https://cointelegraph.com/news/breez-bitcoin-wallets-send-usdc-usdt-without-holding-stablecoins?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) ⭐️ 6.0/10

Breez 推出了一项新的 SDK 功能，允许开发者将比特币支付路由到超过 30 条区块链上的 USDC 和 USDT 接收方，而无需用户持有稳定币。 这一创新连接了比特币和稳定币生态系统，使比特币持有者无需兑换即可使用广泛使用的稳定币进行支付，可能扩大比特币在日常交易和 DeFi 中的实用性。 该功能是 Breez SDK 的一部分，基于 Spark 构建，Spark 是一个原生比特币 Layer 2，支持即时结算和多资产。它支持超过 30 条区块链，包括以太坊、Solana 和 Tron 等主要网络。

rss · CoinTelegraph · 6月29日 13:00

**背景**: USDC 和 USDT 等稳定币是与法定货币挂钩的数字资产，常用于支付和 DeFi。比特币虽然具有价值，但由于波动性和结算速度较慢，在日常交易中不太实用。Breez SDK 是一个非托管工具包，允许开发者将比特币支付集成到应用中。这项新功能利用跨链路由，在接收方端将比特币价值转换为稳定币，简化了支付体验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cryptobriefing.com/breez-bitcoin-stablecoin-payments-30-blockchains/">Breez launches Bitcoin - to - stablecoin payments across 30 blockchains</a></li>
<li><a href="https://breez.technology/sdk/">Breez SDK | Add Bitcoin to Any App or Service</a></li>
<li><a href="https://coincentral.com/breez-launches-bitcoin-to-stablecoin-payments-without-holding-usdc-or-usdt/">Breez Launches Bitcoin - to - Stablecoin Payments Without Holding...</a></li>

</ul>
</details>

**标签**: `#Bitcoin`, `#Stablecoins`, `#Payments`, `#SDK`, `#Blockchain`

---

<a id="item-12"></a>
## [Vitalik：混淆技术或可实现链上隐私投票](https://cointelegraph.com/news/vitalik-buterin-private-onchain-voting-obfuscation?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) ⭐️ 6.0/10

以太坊联合创始人 Vitalik Buterin 提出，不可区分混淆（iO）最终可能实现无需可信委员会的隐私、抗共谋链上投票，尽管该技术目前仍不实用。 如果实现，基于 iO 的投票可能通过确保选民隐私和防止共谋来改变 DAO 和 DeFi 协议的治理，解决当前链上投票系统的关键限制。 不可区分混淆隐藏程序实现的同时允许其运行，但当前的候选方案极不实用——例如，混淆一个简单的 32 位 AND 函数会产生近 12GB 的程序。

rss · CoinTelegraph · 6月29日 10:53

**背景**: 不可区分混淆（iO）是一种密码学原语，使计算相同函数的两个程序无法区分，从而隐藏其内部逻辑。它被认为是“最佳可能”的混淆，理论上可以构造许多其他密码学原语。然而，已知的 iO 构造依赖于未经证实的假设，且远未达到实际部署的程度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Indistinguishability_obfuscation">Indistinguishability obfuscation</a></li>
<li><a href="https://coinfractal.com/vitalik-buterin-indistinguishability-obfuscation-private-onchain-voting/">Vitalik: Obfuscation Could Power Private Onchain Voting</a></li>
<li><a href="https://coinmarketcap.com/academy/article/vitalik-buterin-obfuscation-private-onchain-voting">Vitalik Buterin Says Obfuscation Could Enable Private On - Chain Voting</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#blockchain`, `#voting`, `#privacy`

---