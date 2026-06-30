---
layout: default
title: "Horizon Summary: 2026-06-30 (ZH)"
date: 2026-06-30
lang: zh
---

> 从 176 条内容中筛选出 11 条重要资讯。

---

1. [vLLM v0.24.0 新增 MiniMax-M3 支持与 DeepSeek-V4 优化](#item-1) ⭐️ 8.0/10
2. [shot-scraper video：通过故事板让代理录制演示视频](#item-2) ⭐️ 8.0/10
3. [OpenAI 推出基因组学 AI 基准 GeneBench-Pro](#item-3) ⭐️ 8.0/10
4. [OpenAI 通过核心转储流行病学修复 18 年历史漏洞](#item-4) ⭐️ 8.0/10
5. [Arcturus 用纳米注入铜将电网损耗减半](#item-5) ⭐️ 8.0/10
6. [亚马逊斥资 10 亿美元成立 FDE 部门部署 AI 代理](#item-6) ⭐️ 8.0/10
7. [韩国承诺超 5500 亿美元缓解内存芯片短缺](#item-7) ⭐️ 8.0/10
8. [分层 AI 绘制 RNA 剪接中的长程 DNA 信号](#item-8) ⭐️ 8.0/10
9. [人工智能或变革乳腺癌检测与复发预测](#item-9) ⭐️ 7.0/10
10. [MIT 问答探讨当前与未来的智能体 AI](#item-10) ⭐️ 7.0/10
11. [纳斯达克通过 Pyth 网络将市场数据扩展至区块链](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [vLLM v0.24.0 新增 MiniMax-M3 支持与 DeepSeek-V4 优化](https://github.com/vllm-project/vllm/releases/tag/v0.24.0) ⭐️ 8.0/10

vLLM v0.24.0 新增了对 MiniMax-M3 模型的支持，并对 DeepSeek-V4 进行了重大优化，包括 FlashInfer 稀疏索引缓存和预填充块规划改进。该版本还扩展了 Model Runner V2，默认支持量化模型，并添加了新的流式解析引擎。 此版本通过支持 MiniMax-M3 和 DeepSeek-V4 等前沿模型，显著扩展了 vLLM 的模型生态，这些模型对于长上下文推理和智能体工作流至关重要。特别是对 DeepSeek-V4 的性能优化，实现了更快、更高效的推理，惠及整个 AI/ML 社区。 该版本包含来自 256 位贡献者的 571 次提交，其中 77 位是新贡献者。关键技术新增包括 MiniMax 稀疏注意力（MSA）支持、MXFP4 量化、FP8 稀疏 GQA 以及针对 MiniMax-M3 的大量 AMD/ROCm 调优，还有针对 DeepSeek-V4 的集群协作 topK 内核和原生 DSA 索引器解码。

github · khluu · 6月29日 19:41

**背景**: vLLM 是一个用于大型语言模型（LLM）的高性能推理引擎，广泛用于服务 GPT 和 Llama 等模型。MiniMax-M3 是一个多模态视觉语言模型，采用混合专家（MoE）架构，支持高达 100 万 token 的上下文窗口。DeepSeek-V4 是一系列 MoE 语言模型，参数最多达 1.6T，专为高效的长上下文推理而设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.minimax.io/blog/minimax-m3">MiniMax M3: Frontier Coding, 1M Context, Native Multimodality — All in One Model - MiniMax Research | MiniMax</a></li>
<li><a href="https://arxiv.org/abs/2606.19348">[2606.19348] DeepSeek-V4: Towards Highly Efficient Million ...</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#DeepSeek-V4`, `#MiniMax-M3`, `#GPU optimization`

---

<a id="item-2"></a>
## [shot-scraper video：通过故事板让代理录制演示视频](https://simonwillison.net/2026/Jun/30/shot-scraper-video/#atom-everything) ⭐️ 8.0/10

Simon Willison 发布了 shot-scraper 1.10，新增了“video”命令，该命令接受一个 storyboard.yml 文件，并使用 Playwright 录制 Web 应用程序操作的视频，从而使编码代理能够生成其工作的可视化证明。 该工具满足了 AI 辅助开发中的实际需求，允许代理自动生成视频演示，帮助开发者验证代码是否按预期工作，从而简化了代理驱动工作流中的反馈循环。 storyboard.yml 文件定义了服务器设置、视口大小、光标可见性、等待条件、JavaScript 注入以及包含暂停和点击等动作的场景序列。该命令支持通过 JSON cookie 文件进行身份验证，并输出 WebM 或 MP4 格式的视频。

rss · Simon Willison · 6月30日 16:54

**背景**: shot-scraper 是一个基于 Playwright 的命令行工具，用于自动截取网站截图。新的视频功能将其扩展为录制完整的浏览器会话，通过 YAML 故事板脚本控制用户交互。这反映了编码代理需要超越静态截图来展示其输出的更广泛趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/30/shot-scraper-video/">Have your agent record video demos of its work with shot ...</a></li>
<li><a href="https://github.com/simonw/shot-scraper">GitHub - simonw/shot-scraper: A command-line utility for ... GitHub - hval/shotscraper: https://www.nettavisen.no · GitHub Simon Willison’s Weblog - vuink.com shot-scraper · PyPI Simon Willison on shot-scraper</a></li>
<li><a href="https://playwright.dev/docs/videos">Videos | Playwright</a></li>

</ul>
</details>

**标签**: `#developer-tools`, `#playwright`, `#AI-agents`, `#video-recording`, `#automation`

---

<a id="item-3"></a>
## [OpenAI 推出基因组学 AI 基准 GeneBench-Pro](https://openai.com/index/introducing-genebench-pro) ⭐️ 8.0/10

OpenAI 推出了 GeneBench-Pro，这是一个新的基准测试，旨在使用复杂的真实世界数据集评估 AI 在基因组学、生物学和科学研究中的表现。 该基准为评估基因组学中的 AI 模型提供了严格标准，可能加速药物发现、个性化医疗和生物学研究的进展。 GeneBench-Pro 包含 129 项评估，涵盖 10 个主要领域和 21 个子领域，专注于基因组学和转化生物医学中的多阶段统计推理。

rss · OpenAI Blog · 6月30日 00:00

**背景**: GeneBench-Pro 建立在早期的 GeneBench 之上，后者测试 AI 代理在科学工作流程中的多阶段推理能力。新基准使用更复杂的真实世界案例研究，以更好地反映基因组学研究中的实际挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.biorxiv.org/content/10.64898/2026.06.29.735386v1">GeneBench-Pro: Evaluating Multistage Statistical Reasoning\\in Genomics, Quantitative Biology, and Translational Biomedicine | bioRxiv</a></li>
<li><a href="https://www.startuphub.ai/ai-news/artificial-intelligence/2026/openai-unveils-genebench-pro-benchmark">OpenAI Unveils Genebench-Pro Benchmark | StartupHub.ai</a></li>
<li><a href="https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf">GeneBench: Assessing AI Agents for Multi-Stage Inference ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#benchmark`, `#genomics`, `#scientific research`, `#OpenAI`

---

<a id="item-4"></a>
## [OpenAI 通过核心转储流行病学修复 18 年历史漏洞](https://openai.com/index/core-dump-epidemiology-data-infrastructure-bug) ⭐️ 8.0/10

OpenAI 工程师利用大规模核心转储分析来调试罕见的基础设施崩溃，发现了一个硬件故障和一个存在 18 年的软件漏洞。 这种被称为“核心转储流行病学”的新型调试方法展示了一种可扩展的方法来诊断大规模 AI 基础设施中难以捉摸的故障，可能影响整个行业的可靠性实践。 该漏洞持续了 18 年，通过传统调试方法未被发现。该分析结合了自动核心转储收集和统计相关性，在数千台服务器中定位根本原因。

rss · OpenAI Blog · 6月30日 00:00

**背景**: 核心转储是程序崩溃时内存的快照，通常由操作系统生成。分析核心转储有助于开发人员理解崩溃原因。“核心转储流行病学”指的是系统性地收集和分析多台机器上的核心转储，以识别罕见故障的模式和根本原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.siliconreport.com/openai-details-core-dump-epidemiology-for-infrastructure-debugging-8b6d27b1">OpenAI Details 'Core Dump Epidemiology' for Infrastructure ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Core_dump">Core dump - Wikipedia</a></li>
<li><a href="https://sergioprado.blog/linux-core-dump-analysis/">Linux core dump analysis - sergioprado.blog</a></li>

</ul>
</details>

**标签**: `#debugging`, `#infrastructure`, `#reliability`, `#core dump`, `#OpenAI`

---

<a id="item-5"></a>
## [Arcturus 用纳米注入铜将电网损耗减半](https://techcrunch.com/2026/06/30/arcturus-could-halve-the-grids-electrical-losses-using-its-nano-infused-copper/) ⭐️ 8.0/10

隐秘初创公司 Arcturus 开发了一种基于激光的工艺，将碳纳米材料注入铜中，声称可将电网的电力损耗减半。 如果得到验证，这一突破将大幅提升电网基础设施的能效，减少电力浪费，并降低全球公用事业和消费者的成本。 该公司使用激光将碳纳米材料注入铜中，从而增强其导电性。然而，这些说法目前尚未得到验证，且缺乏公开的技术细节。

rss · 36氪 - 科技 · 6月30日 15:01

**背景**: 电网因铜线电阻而损失约 5-10% 的传输能量（以热量形式）。碳纳米材料（如石墨烯）的导电性优于铜，但将其整合到块状金属中一直具有挑战性。Arcturus 的激光注入技术旨在制造一种复合材料，兼具碳的导电性和铜的机械性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/30/arcturus-could-halve-the-grids-electrical-losses-using-its-nano-infused-copper/">Arcturus could halve the grid’s electrical losses using its nano-infused copper | TechCrunch</a></li>

</ul>
</details>

**标签**: `#energy`, `#materials science`, `#nanotechnology`, `#grid efficiency`

---

<a id="item-6"></a>
## [亚马逊斥资 10 亿美元成立 FDE 部门部署 AI 代理](https://techcrunch.com/2026/06/30/amazon-launches-new-1-billion-fde-org-following-openai-and-anthropic/) ⭐️ 8.0/10

亚马逊云服务（AWS）宣布成立一个耗资 10 亿美元的新内部组织，专注于在客户公司内部署专用 AI 代理的前沿部署工程师（FDE）。工程师将入驻客户现场，确保快速部署并帮助客户实现自主运维。 此举标志着云服务提供商大力投资于现场 AI 部署服务的重要行业趋势，紧随 OpenAI 和 Anthropic 的类似举措。通过减少部署摩擦和培养客户专业知识，这可能加速企业对 AI 代理的采用。 FDE 模式由 Palantir 首创，工程师在客户现场工作以定制和部署解决方案。亚马逊的新部门将专注于专用代理——为特定任务（如销售线索培育或客服分流）设计的 AI 系统。

rss · 36氪 - 科技 · 6月30日 15:00

**背景**: 前沿部署工程师（FDE）是嵌入客户组织，在运营环境中开发、定制和部署技术解决方案的专业人员。专用代理是专注于单一任务的 AI 系统，能够执行通用大语言模型无法完成的行动。随着企业寻求有效将 AI 集成到工作流程中，这种方法日益流行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Forward_Deployed_Engineer">Forward Deployed Engineer - Wikipedia</a></li>
<li><a href="https://techcrunch.com/2026/06/30/amazon-launches-new-1-billion-fde-org-following-openai-and-anthropic/">Amazon launches new $1 billion FDE org, following OpenAI and Anthropic | TechCrunch</a></li>
<li><a href="https://www.salesforce.com/blog/autonomous-agents/">Why Purpose-Built Agents are the Future of AI at Work</a></li>

</ul>
</details>

**标签**: `#AI`, `#Amazon`, `#enterprise`, `#agents`, `#investment`

---

<a id="item-7"></a>
## [韩国承诺超 5500 亿美元缓解内存芯片短缺](https://techcrunch.com/2026/06/29/south-korean-tech-giants-commit-over-550b-to-ease-ramageddon/) ⭐️ 8.0/10

韩国两大内存芯片公司承诺投入超过 5500 亿美元建设新的晶圆厂，旨在缓解被称为“RAMageddon”的全球内存短缺，并加强人工智能基础设施。 这项巨额投资解决了导致内存价格上涨并制约 AI 数据中心扩张的关键行业短缺问题，使韩国成为全球 AI 硬件供应链中的关键参与者。 被称为“RAMageddon”的短缺始于 2025 年，原因是制造产能被重新分配给高利润的 AI 内存产品，据行业高管预计，短缺将持续到至少 2027 年或 2028 年。

rss · 36氪 - 科技 · 6月29日 18:07

**背景**: 内存芯片（如 DRAM 和 NAND 闪存）是计算机、服务器和 AI 系统中的关键组件。当前的短缺源于结构性转变：晶圆厂优先生产用于 AI 数据中心的高利润内存，而非消费级产品，导致供应紧张和价格上涨。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RAMmageddon">RAMmageddon</a></li>
<li><a href="https://en.wikipedia.org/wiki/List_of_semiconductor_fabrication_plants">List of semiconductor fabrication plants - Wikipedia</a></li>

</ul>
</details>

**标签**: `#memory chips`, `#AI infrastructure`, `#semiconductor`, `#investment`, `#South Korea`

---

<a id="item-8"></a>
## [分层 AI 绘制 RNA 剪接中的长程 DNA 信号](https://news.google.com/rss/articles/CBMiWEFVX3lxTE55aXEzVDdCTXhTdW5IOGdsUlB0S3gtZ3VSTTdDbE1qeDBJS2I1bW9RejdQYi1OM19pb09GZjY5SGwwRnV0OXZCZXFLOXg4QnBBOTRRZXJnaGM?oc=5) ⭐️ 8.0/10

研究人员开发了一种分层人工智能模型，用于绘制调控 RNA 剪接的长程 DNA 信号，揭示了远端基因组元件如何影响剪接位点选择。 这一进展加深了对基因调控的理解，有助于预测遗传变异对剪接的影响，并推动剪接相关疾病的疗法开发。 该分层 AI 模型整合了从局部剪接位点到远端调控元件的多层次基因组信息，以高精度预测剪接结果。

google_news · EurekAlert! · 6月30日 13:18

**背景**: RNA 剪接是从前体 mRNA 中去除内含子、连接外显子以形成成熟 mRNA 的过程。位于剪接位点远处的增强子和沉默子等长程 DNA 信号可影响剪接决策，但研究起来颇具挑战。传统模型通常关注局部序列，忽略了这些远端调控效应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RNA_splicing">RNA splicing - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#computational biology`, `#RNA splicing`, `#genomics`, `#machine learning`

---

<a id="item-9"></a>
## [人工智能或变革乳腺癌检测与复发预测](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBPbkVuSFFDbFF2YU9rUHhQZ09qZFg0YzdPYllxbXIxWXdkM3diaGZKNllMVEhMdC1ucWlacDNsdmcybzFScThUMXEtMzZWQ29mYmhHRkhjSW9MQU1p?oc=5) ⭐️ 7.0/10

EurekAlert! 的一份新报告指出，人工智能在改善乳腺癌检测和预测复发方面展现出潜力，可能改变当前的诊断实践。 这一进展可能带来更早、更准确的乳腺癌诊断，减少假阳性并改善患者预后，同时实现个性化复发监测。 该报告未指定具体的 AI 模型或数据集，但强调 AI 算法可分析乳腺 X 光片及其他影像数据，检测人类放射科医生可能遗漏的细微模式。

google_news · EurekAlert! · 6月30日 16:33

**背景**: 乳腺癌是全球最常见的癌症之一，早期检测可显著提高生存率。传统筛查依赖乳腺 X 光摄影，但其灵敏度和特异性有限。AI（尤其是深度学习）已越来越多地应用于医学影像，以提升诊断准确性。

**标签**: `#AI`, `#healthcare`, `#breast cancer`, `#machine learning`

---

<a id="item-10"></a>
## [MIT 问答探讨当前与未来的智能体 AI](https://news.google.com/rss/articles/CBMidkFVX3lxTE5RM1ZBZHlsbkR4dlJscXJLMkhFUzN1S280eXBsV1hCXzdCOTBraWZ1cUt1SUhqXzBUbThPSnBQdWpKTTI2aXdxQTdHbk9SM1d2NGluUXZ0cWktNzdWeS1xZHRQcVhDcWs5M2R4YXdUTGVvMThCRXc?oc=5) ⭐️ 7.0/10

MIT News 发表了一篇问答文章，探讨了智能体 AI 的当前状态和未来愿景，汇集了研究人员和实践者的见解。 随着自主 AI 系统日益普及，这场讨论有助于厘清智能体 AI 不断演变的定义及其对行业的潜在影响。 文章可能涵盖智能体 AI 与生成式 AI 的区别、自主性等级以及构建可靠智能体所面临的挑战。

google_news · MIT News · 6月30日 15:30

**背景**: 智能体 AI 指能够自主追求目标、使用工具并在有限人类监督下采取行动的 AI 系统。它代表了超越主要生成内容的生成式 AI 的演进。关键概念包括感知、推理、规划和执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained - MIT Sloan</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-ai-vs-generative-ai">Agentic AI vs. Generative AI | IBM</a></li>

</ul>
</details>

**标签**: `#agentic AI`, `#artificial intelligence`, `#MIT`, `#AI research`

---

<a id="item-11"></a>
## [纳斯达克通过 Pyth 网络将市场数据扩展至区块链](https://www.coindesk.com/markets/2026/06/30/nasdaq-expands-distribution-of-its-market-data-into-blockchain-infrastructure) ⭐️ 6.0/10

纳斯达克正通过 Pyth Network 区块链分发其 TotalView 股票数据，使实时市场数据可用于链上平台和代币化证券。该计划还涉及与 Kraken 的合作，并为 Ostium 的股票永续合约提供支持。 这标志着传统金融采用区块链基础设施的重要一步，实现了对纳斯达克市场数据的可编程和去中心化访问。它可能加速现实世界资产融入 DeFi，并吸引更多机构参与。 数据通过 Pyth Network 分发，这是一个已为许多 DeFi 协议提供价格馈送的去中心化预言机。纳斯达克的 TotalView 是一款提供详细订单簿信息的优质数据产品。

rss · CoinDesk · 6月30日 13:00

**背景**: 像 Pyth 这样的区块链预言机将链下数据（如股票价格）桥接到链上智能合约。纳斯达克的举措顺应了传统金融机构探索区块链以提高效率和创造新收入来源的更广泛趋势。传统金融与区块链的融合正在加速，银行和交易所越来越多地集成分布式账本技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cryptobriefing.com/nasdaq-blockchain-market-data-distribution/">Nasdaq expands market data distribution into blockchain ...</a></li>
<li><a href="https://www.coindesk.com/markets/2026/06/30/nasdaq-expands-distribution-of-its-market-data-into-blockchain-infrastructure">Nasdaq expands distribution of its market data into ...</a></li>
<li><a href="https://tradersunion.com/news/cryptocurrency-news/show/2530960-nasdaq-market-data-pyth-blockchain/">Nasdaq expands market data distribution through Pyth ...</a></li>

</ul>
</details>

**标签**: `#blockchain`, `#market data`, `#finance`, `#Nasdaq`

---