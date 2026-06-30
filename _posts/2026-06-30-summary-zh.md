---
layout: default
title: "Horizon Summary: 2026-06-30 (ZH)"
date: 2026-06-30
lang: zh
---

> 从 127 条内容中筛选出 6 条重要资讯。

---

1. [最高法院裁定地理围栏搜查令需受宪法保护](#item-1) ⭐️ 9.0/10
2. [Ornith-1.0：用于智能体编程的自脚手架大语言模型](#item-2) ⭐️ 8.0/10
3. [华盛顿邮报测试 AI 聊天机器人政治偏见](#item-3) ⭐️ 8.0/10
4. [纽约梅隆银行为机构客户推出 USDC 铸造与赎回服务](#item-4) ⭐️ 7.0/10
5. [患者将 AI 工具带入治疗会话](#item-5) ⭐️ 7.0/10
6. [重新思考 AI 治理：关键问题](#item-6) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [最高法院裁定地理围栏搜查令需受宪法保护](https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision) ⭐️ 9.0/10

美国最高法院裁定，要求科技公司提供指定区域内所有设备位置数据的地理围栏搜查令，必须遵守第四修正案对不合理搜查和扣押的保护。 这项里程碑式的裁决极大地限制了执法部门在没有个别嫌疑的情况下进行大规模数字监控的能力，为数字时代的隐私权树立了关键先例。 该案涉及一起银行抢劫案，谷歌提供了银行周围 150 米范围内 19 台设备的位置数据。法院认为，获取此类历史位置数据构成第四修正案下的搜查，需要基于可能原因获得搜查令。

hackernews · cdrnsf · 6月29日 15:54 · [社区讨论](https://news.ycombinator.com/item?id=48720924)

**背景**: 地理围栏搜查令，也称为反向位置搜查令，允许执法部门搜索公司数据库中在特定时间位于虚拟边界（地理围栏）内的所有移动设备。这些搜查令因可能收集无辜旁观者的数据而引发争议。第四修正案保护公民免受不合理搜查，最高法院此前已在 Riley 诉 California 案和 Carpenter 诉 United States 案中将保护范围扩展至数字数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Geofence_warrant">Geofence warrant - Wikipedia</a></li>
<li><a href="https://www.brennancenter.org/our-work/policy-solutions/fourth-amendment-digital-age">The Fourth Amendment in the Digital Age | Brennan Center for Justice</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍称赞该裁决是隐私权的胜利，一些人注意到法院在意见中引用了事实来源。其他人则提出对其他监控技术（如自动车牌识别器）的影响，少数人批评持异议的大法官倾向于支持无限制的政府权力。

**标签**: `#privacy`, `#supreme court`, `#surveillance`, `#digital rights`, `#law`

---

<a id="item-2"></a>
## [Ornith-1.0：用于智能体编程的自脚手架大语言模型](https://simonwillison.net/2026/Jun/29/ornith/#atom-everything) ⭐️ 8.0/10

DeepReinforce 发布了 Ornith-1.0，这是一个基于 Gemma 4 和 Qwen 3.5 构建的开权重（MIT 许可）智能体编程大语言模型系列，尺寸从 9B 到 397B 不等。它在编程基准测试中达到了同尺寸开源模型的最先进性能。 Ornith-1.0 引入了一种自脚手架训练框架，模型学会同时生成解决方案轨迹和任务特定的脚手架，无需人工设计的脚手架即可自我改进。这可能会显著提升开源智能体编程能力，并使强大的编程助手可在本地硬件上运行。 该模型系列包括 9B Dense、31B Dense、35B MoE 和 397B MoE 变体，均采用 MIT 许可。早期用户报告显示，它生成的思维链更短，比 Qwen 3.6 35B 等同类模型快达 3 倍，同时保持高编程性能。

rss · Simon Willison · 6月29日 16:17

**背景**: 智能体编程指的是能够自主使用工具（如代码编辑器、终端）解决编程任务的大语言模型。传统方法依赖手工制作的脚手架（harness）来指导模型的工具使用。Ornith-1.0 的自脚手架创新使模型在训练过程中学习自己的脚手架策略，提高了效率和效果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deep-reinforce.com/ornith_1_0.html">Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding | DeepReinforce Blog | Jun. 2026</a></li>
<li><a href="https://essamamdani.com/blog/ornith-1-0-self-scaffolding-llm-coding-2026">Ornith-1.0: The Self-Scaffolding LLM That Teaches Itself to Code Better | Essa Mamdani | Essa Mamdani</a></li>
<li><a href="https://huggingface.co/deepreinforce-ai">deepreinforce-ai (DeepReinforce)</a></li>

</ul>
</details>

**社区讨论**: 社区反馈总体积极：用户认为 Ornith-1.0 比之前的本地模型更有用，有人指出这是第一个没有被立即拒绝的 Qwen 微调模型。另一位用户报告说它比 Qwen 3.6 35B 略好，并且由于思维链更短，速度提高了 3 倍。一些用户质疑其新颖性，并询问有关自我改进机制的更多细节。

**标签**: `#LLM`, `#open-source`, `#coding`, `#AI agents`, `#model release`

---

<a id="item-3"></a>
## [华盛顿邮报测试 AI 聊天机器人政治偏见](https://news.google.com/rss/articles/CBMixwFBVV95cUxNcjNMZk5ZYVBRRHlTbDJrZl85THhCTHJvczVHMzlPcnpUdndRdkV1NGZoNFdvMzNBLVdZaHZpS0tEY1dfWFBYTWtKUXpnQzhFa09vMXBHYmNuOEV3TmJuRWVXeTFvQW1adlNBRDg2R0NBUEhQLXlwdWZHVHNLRUVXYjdRUk9FTjFXSDRGenUyZkZxMkdZelk4OWF5VGI4S2Q4U3lyQUpEWEROTFJLUlM3alNwaEQtV1FveVU4bjV1dW1SM3ZvenFZ?oc=5) ⭐️ 8.0/10

《华盛顿邮报》对包括 ChatGPT 在内的主要 AI 聊天机器人进行了系统性测试，以评估其政治偏见，并公布了测试结果。 这项调查揭示了广泛使用的 AI 系统中潜在的政治偏见，引发了对 AI 生成内容公平性和可信度的担忧。 测试方法可能包括向聊天机器人提出带有政治色彩的提示，并分析其回答是否存在党派倾向。

google_news · The Washington Post · 6月30日 01:23

**背景**: 像 ChatGPT 这样的 AI 聊天机器人是在互联网上的大型数据集上训练的，这些数据可能包含有偏见或不平衡的政治观点。评估和减轻这种偏见是 AI 伦理和负责任部署中的关键挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.fluence.network/blog/llm-evaluation-framework/">LLM Evaluation Framework for RAG and AI Agents</a></li>
<li><a href="https://www.langchain.com/resources/how-to-evaluate-llms">Evaluating LLMs and Agents: Benchmarks, Evals & Guardrails</a></li>
<li><a href="https://openfabric.ai/blog/llm-evaluation-methodologies-a-deep-dive-into-llm-evals">LLM Evaluation methodologies : A Deep Dive into LLM Evals</a></li>

</ul>
</details>

**标签**: `#AI bias`, `#ChatGPT`, `#political bias`, `#AI ethics`, `#LLM evaluation`

---

<a id="item-4"></a>
## [纽约梅隆银行为机构客户推出 USDC 铸造与赎回服务](https://www.coindesk.com/business/2026/06/29/wall-street-s-bny-expands-stablecoin-services-for-institutions-starting-with-circle-s-usdc) ⭐️ 7.0/10

纽约梅隆银行扩展其数字资产托管平台，支持 Circle 的 USDC，使机构客户能够直接通过该银行存储、转移、铸造和赎回该稳定币。 此举标志着传统金融对稳定币主流采用的重要一步，一家华尔街主要托管机构现在为机构投资者提供集成的稳定币服务。 USDC 是纽约梅隆银行平台上首个可用的稳定币，该银行已是 USDC 储备的主要托管人，这加深了其与 Circle 的合作关系。

rss · CoinDesk · 6月29日 14:46

**背景**: 纽约梅隆银行管理着 46.7 万亿美元资产，于 2022 年 10 月成为首家获得 SEC 和 NY DFS 批准为机构客户持有比特币和以太坊的美国银行。像 USDC 这样的稳定币是与法定货币挂钩的数字代币，可实现高效的链上交易。铸造和赎回指的是稳定币与法定货币之间的创建和兑换。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cointelegraph.com/news/bny-adds-usdc-minting-and-redemption-to-institutional-custody-platform">BNY adds USDC minting and redemption to institutional custody ...</a></li>
<li><a href="https://tokenmetrics.com/usdc/news/bny-usdc-minting-institutional-custody/">BNY Adds USDC Minting To Institutional Custody Platform</a></li>
<li><a href="https://cryptobriefing.com/bny-mellon-usdc-digital-asset-custody/">BNY Mellon integrates USDC as first stablecoin on Digital Asset...</a></li>

</ul>
</details>

**标签**: `#stablecoins`, `#institutional crypto`, `#BNY Mellon`, `#USDC`, `#fintech`

---

<a id="item-5"></a>
## [患者将 AI 工具带入治疗会话](https://news.google.com/rss/articles/CBMibEFVX3lxTE1WWnJKR2tRSjN0dk1PajZUX085VmM3aGxKZWRJWGNnTjVvSHZSZWlnd05oM2llajF6YXBDRV8zOTRFRjV6ZTF2SW5FUUh2UU5OLVNMN0tYX2k2cXZvZHFvU2c5UXF6OHNJY3lieQ?oc=5) ⭐️ 7.0/10

患者越来越多地在治疗会话中使用聊天机器人、语言模型等 AI 工具，这一趋势由美国心理学会强调。 这一趋势挑战了传统的治疗边界，并引发关于隐私、疗效和治疗师角色的伦理问题，可能重塑心理健康实践。 APA 报告指出，一些患者使用 AI 进行自我诊断、情感支持或为治疗做准备，而治疗师则努力思考如何负责任地整合这些工具。

google_news · American Psychological Association (APA) · 6月30日 07:22

**背景**: AI 在心理健康领域的应用正在增长，许多应用提供类似治疗的互动。但患者将自带的 AI 带入正式治疗是一个较新的现象，模糊了专业帮助与自助之间的界限。

**标签**: `#AI in healthcare`, `#mental health`, `#therapy`, `#ethics`, `#AI adoption`

---

<a id="item-6"></a>
## [重新思考 AI 治理：关键问题](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPaXhGeDlGNzRDMkVFUmlGYmFFamh1SWZoRi1rNl9FeHhSZERYTExoZXNHNHloaTRtbzFEa25WNkRNOG9nN1NoUHdkT2R5T2JpYS1BbGR2bjZBd1B1RmNDSDZqTmk1UzdfWHUyX0IzM1lJWkVlRWlQeTNtNUZHdXg3LWJKMFhudDM1?oc=5) ⭐️ 7.0/10

MIT 斯隆管理评论发表文章，指出 AI 治理的核心问题不在于控制 AI，而在于如何设计符合人类价值观和社会目标的系统。 这一观点将讨论从基于恐惧的监管转向主动设计，影响政策制定者和组织对待 AI 伦理与治理框架的方式。 文章强调治理应关注 AI 使用的目的和背景，而不仅仅是技术能力或风险。

google_news · MIT Sloan Management Review · 6月30日 11:00

**背景**: AI 治理指指导人工智能开发和部署的政策、法律和框架。当前的讨论常集中于偏见、隐私和就业替代等风险。

**标签**: `#AI governance`, `#artificial intelligence`, `#policy`, `#ethics`

---