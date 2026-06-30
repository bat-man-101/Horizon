---
layout: default
title: "Horizon Summary: 2026-06-30 (ZH)"
date: 2026-06-30
lang: zh
---

> 从 133 条内容中筛选出 10 条重要资讯。

---

1. [最高法院裁定地理围栏搜查令需受第四修正案保护](#item-1) ⭐️ 9.0/10
2. [vLLM v0.24.0：支持 MiniMax-M3，深度优化 DeepSeek-V4](#item-2) ⭐️ 8.0/10
3. [llama.cpp b9840 增加对 DeepSeek V4 的支持](#item-3) ⭐️ 8.0/10
4. [Ornith-1.0：用于智能体编程的自脚手架大语言模型](#item-4) ⭐️ 8.0/10
5. [ChatGPT 推翻陈立杰苦思 7 年的计算几何难题](#item-5) ⭐️ 8.0/10
6. [MiCA 截止日期或迫使 1000 万欧盟加密用户离开平台](#item-6) ⭐️ 8.0/10
7. [OpenAI 绘制 AI 对欧盟就业的影响图](#item-7) ⭐️ 6.0/10
8. [摩根大通扩大区块链结算网络以优化跨境支付](#item-8) ⭐️ 6.0/10
9. [Vitalik Buterin：混淆技术或可实现链上私密投票](#item-9) ⭐️ 6.0/10
10. [国际清算银行警告 AI 投资热潮或引发全球金融危机](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [最高法院裁定地理围栏搜查令需受第四修正案保护](https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision) ⭐️ 9.0/10

美国最高法院裁定，地理围栏搜查令（要求科技公司提供特定区域内所有设备的位置数据）必须符合第四修正案关于可能原因和特定性的要求。Chatrie 诉美国案的判决为数字隐私设立了里程碑式的先例。 该裁决限制了执法部门通过地理围栏搜查令进行大规模监控的能力，保护无辜旁观者的位置数据不被无司法监督地收集。它强化了数字时代的第四修正案保护，并可能影响全球类似案件。 法院认为地理围栏搜查令属于第四修正案下的“搜查”，需要基于可能原因并具体描述搜查地点的搜查令。由卡根大法官撰写的意见引用了 2014 年 Riley 诉加州案关于手机搜查的判决。

hackernews · cdrnsf · 6月29日 15:54 · [社区讨论](https://news.ycombinator.com/item?id=48720924)

**背景**: 地理围栏搜查令允许警方要求谷歌等公司提供在特定时间窗口内位于犯罪现场周围虚拟边界（地理围栏）内的所有设备列表。批评者认为这些搜查令违宪，因为它们实际上搜查了区域内的所有人，而不仅仅是嫌疑人。该案源于 2018 年一起银行抢劫案，谷歌提供了银行附近 19 台设备的数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/04/28/scotus-chatrie-geofence-search-warrant-ruling-arguments/">US Supreme Court appears split over controversial use of ' geofence ...</a></li>
<li><a href="https://www.texaspolicyresearch.com/decision-on-geofence-warrants-a-critical-blow-to-mass-surveillance/">Decision on Geofence Warrants : A Critical... - Texas Policy Research</a></li>
<li><a href="https://www.culawreview.org/journal/mapping-the-future-of-surveillance-geofence-warrants-and-the-risks-of-chatrie">Mapping the Future of Surveillance: Geofence Warrants and the Risks...</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞该裁决是隐私权的胜利，有人指出法院在意见中引用来源是积极信号。另一位评论者强调了窃听的历史类比，指出物理限制曾限制了滥用，但数字监控缺乏这些限制。第三位评论者分享了一个例子，说明即使没有手机，位置数据也能识别个人，展示了此类技术的威力。

**标签**: `#privacy`, `#supreme court`, `#geofence warrants`, `#digital rights`, `#law enforcement`

---

<a id="item-2"></a>
## [vLLM v0.24.0：支持 MiniMax-M3，深度优化 DeepSeek-V4](https://github.com/vllm-project/vllm/releases/tag/v0.24.0) ⭐️ 8.0/10

vLLM v0.24.0 新增了对 MiniMax-M3 模型的支持，并对 DeepSeek-V4 进行了重大优化，包括 FlashInfer 稀疏索引缓存和 prefill 分块规划改进。该版本还引入了默认支持量化的 Model Runner V2、流式解析引擎，以及用于专家并行性的 DeepEP v2 集成。 此版本显著增强了 vLLM 服务前沿模型（如 MiniMax-M3 和 DeepSeek-V4）的能力，这些模型在编程、智能体推理和长上下文任务中处于领先地位。优化提高了推理吞吐量和延迟，使依赖 vLLM 进行高效 LLM 服务的广大 AI 社区受益。 该版本包含来自 256 位贡献者的 571 次提交，其中 77 位是新贡献者。关键技术新增包括 MiniMax-M3 的 MXFP4 支持、DeepSeek-V4 的集群协作 topK 内核，以及具有 API 密钥认证和 CORS 支持的新 Rust 前端。vLLM 还更改了设备选择方式，不再在内部设置 CUDA_VISIBLE_DEVICES。

github · khluu · 6月29日 19:41

**背景**: vLLM 是一个高性能的开源 LLM 推理和服务库，以其高效的内存管理和快速解码而广泛使用。MiniMax-M3 是一个前沿的开源权重模型，具有 1M 上下文窗口和多模态能力，而 DeepSeek-V4 是一个 1 万亿参数的混合专家模型。FlashInfer 是一个用于 LLM 服务的内核库，提供高效的注意力机制，如稀疏注意力和分页注意力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.minimax.io/models/text/m3">MiniMax M3 - Coding & Agentic Frontier, 1M Context, Multimodal</a></li>
<li><a href="https://deepseek.ai/deepseek-v4">DeepSeek V 4 (2026) — 1T Params, Benchmarks & Pricing</a></li>

</ul>
</details>

**社区讨论**: 社区评论并非直接关于 vLLM v0.24.0，而是讨论另一个模型（可能是 Qwen 微调版）。评论意见不一：一些人认为它在创造性编码解决方案方面表现良好，而另一些人则指出存在幻觉和在消费级硬件上的限制。这些评论与本版本无关。

**标签**: `#vLLM`, `#LLM inference`, `#model optimization`, `#open source`, `#AI infrastructure`

---

<a id="item-3"></a>
## [llama.cpp b9840 增加对 DeepSeek V4 的支持](https://github.com/ggml-org/llama.cpp/releases/tag/b9840) ⭐️ 8.0/10

llama.cpp b9840 引入了对 DeepSeek V4 模型架构的支持，包括转换脚本、推理图以及对 V4-Pro 和 V4-Flash 两种变体的优化。 此次更新使得在消费级硬件上本地高效推理 DeepSeek V4（一种最先进的开源 MoE 模型）成为可能，扩大了先进 AI 能力的可及性。 该版本包含多平台二进制文件（macOS、Linux、Windows、Android），并支持 DeepSeek V4 的闪存注意力、图复用和部分检查点等功能。

github · github-actions[bot] · 6月29日 10:25

**背景**: llama.cpp 是一个流行的开源项目，用于在 CPU 和 GPU 上本地运行大型语言模型，依赖极少。DeepSeek V4 是 DeepSeek 以 MIT 许可证发布的一系列混合专家（MoE）模型，拥有高达 1.6 万亿总参数和 100 万 token 的上下文窗口。GGUF 格式用于存储量化模型以实现高效推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ggml-org/llama.cpp/releases">Releases · ggml-org/ llama . cpp</a></li>
<li><a href="https://www.morphllm.com/deepseek-v4">DeepSeek V4: 1.6T MoE, 1M Context, $0.87/M Output. Architecture ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/GGUF">GGUF - Wikipedia</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#DeepSeek V4`, `#LLM inference`, `#open-source`, `#machine learning`

---

<a id="item-4"></a>
## [Ornith-1.0：用于智能体编程的自脚手架大语言模型](https://simonwillison.net/2026/Jun/29/ornith/#atom-everything) ⭐️ 8.0/10

DeepReinforce 发布了 Ornith-1.0，这是一个用于智能体编程的开源权重大语言模型系列（MIT 许可证），尺寸从 9B 到 397B，基于 Gemma 4 和 Qwen 3.5 构建。在编程基准测试中，它在同尺寸开源模型中达到了最先进的性能。 Ornith-1.0 引入了一种自脚手架训练框架，模型学会同时生成解决方案和任务特定的脚手架，可能减少对人类设计的智能体框架的依赖。这可以加速自主编程智能体的开发，并降低开源智能体编程的门槛。 该模型系列包括 9B Dense、31B Dense、35B MoE 和 397B MoE 变体，全部采用 MIT 许可证。35B MoE 变体在单 GPU 上以 103 tokens/秒运行，4-bit 量化后仅需 20GB。底层基础模型（Gemma 4 和 Qwen 3.5）采用 Apache 2.0 许可证。

rss · Simon Willison · 6月29日 16:17

**背景**: 智能体编程是指 AI 系统以最少的人类干预执行多步骤软件开发任务。传统的基于大语言模型的编程智能体依赖人类编写的脚手架（框架）来指导工具使用和推理。自脚手架是一种新范式，模型学会生成自己的任务特定脚手架，并与解决方案策略共同进化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deep-reinforce.com/ornith_1_0.html">Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding | DeepReinforce Blog | Jun. 2026</a></li>
<li><a href="https://essamamdani.com/blog/ornith-1-0-self-scaffolding-llm-coding-2026">Ornith-1.0: The Self-Scaffolding LLM That Teaches Itself to Code Better | Essa Mamdani | Essa Mamdani</a></li>
<li><a href="https://www.mindstudio.ai/blog/self-scaffolding-ai-models-ornith-1-0">Self-Scaffolding AI Models: How Ornith 1.0 Writes Its Own Agent Harness | MindStudio</a></li>

</ul>
</details>

**社区讨论**: 社区评论褒贬不一：一些用户报告在编程任务上表现良好且能提供创造性解决方案，而另一些用户则指出在无工具聊天时表现不佳且容易产生幻觉。有人怀疑这仅仅是 Qwen 或 Gemma 的微调版本，并且对可访问性表示担忧（例如，9B 模型需要 80GB GPU）。

**标签**: `#LLM`, `#open-source`, `#coding`, `#agentic`, `#model release`

---

<a id="item-5"></a>
## [ChatGPT 推翻陈立杰苦思 7 年的计算几何难题](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&mid=2652709773&idx=2&sn=68bde762eb0070f5bd61518728971232) ⭐️ 8.0/10

据报道，ChatGPT 解决了困扰著名研究员陈立杰七年的计算几何核心问题，该成果基于 OpenAI 近期解决的一个 Erdős 猜想。 这表明 AI 解决长期数学难题的能力日益增强，可能加速计算几何及相关领域的研究。 该问题是陈立杰研究了七年的计算几何核心难题。解决方案基于 OpenAI 此前解决的 Erdős 猜想，但问题及解决方案的具体细节尚未公开。

rss · 新智元 · 6月29日 05:01

**背景**: 计算几何研究几何问题的算法，如点定位和范围搜索。陈立杰是著名的计算机科学家，以复杂性理论研究闻名。Erdős 猜想是 Paul Erdős 提出的著名数论未解问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Computational_geometry">Computational geometry - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#computational geometry`, `#ChatGPT`, `#OpenAI`, `#breakthrough`

---

<a id="item-6"></a>
## [MiCA 截止日期或迫使 1000 万欧盟加密用户离开平台](https://www.coindesk.com/business/2026/06/29/mica-july-1-deadline-could-leave-10-million-crypto-users-searching-for-a-new-platform-in-the-eu) ⭐️ 8.0/10

欧盟《加密资产市场法案》（MiCA）面临 7 月 1 日的截止日期，由于许多交易所尚未获得必要许可，约 1000 万加密用户可能失去合规平台。 这一截止日期标志着欧盟加密市场的重大监管变革，可能扰乱数百万用户的访问，迫使交易所要么合规要么退出该地区，为全球加密监管树立先例。 MiCA 于 2023 年 6 月生效，要求加密资产服务提供商在 2026 年 7 月 1 日前获得授权；不合规平台将面临执法行动，包括可能禁止服务欧盟客户。

rss · CoinDesk · 6月29日 15:03

**背景**: MiCA 是欧盟针对加密资产的全面监管框架，旨在保护投资者、确保市场诚信并促进创新。它涵盖加密资产发行人、交易所和钱包提供商，要求其满足严格合规标准，如反洗钱（AML）和消费者保护规则。该法规分阶段实施，全面应用截止日期即将在 2026 年 7 月到来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Markets_in_Crypto-Assets">Markets in Crypto -Assets - Wikipedia</a></li>
<li><a href="https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica">Markets in Crypto -Assets Regulation ( MiCA )</a></li>
<li><a href="https://aurum.law/newsroom/EU-MiCA-Regulation">EU MiCA Regulation : Crypto Compliance Guide | Aurum</a></li>

</ul>
</details>

**标签**: `#crypto regulation`, `#MiCA`, `#EU`, `#blockchain`, `#finance`

---

<a id="item-7"></a>
## [OpenAI 绘制 AI 对欧盟就业的影响图](https://openai.com/index/mapping-ai-jobs-transition-eu) ⭐️ 6.0/10

OpenAI 发布了一份报告，绘制了 AI 如何重塑欧盟各职业的图景，识别出面临自动化风险的岗位、有望增长的岗位以及可能发生变化的工作流程。 这份报告提供了高层次的概述，可能为欧盟政策和劳动力规划提供参考，突显了随着 AI 采用加速，技能重塑和适应的必要性。 该报告将职业分为自动化、增长和工作流程变化三类，但缺乏具体的技术细节或定量预测。

rss · OpenAI Blog · 6月29日 07:00

**背景**: 像大型语言模型这样的 AI 技术越来越能够执行传统上由人类完成的任务，引发了关于岗位替代和转型的讨论。欧盟一直通过《AI 法案》积极监管 AI，了解其对劳动力的影响对政策制定至关重要。

**标签**: `#AI`, `#labor`, `#EU`, `#automation`, `#workforce`

---

<a id="item-8"></a>
## [摩根大通扩大区块链结算网络以优化跨境支付](https://www.coindesk.com/business/2026/06/29/j-p-morgan-broadens-blockchain-settlement-network-as-banks-modernize-cross-border-payments) ⭐️ 6.0/10

摩根大通扩大了其 Kinexys 区块链结算网络，深化了在亚太地区的覆盖，该平台迄今已处理超过 4 万亿美元的交易。 此次扩张标志着区块链在核心银行基础设施中的应用日益增长，可能降低跨境支付的成本和结算时间，而传统上这些支付依赖 SWIFT 等较慢的系统。 Kinexys 是一个由银行主导的区块链平台，提供可编程支付、资产代币化和近乎实时的结算。最新扩张聚焦亚太地区，这是跨境贸易的关键区域。

rss · CoinDesk · 6月29日 15:23

**背景**: 传统的跨境支付通常使用 SWIFT 等代理银行网络，可能缓慢且成本高昂。基于区块链的结算网络提供了更快、透明且可编程的替代方案。摩根大通的 Kinexys 就是这样一个企业级解决方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.coindesk.com/business/2026/06/29/j-p-morgan-broadens-blockchain-settlement-network-as-banks-modernize-cross-border-payments">J . P . Morgan broadens Kinexys blockchain settlement network as...</a></li>
<li><a href="https://www.jpmorgan.com/kinexys/index">Kinexys: Enterprise Bank-Led Blockchain Solutions</a></li>
<li><a href="https://www.paycio.com/blog/blockchain-cross-border-payments-and-how-do-they-work">Blockchain Cross - border Payments & How Do They Work</a></li>

</ul>
</details>

**标签**: `#blockchain`, `#finance`, `#cross-border payments`, `#J.P. Morgan`

---

<a id="item-9"></a>
## [Vitalik Buterin：混淆技术或可实现链上私密投票](https://cointelegraph.com/news/vitalik-buterin-private-onchain-voting-obfuscation?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) ⭐️ 6.0/10

以太坊联合创始人 Vitalik Buterin 提出，不可区分混淆（iO）最终可能实现无需可信委员会的私密、抗合谋的链上投票，尽管该技术目前尚不实用。 如果实现，基于 iO 的投票将显著提升 DAO 治理和 DeFi 协议的隐私与安全性，减少对可信第三方的依赖并降低合谋风险。 不可区分混淆是一种隐藏程序实现同时保留其功能的密码学原语，但当前的候选方案极不实用——例如，混淆一个简单的 32 位 AND 函数会产生近 12GB 的程序。

rss · CoinTelegraph · 6月29日 10:53

**背景**: 不可区分混淆（iO）是一种软件混淆形式，其中计算相同函数的任意两个程序的混淆版本在计算上是不可区分的。它被视为一种“密码学完备”原语，因为可用于构建几乎所有其他密码学原语。然而，已知的 iO 构造依赖于复杂的数学假设，距离实际部署还很遥远。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Indistinguishability_obfuscation">Indistinguishability obfuscation</a></li>
<li><a href="https://coinmarketcap.com/academy/article/vitalik-buterin-obfuscation-private-onchain-voting">Vitalik Buterin Says Obfuscation Could Enable Private On - Chain Voting</a></li>
<li><a href="https://coinfractal.com/vitalik-buterin-indistinguishability-obfuscation-private-onchain-voting/">Vitalik: Obfuscation Could Power Private Onchain Voting</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#voting`, `#privacy`, `#blockchain`, `#Ethereum`

---

<a id="item-10"></a>
## [国际清算银行警告 AI 投资热潮或引发全球金融危机](https://cointelegraph.com/news/bis-sounds-alarm-on-ai-exuberance-as-debt-fueled-boom-risks-bust?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) ⭐️ 6.0/10

国际清算银行（BIS）警告称，由债务和高杠杆非银行结构推动的过度 AI 投资可能导致全球金融不稳定。 这一警告突显了可能影响全球金融市场的系统性风险，因为杠杆化 AI 投资的快速平仓可能引发更广泛的金融危机。 BIS 报告指出，AI 投资融资严重依赖债务和高杠杆的非银行结构，这些结构可能迅速平仓并导致系统性破坏。

rss · CoinTelegraph · 6月29日 05:31

**背景**: 国际清算银行是一家为中央银行服务的国际金融机构，负责监测全球金融稳定。系统性风险是指金融服务中断的风险，可能对实体经济产生严重的负面影响。杠杆化非银行结构包括对冲基金和私募股权公司等大量借贷投资的实体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bis.org/publ/othp08.htm">Systemic risk: how to deal with it?</a></li>
<li><a href="https://www.fitchratings.com/research/banks/non-bank-entities-face-greater-us-leveraged-lending-risk-vs-banks-06-03-2020">Non-Bank Entities Face Greater US Leveraged Lending Risk vs Banks</a></li>

</ul>
</details>

**标签**: `#AI`, `#finance`, `#systemic risk`, `#BIS`

---