---
layout: default
title: "Horizon Summary: 2026-07-01 (ZH)"
date: 2026-07-01
lang: zh
---

> 从 184 条内容中筛选出 14 条重要资讯。

---

**📌 其他（3）**
  1. [Claude Code 隐写标记请求](#item-1) ⭐️ 9.0/10
  2. [美国解除对 Anthropic 的 Claude Fable 5 和 Mythos 5 的出口管制](#item-2) ⭐️ 9.0/10
  3. [Anthropic 推出面向科研人员的 Claude Science](#item-3) ⭐️ 8.0/10

**🚀 科技动态（3）**
  4. [Realta Fusion 声称首次直接从聚变反应发电](#item-4) ⭐️ 9.0/10
  5. [特斯拉在奥斯汀开始测试无方向盘 Cybercab](#item-5) ⭐️ 8.0/10
  6. [Arcturus 用纳米注入铜将电网损耗减半](#item-6) ⭐️ 8.0/10

**🤖 AI 新闻（3）**
  7. [Claude Sonnet 5 发布，性能接近 Opus](#item-7) ⭐️ 8.0/10
  8. [shot-scraper video：让 AI 代理自动录制演示视频](#item-8) ⭐️ 8.0/10
  9. [ChatGPT 全球采用率持续增长](#item-9) ⭐️ 7.0/10

**🔬 半导体（1）**
  10. [企业 Token 支出比炒作更理性](#item-10) ⭐️ 7.0/10

**₿ 加密资产（1）**
  11. [美国参议员提出法案，阻止对手获取 AI 技术](#item-11) ⭐️ 7.0/10

**📰 热点新闻（3）**
  12. [中国应对 AI 失业的计划](#item-12) ⭐️ 7.0/10
  13. [美团用国产芯片训练万亿参数 AI 模型](#item-13) ⭐️ 7.0/10
  14. [特朗普 2025 年财务报告显示加密货币收入达 140 亿美元](#item-14) ⭐️ 6.0/10
---

## 📌 其他

<a id="item-1"></a>
## [Claude Code 隐写标记请求](https://thereallo.dev/blog/claude-code-prompt-steganography) ⭐️ 9.0/10

一位开发者发现，Anthropic 的 Claude Code 工具（版本 2.1.196）会根据用户的 API 基础 URL 和时区，在系统提示中静默嵌入不可见的 Unicode 隐写标记，从而在未公开的情况下对请求进行指纹识别。 这一发现削弱了对 AI 服务提供商的信任，因为它表明 Anthropic 通过其开发者工具秘密追踪用户，可能违反了透明度预期，并引发了全球开发者的隐私担忧。 这些标记似乎旨在标记与中国相关的流量，可能是为了检测模型蒸馏行为。该技术是通过反编译本地 Claude Code 安装包发现的，Anthropic 未对此行为进行文档说明或公开披露。

hackernews · kirushik · 6月30日 15:44 · [社区讨论](https://news.ycombinator.com/item?id=48734373)

**背景**: 隐写术是一种将信息隐藏在其他数据中的做法，例如在文本中使用不可见的 Unicode 字符。Claude Code 是 Anthropic 推出的基于终端的 AI 编码代理，它会向公司 API 发送提示。隐藏标记被嵌入系统提示中，使得 Anthropic 即使通过代理路由也能识别请求来源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aimadetools.com/blog/claude-code-steganography-explained/">Claude Code Is Steganographically Marking Requests: What It Means</a></li>
<li><a href="https://byteiota.com/claude-code-is-marking-requests-what-anthropic-hid/">Claude Code Is Marking Requests: What Anthropic Hid</a></li>
<li><a href="https://aiproductivity.ai/news/claude-code-prompt-steganography-hidden-markers/">Claude Code Prompt Steganography Discovered - aiproductivity.ai</a></li>

</ul>
</details>

**社区讨论**: Hacker News 社区表达了强烈担忧，许多人批评 Anthropic 缺乏透明度，并呼吁使用本地 AI 解决方案。一些评论者淡化其严重性，认为意图（检测中国模型蒸馏）很明显，而另一些人则指出实现方式粗糙，并质疑是否还有其他隐藏行为。

**标签**: `#AI`, `#security`, `#steganography`, `#Anthropic`, `#developer tools`

---

<a id="item-2"></a>
## [美国解除对 Anthropic 的 Claude Fable 5 和 Mythos 5 的出口管制](https://twitter.com/AnthropicAI/status/2072106151890809341) ⭐️ 9.0/10

美国商务部解除了对 Anthropic 的 Claude Fable 5 和 Mythos 5 的出口管制，允许从 2026 年 7 月 1 日起在全球部署这些先进 AI 模型。 这一政策转变标志着对前沿 AI 出口更为宽松的立场，但社区讨论凸显了对企业依赖美国 AI 模型以及监管不可预测性的担忧。 Fable 5 将在 Claude Platform、Claude.ai、Claude Code 和 Claude Cowork 上全球可用，但最初不能用于编码任务，这些任务将回退到 Opus 4.8。

hackernews · Pragmata · 6月30日 23:55 · [社区讨论](https://news.ycombinator.com/item?id=48740771)

**背景**: Claude Fable 5 和 Mythos 5 是 Anthropic 最强大的模型，专为网络安全漏洞发现而设计。由于安全和滥用担忧，之前实施了出口管制，但经过与美国政府的谈判，Anthropic 实施了新的分类器以阻止网络安全任务，从而使得管制得以解除。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/redeploying-fable-5">Redeploying Claude Fable 5 \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable_5">Claude Fable 5</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Mythos">Claude Mythos - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者对在美国前沿模型上构建关键业务功能表示怀疑，因为监管不可预测，有人指出损害已经造成。其他人则强调 Fable 5 最初不能用于编码，并质疑过程的透明度。

**标签**: `#AI regulation`, `#export controls`, `#Anthropic`, `#policy`, `#frontier models`

---

<a id="item-3"></a>
## [Anthropic 推出面向科研人员的 Claude Science](https://claude.com/product/claude-science) ⭐️ 8.0/10

Anthropic 推出了 Claude Science，这是一个专为科学研究设计的 AI 工作台，集成了高性能计算（HPC）和数据库，采用本地服务器加 Web 界面的架构。 该产品满足了科学计算中的关键需求，使研究人员能够在安全环境中对敏感数据运行复杂分析，有望加速生物信息学和基因组学等领域的发现。 Claude Science 运行本地服务器并通过浏览器 UI 连接，适用于高度受控的制药环境。它能生成可审计的工件，并与机构集群集成，但不适用于临床或诊断用途。

hackernews · lebovic · 6月30日 17:07 · [社区讨论](https://news.ycombinator.com/item?id=48735770)

**背景**: 科学研究通常涉及大型数据集和复杂的计算工作流，需要 HPC 资源。传统 AI 工具并非为集成机构集群或安全处理敏感数据而设计。Claude Science 通过提供一个可定制的工作台，连接到研究人员现有的基础设施，弥补了这一差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-science-ai-workbench">Claude Science, an AI workbench for scientists \ Anthropic</a></li>
<li><a href="https://claude.com/docs/claude-science/overview">Claude Science - Claude.ai Documentation</a></li>
<li><a href="https://www.technologyreview.com/2026/06/30/1139987/claude-science-is-anthropics-newest-flagship-product/">Claude Science is Anthropic’s newest flagship product</a></li>

</ul>
</details>

**社区讨论**: 早期用户印象深刻：一位研究人员用它分析全基因组测序数据，大约一分钟就解决了一个关于新生突变的问题。一个集成 HPC 工具的创始人指出，与机构集群的集成非常有价值。另一位科学家强调它加快了生物信息学工作流，但也指出跟上 AI 生成的模型存在挑战。

**标签**: `#AI`, `#Science`, `#Bioinformatics`, `#Anthropic`, `#Product Launch`

---

## 🚀 科技动态

<a id="item-4"></a>
## [Realta Fusion 声称首次直接从聚变反应发电](https://techcrunch.com/2026/06/30/realta-fusion-generates-electricity-directly-from-a-fusion-reaction-an-apparent-first/) ⭐️ 9.0/10

Realta Fusion 实现了一个里程碑，通过原型转换器从聚变反应中直接收集阿尔法粒子，产生 100 伏、数安培的电流，点亮了灯泡。 这种直接能量转换可通过提高效率显著改善聚变反应堆的经济性，使商业聚变能更接近现实，并可能改变全球能源生产格局。 这家初创公司在其反应堆上安装了一个原型转换器，用于捕获氘氚聚变产生的阿尔法粒子，产生了足以点亮几个灯泡的电力。氘氚聚变反应中约 20% 的能量由阿尔法粒子携带。

rss · 36氪 - 科技 · 6月30日 19:12

**背景**: 聚变能旨在通过融合轻原子核来复制太阳的能量来源，释放巨大能量。传统设计通过蒸汽轮机将聚变热转化为电能，而直接能量转换则直接捕获带电粒子，可能提高效率。Realta Fusion 采用名为 CoSMo 聚变的紧凑、可扩展设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/30/realta-fusion-generates-electricity-directly-from-a-fusion-reaction-an-apparent-first/">Realta Fusion generates electricity directly from a fusion ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Direct_energy_conversion">Direct energy conversion - Wikipedia</a></li>
<li><a href="https://realtafusion.com/technology/">Technology - Realta Fusion</a></li>

</ul>
</details>

**标签**: `#fusion energy`, `#energy technology`, `#physics`, `#breakthrough`

---

<a id="item-5"></a>
## [特斯拉在奥斯汀开始测试无方向盘 Cybercab](https://techcrunch.com/2026/06/30/tesla-starts-testing-cybercab-without-pedals-or-a-steering-wheel-in-austin/) ⭐️ 8.0/10

特斯拉已开始在德克萨斯州奥斯汀的公共道路上测试其完全自动驾驶的 Cybercab，该车没有踏板或方向盘，标志着向推出机器人出租车网络迈出了具体一步。 这一测试里程碑使特斯拉更接近实现埃隆·马斯克长期承诺的机器人出租车网络，可能颠覆网约车行业并加速自动驾驶汽车的普及。 Cybercab 是一款专为完全自动驾驶设计的双座电动车，于 2026 年 2 月开始生产。其整备质量为 3113 磅，电机功率 219 马力，电池容量 48 千瓦时，未经调整的续航里程为 418 英里。

rss · 36氪 - 科技 · 6月30日 15:32

**背景**: 特斯拉的机器人出租车服务使用配备全自动驾驶（FSD）软件的车辆，于 2025 年 6 月在奥斯汀有限度推出。Cybercab 于 2024 年 10 月作为概念车亮相，旨在成为该服务的专用车辆，无需人工操控。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Cybercab">Tesla Cybercab - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Robotaxi">Tesla Robotaxi - Wikipedia</a></li>
<li><a href="https://electrek.co/2026/06/15/tesla-cybercab-epa-specs-curb-weight-battery-motor-power/">Tesla Cybercab full specs revealed: 3,113 lbs, 219 HP, 48 kWh</a></li>

</ul>
</details>

**标签**: `#Tesla`, `#autonomous vehicles`, `#robotaxi`, `#Cybercab`

---

<a id="item-6"></a>
## [Arcturus 用纳米注入铜将电网损耗减半](https://techcrunch.com/2026/06/30/arcturus-could-halve-the-grids-electrical-losses-using-its-nano-infused-copper/) ⭐️ 8.0/10

隐形初创公司 Arcturus 以 800 万美元种子轮融资走出隐身模式，公开了其利用激光将碳纳米材料注入铜的工艺，该工艺可大幅提高导电性，并有望将电网电力损耗减半。 如果成功，这项技术可以显著减少电网和数据中心的能源浪费，带来可观的成本节约和更低的碳排放，对能源基础设施和可持续性具有广泛影响。 Arcturus 已累计融资 1000 万美元，投资者包括 Initialized Capital、Breakthrough Energy Discovery、Toyota Ventures 和 Wireframe Ventures。该公司尚未披露所用碳纳米材料的具体成分，但很可能是碳纳米管或石墨烯衍生物。

rss · 36氪 - 科技 · 6月30日 15:01

**背景**: 电网因铜等导体的电阻而以热量形式损失大量能量。在不更换整个基础设施的情况下提高现有材料的导电性是一个重大挑战。Arcturus 使用激光将碳纳米材料嵌入铜中，增强电子流动并减少电阻损耗。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/30/arcturus-could-halve-the-grids-electrical-losses-using-its-nano-infused-copper/">Arcturus could halve the grid’s electrical losses using its ...</a></li>

</ul>
</details>

**标签**: `#energy`, `#nanotechnology`, `#materials science`, `#electrical grid`, `#startup`

---

## 🤖 AI 新闻

<a id="item-7"></a>
## [Claude Sonnet 5 发布，性能接近 Opus](https://simonwillison.net/2026/Jun/30/claude-sonnet-5/#atom-everything) ⭐️ 8.0/10

Anthropic 于 2026 年 6 月 30 日发布了 Claude Sonnet 5，声称其性能接近 Opus 4.8，但价格更低。该模型拥有 100 万 token 的上下文窗口、12.8 万 token 的最大输出，以及新的分词器，英文文本的 token 数量增加约 30%。 此次发布缩小了中端与顶级模型之间的差距，以更低成本提供接近旗舰的性能，可能改变开发者的采用模式。系统卡还揭示了监管考量：与更强大的 Mythos 5 不同，Sonnet 5 被认为足够安全，无需政府阻止即可发布。 Sonnet 5 不再支持 temperature、top_p 和 top_k 采样参数，并默认启用自适应思考。定价与 Sonnet 4.6 相同（每百万 token 3/15 美元），但由于新分词器导致英文文本 token 数量增加，实际成本上升约 30%。

rss · Simon Willison · 6月30日 21:23

**背景**: Anthropic 的 Claude 模型系列包括 Sonnet（中端）和 Opus（旗舰）层级。该公司还有一个更强大的 Mythos 5 模型，出于安全考虑，仅在政府批准后才允许有限发布。系统卡详细说明了模型能力和安全评估，帮助开发者和监管者了解风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-sonnet-5">Introducing Claude Sonnet 5 \ Anthropic</a></li>
<li><a href="https://www-cdn.anthropic.com/480e0bb54327b9622282e9c39a83a4f490ed377e/Claude+Sonnet+5+System+Card.pdf">System Card: Claude Sonnet 5 June 30, 2026 anthropic.com</a></li>
<li><a href="https://llm-stats.com/blog/research/claude-sonnet-5-vs-claude-opus-4-8">Claude Sonnet 5 vs Claude Opus 4.8: The Complete Comparison</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的社区评论褒贬不一：一些用户指出 Sonnet 5 的性能与 GLM 5.2 相当但更简洁，而另一些人则认为 Opus 4.8 在更高努力水平下性价比更好。考虑到定价和分词器的变化，一些人对何时使用 Sonnet 5 而非 Opus 感到困惑。

**标签**: `#AI`, `#Claude`, `#Anthropic`, `#LLM`, `#model release`

---

<a id="item-8"></a>
## [shot-scraper video：让 AI 代理自动录制演示视频](https://simonwillison.net/2026/Jun/30/shot-scraper-video/#atom-everything) ⭐️ 8.0/10

Simon Willison 发布了 shot-scraper 1.10，新增了“shot-scraper video”命令，该命令利用 Playwright 根据 YAML storyboard 文件中定义的流程录制 WebM 格式的视频。 该工具使编码代理能够自动生成其工作的视频演示，满足了代理工作流中验证和展示代理行为的关键需求。 该命令接受一个 storyboard.yml 文件，其中指定了服务器设置、视口、光标可见性、JavaScript 覆盖（例如剪贴板模拟）以及包含点击和暂停等操作的场景序列。它支持通过 cookie 进行身份验证，并输出 WebM 文件。

rss · Simon Willison · 6月30日 16:54

**背景**: shot-scraper 是一个命令行工具，用于使用 Playwright 截取屏幕截图和抓取网页。新的视频功能将其扩展为录制完整会话，使 AI 代理无需手动屏幕录制即可展示其工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://shot-scraper.datasette.io/en/stable/video.html">Recording videos - shot - scraper</a></li>
<li><a href="https://simonwillison.net/2026/Jun/30/shot-scraper-video/">Have your agent record video demos of its work with shot - scraper ...</a></li>
<li><a href="https://github.com/simonw/shot-scraper">GitHub - simonw/ shot - scraper : A command-line utility for taking...</a></li>

</ul>
</details>

**标签**: `#agentic-ai`, `#testing`, `#developer-tools`, `#playwright`, `#automation`

---

<a id="item-9"></a>
## [ChatGPT 全球采用率持续增长](https://openai.com/index/how-chatgpt-adoption-has-expanded) ⭐️ 7.0/10

OpenAI 发布了新的 Signals 数据，显示 ChatGPT 的全球采用率正在增长，用户使用频率增加，探索更多功能，并在不同地区和语言中推动增长。 这表明 ChatGPT 正更深入地融入日常工作和跨文化场景，标志着 AI 市场日趋成熟，用户基础已超越早期采用者。 数据来自追踪使用模式的 OpenAI Signals，但公告缺乏具体指标或地区细分，因此是高层概述而非详细分析。

rss · OpenAI Blog · 6月30日 09:00

**背景**: ChatGPT 是 OpenAI 开发的对话式 AI 模型，于 2022 年底推出。其采用率指标被密切关注，作为 AI 市场增长和用户接受度的指标。

**标签**: `#ChatGPT`, `#AI adoption`, `#OpenAI`, `#market trends`

---

## 🔬 半导体

<a id="item-10"></a>
## [企业 Token 支出比炒作更理性](https://newsletter.semianalysis.com/p/tokenbudgeting-our-conversations) ⭐️ 7.0/10

Semianalysis 报道称，与企业对话显示，广泛过度使用 Token（即“TokenMaxxing”）并不像炒作的那样普遍，企业表现出更理性的支出模式。 该分析揭穿了“TokenMaxxing”的炒作，提供了企业采用 LLM 的现实洞察，帮助从业者和投资者理解实际的 Token 经济。 该文章基于与企业对话，指出虽然存在一些 Token 浪费，但大多数组织在谨慎预算，而非不加区分地最大化使用。

rss · Semianalysis · 6月30日 18:32

**背景**: TokenMaxxing 指的是最大化 AI 使用量的做法，通常以 Token 消耗量衡量，有时被视为生产力表演。Token 是 AI 模型处理的数据单元，其成本是企业 AI 经济学的关键因素。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Token_maxxing">Token maxxing - Wikipedia</a></li>
<li><a href="https://blogs.nvidia.com/blog/ai-tokens-explained/">What Are AI Tokens ? The Language and Currency... | NVIDIA Blog</a></li>

</ul>
</details>

**标签**: `#AI/ML`, `#enterprise`, `#LLM`, `#token economics`, `#industry analysis`

---

## ₿ 加密资产

<a id="item-11"></a>
## [美国参议员提出法案，阻止对手获取 AI 技术](https://www.coindesk.com/policy/2026/06/30/u-s-senators-seek-to-block-foreign-adversaries-from-ai-technology-in-new-bill) ⭐️ 7.0/10

一个跨党派美国参议员团体提出一项法案，旨在限制向中国、俄罗斯等外国对手转让先进人工智能技术。 该法案可能显著重塑全球人工智能供应链和技术转让，影响美国公司及国际 AI 发展。 该法案针对被认为对国家安全至关重要的人工智能技术，包括出口管制和投资审查条款。

rss · CoinDesk · 6月30日 23:02

**背景**: 美国政府日益关注限制对手获取敏感技术，尤其是被视为军民两用技术的人工智能。此前已采取包括对先进半导体实施出口限制等措施。

**标签**: `#AI policy`, `#geopolitics`, `#regulation`, `#technology access`

---

## 📰 热点新闻

<a id="item-12"></a>
## [中国应对 AI 失业的计划](https://news.google.com/rss/articles/CBMigwFBVV95cUxQOERiSFVoaHY5ZkNwWURzMWUyRDV3ZHl1MkpuZDlDcVhQaXN1dEhYQXZhd3oxNFdjYUZFOFFQTW1LdUItQ092ODRSVV9ickRoT1pwYWNJVlQwQ1NNVS0teExQbkM3WkUwSmd2LUlmcy1waFdKSkptcHJpbEM2MV9iZlZtUQ?oc=5) ⭐️ 7.0/10

《纽约时报》报道了中国通过再培训计划和社会安全网来缓解 AI 导致的失业问题的策略。 这一政策方法可能为其他面临 AI 导致失业的国家提供参考，凸显了技术进步与社会稳定之间的平衡。 文章讨论了政府资助的再培训和扩大失业救济等具体措施，但摘要中未提供确切细节。

google_news · The New York Times · 7月1日 04:42

**背景**: AI 和自动化预计将颠覆全球劳动力市场，中国因其庞大的制造业劳动力而面临特别压力。中国政府历来采用国家主导的干预措施来管理经济转型。

**标签**: `#AI`, `#labor`, `#China`, `#policy`, `#automation`

---

<a id="item-13"></a>
## [美团用国产芯片训练万亿参数 AI 模型](https://news.google.com/rss/articles/CBMi2AFBVV95cUxOWEJOc2tfMDNfQll0RHlyRy1uRU1IcWozeHNRTUxJQllWMFJTMXF2X0xhSk92VTZDMXhESi04UEJVWU5tb0EtX014Z3lScmpUd2dMODZFd0JYcjRhWko0V2ZzN195VlU5SUJXYjZYckFUcnV3REttNWVhNkVNVGhHNFZ6SXp2VFZTUWo4UF9OQ2xmMHd0NkRBV1Jwc2xpbWhhTHQyb0Y5dFNsUzh5RXB6NG14TGh4c2VvNGdKMUdOWWs3STBjVVdmV0tPNURyRzRPcEF5cGwzSTHSAd4BQVVfeXFMUEpUaVI2N1Exa25YaEM5Q2YtX19kUEk3N0I0c0x0aDU3MG5jQktnS1BucWoxMW5LTFUycEp6c2c4MEhHa3dwR2RlVXREZzBSa2Q0V09JdUJpdnktdzllWmRzb2dDV1pZYUFsUThPVGQ0NGJnV195ZUo0RENMN2Y0Ym9lTEVfakViVVN4d0E5TE9wOGk3RGg2TVE2Uk0zVUdjMjlsWHRaQzc4UUFOS2xfeTBnUVVLRm9XRFVfUHNRWjA3R0NlSjZ5VXA2LWtiV3VfOFM2ODdDYWt1eC1sV0xR?oc=5) ⭐️ 7.0/10

美团宣布其新 AI 模型 LongCat-2.0（拥有 1.6 万亿参数）完全使用国产芯片训练，这是首次如此规模的模型在国产计算集群上完成训练。 这表明中国在不依赖受美国出口限制的英伟达芯片的情况下，训练前沿 AI 模型的能力正在增强，可能减少中国对外国半导体的依赖。 LongCat-2.0 在包含 5 万颗国产芯片的集群上使用 ASIC 超级计算单元训练，该模型已开源。美团从 2023 年开始探索使用国产芯片。

google_news · The Economic Times · 6月30日 07:21

**背景**: 美国的出口管制限制了华为等中国公司获取英伟达 H100、A100 等先进 AI 芯片。此前大多数中国 AI 模型依赖英伟达硬件进行训练，国产芯片主要用于推理。美团的成就表明国产芯片现在能够处理最苛刻的训练任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techxplore.com/news/2026-06-china-meituan-ai-domestic-chips.html">China's Meituan says new AI model trained on domestic chips</a></li>
<li><a href="https://thenextweb.com/news/chinas-meituan-says-its-new-ai-model-was-trained-on-domestic-chips">China’s Meituan says its new AI model was trained on domestic ...</a></li>
<li><a href="https://economictimes.indiatimes.com/tech/artificial-intelligence/chinas-meituan-says-new-ai-model-trained-on-domestic-chips/articleshow/132086878.cms">China's Meituan says new AI model trained on domestic chips</a></li>

</ul>
</details>

**标签**: `#AI`, `#semiconductors`, `#China`, `#Meituan`, `#hardware`

---

<a id="item-14"></a>
## [特朗普 2025 年财务报告显示加密货币收入达 140 亿美元](http://www3.nhk.or.jp/news/html/20260701/k10015166021000.html) ⭐️ 6.0/10

美国政府公布了特朗普总统 2025 年的财务报告，显示其主要收入来自加密资产，总额至少为 140 亿美元（约合 2300 亿日元）。 这一披露凸显了高层政治与加密货币日益交织的趋势，可能影响监管态度和公众对数字资产的看法。 报告金额至少为 140 亿美元，折合约 2300 亿日元，媒体强调主要收益与加密货币相关。

rss · NHK World - Japan/Asia · 7月1日 06:40

**背景**: 美国总统每年需披露财务信息以确保透明度并避免利益冲突。加密货币资产（如比特币和以太坊）在高净值投资组合中日益突出。

**标签**: `#cryptocurrency`, `#politics`, `#finance`

---