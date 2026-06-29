---
layout: default
title: "Horizon Summary: 2026-06-29 (ZH)"
date: 2026-06-29
lang: zh
---

> 从 88 条内容中筛选出 8 条重要资讯。

---

1. [最高法院：地理围栏搜查令需受宪法保护](#item-1) ⭐️ 9.0/10
2. [谷歌 AI 同行评审处理约 1 万篇论文，错误率降低 34%](#item-2) ⭐️ 9.0/10
3. [llama.cpp b9840 新增 DeepSeek V4 支持](#item-3) ⭐️ 8.0/10
4. [Ornith-1.0：开源自脚手架编码大模型](#item-4) ⭐️ 8.0/10
5. [ChatGPT 推翻陈立杰苦思 7 年的计算几何难题](#item-5) ⭐️ 8.0/10
6. [Jon Udell：邀请智能体加入循环，而非被排除在外](#item-6) ⭐️ 7.0/10
7. [Hack Your Summer：面向学生的免费四周冲刺项目](#item-7) ⭐️ 6.0/10
8. [OpenAI 绘制欧盟 AI 就业变化图](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [最高法院：地理围栏搜查令需受宪法保护](https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision) ⭐️ 9.0/10

美国最高法院以 6 比 3 裁定，地理围栏搜查令需受第四修正案的宪法保护，限制了无证获取智能手机位置数据的行为。由大法官埃琳娜·卡根撰写的判决认为，用户不会因选择加入谷歌的位置历史记录而丧失隐私预期。 这一里程碑式的裁决显著限制了执法部门将地理围栏搜查令用作大规模监控工具的能力，加强了数百万智能手机用户的数字隐私权。它为第四修正案适用于现代位置追踪技术树立了先例，将影响未来的调查和科技公司的数据共享实践。 该案（Chatrie 诉美国）涉及一名银行抢劫嫌疑人，通过地理围栏搜查令从谷歌的 Sensorvault 获取位置数据而被识别。法院将此案与 2018 年 Carpenter 案（要求对基站位置信息获取搜查令）区分开来，明确将同样的保护适用于地理围栏搜查令。

hackernews · cdrnsf · 6月29日 15:54 · [社区讨论](https://news.ycombinator.com/item?id=48720924)

**背景**: 地理围栏搜查令是一种强制谷歌等公司识别特定时间段内特定地理区域内所有设备的搜查令。执法部门利用这些搜查令通过收集大量无辜旁观者的位置数据来识别未知嫌疑人。第四修正案保护公民免受不合理搜查和扣押，最高法院此前已裁定长期位置追踪需要搜查令。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision">US supreme court rules geofence warrants require constitutional privacy protections | US supreme court | The Guardian</a></li>

</ul>
</details>

**社区讨论**: 评论者对该裁决表示强烈支持，有人指出在没有手机的情况下进行位置追踪的历史案例（如彼得雷乌斯丑闻）。其他人批评持异议的大法官阿利托和托马斯支持无限政府权力，而少数人质疑实际影响，例如警方现在是否需要在获得搜查令前对特定嫌疑人具备可能原因。

**标签**: `#privacy`, `#supreme court`, `#geofence warrants`, `#law enforcement`, `#constitutional law`

---

<a id="item-2"></a>
## [谷歌 AI 同行评审处理约 1 万篇论文，错误率降低 34%](https://www.reddit.com/r/MachineLearning/comments/1uio9rb/googles_agentic_peerreviewer_handled_10k_papers/) ⭐️ 9.0/10

谷歌在顶级计算机科学会议 ICML 和 STOC 部署了一个智能体 AI 同行评审系统，以 30 分钟的周转时间处理了约 1 万篇论文，正式研究论文显示，它比零样本提示多捕捉了 34%的数学错误。 这为在会议规模上实现 AI 自动科学评审开创了先例，可能加速同行评审过程并减轻人类评审员的负担，同时提高对数学内容的错误检测能力。 该智能体 AI 评审系统每篇论文的周转时间为 30 分钟，而人类评审需要数月，其正式论文现已发布在 arXiv 上（2606.28277）。该系统采用智能体工作流，而非简单的零样本提示。

reddit · r/MachineLearning · /u/Justgototheeffinmoon · 6月29日 10:05

**背景**: 同行评审是专家在论文发表前评估其质量和正确性的过程。零样本提示是一种让 AI 模型在没有示例的情况下执行任务的技术，而智能体 AI 系统则通过多步推理和工具使用来获得更好的结果。

**标签**: `#AI`, `#peer review`, `#machine learning`, `#Google`, `#automation`

---

<a id="item-3"></a>
## [llama.cpp b9840 新增 DeepSeek V4 支持](https://github.com/ggml-org/llama.cpp/releases/tag/b9840) ⭐️ 8.0/10

llama.cpp 版本 b9840 新增了对 DeepSeek V4 模型架构的支持，包括转换、推理和优化。该版本还启用了 flash attention、图复用和多序列推理。 此版本使得在消费级硬件上本地高效推理 DeepSeek V4 成为可能，该模型是最先进的混合专家模型，参数高达 1.6 万亿。这极大地扩展了开源大语言模型生态系统的能力。 DeepSeek V4 模型采用混合注意力架构，结合了压缩稀疏注意力（CSA）和重度压缩注意力（HCA）。该版本支持 DeepSeek-V4-Pro（总计 1.6T，激活 49B）和 DeepSeek-V4-Flash（总计 284B，激活 13B）两种变体。

github · github-actions[bot] · 6月29日 10:25

**背景**: llama.cpp 是一个开源的 C/C++ 库，用于在 CPU 和 GPU 上本地运行大型语言模型。它使用 GGUF 格式存储量化模型，从而在消费级硬件上实现高效推理。DeepSeek V4 是 DeepSeek 最新推出的混合专家模型系列，采用新颖的混合注意力机制以支持长上下文处理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro">deepseek-ai/DeepSeek-V4-Pro · Hugging Face</a></li>
<li><a href="https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond">The Complete Guide to DeepSeek Models: V3, R1, V4 and Beyond</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#DeepSeek V4`, `#LLM inference`, `#open-source`, `#machine learning`

---

<a id="item-4"></a>
## [Ornith-1.0：开源自脚手架编码大模型](https://simonwillison.net/2026/Jun/29/ornith/#atom-everything) ⭐️ 8.0/10

DeepReinforce 发布了 Ornith-1.0，这是一个采用 MIT 许可证的开源权重大模型系列（9B 到 397B），通过自脚手架训练框架在编码基准上达到了最先进水平。 此次发布以宽松许可证为开源社区带来了具有竞争力的编码性能，使更广泛的用户能够访问和定制用于智能体编码任务。 模型变体包括 9B Dense、31B Dense、35B MoE 和 397B MoE，基于 Gemma 4 和 Qwen 3.5（均为 Apache 2.0 许可证）构建。自脚手架方法在强化学习过程中联合优化解决方案生成和任务特定脚手架。

rss · Simon Willison · 6月29日 16:17

**背景**: 智能体编码是指 AI 智能体自主执行多步软件开发任务。传统的基于 LLM 的编码智能体使用固定脚手架（harness）来引导模型，而 Ornith-1.0 学习生成自己的脚手架，从而随时间提升性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deep-reinforce.com/ornith_1_0.html">Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding | DeepReinforce Blog | Jun. 2026</a></li>
<li><a href="https://essamamdani.com/blog/ornith-1-0-self-scaffolding-llm-coding-2026">Ornith-1.0: The Self-Scaffolding LLM That Teaches Itself to Code Better | Essa Mamdani | Essa Mamdani</a></li>
<li><a href="https://ornith.site/">Ornith 1 . 0 — Open-Source Agentic Coding Models</a></li>

</ul>
</details>

**社区讨论**: 社区初步反馈积极，用户报告在 LM Studio 和 Pi 集成中表现良好。部分讨论关注与底层 Apache 2.0 模型的许可证兼容性。

**标签**: `#LLM`, `#open-source`, `#coding`, `#AI`, `#machine learning`

---

<a id="item-5"></a>
## [ChatGPT 推翻陈立杰苦思 7 年的计算几何难题](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&mid=2652709773&idx=2&sn=68bde762eb0070f5bd61518728971232) ⭐️ 8.0/10

据报道，ChatGPT 解决了一个困扰著名研究员陈立杰七年的核心计算几何问题，该成果基于 OpenAI 近期解决的一个 Erdős 猜想。 这表明大型语言模型现在能够解决理论计算机科学中长期存在的开放问题，可能加速计算几何及相关领域的研究。 该问题是计算几何中的一个核心问题，陈立杰研究了七年未果。解决方案利用了 OpenAI 最近证明的 Erdős 猜想。

rss · 新智元 · 6月29日 05:01

**背景**: 计算几何研究几何问题的算法，常涉及点、线和形状。陈立杰是清华大学姚班出身的著名计算机科学家，以计算复杂性研究闻名。Erdős 猜想是算术组合学中关于等差数列的著名问题，近期被 OpenAI 解决。

**标签**: `#AI`, `#computational geometry`, `#ChatGPT`, `#breakthrough`, `#OpenAI`

---

<a id="item-6"></a>
## [Jon Udell：邀请智能体加入循环，而非被排除在外](https://simonwillison.net/2026/Jun/28/jon-udell/#atom-everything) ⭐️ 7.0/10

Jon Udell 认为，软件团队不应成为将权力让给机器的“人在回路中”，而应邀请 AI 智能体作为团队成员加入现有工作流，保持人类控制权并确保所有智能体贡献可审查。 这种重新定义将叙事从人类从属转向人类主导，解决了关于不可审查的 PR 和黑箱流程的担忧，推动了一种协作模式，即 AI 增强而非取代人类判断。 Udell 特别批评“人在回路中”这一说法将权力让给机器，并主张“智能体在回路中”，即邀请智能体加入团队现有循环。他强调智能体辅助流程不应是接收提示并输出功能而未经审查的黑箱。

rss · Simon Willison · 6月28日 21:57

**背景**: 智能体软件开发使用 AI 智能体自主执行编码、测试和部署等任务。传统的“人在回路中”模式将人类作为监督者或后备，但 Udell 认为这仍以机器为中心。他提出的“邀请智能体加入循环”将人类作为主要决策者，智能体作为协作者，其工作始终可审查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Human-in-the-loop">Human - in - the - loop - Wikipedia</a></li>
<li><a href="https://www.ness.com/blog/what-is-agentic-software-development/">Agentic Software Development : Beyond Metrics and Speed</a></li>

</ul>
</details>

**标签**: `#agentic development`, `#human-in-the-loop`, `#software engineering`, `#AI`

---

<a id="item-7"></a>
## [Hack Your Summer：面向学生的免费四周冲刺项目](https://simonwillison.net/2026/Jun/28/hack-your-summer/#atom-everything) ⭐️ 6.0/10

Hack Your Summer 是一个免费的四周生产冲刺项目，面向本科生和研究生，旨在通过构建真实项目来替代稀缺的实习机会。第二期将于 7 月 13 日开始，申请截止日期为 7 月 8 日。 该计划应对了影响美国大学生的实习短缺问题，提供了一种结构化的方式来获得实践经验并构建可展示的作品。它有助于弥合学术学习与行业期望之间的差距。 该计划免费开放给本科生、研究生和应届毕业生。它包括来自志愿者的指导，并专注于创建可展示给未来雇主的切实可见的公开作品。

rss · Simon Willison · 6月28日 19:26

**背景**: 许多美国公司减少了招聘和实习生指导能力，导致学生的实习机会减少。Hack Your Summer 通过模拟真实的生产环境并提供导师支持，提供了另一种选择。

**标签**: `#education`, `#internship`, `#student-projects`, `#summer-program`

---

<a id="item-8"></a>
## [OpenAI 绘制欧盟 AI 就业变化图](https://openai.com/index/mapping-ai-jobs-transition-eu) ⭐️ 6.0/10

该报告提供了 AI 对欧洲劳动力市场潜在影响的数据驱动概述，有助于政策制定者、企业和工作者预测并准备劳动力转型。 该报告涵盖了广泛的欧盟职业，并根据受 AI 驱动变化的暴露程度对其进行分类，但缺乏具体的技术细节或个别岗位的精细数据。

rss · OpenAI Blog · 6月29日 07:00

**背景**: 像大型语言模型这样的 AI 技术越来越能够自动化认知任务，引发了关于岗位替代的担忧。该报告旨在量化欧盟哪些行业和角色最脆弱或可能受益。

**标签**: `#AI`, `#labor market`, `#Europe`, `#automation`, `#OpenAI`

---