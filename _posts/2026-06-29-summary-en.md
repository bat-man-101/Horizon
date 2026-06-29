---
layout: default
title: "Horizon Summary: 2026-06-29 (EN)"
date: 2026-06-29
lang: en
---

> From 88 items, 8 important content pieces were selected

---

1. [Supreme Court: Geofence Warrants Need Constitutional Protections](#item-1) ⭐️ 9.0/10
2. [Google's AI Peer-Reviewer Processes ~10K Papers, Cuts Errors 34%](#item-2) ⭐️ 9.0/10
3. [llama.cpp b9840 Adds DeepSeek V4 Support](#item-3) ⭐️ 8.0/10
4. [Ornith-1.0: Open-Source Self-Scaffolding LLMs for Coding](#item-4) ⭐️ 8.0/10
5. [ChatGPT Overturns Chen Lijie's 7-Year Computational Geometry Problem](#item-5) ⭐️ 8.0/10
6. [Jon Udell: Invite Agents Into the Loop, Don't Be Excluded](#item-6) ⭐️ 7.0/10
7. [Hack Your Summer: Free 4-Week Sprint for Students](#item-7) ⭐️ 6.0/10
8. [OpenAI Maps AI Job Shifts Across EU](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Supreme Court: Geofence Warrants Need Constitutional Protections](https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision) ⭐️ 9.0/10

The US Supreme Court ruled 6-3 that geofence warrants require constitutional protections under the Fourth Amendment, limiting warrantless access to smartphone location data. The decision, written by Justice Elena Kagan, held that users do not forfeit privacy expectations by opting into Google's location history. This landmark ruling significantly curtails law enforcement's ability to use geofence warrants as a dragnet surveillance tool, strengthening digital privacy rights for millions of smartphone users. It sets a precedent that the Fourth Amendment applies to modern location-tracking technologies, impacting future investigations and tech company data-sharing practices. The case, Chatrie v. United States, involved a bank robbery suspect identified through a geofence warrant that obtained location data from Google's Sensorvault. The court distinguished this from the 2018 Carpenter decision, which required a warrant for cell-site location information, by explicitly applying the same protection to geofence warrants.

hackernews · cdrnsf · Jun 29, 15:54 · [Discussion](https://news.ycombinator.com/item?id=48720924)

**Background**: A geofence warrant is a search warrant that compels a company like Google to identify all devices within a specific geographic area during a certain time period. These warrants have been used by law enforcement to identify unknown suspects by sweeping up location data from many innocent bystanders. The Fourth Amendment protects against unreasonable searches and seizures, and the Supreme Court has previously ruled that long-term location tracking requires a warrant.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision">US supreme court rules geofence warrants require constitutional privacy protections | US supreme court | The Guardian</a></li>

</ul>
</details>

**Discussion**: Commenters expressed strong support for the ruling, with some noting historical examples of location tracking without phones (e.g., the Petraeus affair). Others criticized dissenting justices Alito and Thomas for supporting unlimited government power, while a few questioned practical implications, such as whether police now need probable cause for a specific suspect before obtaining a warrant.

**Tags**: `#privacy`, `#supreme court`, `#geofence warrants`, `#law enforcement`, `#constitutional law`

---

<a id="item-2"></a>
## [Google's AI Peer-Reviewer Processes ~10K Papers, Cuts Errors 34%](https://www.reddit.com/r/MachineLearning/comments/1uio9rb/googles_agentic_peerreviewer_handled_10k_papers/) ⭐️ 9.0/10

Google deployed an agentic AI peer-reviewer at top CS conferences ICML and STOC, reviewing approximately 10,000 papers with a 30-minute turnaround, and a formal research paper shows it catches 34% more mathematical errors than zero-shot prompting. This sets a precedent for AI-automated scientific review at conference scale, potentially accelerating peer review and reducing human reviewer burden, while improving error detection in mathematical content. The agentic AI reviewer achieved a 30-minute turnaround per paper, compared to months for human review, and its formal paper is now available on arXiv (2606.28277). The system uses an agentic workflow rather than simple zero-shot prompting.

reddit · r/MachineLearning · /u/Justgototheeffinmoon · Jun 29, 10:05

**Background**: Peer review is a process where experts evaluate research papers before publication to ensure quality and correctness. Zero-shot prompting is a technique where an AI model performs a task without any examples, while agentic AI systems use multi-step reasoning and tool use to achieve better results.

**Tags**: `#AI`, `#peer review`, `#machine learning`, `#Google`, `#automation`

---

<a id="item-3"></a>
## [llama.cpp b9840 Adds DeepSeek V4 Support](https://github.com/ggml-org/llama.cpp/releases/tag/b9840) ⭐️ 8.0/10

llama.cpp release b9840 adds support for the DeepSeek V4 model architecture, including conversion, inference, and optimizations. The release also enables flash attention, graph reuse, and multi-sequence inference. This release enables local, efficient inference of DeepSeek V4, a state-of-the-art Mixture-of-Experts model with up to 1.6 trillion parameters, on consumer hardware. It significantly expands the capabilities of the open-source LLM ecosystem. DeepSeek V4 models use a hybrid attention architecture combining Compressed Sparse Attention (CSA) and Heavily Compressed Attention (HCA). The release includes support for both DeepSeek-V4-Pro (1.6T total, 49B activated) and DeepSeek-V4-Flash (284B total, 13B activated) variants.

github · github-actions[bot] · Jun 29, 10:25

**Background**: llama.cpp is an open-source C/C++ library for running large language models locally on CPUs and GPUs. It uses the GGUF format to store quantized models, enabling efficient inference on consumer hardware. DeepSeek V4 is a recent Mixture-of-Experts model series from DeepSeek, featuring a novel hybrid attention mechanism for long-context processing.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro">deepseek-ai/DeepSeek-V4-Pro · Hugging Face</a></li>
<li><a href="https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond">The Complete Guide to DeepSeek Models: V3, R1, V4 and Beyond</a></li>

</ul>
</details>

**Tags**: `#llama.cpp`, `#DeepSeek V4`, `#LLM inference`, `#open-source`, `#machine learning`

---

<a id="item-4"></a>
## [Ornith-1.0: Open-Source Self-Scaffolding LLMs for Coding](https://simonwillison.net/2026/Jun/29/ornith/#atom-everything) ⭐️ 8.0/10

DeepReinforce released Ornith-1.0, a family of open-weight LLMs (9B to 397B) under the MIT license, achieving state-of-the-art coding benchmark performance via a self-scaffolding training framework. This release brings competitive coding performance to the open-source community with a permissive license, enabling broader access and customization for agentic coding tasks. The model variants include 9B Dense, 31B Dense, 35B MoE, and 397B MoE, built on top of Gemma 4 and Qwen 3.5, both Apache 2.0 licensed. The self-scaffolding approach jointly optimizes solution generation and task-specific harnesses during reinforcement learning.

rss · Simon Willison · Jun 29, 16:17

**Background**: Agentic coding refers to AI agents performing multi-step software development tasks autonomously. Traditional LLM-based coding agents use fixed scaffolds (harnesses) to guide the model, but Ornith-1.0 learns to generate its own scaffolds, improving performance over time.

<details><summary>References</summary>
<ul>
<li><a href="https://deep-reinforce.com/ornith_1_0.html">Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding | DeepReinforce Blog | Jun. 2026</a></li>
<li><a href="https://essamamdani.com/blog/ornith-1-0-self-scaffolding-llm-coding-2026">Ornith-1.0: The Self-Scaffolding LLM That Teaches Itself to Code Better | Essa Mamdani | Essa Mamdani</a></li>
<li><a href="https://ornith.site/">Ornith 1 . 0 — Open-Source Agentic Coding Models</a></li>

</ul>
</details>

**Discussion**: Initial community feedback is positive, with users reporting good performance in LM Studio and Pi integration. Some discussion focuses on licensing compatibility with the underlying Apache 2.0 models.

**Tags**: `#LLM`, `#open-source`, `#coding`, `#AI`, `#machine learning`

---

<a id="item-5"></a>
## [ChatGPT Overturns Chen Lijie's 7-Year Computational Geometry Problem](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&mid=2652709773&idx=2&sn=68bde762eb0070f5bd61518728971232) ⭐️ 8.0/10

ChatGPT reportedly solved a core computational geometry problem that had stumped renowned researcher Chen Lijie for seven years, building on OpenAI's recent resolution of an Erdős conjecture. This demonstrates that large language models can now tackle long-standing open problems in theoretical computer science, potentially accelerating research in computational geometry and related fields. The problem is a core question in computational geometry that Chen Lijie had worked on for seven years without success. The solution leverages the recently proven Erdős conjecture by OpenAI.

rss · 新智元 · Jun 29, 05:01

**Background**: Computational geometry deals with algorithms for geometric problems, often involving points, lines, and shapes. Chen Lijie, a renowned computer scientist from the prestigious Yao Class at Tsinghua University, is known for his work in computational complexity. The Erdős conjecture, recently solved by OpenAI, is a famous problem in arithmetic combinatorics about arithmetic progressions.

**Tags**: `#AI`, `#computational geometry`, `#ChatGPT`, `#breakthrough`, `#OpenAI`

---

<a id="item-6"></a>
## [Jon Udell: Invite Agents Into the Loop, Don't Be Excluded](https://simonwillison.net/2026/Jun/28/jon-udell/#atom-everything) ⭐️ 7.0/10

Jon Udell argues that instead of being a 'human in the loop' ceding authority to machines, software teams should invite AI agents into their existing workflows as team members, keeping humans in control and ensuring all agent contributions are reviewable. This reframing shifts the narrative from human subordination to human agency in agentic software development, addressing concerns about unreviewable PRs and black-box processes. It promotes a collaborative model where AI augments rather than replaces human judgment. Udell specifically criticizes the phrase 'human in the loop' for ceding authority to machines, and advocates for 'agent in the loop' where agents are invited into the team's existing loop. He emphasizes that agent-assisted processes should not be black boxes that take prompts and emit features without review.

rss · Simon Willison · Jun 28, 21:57

**Background**: Agentic software development uses AI agents to autonomously perform tasks like coding, testing, and deployment. The traditional 'human-in-the-loop' model places a human as a supervisor or fallback, but Udell argues this still centers the machine. His alternative 'invite agents into the loop' keeps the human as the primary decision-maker, with agents as collaborators whose work is always reviewable.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Human-in-the-loop">Human - in - the - loop - Wikipedia</a></li>
<li><a href="https://www.ness.com/blog/what-is-agentic-software-development/">Agentic Software Development : Beyond Metrics and Speed</a></li>

</ul>
</details>

**Tags**: `#agentic development`, `#human-in-the-loop`, `#software engineering`, `#AI`

---

<a id="item-7"></a>
## [Hack Your Summer: Free 4-Week Sprint for Students](https://simonwillison.net/2026/Jun/28/hack-your-summer/#atom-everything) ⭐️ 6.0/10

Hack Your Summer is a free 4-week production sprint for undergraduate and graduate students to build real projects, launched as an alternative to scarce internships. A second cohort starts July 13, with applications due by July 8. This initiative addresses the internship shortage affecting US college students, offering a structured way to gain practical experience and build portfolio-worthy work. It could help bridge the gap between academic learning and industry expectations. The program is free and open to undergraduate students, graduate students, and recent graduates. It includes mentorship from volunteers and focuses on creating tangible, public-facing work that can be shown to future employers.

rss · Simon Willison · Jun 28, 19:26

**Background**: Many US companies have reduced hiring and intern coaching capacity, leading to fewer internship opportunities for students. Hack Your Summer provides an alternative by simulating a real-world production environment with mentor support.

**Tags**: `#education`, `#internship`, `#student-projects`, `#summer-program`

---

<a id="item-8"></a>
## [OpenAI Maps AI Job Shifts Across EU](https://openai.com/index/mapping-ai-jobs-transition-eu) ⭐️ 6.0/10

OpenAI released a report mapping how AI could reshape occupations across the EU, identifying jobs at risk of automation, those poised for growth, and roles likely to see workflow changes. This report provides a data-driven overview of AI's potential impact on the European labor market, helping policymakers, businesses, and workers anticipate and prepare for workforce transitions. The report covers a wide range of EU occupations and categorizes them by exposure to AI-driven changes, but lacks specific technical details or granular data on individual job roles.

rss · OpenAI Blog · Jun 29, 07:00

**Background**: AI technologies like large language models are increasingly capable of automating cognitive tasks, raising concerns about job displacement. This report aims to quantify which sectors and roles in the EU are most vulnerable or likely to benefit.

**Tags**: `#AI`, `#labor market`, `#Europe`, `#automation`, `#OpenAI`

---