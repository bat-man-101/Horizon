---
layout: default
title: "Horizon Summary: 2026-06-30 (ZH)"
date: 2026-06-30
lang: zh
---

> 从 151 条内容中筛选出 10 条重要资讯。

---

1. [vLLM v0.24.0 新增 MiniMax-M3 支持与 DeepSeek-V4 优化](#item-1) ⭐️ 8.0/10
2. [OpenAI 通过核心转储分析修复了 18 年的旧 bug](#item-2) ⭐️ 8.0/10
3. [特斯拉在奥斯汀开始测试无方向盘 Cybercab](#item-3) ⭐️ 8.0/10
4. [亚马逊斥资 10 亿美元成立 FDE 部门部署 AI 代理](#item-4) ⭐️ 8.0/10
5. [韩国承诺超 5500 亿美元缓解内存芯片短缺](#item-5) ⭐️ 8.0/10
6. [AI 破解 RNA 剪接中的长程 DNA 信号](#item-6) ⭐️ 8.0/10
7. [纽约人寿 8000 亿美元资产管理公司推出首个代币化基金](#item-7) ⭐️ 7.0/10
8. [MIT 问答探讨当前与未来的智能体 AI](#item-8) ⭐️ 7.0/10
9. [国际象棋特级大师批评 AI 愿景者的盲点](#item-9) ⭐️ 7.0/10
10. [OpenAI 报告 ChatGPT 全球采用增长](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [vLLM v0.24.0 新增 MiniMax-M3 支持与 DeepSeek-V4 优化](https://github.com/vllm-project/vllm/releases/tag/v0.24.0) ⭐️ 8.0/10

vLLM v0.24.0 引入了对 MiniMax-M3 模型的支持，并为 DeepSeek-V4 提供了重大性能优化，包括 FlashInfer 稀疏索引缓存和集群协作 topK 内核。 此版本显著提升了两款前沿模型的推理效率，使得在生产环境中部署大型语言模型更快、更具成本效益。 FlashInfer 稀疏索引缓存将首 token 延迟（TTFT）降低 2–4%，而集群协作 topK 内核降低了 DeepSeek-V4 稀疏注意力的延迟。此版本包含来自 256 位贡献者的 571 次提交。

github · khluu · 6月29日 19:41

**背景**: vLLM 是一个高吞吐量、内存高效的大型语言模型推理引擎。DeepSeek-V4 和 MiniMax-M3 是先进的模型，需要优化的内核以实现高效服务。FlashInfer 是一个提供高性能注意力实现的内核库，而集群协作 topK 内核是用于稀疏注意力索引选择的自定义内核。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.flashinfer.ai/api/sparse.html">flashinfer.sparse - FlashInfer 0.6.13 documentation</a></li>
<li><a href="https://github.com/flashinfer-ai/flashinfer">GitHub - flashinfer-ai/flashinfer: FlashInfer: Kernel Library ... flashinfer_sparse - vLLM FlashInfer 0.2 - Efficient and Customizable Kernels for LLM ... FlashInfer: Efficient and Customizable Attention Engine for ... flashinfer/flashinfer/sparse.py at main · flashinfer-ai ... Dissecting FlashInfer - A Systems Perspective on High ...</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#DeepSeek`, `#MiniMax`, `#performance optimization`

---

<a id="item-2"></a>
## [OpenAI 通过核心转储分析修复了 18 年的旧 bug](https://openai.com/index/core-dump-epidemiology-data-infrastructure-bug) ⭐️ 8.0/10

OpenAI 工程师通过大规模核心转储分析来调试罕见的基础设施崩溃，发现了一个硬件故障和一个存在 18 年的软件 bug。 这展示了一种新颖的、数据驱动的调试大规模系统中罕见故障的方法，对整个行业的可靠性工程具有启示意义。 该 bug 持续了 18 年，分析需要收集并检查数千台机器的核心转储文件才能确定根本原因。

rss · OpenAI Blog · 6月30日 00:00

**背景**: 核心转储是程序崩溃时内存的快照，用于事后调试。大规模分析核心转储涉及聚合和关联来自许多机器的数据以发现共同模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://stackoverflow.com/questions/8305866/how-do-i-analyze-a-programs-core-dump-file-with-gdb-when-it-has-command-line-pa">linux - How do I analyze a program's core dump file with GDB ... Code sample</a></li>
<li><a href="https://dzone.com/articles/debugging-core-dump-files-on-linux-a-detailed-guid">Debugging Linux Core Dump Files: A Detailed Guide - DZone</a></li>

</ul>
</details>

**标签**: `#debugging`, `#infrastructure`, `#reliability`, `#core dump`, `#OpenAI`

---

<a id="item-3"></a>
## [特斯拉在奥斯汀开始测试无方向盘 Cybercab](https://techcrunch.com/2026/06/30/tesla-starts-testing-cybercab-without-pedals-or-a-steering-wheel-in-austin/) ⭐️ 8.0/10

特斯拉已开始在德克萨斯州奥斯汀的公共道路上测试没有踏板或方向盘的 Cybercab 机器人出租车，这标志着向推出全自动驾驶叫车服务迈出了重要一步。 此次测试使埃隆·马斯克长期承诺的机器人出租车网络更接近现实，可能颠覆交通运输行业，并加剧与 Waymo 和 Zoox 等其他自动驾驶公司的竞争。 Cybercab 是一款双座全自动驾驶电动车，设计上无手动控制装置；预计配备约 50 千瓦时电池组，EPA 估计续航里程近 280 英里。

rss · 36氪 - 科技 · 6月30日 15:32

**背景**: 特斯拉于 2024 年 10 月首次发布 Cybercab 概念车，作为其机器人出租车愿景的一部分。该公司的全自动驾驶（FSD）软件支撑其自动驾驶能力，而特斯拉机器人出租车服务于 2025 年 6 月在奥斯汀有限推出，当时使用的车辆仍配备手动控制装置。移除方向盘和踏板代表着向 L5 级自动驾驶的重大飞跃。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Cybercab">Tesla Cybercab - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Robotaxi">Tesla Robotaxi - Wikipedia</a></li>

</ul>
</details>

**标签**: `#autonomous vehicles`, `#Tesla`, `#robotaxi`, `#transportation`, `#AI`

---

<a id="item-4"></a>
## [亚马逊斥资 10 亿美元成立 FDE 部门部署 AI 代理](https://techcrunch.com/2026/06/30/amazon-launches-new-1-billion-fde-org-following-openai-and-anthropic/) ⭐️ 8.0/10

亚马逊云服务（AWS）宣布成立一个耗资 10 亿美元的新内部组织，专注于前部署工程师（FDE），他们将嵌入客户公司以部署定制 AI 代理。此举效仿了 OpenAI 和 Anthropic 的类似举措，强调快速部署和客户自给自足。 这项投资表明亚马逊致力于占领企业 AI 代理市场，随着公司寻求实际部署解决方案，该市场正在快速增长。通过将工程师直接嵌入客户，亚马逊旨在加速采用并减少部署摩擦，可能为企业 AI 服务树立新标准。 由 Palantir 首创的 FDE 模式涉及工程师与客户现场合作，定制和部署技术解决方案。亚马逊的新部门将专注于定制 AI 代理，工程师嵌入公司进行快速合作，并确保客户最终能独立管理代理。

rss · 36氪 - 科技 · 6月30日 15:00

**背景**: 前部署工程师（FDE）是与客户组织紧密合作，在运营环境中开发、定制和部署技术解决方案的专业人员。这种模式在管理 AI 部署方面越来越受欢迎，因为它弥合了产品开发与实际应用之间的差距。亚马逊、OpenAI 和 Anthropic 都在投资这种方法，以帮助企业更有效地采用 AI 代理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/30/amazon-launches-new-1-billion-fde-org-following-openai-and-anthropic/">Amazon launches new $1 billion FDE org, following OpenAI and Anthropic | TechCrunch</a></li>
<li><a href="https://en.wikipedia.org/wiki/Forward_Deployed_Engineer">Forward Deployed Engineer - Wikipedia</a></li>
<li><a href="https://oodaloop.com/briefs/technology/amazon-launches-new-1-billion-fde-org-following-openai-and-anthropic/">Amazon launches new $1 billion FDE org, following OpenAI and Anthropic — OODAloop</a></li>

</ul>
</details>

**标签**: `#Amazon`, `#AI agents`, `#enterprise AI`, `#investment`, `#deployment`

---

<a id="item-5"></a>
## [韩国承诺超 5500 亿美元缓解内存芯片短缺](https://techcrunch.com/2026/06/29/south-korean-tech-giants-commit-over-550b-to-ease-ramageddon/) ⭐️ 8.0/10

韩国顶级内存芯片制造商，包括三星和 SK 海力士，承诺投入超过 5500 亿美元建设新的制造设施，以应对被称为“RAMageddon”的全球内存短缺，并增强 AI 能力。 这项巨额投资旨在缓解自 2025 年以来影响消费和企业 PC 市场的严重内存供应短缺，同时将韩国定位为 AI 基础设施的关键参与者。 据行业分析师称，此次短缺是由于制造能力结构性转向高利润的 AI 数据中心产品所致，预计将持续到至少 2028 年。

rss · 36氪 - 科技 · 6月29日 18:07

**背景**: 全球内存供应短缺，有时被称为“RAMageddon”或“RAMpocalypse”，始于 2025 年，主要影响 DRAM 和 NAND 闪存。与早期疫情时代的芯片短缺不同，此次短缺是由于制造商优先生产 AI 相关芯片而非消费级内存，导致稀缺和价格上涨。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RAMmageddon">RAMmageddon</a></li>
<li><a href="https://en.wikipedia.org/wiki/2024–present_global_memory_supply_shortage">2025–present global memory supply shortage - Wikipedia</a></li>
<li><a href="https://www.cnet.com/tech/computing/tech-companies-are-freaking-out-about-ramageddon/">Tech Companies Are Freaking Out About RAMageddon - CNET</a></li>

</ul>
</details>

**标签**: `#memory chips`, `#AI infrastructure`, `#semiconductor investment`, `#South Korea`, `#hardware`

---

<a id="item-6"></a>
## [AI 破解 RNA 剪接中的长程 DNA 信号](https://news.google.com/rss/articles/CBMiXEFVX3lxTFAyeGJFZG9KOURQZzdSLUNuZnZfNl9vblRoeUhDWWVyTS05VHlkVzZFaVRPYlRZYnA5dTQ1YWdlR0Q2MDl0RXpCd3k3UHFhenhRZVdWX0RNU1A1dmJa?oc=5) ⭐️ 8.0/10

研究人员开发了一种 AI 模型，能够破解调控 RNA 剪接的长程 DNA 信号，这是基因表达的关键过程。这一突破由 EurekAlert!报道，代表了理解远端 DNA 元件如何影响剪接决策的重大进展。 这项工作可能改变我们对基因调控和疾病机制的理解，因为异常剪接与许多遗传疾病和癌症相关。AI 方法能够分析以前难以研究的长程基因组相互作用，可能带来新的治疗靶点。 该 AI 模型专门关注长程 DNA 信号，即位于受其影响的剪接位点远处的调控元件。该研究可能利用深度学习，根据数千到数百万碱基对距离的基因组序列上下文来预测剪接结果。

google_news · EurekAlert! · 6月30日 11:17

**背景**: RNA 剪接是从前体 mRNA 中去除内含子并将外显子连接起来形成成熟 mRNA 的过程。可变剪接允许单个基因产生多种蛋白质变体，其调控涉及近端和远端 DNA 元件。长程 DNA 信号，如增强子和沉默子，可以通过环化到靶点来影响剪接，但识别这些相互作用一直具有挑战性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RNA_splicing">RNA splicing - Wikipedia</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4360811/">Mechanism of alternative splicing and its regulation - PMC</a></li>
<li><a href="https://www.nature.com/articles/s41467-025-65077-4">DNALONGBENCH: a benchmark suite for long-range DNA prediction tasks | Nature Communications</a></li>

</ul>
</details>

**标签**: `#AI`, `#genomics`, `#RNA splicing`, `#bioinformatics`, `#machine learning`

---

<a id="item-7"></a>
## [纽约人寿 8000 亿美元资产管理公司推出首个代币化基金](https://www.coindesk.com/business/2026/06/29/new-york-life-makes-tokenization-debut-with-onchain-high-yield-bond-fund-with-centrifuge) ⭐️ 7.0/10

纽约人寿旗下 8000 亿美元资产管理公司通过 Centrifuge 平台推出了其首个代币化基金，标志着机构采用区块链资产管理的重要里程碑。 此举表明机构对代币化的信心不断增强，可能为更多传统金融巨头将区块链技术整合到资产管理中铺平道路，从而提高效率和流动性。 该基金是一种高收益债券基金，在 Centrifuge 基础设施上实现代币化，该基础设施提供自动化合规、多链覆盖和深度 DeFi 连接。Centrifuge 是最早且最大的代币化平台之一，连接传统资本市场与链上轨道。

rss · CoinDesk · 6月30日 11:20

**背景**: 代币化是将传统投资基金份额表示为区块链上的数字代币的过程，取代传统的过户代理和经纪人。这项技术可以简化运营、降低成本并实现部分所有权。Centrifuge 是代币化现实世界资产（包括基金、私人信贷和房地产）的领先平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://centrifuge.io/">Centrifuge | Infrastructure for Onchain Asset Management</a></li>
<li><a href="https://www.gemini.com/cryptopedia/centrifuge-crypto-tinlake-tokenization-real-world-assets">Centrifuge: Tokenization of Real-World Assets | Gemini</a></li>
<li><a href="https://chain.link/article/fund-tokenization">What Is Fund Tokenization? | Chainlink</a></li>

</ul>
</details>

**标签**: `#tokenization`, `#institutional adoption`, `#DeFi`, `#asset management`, `#blockchain`

---

<a id="item-8"></a>
## [MIT 问答探讨当前与未来的智能体 AI](https://news.google.com/rss/articles/CBMidkFVX3lxTE5RM1ZBZHlsbkR4dlJscXJLMkhFUzN1S280eXBsV1hCXzdCOTBraWZ1cUt1SUhqXzBUbThPSnBQdWpKTTI2aXdxQTdHbk9SM1d2NGluUXZ0cWktNzdWeS1xZHRQcVhDcWs5M2R4YXdUTGVvMThCRXc?oc=5) ⭐️ 7.0/10

MIT News 发布了一篇问答文章，通过 MIT 研究人员的专家见解，审视了智能体 AI 的当前状态及其期望的未来发展方向。 这场讨论澄清了智能体 AI 不断演变的定义，这对于 AI 系统变得更加自主并能够执行多步骤任务至关重要，将影响从医疗到金融等行业。 文章可能区分了智能体 AI 与生成式 AI，强调目标导向行为、工具使用和有限监督是关键属性。

google_news · MIT News · 6月30日 15:30

**背景**: 智能体 AI 是指能够自主感知、推理并行动以实现特定目标的 AI 系统，通常使用大语言模型进行控制。与生成式 AI（创建内容）不同，智能体 AI 专注于在最少人工干预下完成任务。随着 AI 代理在客户服务和机器人等实际应用中的部署，这一概念日益受到关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained | MIT Sloan</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-ai">What is Agentic AI? | IBM</a></li>

</ul>
</details>

**标签**: `#AI`, `#agentic AI`, `#MIT`, `#research`

---

<a id="item-9"></a>
## [国际象棋特级大师批评 AI 愿景者的盲点](https://news.google.com/rss/articles/CBMikwFBVV95cUxNVmdsYmR1c0hxSGxxN2lLV1RmaEJQSUkxOS1jSW96LWF3NHU0RVVydEhGam1fd285Y2R4ajRVWHZDOUc4LWpVcnpzTzM0NldMdFlfZ0ZPNTl2Z3lRVGhuNm1XQ1gyM3J3bVFVMlpVa0ljN2EzU1BfeWFGNE5xcHJCWGkta0N4OFFta0dhQ2JtX2xpUE0?oc=5) ⭐️ 7.0/10

来自高级人类专家的这一观点挑战了 AI 将很快在所有领域超越人类认知的主流叙事，凸显了当前 AI 系统的持久局限性。 这位特级大师强调，人类决策依赖于模式识别、直觉和情境理解，而像大语言模型这样的 AI 模型无法复制。该文章是评论而非同行评审研究，但由于作者的专业知识而具有分量。

google_news · The Washington Post · 6月30日 15:32

**背景**: 国际象棋长期以来一直是 AI 进步的基准，从 1997 年深蓝击败加里·卡斯帕罗夫，到 AlphaZero 通过自我对弈掌握棋局。然而，特级大师们认为，国际象棋不仅仅是蛮力计算，还包括心理因素和创造力，这是当前 AI 所缺乏的。

**标签**: `#AI`, `#chess`, `#opinion`, `#human intelligence`

---

<a id="item-10"></a>
## [OpenAI 报告 ChatGPT 全球采用增长](https://openai.com/index/how-chatgpt-adoption-has-expanded) ⭐️ 6.0/10

OpenAI 发布了新的 Signals 数据，显示 ChatGPT 的全球采用率正在增长，用户使用频率增加，并在不同地区和语言中探索更多功能。 这表明 ChatGPT 正更深入地融入用户的工作流程，可能推动对 AI 基础设施的进一步投资，并影响竞争对手如何定位自己的 AI 助手。 报告强调了多个地区和语言的增长，但未提供具体的采用数字或按行业或用例的细分。

rss · OpenAI Blog · 6月30日 09:00

**背景**: ChatGPT 是由 OpenAI 开发的基于大语言模型的聊天机器人，于 2022 年 11 月推出。使用频率和功能探索等采用指标有助于衡量用户如何将 AI 融入日常任务。

**标签**: `#ChatGPT`, `#AI adoption`, `#OpenAI`, `#LLMs`

---