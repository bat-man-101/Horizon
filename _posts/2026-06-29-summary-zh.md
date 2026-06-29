---
layout: default
title: "Horizon Summary: 2026-06-29 (ZH)"
date: 2026-06-29
lang: zh
---

> 从 88 条内容中筛选出 8 条重要资讯。

---

1. [最高法院：地理围栏搜查令需受宪法保护](#item-1) ⭐️ 9.0/10
2. [ChatGPT 推翻陈立杰苦研 7 年的计算几何难题](#item-2) ⭐️ 9.0/10
3. [谷歌 AI 同行评审员处理约 1 万篇顶会论文](#item-3) ⭐️ 9.0/10
4. [llama.cpp b9840 新增 DeepSeek V4 支持](#item-4) ⭐️ 8.0/10
5. [Ornith-1.0：面向智能体编程的开源权重大模型系列](#item-5) ⭐️ 8.0/10
6. [Jon Udell：将“人在回路”翻转为“智能体在回路”](#item-6) ⭐️ 8.0/10
7. [Hack Your Summer：面向学生的免费四周冲刺项目](#item-7) ⭐️ 6.0/10
8. [OpenAI 报告绘制欧盟 AI 就业影响图](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [最高法院：地理围栏搜查令需受宪法保护](https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision) ⭐️ 9.0/10

美国最高法院裁定，要求科技公司提供特定区域内所有设备位置数据的地理围栏搜查令，必须遵守第四修正案关于禁止不合理搜查和扣押的保护。 这一里程碑式的裁决极大地限制了执法部门未经授权批量收集位置数据的行为，加强了数百万智能手机用户的数字隐私权，并为未来的监控技术树立了先例。 该裁决源于一起银行抢劫案，谷歌提供了案发现场附近 19 台设备的位置数据；法院认为此类搜查令需要具备可能原因和特定性，类似于传统搜查令。

hackernews · cdrnsf · 6月29日 15:54 · [社区讨论](https://news.ycombinator.com/item?id=48720924)

**背景**: 地理围栏搜查令是一种法院命令，要求谷歌等公司识别特定时间段内特定地理区域内的所有移动设备。第四修正案保护公民免受不合理搜查，但其在数字位置数据上的应用一直存在争议。最高法院 2026 年的裁决将 Carpenter 诉美国案等早期判例扩展到地理围栏搜查令。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Geofence_warrant">Geofence warrant - Wikipedia</a></li>
<li><a href="https://legalclarity.org/what-is-a-geofence-warrant-and-how-does-it-work/">What Is a Geofence Warrant: Fourth Amendment Challenges</a></li>
<li><a href="https://www.congress.gov/crs_external_products/LSB/PDF/LSB11274/LSB11274.4.pdf">Geofence Warrants and the Fourth Amendment - Congress.gov</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了宽慰和赞同，一些人指出实际影响是警方现在必须在获得位置数据前对特定个人有合理怀疑。其他人批评持反对意见的法官 Alito、Thomas 和 Barrett。有人分享了完整判决书的 PDF 链接。

**标签**: `#privacy`, `#supreme court`, `#fourth amendment`, `#geofence warrants`, `#digital rights`

---

<a id="item-2"></a>
## [ChatGPT 推翻陈立杰苦研 7 年的计算几何难题](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&mid=2652709773&idx=2&sn=68bde762eb0070f5bd61518728971232) ⭐️ 9.0/10

据报道，ChatGPT 在 OpenAI 解决 Erdős 猜想的基础上，推翻了一个计算几何核心难题，该问题曾是姚班传奇人物陈立杰苦思 7 年的课题。 这标志着 AI 辅助理论研究的一个范式转变，表明大型语言模型能够为计算几何和理论计算机科学中长期未解的难题做出贡献。 由于内容碎片化，具体问题及 ChatGPT 贡献的确切性质尚不明确，但该突破直接建立在 OpenAI 近期解决 Erdős 猜想的基础之上。

rss · 新智元 · 6月29日 05:01

**背景**: Erdős 猜想是数学中一个著名的未解问题，常指关于算术级数的 Erdős–Turán 猜想。陈立杰是中国著名的理论计算机科学家，以计算复杂性方面的工作闻名。姚班是清华大学一个享有盛誉的精英本科项目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Erdős_conjecture">Erdős conjecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/List_of_conjectures_by_Paul_Erdős">List of conjectures by Paul Erdős - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Erdős_conjecture_on_arithmetic_progressions">Erdős conjecture on arithmetic progressions - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#computational geometry`, `#OpenAI`, `#ChatGPT`, `#theoretical computer science`

---

<a id="item-3"></a>
## [谷歌 AI 同行评审员处理约 1 万篇顶会论文](https://www.reddit.com/r/MachineLearning/comments/1uio9rb/googles_agentic_peerreviewer_handled_10k_papers/) ⭐️ 9.0/10

谷歌在 ICML 和 STOC 部署了一个智能体 AI 同行评审员，以 30 分钟的处理时间评审了约 1 万篇论文，正式研究论文显示其比零样本提示多检测出 34%的数学错误。 这为会议规模的 AI 自动化科学评审开创了先例，可能加速同行评审过程并提高数学内容错误检测能力，从而改变会议处理论文评审的方式。 该智能体 AI 评审员在捕捉数学错误方面比零样本提示提高了 34%，记录这项工作的正式论文现已发布在 arXiv 上（2606.28277）。

reddit · r/MachineLearning · /u/Justgototheeffinmoon · 6月29日 10:05

**背景**: 零样本提示是一种 AI 模型在没有示例的情况下仅依靠预训练知识执行任务的技术。智能体 AI 系统旨在通过规划和执行动作来自主完成多步骤任务，例如评审论文。ICML 和 STOC 分别是机器学习和计算理论领域的顶级计算机科学会议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.28277">Towards Automating Scientific Review with Google's Paper Assistant...</a></li>
<li><a href="https://www.promptingguide.ai/techniques/zeroshot">Zero-Shot Prompting | Prompt Engineering Guide</a></li>
<li><a href="https://acm-stoc.org/">ACM STOC Conference : The ACM Symposium on Theory of Computing</a></li>

</ul>
</details>

**标签**: `#AI`, `#peer review`, `#machine learning`, `#conference`, `#automation`

---

<a id="item-4"></a>
## [llama.cpp b9840 新增 DeepSeek V4 支持](https://github.com/ggml-org/llama.cpp/releases/tag/b9840) ⭐️ 8.0/10

llama.cpp 版本 b9840 新增了对 DeepSeek V4 模型架构的支持，包括转换脚本、推理图以及闪存注意力和图重用等优化。 这使得通过 llama.cpp 轻量级 C/C++ 实现，能够在消费级硬件上本地高效推理 DeepSeek V4——一个拥有新颖 Engram 记忆架构的万亿参数模型。 该版本包含多位开发者的贡献，包括 Sinkhorn 算法的修正、闪存注意力的填充，以及对 DeepSeek V4 和 V4 Pro 两种变体的支持。初始仅支持单序列推理。

github · github-actions[bot] · 6月29日 10:25

**背景**: llama.cpp 是一个开源 C/C++ 项目，用于在 CPU 和 GPU 上本地运行大型语言模型。DeepSeek V4 是由 DeepSeek 开发的万亿参数模型，采用新的 Engram 记忆架构，提高了效率和上下文处理能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepseek.ai/deepseek-v4">DeepSeek V 4 (2026) — 1T Params, Benchmarks & Pricing</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek - Wikipedia</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#DeepSeek V4`, `#LLM inference`, `#open source`, `#machine learning`

---

<a id="item-5"></a>
## [Ornith-1.0：面向智能体编程的开源权重大模型系列](https://simonwillison.net/2026/Jun/29/ornith/#atom-everything) ⭐️ 8.0/10

DeepReinforce 发布了 Ornith-1.0，这是一个采用 MIT 许可证的全新开源权重大模型系列，在编程基准测试上达到了最先进的性能。该系列包括 9B Dense、31B Dense、35B MoE 和 397B MoE 四种变体，基于 Gemma 4 和 Qwen 3.5 构建。 Ornith-1.0 的重要性在于它以宽松的 MIT 许可证将最先进的智能体编程能力带给了开源社区，使开发者能够在本地运行强大的编程智能体。这可能会加速 AI 辅助软件开发的普及，并减少对专有模型的依赖。 该模型采用自脚手架方法，无需外部组件或架构修改，将隐式推理转化为显式的文本分解。初步测试表明，它能够熟练地在智能体框架中处理多次工具调用，图像生成速度达到 103 tokens/秒。

rss · Simon Willison · 6月29日 16:17

**背景**: 智能体编程是指使用 AI 智能体辅助软件开发任务，如代码生成、调试和测试。自脚手架是一种技术，大模型利用自身推理将复杂任务分解为子任务，无需外部脚手架工具。混合专家模型（MoE）是一种使用多个专门子模型来提高效率的架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=48709744">Ornith-1.0: Self - Scaffolding LLMs for Agentic Coding | Hacker News</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agentic_coding">Agentic coding</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>

</ul>
</details>

**标签**: `#LLM`, `#open-source`, `#coding`, `#agentic`, `#model release`

---

<a id="item-6"></a>
## [Jon Udell：将“人在回路”翻转为“智能体在回路”](https://simonwillison.net/2026/Jun/28/jon-udell/#atom-everything) ⭐️ 8.0/10

Jon Udell 提议将“人在回路”重新定义为“智能体在回路”，主张人类应主导流程并邀请 AI 智能体作为协作者，而非被降级为监督角色。 这种重新定义改变了人机协作中的权力动态，强调人类主导权和可审查性，对于在 AI 辅助软件开发中建立信任和安全性至关重要。 Udell 特别警告了智能体生成的“不可审查的拉取请求”，倡导透明、由人类主导的流程，让智能体在既定工作流中做出贡献。

rss · Simon Willison · 6月28日 21:57

**背景**: “人在回路”这一短语传统上描述人类监督 AI 决策的系统。然而，批评者认为它暗示人类是自动化流程的次要角色。Udell 的“智能体在回路”翻转了这一概念，将人类定位为主要决策者，邀请 AI 智能体协助而非取代他们的工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://waxell.ai/blog/human-in-the-loop-vs-human-on-the-loop-ai-agents">Human - in - the - Loop vs Human -on- the - Loop for AI Agents</a></li>
<li><a href="https://www.growthjockey.com/blogs/human-in-the-loop-vs-agentic-ai">Human in the Loop (HITL) vs . Agentic AI: A Detailed Comparison</a></li>
<li><a href="https://rossjax.medium.com/if-theres-a-human-in-the-loop-is-it-even-an-agent-165810693233">If there’s a Human In The Loop , Is It Even an Agent ? | Medium</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#software development`, `#human-AI collaboration`, `#code review`

---

<a id="item-7"></a>
## [Hack Your Summer：面向学生的免费四周冲刺项目](https://simonwillison.net/2026/Jun/28/hack-your-summer/#atom-everything) ⭐️ 6.0/10

Hack Your Summer 是一个面向本科生和研究生的免费四周生产冲刺项目，旨在帮助学生构建真实项目，以应对美国实习危机。第二期于 7 月 13 日开始，申请截止日期为 7 月 8 日。 该计划为因招聘减少而无法获得传统实习的学生提供了替代途径，帮助他们获得实践经验和可展示的作品。它解决了当前年轻人才就业市场中的关键缺口。 该项目免费，面向本科生、研究生和应届毕业生。它包含行业专业人士的指导，参与者将产出可向未来雇主展示的、面向公众的实际作品。

rss · Simon Willison · 6月28日 19:26

**背景**: 美国实习危机指的是由于公司削减招聘和指导能力，导致可用实习岗位大幅减少。Hack Your Summer 受前美国首席数据科学家 DJ Patil 启发，旨在通过提供结构化的、有导师支持的项目冲刺来填补这一空白。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DJ_Patil">DJ Patil</a></li>

</ul>
</details>

**标签**: `#education`, `#internships`, `#student-projects`, `#summer-program`

---

<a id="item-8"></a>
## [OpenAI 报告绘制欧盟 AI 就业影响图](https://openai.com/index/mapping-ai-jobs-transition-eu) ⭐️ 6.0/10

OpenAI 发布了一份报告，分析人工智能如何改变欧盟各职业，识别出面临自动化风险的岗位、可能增长的岗位以及工作流程将发生变化的岗位。 该报告为政策制定者和企业提供了数据驱动的视角，以预测 AI 驱动的劳动力变化，可能影响整个欧盟的劳动力再培训和战略。 该报告使用一种新颖的方法绘制了各职业的 AI 暴露程度，但摘要中未披露具体技术细节，如使用的模型或数据来源。

rss · OpenAI Blog · 6月29日 07:00

**背景**: AI 自动化一直是劳动经济学中日益受到关注的问题，研究预测将出现大量岗位流失。欧盟通过《AI 法案》积极监管 AI，因此这份报告对于理解特定行业的影响非常及时。

**标签**: `#AI`, `#labor market`, `#EU`, `#automation`

---