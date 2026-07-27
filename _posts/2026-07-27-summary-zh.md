---
layout: default
title: "Horizon Summary: 2026-07-27 (ZH)"
date: 2026-07-27
lang: zh
---

> 从 90 条内容中筛选出 9 条重要资讯。

---

**📌 其他（3）**
  1. [PGSimCity：PostgreSQL 内部架构交互式 3D 可视化工具](#item-1) ⭐️ 7.0/10
  2. [美国公民在机场用 GrapheneOS 胁迫 PIN 擦除手机被起诉](#item-2) ⭐️ 7.0/10
  3. [《面向数据设计导论》PDF 演示文稿](#item-3) ⭐️ 7.0/10

**🤖 AI 新闻（1）**
  4. [MonkeyOCRv2 0.7B 参数模型登顶 17 语种文档解析榜首](#item-4) ⭐️ 7.0/10

**🚀 科技动态（3）**
  5. [Hugging Face CEO 呼吁 OpenAI 被黑后实现“彻底透明”](#item-5) ⭐️ 6.0/10
  6. [脑电波或成物理 AI 训练新数据源](#item-6) ⭐️ 5.0/10
  7. [TechCrunch 分析中国 AI 模型 Kimi 引发的行业恐慌](#item-7) ⭐️ 4.0/10

**₿ 加密资产（1）**
  8. [韩国贸易巨头联合 LG CNS 测试应收账款上链代币化](#item-8) ⭐️ 5.0/10

**📰 热点新闻（1）**
  9. [谷歌启动覆盖 150 多国 1500 万次 AI 聊天的大规模研究](#item-9) ⭐️ 3.0/10
---

## 📌 其他

<a id="item-1"></a>
## [PGSimCity：PostgreSQL 内部架构交互式 3D 可视化工具](https://nikolays.github.io/PGSimCity/) ⭐️ 7.0/10

PGSimCity 是一个新的开源项目，将 PostgreSQL 的内部架构和流程以可在浏览器中实时运行的可探索 3D 城市形式呈现。它以动画交互形式展示了后端进程、共享缓冲区、WAL、检查点、自动清理和复制等核心组件。 该工具让 PostgreSQL 复杂的内核机制更容易被学习者、开发者和数据库管理员理解，有望提升技术教育和新人上手效率。其开源特性也为将类似交互式可视化方案适配到 Kubernetes、云计算等其他复杂系统领域提供了可能。 该项目目前仍处于早期阶段，社区反馈指出自动导览模式和过多的屏幕元素会让新用户感到信息过载。用户还建议增加交互式查询输入功能，以便追踪一条 SQL 语句在系统中的完整执行路径。

hackernews · jonbaer · 7月27日 00:19 · [社区讨论](https://news.ycombinator.com/item?id=49063754)

**背景**: PostgreSQL 是一款广泛使用的开源关系型数据库管理系统，其内部架构包含多个协同工作的进程和内存结构，例如共享缓冲区和预写日志（WAL）。理解这些内部机制通常需要阅读大量文档或研究静态架构图，这对初学者来说往往具有挑战性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nikolays.github.io/PGSimCity/">PGSimCity · How PostgreSQL Works, in 3D</a></li>
<li><a href="https://www.interdb.jp/pg/pgsql02.html">2. Process and Memory Architecture :: Hironobu SUZUKI @ InterDB</a></li>
<li><a href="https://www.enterprisedb.com/blog/postgres-internals-deep-dive-process-architecture">Postgres Internals Deep Dive: Process Architecture</a></li>

</ul>
</details>

**社区讨论**: 社区成员认可这种新颖的呈现方式，但批评自动导览节奏过快、界面元素过于繁杂，建议增加更多交互性并明确起点。多位用户希望可以输入自定义查询来查看完整执行流程，也有用户称赞其界面生动有趣，并认为该思路可复用于其他技术领域。

**标签**: `#postgresql`, `#database-internals`, `#visualization`, `#education`, `#open-source`

---

<a id="item-2"></a>
## [美国公民在机场用 GrapheneOS 胁迫 PIN 擦除手机被起诉](https://www.techspot.com/news/113236-us-prosecutors-charge-atlanta-man-after-grapheneos-phone.html) ⭐️ 7.0/10

一名美国公民在机场接受当局搜查时，使用 GrapheneOS 的胁迫 PIN 码擦除了手机数据，目前正面临刑事指控。这起案件标志着在边境使用设备擦除功能首次引发重大法律冲突。 这起案件可能为美国边境的数字隐私权和政府搜查权的边界树立重要的法律先例。它直接影响使用隐私保护工具的旅行者，并引发关于安全功能在法律层面如何被认定的更广泛讨论。 GrapheneOS 中的胁迫 PIN 功能被设计为输入后会对设备执行完全且不可逆的擦除，以保护数据不被未授权访问。法律专家指出，美国法律不仅看重实际行为，也高度重视行为意图，因此擦除手机的目的可能影响指控结果。

hackernews · eecc · 7月26日 22:21 · [社区讨论](https://news.ycombinator.com/item?id=49063022)

**背景**: GrapheneOS 是一个基于 Android 开源项目（AOSP）的开源移动操作系统，主打安全和隐私保护，主要支持 Google Pixel 设备。胁迫 PIN 是一种备用密码，当输入该密码而非常规解锁密码时，会静默触发设备完全擦除，以在胁迫场景下保护用户数据。美国边境当局对入境人员的电子设备拥有广泛的合法搜查权，这一权力长期以来引发隐私倡导者的公民自由担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GrapheneOS">GrapheneOS</a></li>
<li><a href="https://www.androidauthority.com/grapheneos-duress-pin-3584795/">I use a duress PIN to protect my data — here’s how it works and why everyone needs one</a></li>

</ul>
</details>

**社区讨论**: 评论者就边境擦除手机是否应被认定为非法展开讨论，部分人认为美国法律更看重行为意图而非输入 PIN 这一表面动作。另有用户提出替代安全方案，例如用预设密钥触发设备加密而非完全擦除，或使用类似 VeraCrypt 隐藏卷功能的诱饵系统以降低法律风险。

**标签**: `#privacy`, `#security`, `#law`, `#GrapheneOS`, `#civil-liberties`

---

<a id="item-3"></a>
## [《面向数据设计导论》PDF 演示文稿](https://www.gamedevs.org/uploads/introduction-to-data-oriented-design.pdf) ⭐️ 7.0/10

一份名为《面向数据设计导论》的基础 PDF 演示文稿被分享，重点强调数据布局和缓存效率是算法与系统设计的核心驱动力。该演示文稿由面向数据设计的知名倡导者 Mike Acton 撰写。 这份演示文稿是系统和游戏开发领域经典且有影响力的资料，塑造了开发者通过优先考虑数据组织来优化性能关键型软件的方式。它提供的基础概念能帮助开发者减少 CPU 缓存未命中情况，提升系统整体吞吐量。 该方法倡导使用并行数组（数组结构体）来提升缓存利用率，这与面向对象设计典型的数组结构体形成对比。它强调在编写代码前先定义数据输入和输出，根据应用数据的具体形态定制系统设计。

hackernews · tosh · 7月26日 18:11 · [社区讨论](https://news.ycombinator.com/item?id=49060724)

**背景**: 面向数据设计是一种以提升 CPU 缓存使用效率为目标的程序优化方法，CPU 缓存的访问速度远快于主内存。它专注于组织数据布局以匹配 CPU 获取和处理信息的方式，通常使用并行数组而非数组结构体。该术语由 Noel Llopis 在 2009 年 9 月的一篇文章中正式命名，尽管其底层概念已存在数十年。Mike Acton 等倡导者认为，数据布局应作为软件设计的主要驱动力，而非代码结构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Data-oriented_design">Data-oriented design</a></li>
<li><a href="https://dataorienteddesign.com/dodbook.pdf">Data - Oriented Design</a></li>
<li><a href="https://en.wikipedia.org/wiki/CPU_cache">CPU cache - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者强调面向数据设计的核心是先在代码实现前定义数据，有用户指出其有效性因应用数据形态而异。部分用户质疑该方法只是缓存感知设计的重新包装，或是等同于数组编程，还有人提到适配不断变化的需求等实际挑战。另有评论提到该演示文稿的作者发布了面向数据编程相关的 LLM 技能。

**标签**: `#data-oriented-design`, `#systems-programming`, `#performance-optimization`, `#game-development`, `#software-architecture`

---

## 🤖 AI 新闻

<a id="item-4"></a>
## [MonkeyOCRv2 0.7B 参数模型登顶 17 语种文档解析榜首](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247907283&idx=2&sn=5df8a52712c79f67232ca9672d4cc34e) ⭐️ 7.0/10

MonkeyOCRv2 是一款拥有 0.7B 参数的开源模型，在 17 种语言的文档解析基准测试中取得了第一名。该项目已开源模型权重及相关数据集资源。 这一结果表明，在文档解析这类专项任务中，设计高效的小模型可以超越参数量更大的模型。它推动了高效参数 AI 系统的发展潮流，在保持高性能的同时降低了计算成本。 MonkeyOCRv2 架构包含 ViT-Small、ViT-Base 和 ViTAEv2-Small 等多种视觉编码器变体，不同规模版本的参数量从 2800 万到 1.13 亿不等。该模型基于 MonkeyDoc v2 语料库训练，专注于在单一编码器中统一细粒度文本建模与跨语言泛化能力。

rss · 量子位 · 7月26日 04:30

**背景**: 文档解析是从数字或拍摄的文档中提取文本、表格、版式等结构化信息的任务。MDPBench、OmniDocBench 等多语言文档解析基准用于评估模型在多种语言和真实场景文档上的表现。高效 AI 模型更注重架构优化而非单纯扩大参数量，以实现更高的计算成本性价比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.11562">MonkeyOCRv2: A Visual-Text Foundation Model for Document AI</a></li>
<li><a href="https://github.com/Yuliang-Liu/MonkeyOCRv2">GitHub - Yuliang-Liu/MonkeyOCRv2: MonkeyOCRv2 Vision Encoder — A Document-Native Visual Backbone</a></li>
<li><a href="https://arxiv.org/html/2603.28130">MDPBench: A Benchmark for Multilingual Document Parsing in...</a></li>

</ul>
</details>

**标签**: `#OCR`, `#open-source`, `#efficient AI models`, `#document parsing`, `#multilingual NLP`

---

## 🚀 科技动态

<a id="item-5"></a>
## [Hugging Face CEO 呼吁 OpenAI 被黑后实现“彻底透明”](https://techcrunch.com/2026/07/26/hugging-face-ceo-calls-for-radical-transparency-after-unprecedented-openai-hack/) ⭐️ 6.0/10

在针对 OpenAI 并入侵了 Hugging Face 生产系统的前所未有的自主智能体网络攻击发生后，Hugging Face CEO Clément Delangue 呼吁实现“彻底透明”。Delangue 与 OpenAI 高管会面，要求完全公开事件追踪记录，并承诺投入 1 亿美元用于防御性 AI 安全计算工作。 这一事件标志着首个已知的大规模自主 AI 网络攻击，预示着随着 AI 系统开始自主执行攻击性操作，网络安全格局将发生重大转变。呼吁“彻底透明”可能会为 AI 公司披露安全事件和协作开展防御措施树立新的行业标准。 Anthropic 曾在 2025 年 9 月检测到类似的自主网络间谍活动，其中 AI 自主执行了约 30 家高价值机构 80%至 90%的攻击任务。Delangue 特别要求 OpenAI 公开完整的事件追踪记录，并拨出 1 亿美元的计算资源用于防御性 AI 安全工作。

rss · 36氪 - 科技 · 7月26日 16:33

**背景**: 自主智能体网络攻击是指 AI 系统在极少人工干预下独立规划并执行多阶段攻击任务的攻击行为，这类攻击首次被记录在 2025 年针对多个行业的活动中。Hugging Face 是领先的开源 AI 平台，托管模型和数据集，而 OpenAI 是知名 AI 研究机构，以开发先进 AI 模型著称。此处的“彻底透明”指将安全事件的所有细节（包括技术追踪记录和影响范围）完全向公众披露。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybermagazine.com/news/ai-agents-drive-first-large-scale-autonomous-cyberattack">AI Agents Drive First Large-Scale Autonomous Cyberattack | Cybersecurity Magazine</a></li>
<li><a href="https://techcrunch.com/2026/07/26/hugging-face-ceo-calls-for-radical-transparency-after-unprecedented-openai-hack/">Hugging Face CEO calls for ‘ radical transparency ... | TechCrunch</a></li>
<li><a href="https://superintelligencenews.com/applications/openai-hack-hugging-face-transparency-call/">OpenAI hack sparks Hugging Face transparency call</a></li>

</ul>
</details>

**标签**: `#AI security`, `#cybersecurity`, `#OpenAI`, `#autonomous agents`, `#industry news`

---

<a id="item-6"></a>
## [脑电波或成物理 AI 训练新数据源](https://techcrunch.com/2026/07/26/are-brain-waves-the-next-unlock-for-physical-ai/) ⭐️ 5.0/10

一项新概念提出将脑电波读数作为额外数据源，用于训练前沿物理 AI 模型，突破传统视频输入的局限。这种方法旨在补充现有训练数据，目前这类数据已经需要多摄像头角度和密集标注。 如果这一方法可行，它将为需要理解和交互现实世界的物理 AI 系统提供更丰富、更直观的训练信号。这可能会减少物理 AI 开发对海量视频数据集和人工标注工作的依赖。 这一提议目前仍处于推测阶段，缺乏将脑电波数据整合到物理 AI 训练中的技术细节或实际进展证据。当前的物理 AI 训练已经需要多角度视频数据和高度密集的数据标注才能获得良好性能。

rss · 36氪 - 科技 · 7月27日 00:19

**背景**: 物理 AI 是指能够感知、理解并与物理世界交互的 AI 模型，通常需要大量现实世界的感官数据来进行训练。脑电波读取（也称为脑读取）使用 EEG 电极等传感器来捕获和解释人类大脑的神经活动。机器学习中的密集标注是指在数据集中广泛标记数据的过程，为模型提供更深入的训练信号。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Brain-reading">Brain-reading - Wikipedia</a></li>
<li><a href="https://www.scientificamerican.com/article/machines-that-read-your-brain-waves/">Machines That Read Your Brain Waves | Scientific American</a></li>
<li><a href="https://www.sapien.io/glossary/definition/annotation-density">Explanation of Annotation Density | Sapien's AI Glossary</a></li>

</ul>
</details>

**标签**: `#AI`, `#Physical AI`, `#Neurotechnology`, `#Machine Learning`, `#Research`

---

<a id="item-7"></a>
## [TechCrunch 分析中国 AI 模型 Kimi 引发的行业恐慌](https://techcrunch.com/2026/07/26/making-sense-of-the-panic-over-chinese-ai/) ⭐️ 4.0/10

TechCrunch 的旗舰播客 Equity 最新一期讨论了 Moonshot AI 的 Kimi 模型在硅谷和华尔街引发的广泛恐慌。该播客回顾探讨了行业对这一中国 AI 发展的强烈反应。 这一反应凸显了中国 AI 企业对西方成熟科技和金融领域日益增长的全球竞争压力。这标志着中国的技术突破现在已能够在美国引发即时的市场和行业焦虑。 该讨论是聚焦商业领域的播客回顾，而非技术分析，未提供任何新的模型更新或新颖见解。内容主要围绕市场情绪和行业反应，而非 Kimi 模型的技术规格。

rss · 36氪 - 科技 · 7月26日 19:40

**背景**: Moonshot AI 是一家中国公司，开发了 Kimi 系列大语言模型，其首个版本于 2023 年发布，支持高达 128,000 个 token 的上下文长度。最新模型 Kimi K2 采用混合专家架构，拥有 320 亿激活参数和 1 万亿总参数，支持高达 256K 的上下文长度。Equity 是 TechCrunch 的旗舰播客，主要关注初创企业、科技和风险投资的商业层面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(chatbot)">Kimi (chatbot) - Wikipedia</a></li>
<li><a href="https://moonshotai.github.io/Kimi-K2/">Kimi K2: Open Agentic Intelligence</a></li>
<li><a href="https://techcrunch.com/podcasts/equity/">Equity Archives | TechCrunch</a></li>

</ul>
</details>

**标签**: `#AI`, `#Industry Analysis`, `#Moonshot AI`, `#Chinese Tech`

---

## ₿ 加密资产

<a id="item-8"></a>
## [韩国贸易巨头联合 LG CNS 测试应收账款上链代币化](https://www.coindesk.com/business/2026/07/26/south-korea-trading-giant-puts-receivables-onchain-in-tokenization-test-with-lg-cns) ⭐️ 5.0/10

一家韩国大型贸易公司正通过与 LG CNS 合作，开展将应收账款上链的代币化测试。这一举措是区块链技术在企业的供应链金融领域的实际落地应用。 此次测试展示了韩国企业界在现实世界资产（RWA）代币化方面的渐进式进展，有望改善贸易公司的现金流和流动性。这也凸显了亚洲成熟科技与贸易企业对区块链解决方案的日益接纳。 应收账款代币化是指将发票等法定付款承诺转换为区块链网络上的数字代币，以代表相关所有权。LG CNS 此前曾基于 R3 的 Corda 等解决方案开发过面向金融和供应链场景的区块链平台。

rss · CoinDesk · 7月27日 00:00

**背景**: 应收账款是指客户因购买商品或接受服务而欠企业的款项，通常以发票形式记录。代币化是指将现实世界资产或相关权利表示为区块链上的数字代币的过程，这能提升透明度并便于转让或融资。现实世界资产（RWA）代币化已越来越多地应用于供应链金融等领域，以释放流动性并提升运营效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.hashcashconsultants.com/digital-assets/assets/trade-receivables/">Trade Receivables - Hashcashconsultants</a></li>
<li><a href="https://tokenminds.co/blog/how-receivables-tokenization-is-transforming-business-cash-flow-and-liquidity">How Receivables Tokenization Is Transforming Business Cash Flow and Liquidity</a></li>
<li><a href="https://hardwaresfera.com/en/noticias/lg-cns-desarrolla-blockchain-la-comercializacion-la-operacion-companias/">LG CNS develops a blockchain for commercialization and operation...</a></li>

</ul>
</details>

**标签**: `#blockchain`, `#tokenization`, `#enterprise`, `#supply chain finance`, `#RWA`

---

## 📰 热点新闻

<a id="item-9"></a>
## [谷歌启动覆盖 150 多国 1500 万次 AI 聊天的大规模研究](https://news.google.com/rss/articles/CBMi0AFBVV95cUxONjVMM0FWS3NUaXpHS2diSnRaM2hHaElWSXpsZ1I4cXpwTW1IMnV6Q01EUVE2dmh2WTFqQUZRVVdZb2Fma2h0ZkJKWFNleFoyRlZnbko3NUF1ZXJ5bUVFS3hLTkdvN2ZvYlJiYmk0OE1VUTV2bXBiVTV6ak8wMkQwcHBIRGR1cVFDeHpxaXdxcmpNQjlRYTdUQTB1SmtMX3lyNE13aGRkWTVveU0yZENtalZ2OW42WnE2SXNTSXJTV1pJdk1UY2RONExPaWdoMW1J?oc=5) ⭐️ 3.0/10

谷歌启动了一项大规模研究，分析超过 150 个国家的 1500 万次 AI 聊天内容。该计划旨在考察全球 AI 使用的模式和趋势。 这项研究可以为全球用户如何与 AI 工具互动提供有价值的见解，为未来的产品开发和决策提供参考。它还有助于识别不同地区在 AI 采用和使用习惯上的差异。 该研究覆盖范围极广，包含超过 150 个国家，数据集规模达 1500 万次聊天。现有信息中未披露具体涉及的 AI 平台或研究的时间范围。

google_news · Судово-юридична газета · 7月26日 18:42

**标签**: `#AI`, `#research`, `#Google`, `#user study`

---