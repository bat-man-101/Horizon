---
layout: default
title: "Horizon Summary: 2026-06-30 (ZH)"
date: 2026-06-30
lang: zh
---

> 从 150 条内容中筛选出 10 条重要资讯。

---

1. [vLLM v0.24.0 新增 MiniMax-M3 支持与 DeepSeek-V4 优化](#item-1) ⭐️ 8.0/10
2. [OpenAI 通过核心转储流行病学修复 18 年历史漏洞](#item-2) ⭐️ 8.0/10
3. [特斯拉在奥斯汀开始测试无方向盘和踏板的 Cybercab](#item-3) ⭐️ 8.0/10
4. [Arcturus 利用纳米铜将电网损耗减半](#item-4) ⭐️ 8.0/10
5. [亚马逊斥资 10 亿美元成立 FDE 部门，专注 AI 代理部署](#item-5) ⭐️ 8.0/10
6. [AI 破译 RNA 剪接背后的长程 DNA 信号](#item-6) ⭐️ 8.0/10
7. [纳斯达克将市场数据分发扩展至区块链](#item-7) ⭐️ 7.0/10
8. [MIT 问答：定义当今的智能体 AI 及其未来](#item-8) ⭐️ 7.0/10
9. [国际象棋特级大师批评 AI 愿景家](#item-9) ⭐️ 7.0/10
10. [OpenAI 报告 ChatGPT 全球采用增长](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [vLLM v0.24.0 新增 MiniMax-M3 支持与 DeepSeek-V4 优化](https://github.com/vllm-project/vllm/releases/tag/v0.24.0) ⭐️ 8.0/10

vLLM v0.24.0 新增了对 MiniMax-M3 模型的支持，并对 DeepSeek-V4 进行了重大优化，包括 FlashInfer 稀疏索引缓存和预填充块规划。该版本还扩展了 Model Runner V2，默认支持量化模型，并集成了 DeepEP v2 以实现专家并行。 此版本显著增强了 vLLM 对 MiniMax-M3 和 DeepSeek-V4 等前沿模型的支持，这些模型对长上下文推理和智能体任务至关重要。优化提高了推理吞吐量和延迟，惠及更广泛的 AI/ML 基础设施社区。 该版本包含来自 256 位贡献者的 571 次提交，新增了用于工具调用解析的流式解析器引擎以及对 DiffusionGemma 的支持。设备选择现在使用新的 `device_ids` 参数，而不是在内部设置 `CUDA_VISIBLE_DEVICES`。

github · khluu · 6月29日 19:41

**背景**: vLLM 是一个高吞吐量、内存高效的大型语言模型（LLM）推理和服务引擎，广泛用于生产级 AI 部署。MiniMax-M3 是一个多模态视觉语言模型，采用混合专家架构，支持高达 100 万 token 的上下文窗口；而 DeepSeek-V4 是一个庞大的 MoE 模型，总参数高达 1.6T。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm">GitHub - vllm-project/vllm: A high-throughput and memory-efficient inference and serving engine for LLMs · GitHub</a></li>
<li><a href="https://www.minimax.io/blog/minimax-m3">MiniMax M3: Frontier Coding, 1M Context, Native Multimodality — All in One Model - MiniMax Research | MiniMax</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro">deepseek-ai/DeepSeek-V4-Pro · Hugging Face</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#DeepSeek`, `#MiniMax`, `#open source`

---

<a id="item-2"></a>
## [OpenAI 通过核心转储流行病学修复 18 年历史漏洞](https://openai.com/index/core-dump-epidemiology-data-infrastructure-bug) ⭐️ 8.0/10

OpenAI 工程师利用大规模核心转储分析来调试罕见的基础设施崩溃，发现了一个硬件故障和一个存在 18 年的软件漏洞。 这展示了一种新颖的、流行病学式的调试大规模系统中罕见故障的方法，有望改善整个行业的可靠性工程实践。 该漏洞已存在 18 年，分析结合了数千台机器的核心转储数据以确定根本原因。修复涉及硬件更换和软件补丁。

rss · OpenAI Blog · 6月30日 00:00

**背景**: 核心转储是一个文件，包含进程崩溃时内存的快照，常用于事后调试。大规模系统会产生大量核心转储，像流行病学研究一样集体分析它们，可以揭示模式，从而定位难以捉摸的漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Core_dump">Core dump - Wikipedia</a></li>
<li><a href="https://sergioprado.blog/linux-core-dump-analysis/">Linux core dump analysis - sergioprado.blog</a></li>
<li><a href="https://dzone.com/articles/debugging-core-dump-files-on-linux-a-detailed-guid">Debugging Linux Core Dump Files: A Detailed Guide</a></li>

</ul>
</details>

**标签**: `#debugging`, `#infrastructure`, `#reliability`, `#core dump`, `#OpenAI`

---

<a id="item-3"></a>
## [特斯拉在奥斯汀开始测试无方向盘和踏板的 Cybercab](https://techcrunch.com/2026/06/30/tesla-starts-testing-cybercab-without-pedals-or-a-steering-wheel-in-austin/) ⭐️ 8.0/10

特斯拉已开始在德克萨斯州奥斯汀的公共道路上测试其无方向盘和踏板的 Cybercab 机器人出租车，这标志着向全自动驾驶叫车服务迈出了重要一步。 此次测试使埃隆·马斯克长期承诺的机器人出租车网络更接近现实，并可能加速自动驾驶汽车在叫车行业的普及，挑战 Waymo 和 Zoox 等竞争对手。 Cybercab 是一款专为自动驾驶设计的两座电动车，配备约 50 千瓦时的电池组，预计续航里程近 280 英里。生产始于 2026 年 2 月，该车旨在无需人工操控即可运行。

rss · 36氪 - 科技 · 6月30日 15:32

**背景**: 特斯拉多年来一直在开发全自动驾驶（FSD）软件，而 Cybercab 是为其机器人出租车网络专门打造的车辆。该公司于 2025 年 6 月在奥斯汀使用现有特斯拉车辆推出了有限的机器人出租车服务，但 Cybercab 代表了一个没有手动控制的专用自动驾驶平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Cybercab">Tesla Cybercab</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Robotaxi">Tesla Robotaxi - Wikipedia</a></li>
<li><a href="https://www.caranddriver.com/news/a71590701/tesla-cybercab-specs-epa-documents-revealed/">We Have New Tesla Cybercab Specs Before You're Supposed to See Them Thanks to EPA Documents</a></li>

</ul>
</details>

**标签**: `#Tesla`, `#autonomous vehicles`, `#robotaxi`, `#self-driving`

---

<a id="item-4"></a>
## [Arcturus 利用纳米铜将电网损耗减半](https://techcrunch.com/2026/06/30/arcturus-could-halve-the-grids-electrical-losses-using-its-nano-infused-copper/) ⭐️ 8.0/10

隐秘初创公司 Arcturus 开发了一种基于激光的工艺，将碳纳米材料注入铜中，显著提高了其导电性，并有可能将电网损耗减半。 如果成功，这项技术可以显著减少电力传输中的能源浪费，降低电网成本和碳排放。 该公司声称其纳米铜薄膜的电导率可提高多达 30%，并且块状导体也有望获得类似的提升。

rss · 36氪 - 科技 · 6月30日 15:01

**背景**: 电网因铜和铝导体的电阻而损失约 5-10% 的传输能量，以热量的形式散失。石墨烯等纳米碳材料具有优异的导电性，但难以与金属结合。Arcturus 使用激光将碳纳米材料嵌入铜中，制造出导电效率更高的复合材料。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/30/arcturus-could-halve-the-grids-electrical-losses-using-its-nano-infused-copper/">Arcturus could halve the grid’s electrical losses using its nano-infused copper | TechCrunch</a></li>
<li><a href="https://www.anl.gov/amd/nanocarboninfused-metallic-conductors">Nanocarbon-infused Metallic Conductors | Argonne National Laboratory</a></li>

</ul>
</details>

**标签**: `#nanotechnology`, `#energy`, `#materials science`, `#electrical grid`

---

<a id="item-5"></a>
## [亚马逊斥资 10 亿美元成立 FDE 部门，专注 AI 代理部署](https://techcrunch.com/2026/06/30/amazon-launches-new-1-billion-fde-org-following-openai-and-anthropic/) ⭐️ 8.0/10

亚马逊云服务（AWS）宣布成立一个耗资 10 亿美元的新内部组织，由前部署工程师（FDE）组成，他们将嵌入客户公司，部署专门构建的 AI 代理。此举紧随 OpenAI 和 Anthropic 之后。 这项投资标志着行业向专业化、实践型 AI 部署服务的重大趋势，通过提供专属工程支持和培养客户自给自足能力，可能加速企业对 AI 代理的采用。 新团队的工程师将专注于快速参与和客户自给自足，部署为特定任务而非通用聊天机器人设计的专用代理。FDE 模式由 Palantir 首创，并越来越多地用于 AI 部署。

rss · 36氪 - 科技 · 6月30日 15:00

**背景**: 前部署工程师（FDE）与客户紧密合作，在运营环境中开发、定制和部署技术解决方案。专用 AI 代理专注于一项特定任务并能采取行动，不同于通用 GPT 工具。亚马逊此举紧随 OpenAI 和 Anthropic 的类似投资，反映出对定制化 AI 解决方案的日益重视。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/30/amazon-launches-new-1-billion-fde-org-following-openai-and-anthropic/">Amazon launches new $1 billion FDE org, following OpenAI and Anthropic | TechCrunch</a></li>
<li><a href="https://en.wikipedia.org/wiki/Forward_Deployed_Engineer">Forward Deployed Engineer - Wikipedia</a></li>
<li><a href="https://www.salesforce.com/blog/autonomous-agents/">Why Purpose-Built Agents are the Future of AI at Work</a></li>

</ul>
</details>

**标签**: `#Amazon`, `#AI agents`, `#enterprise AI`, `#industry trend`

---

<a id="item-6"></a>
## [AI 破译 RNA 剪接背后的长程 DNA 信号](https://news.google.com/rss/articles/CBMiXEFVX3lxTFAyeGJFZG9KOURQZzdSLUNuZnZfNl9vblRoeUhDWWVyTS05VHlkVzZFaVRPYlRZYnA5dTQ1YWdlR0Q2MDl0RXpCd3k3UHFhenhRZVdWX0RNU1A1dmJa?oc=5) ⭐️ 8.0/10

研究人员开发了一种 AI 模型，能够识别并解读调控 RNA 剪接的长程 DNA 信号，这是基因表达的关键过程。该突破在 EurekAlert!上报道，代表了深度学习在基因组学中的新应用。 理解 RNA 剪接中的长程 DNA 信号有助于揭示遗传疾病机制并发现新的治疗靶点。这项工作展示了 AI 在解析此前难以研究的复杂生物机制方面的潜力。 该 AI 模型专门破译远离剪接位点的信号，这些信号传统上难以捕捉。研究强调了非编码 DNA 区域在调控剪接中的重要性。

google_news · EurekAlert! · 6月30日 11:17

**背景**: RNA 剪接是从前体 mRNA 中去除内含子并将外显子连接形成成熟 mRNA 的过程。长程 DNA 信号是位于剪接位点远处的调控元件，影响剪接效率和准确性。AI 模型能够学习基因组序列中传统方法难以检测的复杂模式。

**标签**: `#AI`, `#genomics`, `#RNA splicing`, `#deep learning`, `#bioinformatics`

---

<a id="item-7"></a>
## [纳斯达克将市场数据分发扩展至区块链](https://www.coindesk.com/markets/2026/06/30/nasdaq-expands-distribution-of-its-market-data-into-blockchain-infrastructure) ⭐️ 7.0/10

纳斯达克宣布将通过区块链基础设施分发其市场数据，将传统金融数据与去中心化技术相结合。 此举标志着区块链在传统金融领域的主流采用日益增长，可能提高市场数据分发的透明度和效率。 该计划利用区块链的不可篡改性和实时能力，为投资者和机构提供更安全、更及时的数据访问。

rss · CoinDesk · 6月30日 13:00

**背景**: 纳斯达克是一家全球证券交易所运营商，传统上通过中心化系统分发市场数据。区块链技术提供了一种去中心化账本，可以增强数据完整性并减少延迟。

**标签**: `#blockchain`, `#market data`, `#Nasdaq`, `#fintech`, `#infrastructure`

---

<a id="item-8"></a>
## [MIT 问答：定义当今的智能体 AI 及其未来](https://news.google.com/rss/articles/CBMidkFVX3lxTE5RM1ZBZHlsbkR4dlJscXJLMkhFUzN1S280eXBsV1hCXzdCOTBraWZ1cUt1SUhqXzBUbThPSnBQdWpKTTI2aXdxQTdHbk9SM1d2NGluUXZ0cWktNzdWeS1xZHRQcVhDcWs5M2R4YXdUTGVvMThCRXc?oc=5) ⭐️ 7.0/10

MIT News 发表了一篇问答文章，探讨了智能体 AI 系统的当前定义、能力以及期望的未来，其中包含了 MIT 研究人员的专家见解。 这篇文章为智能体 AI 提供了权威视角，这是一个快速发展的领域，可能重塑 AI 系统与世界的交互方式，因此对研究人员和从业者来说至关重要。 问答形式允许对智能体 AI 当前的局限性和潜力进行细致讨论，包括自主性、目标导向行为和安全考虑等主题。

google_news · MIT News · 6月30日 15:30

**背景**: 智能体 AI 指的是能够自主行动以实现目标的 AI 系统，区别于仅对提示做出响应的被动模型。这一概念对于构建能够在动态环境中规划、推理和执行任务的 AI 智能体至关重要。

**标签**: `#AI`, `#agentic AI`, `#research`, `#MIT`

---

<a id="item-9"></a>
## [国际象棋特级大师批评 AI 愿景家](https://news.google.com/rss/articles/CBMikwFBVV95cUxNVmdsYmR1c0hxSGxxN2lLV1RmaEJQSUkxOS1jSW96LWF3NHU0RVVydEhGam1fd285Y2R4ajRVWHZDOUc4LWpVcnpzTzM0NldMdFlfZ0ZPNTl2Z3lRVGhuNm1XQ1gyM3J3bVFVMlpVa0ljN2EzU1BfeWFGNE5xcHJCWGkta0N4OFFta0dhQ2JtX2xpUE0?oc=5) ⭐️ 7.0/10

一位国际象棋特级大师在《华盛顿邮报》发表评论文章，认为 AI 愿景家误解了人类智能和决策的关键方面。 来自 AI 已实现超人类表现领域的视角，对 AI 的局限性提出了细致批评，挑战了人类认知可被机器完全复制的说法。 这位特级大师可能利用与象棋 AI 的个人经验，强调人类直觉与机器计算之间的差异，但全文需付费阅读。

google_news · The Washington Post · 6月30日 15:32

**背景**: 自 1997 年深蓝击败加里·卡斯帕罗夫以来，国际象棋一直是 AI 的基准。现代象棋引擎如 Stockfish 和 AlphaZero 已超越人类特级大师，但这位大师认为 AI 仍缺乏对棋局的真正理解。

**标签**: `#AI`, `#chess`, `#opinion`, `#human intelligence`

---

<a id="item-10"></a>
## [OpenAI 报告 ChatGPT 全球采用增长](https://openai.com/index/how-chatgpt-adoption-has-expanded) ⭐️ 6.0/10

OpenAI 发布了新的 Signals 数据，显示 ChatGPT 在全球范围内的采用正在增长，用户使用量增加并探索更多功能。 这表明 ChatGPT 正更深入地融入各地区和语言的日常工作流程，可能加速各行业对 AI 的采用。 数据突出了跨地区和语言的增长，但报告缺乏关于扩张的具体指标或技术细节。

rss · OpenAI Blog · 6月30日 09:00

**背景**: ChatGPT 是 OpenAI 开发的对话式 AI 模型，于 2022 年底推出。其采用情况通过多种指标进行追踪，本报告提供了全球趋势的高层概述。

**标签**: `#ChatGPT`, `#AI adoption`, `#OpenAI`, `#trends`

---