---
layout: default
title: "Horizon Summary: 2026-06-29 (EN)"
date: 2026-06-29
lang: en
---

> From 89 items, 8 important content pieces were selected

---

1. [Supreme Court Rules Geofence Warrants Need Constitutional Protections](#item-1) ⭐️ 9.0/10
2. [ChatGPT Overturns 7-Year Work on Erdős Conjecture](#item-2) ⭐️ 9.0/10
3. [Google's AI Peer-Reviewer Handles 10K Papers, Catches 34% More Errors](#item-3) ⭐️ 9.0/10
4. [llama.cpp b9840 Adds DeepSeek V4 Support](#item-4) ⭐️ 8.0/10
5. [Ornith-1.0: Open-Weight LLM for Agentic Coding](#item-5) ⭐️ 8.0/10
6. [Jon Udell: Flip 'Human in the Loop' to 'Agent in the Loop'](#item-6) ⭐️ 8.0/10
7. [Hack Your Summer: Free 4-Week Student Project Sprint](#item-7) ⭐️ 6.0/10
8. [OpenAI Maps AI Job Shifts Across EU](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Supreme Court Rules Geofence Warrants Need Constitutional Protections](https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision) ⭐️ 9.0/10

The US Supreme Court ruled that geofence warrants, which allow law enforcement to obtain location data of all devices within a specific area, require constitutional protections under the Fourth Amendment, limiting warrantless access to such data. This landmark decision significantly strengthens digital privacy rights by requiring probable cause and a warrant for bulk location data, affecting how law enforcement investigates crimes and setting a precedent for future digital surveillance cases. The case originated from a bank robbery where Google provided location data of 19 devices near the crime scene; the Court ruled that such broad data collection violates the Fourth Amendment's protection against unreasonable searches.

hackernews · cdrnsf · Jun 29, 15:54 · [Discussion](https://news.ycombinator.com/item?id=48720924)

**Background**: A geofence warrant, also known as a reverse location warrant, allows law enforcement to search a database like Google's Sensorvault for all devices within a defined geographic area during a specific time. The Fourth Amendment protects against unreasonable searches and seizures, but its application to digital location data has been debated, especially after the 2018 Carpenter v. United States decision.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Geofence_warrant">Geofence warrant</a></li>

</ul>
</details>

**Discussion**: Commenters noted historical examples of location tracking without phones, such as the Paula Broadwell case, and discussed the practical implications, with some surprised that Justice Barrett joined the minority. The full decision PDF was shared for further reading.

**Tags**: `#privacy`, `#supreme court`, `#fourth amendment`, `#digital rights`, `#law enforcement`

---

<a id="item-2"></a>
## [ChatGPT Overturns 7-Year Work on Erdős Conjecture](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&mid=2652709773&idx=2&sn=68bde762eb0070f5bd61518728971232) ⭐️ 9.0/10

ChatGPT reportedly disproved a core computational geometry conjecture related to the Erdős unit distance problem, overturning seven years of work by renowned Chinese computer scientist Chen Lijie. The achievement builds on OpenAI's earlier announcement of solving the Erdős conjecture last month. This marks a milestone in AI-driven mathematics, demonstrating that large language models can not only assist but also independently disprove long-standing conjectures. It challenges the traditional role of human mathematicians and could accelerate discovery in theoretical computer science. The specific conjecture involved the Erdős unit distance problem, which asks for the maximum number of unit distances among n points in the plane. OpenAI's model reportedly produced a counterexample that invalidated a previously assumed structure, though full details have not been released.

rss · 新智元 · Jun 29, 05:01

**Background**: The Erdős unit distance problem, posed by Paul Erdős in 1946, asks for the maximum number of pairs of points at unit distance among n points in the plane. It is a central problem in discrete geometry with implications for graph theory and combinatorial geometry. Chen Lijie, a Turing Award winner and pioneer in computational geometry, had worked on a related conjecture for seven years. OpenAI recently announced that its model solved the original Erdős conjecture, and this new result extends that breakthrough.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/model-disproves-discrete-geometry-conjecture/">An OpenAI model has disproved a central conjecture in... | OpenAI</a></li>
<li><a href="https://scitechdaily.com/for-the-first-time-chatgpt-has-solved-an-unproven-math-problem-in-geometry/">For the First Time, ChatGPT Has Solved an Unproven Math Problem in Geometry</a></li>

</ul>
</details>

**Tags**: `#AI`, `#computational geometry`, `#ChatGPT`, `#Erdős conjecture`, `#theoretical computer science`

---

<a id="item-3"></a>
## [Google's AI Peer-Reviewer Handles 10K Papers, Catches 34% More Errors](https://www.reddit.com/r/MachineLearning/comments/1uio9rb/googles_agentic_peerreviewer_handled_10k_papers/) ⭐️ 9.0/10

Google deployed an agentic AI peer-reviewer at top CS conferences ICML and STOC, processing approximately 10,000 papers with a 30-minute turnaround, and the formal research paper shows it catches 34% more mathematical errors than zero-shot prompting. This sets a precedent for AI-automated scientific review at conference scale, potentially accelerating the peer-review process and reducing reviewer burden while improving error detection in mathematical content. The agentic system uses a multi-step reasoning approach rather than simple zero-shot prompting, enabling it to catch subtle mathematical errors. The formal paper is available on arXiv (2606.28277).

reddit · r/MachineLearning · /u/Justgototheeffinmoon · Jun 29, 10:05

**Background**: Peer review is a cornerstone of scientific publishing but is often slow and overburdened. Zero-shot prompting asks an AI to perform a task without examples, while agentic systems use iterative reasoning and tool use to improve accuracy. Google's work builds on earlier agentic reviewer projects like Stanford's PaperReview.ai.

**Discussion**: The Reddit community expressed excitement about the scale and formal documentation, with some discussing the potential for AI to reduce review times from months to minutes. Others raised concerns about fairness and the risk of AI missing nuanced errors that human reviewers would catch.

**Tags**: `#AI`, `#peer review`, `#machine learning`, `#Google`, `#scientific publishing`

---

<a id="item-4"></a>
## [llama.cpp b9840 Adds DeepSeek V4 Support](https://github.com/ggml-org/llama.cpp/releases/tag/b9840) ⭐️ 8.0/10

llama.cpp release b9840 introduces support for the DeepSeek V4 model architecture, including conversion, inference, and chat template integration, with contributions from multiple developers. This update enables local, efficient inference of DeepSeek V4, a 1-trillion-parameter MoE model, on consumer hardware, significantly expanding the capabilities of the open-source LLM ecosystem. The release includes support for DeepSeek V4 Pro, flash attention, graph reuse, and multi-sequence inference, while also fixing bugs and cleaning up code. The DeepSeek V4 model uses an efficient MoE architecture with up to 1M-token context windows.

github · github-actions[bot] · Jun 29, 10:25

**Background**: llama.cpp is an open-source C/C++ project for running large language models locally on CPUs and GPUs. It uses the GGUF format for efficient model storage and loading. DeepSeek V4 is a 1-trillion-parameter mixture-of-experts model developed by DeepSeek, designed for high-performance coding and reasoning tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://deepseek.ai/deepseek-v4">DeepSeek V 4 (2026) — 1T Params, Benchmarks & Pricing</a></li>
<li><a href="https://en.wikipedia.org/wiki/GGUF">GGUF - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#llama.cpp`, `#DeepSeek V4`, `#machine learning`, `#open source`, `#release`

---

<a id="item-5"></a>
## [Ornith-1.0: Open-Weight LLM for Agentic Coding](https://simonwillison.net/2026/Jun/29/ornith/#atom-everything) ⭐️ 8.0/10

DeepReinforce released Ornith-1.0, a family of open-weight (MIT licensed) LLMs for agentic coding, with sizes from 9B to 397B MoE, built on Gemma 4 and Qwen 3.5. It achieves state-of-the-art performance among open-source models of comparable size on coding benchmarks. Ornith-1.0 brings competitive agentic coding capabilities to the open-source community, enabling developers to run powerful coding agents locally or in custom environments. Its self-scaffolding training approach could influence future LLM development for autonomous task solving. The model family includes 9B Dense, 31B Dense, 35B MoE, and 397B MoE variants, all MIT licensed. Early user reports indicate strong performance in multi-step tool calling tasks, with a 20GB GGUF quantized version running at 103 tokens/second.

rss · Simon Willison · Jun 29, 16:17

**Background**: Agentic coding refers to AI agents that autonomously perform multi-step software development tasks, such as code generation, debugging, and testing. Ornith-1.0 uses a self-scaffolding training framework that jointly learns to solve tasks and construct the scaffolds guiding those solutions, improving efficiency. The model leverages Mixture-of-Experts (MoE) architecture, which activates only relevant subnetworks per token, reducing computational cost.

<details><summary>References</summary>
<ul>
<li><a href="https://deep-reinforce.com/ornith_1_0.html">Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding</a></li>
<li><a href="https://simonwillison.net/2026/Jun/29/ornith/">Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agentic_coding">Agentic coding</a></li>

</ul>
</details>

**Discussion**: The community response is positive, with users praising the model's performance in agentic coding tasks and the permissive MIT license. Some users noted the lack of information about DeepReinforce, but the practical usage tips and benchmark results have generated interest.

**Tags**: `#LLM`, `#open-source`, `#coding`, `#AI agents`, `#machine learning`

---

<a id="item-6"></a>
## [Jon Udell: Flip 'Human in the Loop' to 'Agent in the Loop'](https://simonwillison.net/2026/Jun/28/jon-udell/#atom-everything) ⭐️ 8.0/10

Jon Udell proposes reframing the dominant 'human in the loop' narrative to 'agent in the loop,' arguing that humans should remain the authority who invites AI agents into their existing workflow rather than being inserted into an AI-driven loop. This reframing shifts the power dynamic in AI-assisted software development, emphasizing human control and agency over AI agents, which could lead to more transparent and reviewable development practices. Udell specifically warns against agents creating unreviewable pull requests, advocating for agent-assisted processes that are not black boxes but transparent collaborations where humans retain final authority.

rss · Simon Willison · Jun 28, 21:57

**Background**: The phrase 'human in the loop' (HITL) traditionally describes AI systems that require human approval for critical decisions. However, critics argue that HITL can still place humans in a reactive role, reviewing outputs without full context. Udell's 'agent in the loop' flips this by asserting that the human's workflow is primary, and AI agents are invited participants, not drivers.

<details><summary>References</summary>
<ul>
<li><a href="https://vaiotltd.medium.com/human-in-the-loop-vs-human-on-the-loop-880e4538ca65">Human in the Loop vs Human on the Loop | by VAIOT_LTD | Medium</a></li>
<li><a href="https://www.waxell.ai/blog/human-in-the-loop-vs-human-on-the-loop-ai-agents">Human-in-the-Loop vs Human-on-the-Loop for AI Agents</a></li>
<li><a href="https://grayphite.com/blogs/59/">Grayphite | Cutting-Edge Software, AI Solutions & Emerging Tech...</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#software development`, `#human-AI collaboration`, `#agentic development`

---

<a id="item-7"></a>
## [Hack Your Summer: Free 4-Week Student Project Sprint](https://simonwillison.net/2026/Jun/28/hack-your-summer/#atom-everything) ⭐️ 6.0/10

Hack Your Summer, a free 4-week production sprint for undergraduate and graduate students, has announced a second cohort starting July 13th, with applications due July 8th. The program helps students build real, public-facing projects as an alternative to scarce internships. This initiative addresses the severe internship shortage in the US, offering students a structured way to gain practical experience and build portfolio-worthy work. It provides a scalable, community-supported alternative that could reshape how students demonstrate skills to employers. The program is free and open to undergraduate students, graduate students, and recent graduates. It also seeks volunteer mentors to support participants during the sprint.

rss · Simon Willison · Jun 28, 19:26

**Background**: US college students face a severe internship crisis in 2026, with companies reducing hiring and coaching capacity. Hack Your Summer fills this gap by providing a structured, mentor-guided production sprint where students build real projects they can show employers.

**Tags**: `#education`, `#internship`, `#student-projects`, `#summer-program`

---

<a id="item-8"></a>
## [OpenAI Maps AI Job Shifts Across EU](https://openai.com/index/mapping-ai-jobs-transition-eu) ⭐️ 6.0/10

OpenAI released a report mapping how AI could reshape occupations across the European Union, identifying which jobs may face automation, growth, or workflow changes. This report provides a high-level overview that can inform policymakers, businesses, and workers about potential AI-driven labor market transitions in the EU. The report covers a broad range of EU occupations but lacks deep technical novelty or specific data on timelines and magnitude of changes.

rss · OpenAI Blog · Jun 29, 07:00

**Background**: AI is increasingly capable of automating routine tasks, which can lead to job displacement or augmentation. The EU has been proactive in regulating AI through frameworks like the AI Act, making such workforce analyses relevant for policy planning.

**Tags**: `#AI`, `#labor market`, `#automation`, `#EU`, `#workforce`

---