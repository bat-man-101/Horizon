---
layout: default
title: "Horizon Summary: 2026-06-30 (ZH)"
date: 2026-06-30
lang: zh
---

> 从 156 条内容中筛选出 11 条重要资讯。

---

1. [vLLM v0.24.0 支持 MiniMax-M3，优化 DeepSeek-V4](#item-1) ⭐️ 8.0/10
2. [shot-scraper video 录制代理演示视频](#item-2) ⭐️ 8.0/10
3. [OpenAI 推出基因组学 AI 基准 GeneBench-Pro](#item-3) ⭐️ 8.0/10
4. [核心转储流行病学：修复一个 18 年的旧漏洞](#item-4) ⭐️ 8.0/10
5. [特斯拉在奥斯汀开始测试无方向盘 Cybercab](#item-5) ⭐️ 8.0/10
6. [Arcturus 纳米铜有望将电网损耗减半](#item-6) ⭐️ 8.0/10
7. [亚马逊斥资 10 亿美元成立 FDE 组织，专注 AI 代理部署](#item-7) ⭐️ 8.0/10
8. [纳斯达克将市场数据分发扩展至区块链](#item-8) ⭐️ 7.0/10
9. [人工智能可改变乳腺癌检测与复发预测](#item-9) ⭐️ 7.0/10
10. [MIT 问答探讨当前与未来的智能体 AI](#item-10) ⭐️ 7.0/10
11. [国际象棋特级大师批评 AI 愿景者的理解](#item-11) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [vLLM v0.24.0 支持 MiniMax-M3，优化 DeepSeek-V4](https://github.com/vllm-project/vllm/releases/tag/v0.24.0) ⭐️ 8.0/10

vLLM v0.24.0 新增了对 MiniMax-M3 模型的支持，并对 DeepSeek-V4 进行了重大性能优化，包括 FlashInfer 稀疏索引缓存和预填充分块规划优化。该版本还将 Model Runner V2 扩展为默认支持量化模型，并新增了流式解析引擎。 该版本通过支持 MiniMax-M3 和 DeepSeek-V4 等前沿模型，显著扩展了 vLLM 的模型生态系统，这些模型对编程、智能体任务和长上下文推理至关重要。性能优化降低了推理延迟和成本，惠及依赖 vLLM 进行生产部署的整个 AI/ML 社区。 该版本包含来自 256 位贡献者的 571 次提交，其中 77 位是新贡献者。关键技术新增包括 MiniMax-M3 的 MXFP4 支持、DeepSeek-V4 的集群协作 topK 内核，以及 DeepEP v2 的集成以支持专家并行。

github · khluu · 6月29日 19:41

**背景**: vLLM 是一个开源的高吞吐量大语言模型推理引擎，使用 PagedAttention 实现高效内存管理。MiniMax-M3 是一个具有 100 万上下文和原生多模态能力的前沿开放权重模型，而 DeepSeek-V4 是一个拥有高达 1.6 万亿参数的巨型 MoE 模型。此版本延续了 vLLM 快速迭代以支持最新最大模型的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.minimax.io/models/text/m3">MiniMax M3 - Coding & Agentic Frontier, 1M Context, Multimodal | MiniMax</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro">deepseek-ai/DeepSeek-V4-Pro · Hugging Face</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#DeepSeek-V4`, `#MiniMax-M3`, `#performance optimization`

---

<a id="item-2"></a>
## [shot-scraper video 录制代理演示视频](https://simonwillison.net/2026/Jun/30/shot-scraper-video/#atom-everything) ⭐️ 8.0/10

Simon Willison 发布了 shot-scraper 1.10，新增了 'shot-scraper video' 命令，该命令接受 storyboard.yml 文件并使用 Playwright 录制 Web 应用程序操作的视频。示例视频演示了从粘贴的 CSV/TSV/JSON 数据在 Datasette 中创建新表。 该工具使编码代理能够生成其工作的视觉证据，解决了验证代理生成代码的关键需求。通过提供具体的视频演示，它弥合了自动化代理与人工审查之间的差距。 storyboard.yml 文件定义了操作流程，包括服务器设置、URL、视口、光标可见性、等待条件、JavaScript 注入以及一系列场景（包含点击和暂停等操作）。该命令支持 --auth 用于身份验证 cookie 和 --mp4 输出格式。

rss · Simon Willison · 6月30日 16:54

**背景**: shot-scraper 是一个基于 Playwright 的命令行工具，用于自动截取网站截图。Playwright 是微软开发的跨浏览器 Web 自动化和测试框架。新的 video 命令将 shot-scraper 的能力从静态截图扩展到动态视频录制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/30/shot-scraper-video/">Have your agent record video demos of its work with shot ...</a></li>
<li><a href="https://github.com/simonw/shot-scraper">GitHub - simonw/shot-scraper: A command-line utility for ... Simon Willison’s Weblog - vuink.com shot-scraper · PyPI shot-scraper - Datasette shot-scraper/docs/installation.md at main · simonw/shot-scraper Simon Willison on shot-scraper</a></li>
<li><a href="https://playwright.dev/">Fast and reliable end-to-end testing for modern web apps ...</a></li>

</ul>
</details>

**标签**: `#developer-tools`, `#testing`, `#AI-agents`, `#playwright`, `#video-recording`

---

<a id="item-3"></a>
## [OpenAI 推出基因组学 AI 基准 GeneBench-Pro](https://openai.com/index/introducing-genebench-pro) ⭐️ 8.0/10

OpenAI 推出了 GeneBench-Pro，这是一个扩展的基准测试，用于评估 AI 智能体在基因组学、定量生物学和转化生物医学中复杂多阶段科学分析的表现。 该基准测试满足了生命科学领域对 AI 进行真实评估的需求，可能加速基因组学和个性化医疗中由 AI 驱动的发现。 GeneBench-Pro 包含比其前身 GeneBench 更广泛领域中的更难问题，旨在捕捉真实世界计算生命科学问题的复杂性。

rss · OpenAI Blog · 6月30日 00:00

**背景**: AI 基准测试是衡量 AI 模型在特定任务上表现的标准测试。GeneBench-Pro 专注于基因组学中的多阶段统计推理，要求 AI 智能体执行类似于计算生物学家所做的真实分析。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-genebench-pro/">Introducing GeneBench-Pro - OpenAI</a></li>
<li><a href="https://www.biorxiv.org/content/10.64898/2026.06.29.735386v1">GeneBench-Pro: Evaluating Multistage Statistical Reasoning ...</a></li>
<li><a href="https://cdn.openai.com/pdf/21938268-21af-442f-af93-3b2249afb241/genebench-pro.pdf">GeneBench-Pro:EvaluatingMultistageStatisticalReasoning ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#benchmark`, `#genomics`, `#biology`, `#OpenAI`

---

<a id="item-4"></a>
## [核心转储流行病学：修复一个 18 年的旧漏洞](https://openai.com/index/core-dump-epidemiology-data-infrastructure-bug) ⭐️ 8.0/10

OpenAI 工程师发布了一份白皮书，详细介绍了他们的“核心转储流行病学”方法，该方法通过大规模分析核心转储来调试罕见的基础设施崩溃。这种方法在他们的 AI 基础设施中发现了一个硬件故障和一个存在 18 年的软件漏洞。 这种大规模核心转储分析的新颖应用展示了一种提高复杂分布式系统可靠性的强大技术。这些发现突显了长期存在的漏洞和硬件故障如何未被发现，该方法可被其他组织采用以增强其基础设施调试能力。 该技术被称为“核心转储流行病学”，因为它将崩溃数据视为疾病爆发，分析跨多台机器的模式。这个存在 18 年的漏洞位于一个广泛使用的开源库中，而硬件故障涉及一个微妙的内存损坏问题。

rss · OpenAI Blog · 6月30日 00:00

**背景**: 核心转储是一个文件，包含进程崩溃时内存的快照，通常由 Linux 内核在程序异常终止（例如由于段错误）时生成。分析核心转储有助于开发人员了解崩溃的根本原因。然而，在大规模系统中，手动检查单个核心转储是不切实际的；OpenAI 的方法聚合和关联数千台机器上的崩溃数据，以识别常见模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.siliconreport.com/openai-details-core-dump-epidemiology-for-infrastructure-debugging-8b6d27b1">OpenAI Details 'Core Dump Epidemiology' for Infrastructure ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Core_dump">Core dump - Wikipedia</a></li>

</ul>
</details>

**标签**: `#debugging`, `#infrastructure`, `#core dump`, `#reliability`, `#OpenAI`

---

<a id="item-5"></a>
## [特斯拉在奥斯汀开始测试无方向盘 Cybercab](https://techcrunch.com/2026/06/30/tesla-starts-testing-cybercab-without-pedals-or-a-steering-wheel-in-austin/) ⭐️ 8.0/10

特斯拉已开始在德克萨斯州奥斯汀的公共道路上测试其 Cybercab，这是一款没有踏板或方向盘的完全自动驾驶双座车辆。这是自 2026 年 2 月投产以来，该车辆首次在现实世界中部署。 此次测试是朝着推出特斯拉长期承诺的机器人出租车网络迈出的关键一步，可能颠覆网约车行业。成功将验证特斯拉的全自动驾驶技术，并为商业自动驾驶车队铺平道路。 Cybercab 专为两名乘客设计，完全依赖特斯拉的全自动驾驶（FSD）软件，没有手动控制装置。特斯拉于 2025 年 6 月在奥斯汀有限度地推出了机器人出租车服务，而 Cybercab 测试旨在扩展该服务。

rss · 36氪 - 科技 · 6月30日 15:32

**背景**: 特斯拉 Cybercab 最初于 2024 年 10 月作为概念车亮相，当时有 20 辆原型车在活动中提供短途试乘。它是一款纯电动汽车，旨在作为特斯拉机器人出租车叫车服务的一部分运营。特斯拉在自动驾驶承诺方面一直面临质疑，但此次测试代表了向前迈出的切实一步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cybercab">Cybercab</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Robotaxi">Tesla Robotaxi - Wikipedia</a></li>
<li><a href="https://www.caranddriver.com/news/a71590701/tesla-cybercab-specs-epa-documents-revealed/">We Have New Tesla Cybercab Specs Before You're Supposed to See Them Thanks to EPA Documents</a></li>

</ul>
</details>

**标签**: `#Tesla`, `#autonomous vehicles`, `#robotaxi`, `#self-driving`

---

<a id="item-6"></a>
## [Arcturus 纳米铜有望将电网损耗减半](https://techcrunch.com/2026/06/30/arcturus-could-halve-the-grids-electrical-losses-using-its-nano-infused-copper/) ⭐️ 8.0/10

隐秘初创公司 Arcturus 开发了一种基于激光的工艺，将碳纳米材料注入铜中，显著提高了导电性，有望将电网传输损耗降低高达 50%。 如果实现规模化，这项技术可以显著提高全球电网的能源效率，减少电力浪费，并在无需新建发电厂的情况下降低碳排放。 阿贡国家实验室测量发现，纳米碳注入的铜薄膜导电性提高了约 30%，而 Arcturus 声称其工艺在块体导体中可实现更高的增益。

rss · 36氪 - 科技 · 6月30日 15:01

**背景**: 电网因铜线和铝线的电阻，会以热量形式损失约 5-10%的传输能量。提高导体导电性可减少这些损耗，但传统合金方法已接近基本极限。纳米碳注入（如添加石墨烯或碳纳米管）通过创建更高效的电子路径，提供了一条超越这些极限的途径。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/30/arcturus-could-halve-the-grids-electrical-losses-using-its-nano-infused-copper/">Arcturus could halve the grid’s electrical losses using its nano-infused copper | TechCrunch</a></li>
<li><a href="https://www.anl.gov/amd/nanocarboninfused-metallic-conductors">Nanocarbon-infused Metallic Conductors | Argonne National Laboratory</a></li>

</ul>
</details>

**标签**: `#materials science`, `#energy`, `#nanotechnology`, `#grid infrastructure`

---

<a id="item-7"></a>
## [亚马逊斥资 10 亿美元成立 FDE 组织，专注 AI 代理部署](https://techcrunch.com/2026/06/30/amazon-launches-new-1-billion-fde-org-following-openai-and-anthropic/) ⭐️ 8.0/10

亚马逊云服务（AWS）宣布成立一个耗资 10 亿美元的内部组织，由前向部署工程师（FDE）组成，他们将嵌入客户公司，部署专门构建的 AI 代理。此举紧随 OpenAI 和 Anthropic 之后。 这项投资标志着行业正从通用模型转向专门化、客户定制的 AI 代理部署，通过确保更快、更量身定制的实施，可能加速企业对 AI 的采用。 FDE 模式由 Palantir 首创，工程师在客户现场工作，定制和部署解决方案；亚马逊的新组织将专注于快速介入，并通过专门构建的代理使客户能够自主运营。

rss · 36氪 - 科技 · 6月30日 15:00

**背景**: 前向部署工程师（FDE）是直接与客户组织合作，在运营环境中开发、定制和部署技术解决方案的软件工程师。专门构建的 AI 代理是为特定任务设计的专用自主系统，与通用 AI 模型形成对比。亚马逊此举延续了 OpenAI 和 Anthropic 等 AI 公司创建 FDE 团队以帮助企业有效部署 AI 的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/30/amazon-launches-new-1-billion-fde-org-following-openai-and-anthropic/">Amazon launches new $1 billion FDE org, following OpenAI and Anthropic | TechCrunch</a></li>
<li><a href="https://en.wikipedia.org/wiki/Forward_Deployed_Engineer">Forward Deployed Engineer - Wikipedia</a></li>
<li><a href="https://theriseofthedigitalworkforce.cio.com/drive-ai-value-build-trust-lead-change/why-purpose-built-agents-are-the-future-of-ai-at-work/">Why purpose-built agents are the future of AI at work</a></li>

</ul>
</details>

**标签**: `#AI`, `#Amazon`, `#AI Agents`, `#Enterprise`, `#Investment`

---

<a id="item-8"></a>
## [纳斯达克将市场数据分发扩展至区块链](https://www.coindesk.com/markets/2026/06/30/nasdaq-expands-distribution-of-its-market-data-into-blockchain-infrastructure) ⭐️ 7.0/10

纳斯达克宣布将其市场数据分发扩展至区块链基础设施，将传统金融数据流与去中心化技术相结合。 此举标志着区块链在核心金融基础设施中的主流采用日益增长，可能提高市场数据的透明度、效率和可访问性，惠及更广泛的参与者。 该计划利用纳斯达克现有的市场数据流（如 Nasdaq Basic 和 Nasdaq Last Sale），通过区块链网络进行分发，但具体技术细节和时间表尚未披露。

rss · CoinDesk · 6月30日 13:00

**背景**: 区块链技术因其提供不可篡改、透明和实时数据共享的潜力，正越来越多地被金融机构采用。纳斯达克的举措与银行和交易所探索区块链用于市场数据分发、代币化和结算的更广泛趋势相一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nasdaq.com/solutions/nasdaq-market-data-feeds">Nasdaq Market Data Feeds | Real-time Global Stock Data</a></li>
<li><a href="https://www.weforum.org/stories/2026/01/new-foundation-global-finance-dialogue-between-banks-and-blockchains/">Global finance’s new foundation: banks and blockchains</a></li>

</ul>
</details>

**标签**: `#blockchain`, `#finance`, `#Nasdaq`, `#market data`, `#fintech`

---

<a id="item-9"></a>
## [人工智能可改变乳腺癌检测与复发预测](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBPbkVuSFFDbFF2YU9rUHhQZ09qZFg0YzdPYllxbXIxWXdkM3diaGZKNllMVEhMdC1ucWlacDNsdmcybzFScThUMXEtMzZWQ29mYmhHRkhjSW9MQU1p?oc=5) ⭐️ 7.0/10

最近的一篇文章强调，人工智能在改善乳腺癌检测和预测复发方面显示出潜力，可能改变临床工作流程。 这一进展可能带来更早、更准确的诊断，减少假阳性并改善患者预后，同时实现个性化复发监测。 文章未指定具体的 AI 模型或数据集，但表明 AI 工具正在开发中，用于分析乳腺 X 光片和其他影像数据以识别癌症迹象和复发风险。

google_news · EurekAlert! · 6月30日 16:33

**背景**: 乳腺癌是全球最常见的癌症之一，早期检测对成功治疗至关重要。传统的筛查方法如乳腺 X 光摄影存在局限性，包括假阳性和漏诊。人工智能，尤其是深度学习，在医学影像中显示出潜力，能够识别人类肉眼可能无法察觉的模式。

**标签**: `#AI`, `#healthcare`, `#breast cancer`, `#machine learning`

---

<a id="item-10"></a>
## [MIT 问答探讨当前与未来的智能体 AI](https://news.google.com/rss/articles/CBMidkFVX3lxTE5RM1ZBZHlsbkR4dlJscXJLMkhFUzN1S280eXBsV1hCXzdCOTBraWZ1cUt1SUhqXzBUbThPSnBQdWpKTTI2aXdxQTdHbk9SM1d2NGluUXZ0cWktNzdWeS1xZHRQcVhDcWs5M2R4YXdUTGVvMThCRXc?oc=5) ⭐️ 7.0/10

MIT News 发表了一篇问答文章，探讨了智能体 AI 的当前状态及其期望的未来，并包含了专家见解。 这篇文章为智能体 AI 提供了权威视角，智能体 AI 是快速发展的领域，代表了生成式 AI 之后的下一步，有可能通过自主决策改变各行各业。 智能体 AI 系统是半自主或全自主的，能够自行感知、推理和行动，不同于传统生成式 AI 仅根据提示生成内容。

google_news · MIT News · 6月30日 15:30

**背景**: 智能体 AI，也称为 AI 代理或复合 AI 系统，指的是能够追求目标并以不同程度的自主性采取行动的 AI。这与生成式 AI 形成对比，后者专注于创建文本或图像等内容。MIT 的问答可能讨论了定义、当前能力、局限性以及对未来发展的期望。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained - MIT Sloan</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-ai-vs-generative-ai">Agentic AI vs. generative AI - IBM</a></li>

</ul>
</details>

**标签**: `#agentic AI`, `#AI research`, `#MIT`, `#future of AI`

---

<a id="item-11"></a>
## [国际象棋特级大师批评 AI 愿景者的理解](https://news.google.com/rss/articles/CBMikwFBVV95cUxNVmdsYmR1c0hxSGxxN2lLV1RmaEJQSUkxOS1jSW96LWF3NHU0RVVydEhGam1fd285Y2R4ajRVWHZDOUc4LWpVcnpzTzM0NldMdFlfZ0ZPNTl2Z3lRVGhuNm1XQ1gyM3J3bVFVMlpVa0ljN2EzU1BfeWFGNE5xcHJCWGkta0N4OFFta0dhQ2JtX2xpUE0?oc=5) ⭐️ 7.0/10

一位国际象棋特级大师在《华盛顿邮报》发表评论文章，指出 AI 愿景者误解了人类智能和决策的关键方面。 这位顶级棋手对人与 AI 对手都有深刻体验，其观点挑战了 AI 将很快超越所有人类认知能力的普遍说法。 这位特级大师可能利用自己与 AI 国际象棋引擎对弈的经历，强调 AI 缺乏的直觉、创造力和战略思维等方面的差异。

google_news · The Washington Post · 6月30日 17:02

**背景**: 国际象棋长期以来一直是 AI 进步的基准，像深蓝和 AlphaZero 这样的引擎击败了世界冠军。然而，特级大师们经常指出，AI 的玩法与人类根本不同，侧重于蛮力计算而非人类式的理解。

**标签**: `#AI`, `#chess`, `#opinion`, `#cognition`, `#human vs AI`

---