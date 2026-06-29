---
layout: default
title: "Horizon Summary: 2026-06-29 (ZH)"
date: 2026-06-29
lang: zh
---

> 从 88 条内容中筛选出 8 条重要资讯。

---

1. [谷歌 AI 同行评审系统处理约 1 万篇顶会论文](#item-1) ⭐️ 9.0/10
2. [llama.cpp b9840 新增 DeepSeek V4 支持](#item-2) ⭐️ 8.0/10
3. [火箭实验室历史性收购铱星公司](#item-3) ⭐️ 8.0/10
4. [Ornith-1.0：面向智能体编程的开源大模型系列](#item-4) ⭐️ 8.0/10
5. [ChatGPT 推翻 Erdős 猜想，颠覆陈立杰七年研究](#item-5) ⭐️ 8.0/10
6. [Jon Udell：将“人在回路中”重构为“智能体在回路中”](#item-6) ⭐️ 7.0/10
7. [Hack Your Summer：面向学生的免费四周冲刺项目](#item-7) ⭐️ 7.0/10
8. [OpenAI 绘制 AI 对欧盟就业影响图谱](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [谷歌 AI 同行评审系统处理约 1 万篇顶会论文](https://www.reddit.com/r/MachineLearning/comments/1uio9rb/googles_agentic_peerreviewer_handled_10k_papers/) ⭐️ 9.0/10

谷歌在 ICML 和 STOC 部署了一个智能 AI 同行评审系统，处理了约 1 万篇论文，平均 30 分钟完成评审；正式研究论文显示，该系统比零样本提示多检测出 34%的数学错误。 这为会议规模的 AI 自动化科学评审树立了先例，可能通过减轻评审者负担和提高错误检测能力来改变同行评审流程。 该系统是一种智能 AI，模拟会议同行评审流程的多个方面，生成涵盖方法论、贡献、清晰度和相关工作等方面的结构化评审意见。

reddit · r/MachineLearning · /u/Justgototheeffinmoon · 6月29日 10:05

**背景**: 零样本提示是一种 AI 模型在没有先例的情况下仅依靠预训练知识执行任务的技术。而智能评审系统通过多步推理和工具使用，超越了零样本提示，生成更全面的评审意见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://paperreview.ai/tech-overview">Tech Overview - Stanford Agentic Reviewer - paperreview.ai</a></li>
<li><a href="https://rcgsheffield.github.io/research-ai-landscape/tools/stanford-agentic-reviewer">stanford-agentic-reviewer</a></li>
<li><a href="https://phrasly.ai/blog/zero-shot-prompting/">Zero - Shot Prompting : Definition, Examples & How It Works</a></li>

</ul>
</details>

**标签**: `#AI`, `#peer review`, `#machine learning`, `#automation`, `#research`

---

<a id="item-2"></a>
## [llama.cpp b9840 新增 DeepSeek V4 支持](https://github.com/ggml-org/llama.cpp/releases/tag/b9840) ⭐️ 8.0/10

llama.cpp 版本 b9840 引入了对 DeepSeek V4 的支持，包括模型转换、推理以及闪存注意力和图重用等优化。 此版本使得通过 llama.cpp 在消费级硬件上高效本地推理 DeepSeek V4 成为可能，该模型是拥有 1.6 万亿参数和百万 token 上下文窗口的最先进 MoE 模型。 该版本包含 DeepSeek V4 的转换脚本、用于加速注意力计算的闪存注意力，以及减少 token 生成开销的图重用。它还支持多序列推理和部分检查点。

github · github-actions[bot] · 6月29日 10:25

**背景**: DeepSeek V4 是一个拥有 1.6 万亿参数的混合专家（MoE）模型，采用结合压缩稀疏注意力（CSA）和重度压缩注意力（HCA）的混合注意力架构，以实现长上下文效率。闪存注意力是一种内存高效的算法，可减少注意力计算时间和内存使用。llama.cpp 中的图重用避免了为每个新 token 重建计算图，从而提高了推理速度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/towardsdev/cracking-the-million-token-barrier-a-deep-dive-into-deepseek-v4s-architecture-3a11c6a87b40">Cracking the Million-Token Barrier: A Deep Dive into DeepSeek-V4’s Architecture | by ArXiv In-depth Analysis | Apr, 2026 | Towards Dev</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro">deepseek-ai/DeepSeek-V4-Pro · Hugging Face</a></li>
<li><a href="https://bentoml.com/llm/kernel-optimization/flashattention">FlashAttention | LLM Inference Handbook</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#DeepSeek V4`, `#LLM inference`, `#open-source`, `#machine learning`

---

<a id="item-3"></a>
## [火箭实验室历史性收购铱星公司](https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-acquire-iridium-historic-deal-creating-fully) ⭐️ 8.0/10

火箭实验室宣布收购铱星通信公司，获得其卫星星座和频谱资产，成为一家完全整合的太空公司。 这笔交易使火箭实验室通过同时拥有发射和卫星服务来与 SpaceX 的 Starlink 竞争，可能重塑卫星通信市场。 收购包括铱星公司的 66 颗在轨低轨卫星及其 L 波段频谱，为火箭实验室提供了运营中的星座和来自卫星服务的稳定收入流。

hackernews · everfrustrated · 6月29日 14:09 · [社区讨论](https://news.ycombinator.com/item?id=48719485)

**背景**: 火箭实验室于 2006 年在新西兰成立，是一家提供发射服务和卫星制造的端到端太空公司。铱星公司运营着一个全球低轨卫星星座，用于语音和数据通信，主要用于卫星电话和物联网设备。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Iridium_satellite_constellation">Iridium satellite constellation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rocket_Lab">Rocket Lab - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出了与 SpaceX 的 Starlink 模式的相似之处，一些人表达了对太空垃圾和太空商业化的担忧。其他人则认为此次收购是确保发射需求和扩展卫星服务的明智战略举措。

**标签**: `#space`, `#acquisition`, `#satellite`, `#Rocket Lab`, `#Iridium`

---

<a id="item-4"></a>
## [Ornith-1.0：面向智能体编程的开源大模型系列](https://simonwillison.net/2026/Jun/29/ornith/#atom-everything) ⭐️ 8.0/10

此次发布显著推动了开源智能体编程 AI 的发展，为专有模型提供了一个强大且许可宽松的替代方案，有望加速自主编程智能体的开发，并使最先进的编程大模型更加普及。 该模型系列包括 9B Dense、31B Dense、35B MoE 和 397B MoE 四种变体，均采用 MIT 许可证。早期用户报告显示，其在智能体编程任务中表现强劲，例如导航代码库和执行多步工具调用，在消费级硬件上推理速度可达 103 tokens/秒。

rss · Simon Willison · 6月29日 16:17

**背景**: 智能体编程（Agentic coding）是指 AI 系统自主执行多步软件开发任务，如代码生成、调试和工具使用。Ornith-1.0 基于 Apache 2.0 许可证的预训练模型（Gemma 4 和 Qwen 3.5）构建，确保了兼容性。该模型采用自脚手架（self-scaffolding）方法，即大模型自身管理其推理和工具使用循环，而非依赖外部编排代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agentic_coding">Agentic coding</a></li>

</ul>
</details>

**标签**: `#LLM`, `#open-source`, `#coding`, `#AI`, `#agentic`

---

<a id="item-5"></a>
## [ChatGPT 推翻 Erdős 猜想，颠覆陈立杰七年研究](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&mid=2652709773&idx=2&sn=68bde762eb0070f5bd61518728971232) ⭐️ 8.0/10

据报道，OpenAI 的 ChatGPT 解决了一个与 Erdős 猜想相关的长期未解计算几何问题，而著名理论家陈立杰曾为此研究了七年。 这标志着 AI 驱动数学的一个里程碑，表明大型语言模型能够解决挑战人类专家的深层理论问题，可能加速理论计算机科学的发现。 该问题涉及离散几何中的单位距离猜想，由 Erdős 在 80 多年前提出。OpenAI 的模型不仅推翻了该猜想，还提供了一个构造性反例。

rss · 新智元 · 6月29日 05:01

**背景**: 计算几何中的 Erdős 猜想关注平面上 n 个点之间给定距离出现的最大次数。陈立杰是清华姚班的杰出理论家，现任加州大学伯克利分校教授，曾在相关问题上取得重要进展。单位距离问题是离散几何中的一个经典开放问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/model-disproves-discrete-geometry-conjecture/">An OpenAI model has disproved a central conjecture in... | OpenAI</a></li>

</ul>
</details>

**标签**: `#AI`, `#computational geometry`, `#ChatGPT`, `#theoretical computer science`, `#Erdős conjecture`

---

<a id="item-6"></a>
## [Jon Udell：将“人在回路中”重构为“智能体在回路中”](https://simonwillison.net/2026/Jun/28/jon-udell/#atom-everything) ⭐️ 7.0/10

Jon Udell 提议将“人在回路中”重构为“智能体在回路中”，主张人类应保持控制权，并邀请 AI 智能体加入现有工作流程，而非被机器支配。 这一观点将叙事从 AI 取代人类转向 AI 增强人类能动性，可能影响软件开发团队设计智能体辅助流程并保持人类监督的方式。 Udell 特别警告智能体创建“不可审查的 PR”——因规模过大或不透明而无法适当审查的拉取请求——并倡导透明、协作的智能体工作流程。

rss · Simon Willison · 6月28日 21:57

**背景**: “人在回路中”（HITL）概念传统上将人类作为 AI 决策的必要检查点，但批评者认为这可能将人类降级为被动验证者。Udell 的“智能体在回路中”翻转了这一关系：人类拥有流程，智能体是受邀参与者。不可审查的 PR 是软件开发中的已知痛点，大型或不透明的代码变更会绕过有意义的审查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vaiotltd.medium.com/human-in-the-loop-vs-human-on-the-loop-880e4538ca65">Human in the Loop vs Human on the Loop | by VAIOT_LTD | Medium</a></li>
<li><a href="https://www.auxiliobits.com/blog/how-to-choose-between-autonomous-and-human-in-the-loop-agents/">Choosing Autonomous vs Human-in-the-Loop Agents</a></li>
<li><a href="https://medium.com/@thepassionatecoder/is-this-pull-request-reviewable-e4a7e1bbff31">Is This Pull Request Reviewable?. Intended Audience: software developers… | by The Passionate Coder | Medium</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#software development`, `#human-AI collaboration`, `#coding agents`

---

<a id="item-7"></a>
## [Hack Your Summer：面向学生的免费四周冲刺项目](https://simonwillison.net/2026/Jun/28/hack-your-summer/#atom-everything) ⭐️ 7.0/10

Hack Your Summer 是一个免费的四周生产冲刺项目，面向受实习短缺影响的本科生和研究生，第二期将于 7 月 13 日开始，申请截止日期为 7 月 8 日。 该计划为未能获得稀缺实习机会的学生提供了替代途径，帮助他们构建真实项目并获得指导，从而提升职业前景。 该计划免费，为期 4 周，专注于高速生产冲刺，学生将构建有形的、面向公众的作品。同时接受志愿者导师。

rss · Simon Willison · 6月28日 19:26

**背景**: “生产冲刺”是敏捷项目管理中的一个时间盒周期，通常为 2-4 周，团队在此期间努力产出可交付的产品增量。前美国首席数据科学家 DJ Patil 帮助推广了这一计划。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Scrum_(software_development)">Scrum (project management) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/DJ_Patil">DJ Patil</a></li>

</ul>
</details>

**标签**: `#education`, `#internship`, `#career development`, `#student programs`

---

<a id="item-8"></a>
## [OpenAI 绘制 AI 对欧盟就业影响图谱](https://openai.com/index/mapping-ai-jobs-transition-eu) ⭐️ 6.0/10

OpenAI 发布了一份报告，分析 AI 如何自动化、增强或改变欧盟各职业，提供了潜在就业变化的详细图谱。 该报告为政策制定者和企业提供了数据驱动的视角，以预测 AI 驱动的劳动力市场变化，可能指导欧洲的再培训和经济战略。 该报告将职业分为可能面临自动化的、可能增长的以及工作流程将发生变化的类别，但未说明具体百分比或使用的模型。

rss · OpenAI Blog · 6月29日 07:00

**背景**: 像大语言模型这样的 AI 技术越来越能够执行传统上由人类完成的任务。了解哪些工作最易受影响有助于政府和工人为转型做好准备。

**标签**: `#AI`, `#labor market`, `#Europe`, `#automation`, `#policy`

---