---
layout: default
title: "Horizon Summary: 2026-06-29 (ZH)"
date: 2026-06-29
lang: zh
---

> 从 89 条内容中筛选出 8 条重要资讯。

---

1. [最高法院裁定地理围栏搜查令需受宪法保护](#item-1) ⭐️ 9.0/10
2. [ChatGPT 推翻陈立杰七年研究，Erdős 猜想被解决](#item-2) ⭐️ 9.0/10
3. [谷歌 AI 同行评审处理 1 万篇论文，错误检测率提高 34%](#item-3) ⭐️ 9.0/10
4. [llama.cpp b9840 版本新增 DeepSeek V4 支持](#item-4) ⭐️ 8.0/10
5. [Ornith-1.0：用于智能体编程的开源权重大语言模型](#item-5) ⭐️ 8.0/10
6. [Jon Udell：将“人在回路”翻转为“智能体在回路”](#item-6) ⭐️ 8.0/10
7. [Hack Your Summer：面向学生的免费四周项目冲刺](#item-7) ⭐️ 6.0/10
8. [OpenAI 绘制欧盟人工智能岗位变化图](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [最高法院裁定地理围栏搜查令需受宪法保护](https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision) ⭐️ 9.0/10

美国最高法院裁定，允许执法部门获取特定区域内所有设备位置数据的地理围栏搜查令，需受第四修正案的宪法保护，限制了无证获取此类数据的行为。 这一里程碑式的裁决要求对批量位置数据需具备可能原因并取得搜查令，从而显著加强了数字隐私权，影响执法部门的犯罪调查方式，并为未来的数字监控案件树立了先例。 该案源于一起银行抢劫案，谷歌提供了案发地点附近 19 台设备的位置数据；法院裁定这种广泛的数据收集违反了第四修正案对不合理搜查的保护。

hackernews · cdrnsf · 6月29日 15:54 · [社区讨论](https://news.ycombinator.com/item?id=48720924)

**背景**: 地理围栏搜查令（又称反向位置搜查令）允许执法部门在特定时间段内搜索谷歌 Sensorvault 等数据库，以获取特定地理区域内的所有设备信息。第四修正案保护公民免受不合理搜查和扣押，但其对数字位置数据的适用性一直存在争议，尤其是在 2018 年 Carpenter 诉美国案判决之后。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Geofence_warrant">Geofence warrant</a></li>

</ul>
</details>

**社区讨论**: 评论者提到了无手机时代的位置追踪历史案例（如 Paula Broadwell 案），并讨论了实际影响，有人对 Barrett 大法官加入少数意见感到惊讶。完整判决书 PDF 被分享以供进一步阅读。

**标签**: `#privacy`, `#supreme court`, `#fourth amendment`, `#digital rights`, `#law enforcement`

---

<a id="item-2"></a>
## [ChatGPT 推翻陈立杰七年研究，Erdős 猜想被解决](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&mid=2652709773&idx=2&sn=68bde762eb0070f5bd61518728971232) ⭐️ 9.0/10

据报道，ChatGPT 推翻了一个与 Erdős 单位距离问题相关的核心计算几何猜想，推翻了知名中国计算机科学家陈立杰七年的研究成果。这一成就基于 OpenAI 上个月宣布解决 Erdős 猜想的工作。 这标志着人工智能驱动数学的一个里程碑，表明大型语言模型不仅能辅助，还能独立推翻长期存在的猜想。它挑战了人类数学家的传统角色，可能加速理论计算机科学的发现。 具体猜想涉及 Erdős 单位距离问题，即平面上 n 个点之间单位距离的最大数量。据报道，OpenAI 的模型生成了一个反例，推翻了先前假设的结构，但完整细节尚未公布。

rss · 新智元 · 6月29日 05:01

**背景**: Erdős 单位距离问题由 Paul Erdős 于 1946 年提出，询问平面上 n 个点之间单位距离对的最大数量。这是离散几何的核心问题，对图论和组合几何有影响。陈立杰是图灵奖得主、计算几何先驱，曾花七年时间研究相关猜想。OpenAI 最近宣布其模型解决了原始 Erdős 猜想，这一新结果扩展了该突破。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/model-disproves-discrete-geometry-conjecture/">An OpenAI model has disproved a central conjecture in... | OpenAI</a></li>
<li><a href="https://scitechdaily.com/for-the-first-time-chatgpt-has-solved-an-unproven-math-problem-in-geometry/">For the First Time, ChatGPT Has Solved an Unproven Math Problem in Geometry</a></li>

</ul>
</details>

**标签**: `#AI`, `#computational geometry`, `#ChatGPT`, `#Erdős conjecture`, `#theoretical computer science`

---

<a id="item-3"></a>
## [谷歌 AI 同行评审处理 1 万篇论文，错误检测率提高 34%](https://www.reddit.com/r/MachineLearning/comments/1uio9rb/googles_agentic_peerreviewer_handled_10k_papers/) ⭐️ 9.0/10

谷歌在顶级计算机科学会议 ICML 和 STOC 部署了智能体 AI 同行评审系统，处理了约 1 万篇论文，平均每篇 30 分钟完成评审；正式研究论文显示，相比零样本提示，该系统能多检测出 34%的数学错误。 这为在会议规模上实现 AI 自动科学评审开创了先例，有望加速同行评审流程、减轻评审者负担，同时提高对数学内容的错误检测能力。 该系统采用多步推理方法而非简单的零样本提示，从而能够发现细微的数学错误。正式论文已在 arXiv 上发布（编号 2606.28277）。

reddit · r/MachineLearning · /u/Justgototheeffinmoon · 6月29日 10:05

**背景**: 同行评审是科学出版的基石，但往往缓慢且负担过重。零样本提示要求 AI 在没有示例的情况下执行任务，而智能体系统则通过迭代推理和工具使用来提高准确性。谷歌的工作建立在早期智能体评审项目（如斯坦福的 PaperReview.ai）的基础上。

**社区讨论**: Reddit 社区对此次大规模部署和正式文档表示兴奋，部分用户讨论 AI 将评审时间从数月缩短到数分钟的潜力。也有人担忧公平性以及 AI 可能遗漏人类评审者能发现的细微错误。

**标签**: `#AI`, `#peer review`, `#machine learning`, `#Google`, `#scientific publishing`

---

<a id="item-4"></a>
## [llama.cpp b9840 版本新增 DeepSeek V4 支持](https://github.com/ggml-org/llama.cpp/releases/tag/b9840) ⭐️ 8.0/10

llama.cpp 的 b9840 版本新增了对 DeepSeek V4 模型架构的支持，包括模型转换、推理和聊天模板集成，由多位开发者共同贡献。 此次更新使得在消费级硬件上本地高效推理拥有 1 万亿参数的 MoE 模型 DeepSeek V4 成为可能，极大地扩展了开源大语言模型生态的能力。 该版本包含对 DeepSeek V4 Pro、flash attention、图复用和多序列推理的支持，同时修复了 bug 并清理了代码。DeepSeek V4 模型采用高效的 MoE 架构，支持高达 100 万 token 的上下文窗口。

github · github-actions[bot] · 6月29日 10:25

**背景**: llama.cpp 是一个开源 C/C++ 项目，用于在 CPU 和 GPU 上本地运行大语言模型。它使用 GGUF 格式实现高效的模型存储和加载。DeepSeek V4 是由 DeepSeek 开发的 1 万亿参数混合专家模型，专为高性能编码和推理任务设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepseek.ai/deepseek-v4">DeepSeek V 4 (2026) — 1T Params, Benchmarks & Pricing</a></li>
<li><a href="https://en.wikipedia.org/wiki/GGUF">GGUF - Wikipedia</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#DeepSeek V4`, `#machine learning`, `#open source`, `#release`

---

<a id="item-5"></a>
## [Ornith-1.0：用于智能体编程的开源权重大语言模型](https://simonwillison.net/2026/Jun/29/ornith/#atom-everything) ⭐️ 8.0/10

DeepReinforce 发布了 Ornith-1.0，这是一个面向智能体编程的开源权重（MIT 许可）大语言模型系列，参数规模从 9B 到 397B MoE 不等，基于 Gemma 4 和 Qwen 3.5 构建。在编程基准测试中，它在同等规模的开源模型中达到了最先进的性能。 Ornith-1.0 为开源社区带来了具有竞争力的智能体编程能力，使开发者能够在本地或自定义环境中运行强大的编程智能体。其自脚手架训练方法可能影响未来用于自主任务求解的大语言模型开发。 该模型系列包括 9B Dense、31B Dense、35B MoE 和 397B MoE 变体，均采用 MIT 许可。早期用户报告显示，在多步骤工具调用任务中性能强劲，20GB GGUF 量化版本运行速度可达 103 tokens/秒。

rss · Simon Willison · 6月29日 16:17

**背景**: 智能体编程是指 AI 智能体自主执行多步骤软件开发任务，如代码生成、调试和测试。Ornith-1.0 使用自脚手架训练框架，联合学习解决问题和构建指导解决方案的脚手架，从而提高效率。该模型采用混合专家（MoE）架构，每个 token 仅激活相关的子网络，从而降低计算成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deep-reinforce.com/ornith_1_0.html">Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding</a></li>
<li><a href="https://simonwillison.net/2026/Jun/29/ornith/">Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agentic_coding">Agentic coding</a></li>

</ul>
</details>

**社区讨论**: 社区反响积极，用户称赞该模型在智能体编程任务中的表现以及宽松的 MIT 许可。一些用户注意到关于 DeepReinforce 的信息较少，但实用技巧和基准测试结果引发了兴趣。

**标签**: `#LLM`, `#open-source`, `#coding`, `#AI agents`, `#machine learning`

---

<a id="item-6"></a>
## [Jon Udell：将“人在回路”翻转为“智能体在回路”](https://simonwillison.net/2026/Jun/28/jon-udell/#atom-everything) ⭐️ 8.0/10

Jon Udell 提议将主流的“人在回路”叙事翻转成“智能体在回路”，主张人类应保持主导权，邀请 AI 智能体加入现有工作流程，而非被插入到 AI 驱动的回路中。 这一框架转变改变了 AI 辅助软件开发中的权力动态，强调人类对 AI 智能体的控制与主导，可能推动更透明、可审查的开发实践。 Udell 特别警告智能体生成不可审查的拉取请求，主张智能体辅助流程不应是黑箱，而应是透明的协作，人类保留最终决定权。

rss · Simon Willison · 6月28日 21:57

**背景**: “人在回路”（HITL）传统上指需要人类批准关键决策的 AI 系统。但批评者认为，HITL 仍可能让人类处于被动审查的角色，缺乏完整上下文。Udell 的“智能体在回路”翻转了这一概念，主张人类的工作流程是首要的，AI 智能体是被邀请的参与者，而非驱动者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vaiotltd.medium.com/human-in-the-loop-vs-human-on-the-loop-880e4538ca65">Human in the Loop vs Human on the Loop | by VAIOT_LTD | Medium</a></li>
<li><a href="https://www.waxell.ai/blog/human-in-the-loop-vs-human-on-the-loop-ai-agents">Human-in-the-Loop vs Human-on-the-Loop for AI Agents</a></li>
<li><a href="https://grayphite.com/blogs/59/">Grayphite | Cutting-Edge Software, AI Solutions & Emerging Tech...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#software development`, `#human-AI collaboration`, `#agentic development`

---

<a id="item-7"></a>
## [Hack Your Summer：面向学生的免费四周项目冲刺](https://simonwillison.net/2026/Jun/28/hack-your-summer/#atom-everything) ⭐️ 6.0/10

Hack Your Summer 是一个面向本科生和研究生的免费四周生产冲刺项目，现已宣布第二期将于 7 月 13 日开始，申请截止日期为 7 月 8 日。该项目帮助学生构建真实的、面向公众的项目，以替代稀缺的实习机会。 该计划应对了美国严峻的实习短缺问题，为学生提供了一条结构化的途径来获得实践经验并构建可展示的作品集。它提供了一种可扩展的、社区支持的替代方案，可能重塑学生向雇主展示技能的方式。 该计划免费，面向本科生、研究生和应届毕业生。同时也在招募志愿者导师，在冲刺期间为参与者提供支持。

rss · Simon Willison · 6月28日 19:26

**背景**: 2026 年美国大学生面临严重的实习危机，企业减少了招聘和指导能力。Hack Your Summer 通过提供结构化的、导师指导的生产冲刺来填补这一空白，让学生构建可以向雇主展示的真实项目。

**标签**: `#education`, `#internship`, `#student-projects`, `#summer-program`

---

<a id="item-8"></a>
## [OpenAI 绘制欧盟人工智能岗位变化图](https://openai.com/index/mapping-ai-jobs-transition-eu) ⭐️ 6.0/10

OpenAI 发布了一份报告，绘制了人工智能如何重塑欧盟各职业的图景，识别了哪些岗位可能面临自动化、增长或工作流程变化。 该报告提供了宏观概述，有助于政策制定者、企业和员工了解欧盟劳动力市场可能因人工智能驱动的转型。 该报告涵盖了欧盟广泛的职业类别，但缺乏深度的技术新颖性或关于变化时间表和规模的具体数据。

rss · OpenAI Blog · 6月29日 07:00

**背景**: 人工智能越来越能够自动化常规任务，这可能导致岗位替代或增强。欧盟一直通过《人工智能法案》等框架积极监管人工智能，因此此类劳动力分析对政策规划具有相关性。

**标签**: `#AI`, `#labor market`, `#automation`, `#EU`, `#workforce`

---