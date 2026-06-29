---
layout: default
title: "Horizon Summary: 2026-06-29 (ZH)"
date: 2026-06-29
lang: zh
---

> 从 88 条内容中筛选出 8 条重要资讯。

---

1. [最高法院裁定地理围栏搜查令需受宪法保护](#item-1) ⭐️ 9.0/10
2. [谷歌 AI 同行评审处理约 1 万篇论文，错误捕获率提升 34%](#item-2) ⭐️ 9.0/10
3. [llama.cpp b9840 新增 DeepSeek V4 支持](#item-3) ⭐️ 8.0/10
4. [Ornith-1.0：用于智能编码的开源权重大语言模型](#item-4) ⭐️ 8.0/10
5. [Jon Udell：将“人在回路”翻转为“智能体在回路”](#item-5) ⭐️ 8.0/10
6. [ChatGPT 推翻陈立杰 7 年猜想](#item-6) ⭐️ 8.0/10
7. [OpenAI 报告绘制 AI 对欧盟就业影响图](#item-7) ⭐️ 7.0/10
8. [Hack Your Summer：免费学生暑期冲刺项目](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [最高法院裁定地理围栏搜查令需受宪法保护](https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision) ⭐️ 9.0/10

美国最高法院裁定，地理围栏搜查令需受第四修正案的宪法保护，限制了无证获取位置数据的行为。该裁决于 2026 年 6 月 29 日作出。 这一里程碑式的裁决要求对大规模位置数据搜索需具备合理根据，从而显著影响隐私权和执法实践，为大规模监控时代的数字隐私树立了先例。 该案涉及谷歌提供银行抢劫案附近设备的位置数据，信息分三批共享。法院认为，地理围栏搜查令属于第四修正案禁止的一般搜查令。

hackernews · cdrnsf · 6月29日 15:54 · [社区讨论](https://news.ycombinator.com/item?id=48720924)

**背景**: 地理围栏搜查令是一种允许执法机构获取特定地理区域内、特定时间段内所有移动设备位置数据的搜查令。第四修正案保护公民免受不合理搜查和扣押，而地理围栏搜查令作为数字版的一般搜查令一直存在争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Geofence_warrant">Geofence warrant - Wikipedia</a></li>
<li><a href="https://www.congress.gov/crs-product/LSB11274">Geofence Warrants and the Fourth Amendment | Congress.gov | Library of Congress</a></li>
<li><a href="https://harvardlawreview.org/blog/2025/02/much-ado-about-geofence-warrants/">Much Ado About Geofence Warrants - Harvard Law Review</a></li>

</ul>
</details>

**社区讨论**: 评论者提到了如 Paula Broadwell 案等历史案例，以说明替代识别方法。有人对巴雷特大法官加入少数派表示惊讶，也有人询问实际影响，例如警方现在是否需要在获取位置数据前对特定嫌疑人具备合理根据。

**标签**: `#privacy`, `#supreme court`, `#geofence warrants`, `#law enforcement`, `#constitutional law`

---

<a id="item-2"></a>
## [谷歌 AI 同行评审处理约 1 万篇论文，错误捕获率提升 34%](https://www.reddit.com/r/MachineLearning/comments/1uio9rb/googles_agentic_peerreviewer_handled_10k_papers/) ⭐️ 9.0/10

谷歌在 ICML 和 STOC 会议上部署了代理式 AI 同行评审系统，以 30 分钟的处理时间审阅了约 1 万篇论文，正式论文显示其比零样本提示多捕获 34%的数学错误。 这为会议规模的 AI 辅助科学评审开创了先例，可能加速同行评审流程并提高数学内容错误检测能力，从而改变顶级计算机科学会议处理投稿的方式。 该系统采用代理式工作流程，超越了简单的零样本提示，支持迭代推理和验证。错误检测提升 34%特指数学错误，系统平均每篇论文审阅时间为 30 分钟。

reddit · r/MachineLearning · /u/Justgototheeffinmoon · 6月29日 10:05

**背景**: 同行评审是学术出版中关键但耗时的过程，通常需要数月。零样本提示要求 AI 在没有示例的情况下执行任务，对于数学验证等复杂任务效果较差。代理式 AI 系统通过多步推理和工具使用来提高准确性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://paperreview.ai/tech-overview">Tech Overview - Stanford Agentic Reviewer</a></li>
<li><a href="https://medium.com/data-science-in-your-pocket/andrew-ngs-agentic-reviewer-ai-for-research-paper-reviews-1c2d9cda8086">Andrew NG’s Agentic Reviewer : AI for Research Paper Reviews | by Mehul Gupta | Data Science in Your Pocket | Medium</a></li>

</ul>
</details>

**社区讨论**: Reddit 评论普遍称赞其速度和规模，一些人指出即使不完美的 AI 评审也能通过快速反馈加速研究。其他人则担忧过度依赖 AI 和潜在偏见，但总体对结果的正式文档持积极态度。

**标签**: `#AI`, `#peer review`, `#machine learning`, `#conference`, `#automation`

---

<a id="item-3"></a>
## [llama.cpp b9840 新增 DeepSeek V4 支持](https://github.com/ggml-org/llama.cpp/releases/tag/b9840) ⭐️ 8.0/10

llama.cpp 版本 b9840 新增了对 DeepSeek V4 模型架构的支持，包括 Pro 和 Flash 两种变体，并引入了闪存注意力、图复用和填充等优化以实现高效推理。 此版本使得在消费级硬件上通过 CPU 和 GPU 后端本地推理 DeepSeek V4 成为可能，该模型是拥有高达 1.6 万亿参数的先进混合专家模型，从而让尖端大语言模型技术更加普及。 该版本包含多位开发者的贡献，涉及 Sinkhorn 算法调整、KV 缓存预留以及多序列推理支持。DeepSeek V4 模型采用结合压缩稀疏注意力和重度压缩注意力的混合注意力机制。

github · github-actions[bot] · 6月29日 10:25

**背景**: llama.cpp 是一个开源 C++ 库，用于在 CPU 和 GPU 上高效推理大语言模型，使用 GGUF 格式存储模型。DeepSeek V4 是一个混合专家模型系列，总参数量高达 1.6 万亿，采用混合注意力架构，支持长达一百万个 token 的上下文处理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro">deepseek-ai/DeepSeek-V4-Pro · Hugging Face</a></li>
<li><a href="https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond">The Complete Guide to DeepSeek Models: V3, R1, V4 and Beyond</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#DeepSeek V4`, `#LLM inference`, `#open source`

---

<a id="item-4"></a>
## [Ornith-1.0：用于智能编码的开源权重大语言模型](https://simonwillison.net/2026/Jun/29/ornith/#atom-everything) ⭐️ 8.0/10

DeepReinforce 发布了 Ornith-1.0，这是一个用于智能编码的开源权重大语言模型系列（MIT 许可），提供 9B、31B、35B MoE 和 397B MoE 四种变体，基于 Gemma 4 和 Qwen 3.5 构建。在编码基准测试中，它在同等规模的开源模型中达到了最先进的性能。 此次发布通过提供一个许可宽松、性能卓越的模型，推动了开源智能编码的发展，该模型能够自主规划、编写、测试和修改代码。它降低了开发者和研究人员构建自主编码代理的门槛，无需依赖专有模型。 该模型采用自脚手架技术，即大语言模型生成显式的逐步分解来处理复杂编码任务。早期测试表明，它能够熟练地在多次工具调用中运行代理框架，35B GGUF 量化版本在本地运行速度可达 103 tokens/秒。

rss · Simon Willison · 6月29日 16:17

**背景**: 智能编码是指自主 AI 代理在最少人工干预下规划、编写、测试和修改代码的 AI 辅助软件开发方式。自脚手架技术利用大语言模型阐述记忆算法过程的能力，让其生成显式的逐步分解。混合专家（MoE）模型使用多个较小的专家网络，根据输入激活部分网络，从而实现高效扩展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=48709744">Ornith-1.0: Self - Scaffolding LLMs for Agentic Coding | Hacker News</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agentic_coding">Agentic coding</a></li>
<li><a href="https://cloud.google.com/discover/what-is-agentic-coding">What is agentic coding? How it works and use cases | Google Cloud</a></li>

</ul>
</details>

**标签**: `#LLM`, `#coding`, `#open-source`, `#agentic`, `#model release`

---

<a id="item-5"></a>
## [Jon Udell：将“人在回路”翻转为“智能体在回路”](https://simonwillison.net/2026/Jun/28/jon-udell/#atom-everything) ⭐️ 8.0/10

Jon Udell 提出将主流叙事从“人在回路”翻转为“智能体在回路”，主张人类应保持主导权，邀请 AI 智能体作为团队成员，而非被排除在回路之外。 这一翻转改变了 AI 辅助软件开发中的权力动态，强调人类监督与协作而非黑箱自动化，有望带来更可信、可审查的智能体生成代码。 Udell 的观点出自其博客文章《医生，智能体创建不可审查的 PR 时很痛。别那么做》，该文警告 AI 智能体生成庞大、不透明的拉取请求，并倡导小而可审查的差异提交。

rss · Simon Willison · 6月28日 21:57

**背景**: “人在回路”（HITL）传统上指需要人类批准或干预 AI 行动的系统。Udell 的“智能体在回路”将其翻转，将人类定位为主要决策者，招募 AI 智能体作为协作者。这与智能体软件开发的最佳实践一致，例如保持差异小并需要人类审查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.jonudell.net/2026/06/28/doctor-it-hurts-when-agents-create-unreviewable-prs-dont-do-that/">“Doctor, it hurts when agents create unreviewable PRs .” “Don’t do that.”</a></li>
<li><a href="https://timdeschryver.dev/blog/keep-agentic-ai-simple-a-practical-workflow-for-software-development">Keep Agentic AI Simple: A Practical Workflow for Software Development</a></li>
<li><a href="https://cloud.google.com/discover/what-is-agentic-coding">What is agentic coding? How it works and use cases | Google Cloud</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#software development`, `#human-AI collaboration`, `#agentic development`

---

<a id="item-6"></a>
## [ChatGPT 推翻陈立杰 7 年猜想](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&mid=2652709773&idx=2&sn=68bde762eb0070f5bd61518728971232) ⭐️ 8.0/10

ChatGPT 在 OpenAI 解决 Erdős 猜想的基础上，据称推翻了一个陈立杰研究了七年的计算几何核心猜想。 这展示了 AI 解决长期数学问题的能力日益增强，可能加速计算几何及相关领域的研究。 该反证利用了 OpenAI 最近对 Erdős 猜想的解决方案，但计算几何猜想的具体内容及反证方法尚未公开。

rss · 新智元 · 6月29日 05:01

**背景**: 陈立杰是著名的中国计算机科学家，以计算复杂性和几何学方面的工作闻名。Erdős 猜想是数论中一个著名的未解决问题。OpenAI 最近宣布解决了 Erdős 猜想，为这一新结果提供了基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Erdős_conjecture">Erdős conjecture</a></li>
<li><a href="https://chen-lijie.github.io/">Lijie Chen</a></li>

</ul>
</details>

**标签**: `#AI`, `#computational geometry`, `#ChatGPT`, `#OpenAI`, `#research breakthrough`

---

<a id="item-7"></a>
## [OpenAI 报告绘制 AI 对欧盟就业影响图](https://openai.com/index/mapping-ai-jobs-transition-eu) ⭐️ 7.0/10

OpenAI 发布了一份报告，分析了 AI 如何自动化、增强或改变欧盟各职业，为劳动力转型提供了数据驱动的见解。 该报告为欧盟政策制定者和企业应对 AI 驱动的劳动力市场变化提供了宝贵指导，可能影响劳动力规划和再培训计划。 该报告绘制了哪些职业最易受自动化影响、哪些可能增长以及哪些将经历工作流程变化，但摘要中未详细说明具体数字或模型。

rss · OpenAI Blog · 6月29日 07:00

**背景**: 像大语言模型这样的 AI 技术越来越能够执行传统上由人类完成的任务，引发了关于就业替代和技能转变的讨论。欧盟在 AI 监管方面一直很积极，因此这类报告对政策讨论非常及时。

**标签**: `#AI`, `#labor market`, `#EU`, `#automation`, `#policy`

---

<a id="item-8"></a>
## [Hack Your Summer：免费学生暑期冲刺项目](https://simonwillison.net/2026/Jun/28/hack-your-summer/#atom-everything) ⭐️ 6.0/10

Hack Your Summer 是一个为期四周的免费生产冲刺项目，面向受实习短缺影响的学生；第二期将于 2026 年 7 月 13 日开始，申请截止日期为 7 月 8 日。 该计划为未能获得稀缺实习机会的学生提供了替代途径，帮助他们在严峻的就业市场中构建真实项目并拓展职业人脉。 由于时区协调问题，该项目目前仅限美国学生参加，但组织者希望未来扩展到国际范围。同时也在招募志愿导师。

rss · Simon Willison · 6月28日 19:26

**背景**: 生产冲刺（production sprint）是一个短期的、有时间限制的阶段（通常为 1-4 周），团队在此期间密集工作以产出具体成果，灵感来源于敏捷软件开发中的冲刺概念。实习危机指的是实习岗位数量相对于寻求实习的学生数量严重不足，这一问题在 2025-2026 年因企业招聘减少而加剧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.hackyoursummer.org/">Hack Your Summer</a></li>
<li><a href="https://www.hackyoursummer.org/details">Details — Hack Your Summer</a></li>
<li><a href="https://www.cnn.com/2026/04/06/business/job-market-internships-squeeze">The job market is so tough, young people are struggling just to land internships | CNN Business</a></li>

</ul>
</details>

**标签**: `#education`, `#internships`, `#student-programs`, `#summer-sprint`

---