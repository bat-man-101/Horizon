---
layout: default
title: "Horizon Summary: 2026-06-29 (EN)"
date: 2026-06-29
lang: en
---

> From 88 items, 8 important content pieces were selected

---

1. [Supreme Court rules geofence warrants need warrants](#item-1) ⭐️ 9.0/10
2. [Google's AI Peer-Reviewer Handles ~10K Papers, Catches 34% More Errors](#item-2) ⭐️ 9.0/10
3. [llama.cpp b9840 Adds DeepSeek V4 Support](#item-3) ⭐️ 8.0/10
4. [Ornith-1.0: Open-Weight LLM for Agentic Coding](#item-4) ⭐️ 8.0/10
5. [Jon Udell: Flip 'Human in the Loop' to 'Agent in the Loop'](#item-5) ⭐️ 8.0/10
6. [ChatGPT Disproves Chen Lijie's 7-Year Conjecture](#item-6) ⭐️ 8.0/10
7. [OpenAI Report Maps AI Impact on EU Jobs](#item-7) ⭐️ 7.0/10
8. [Hack Your Summer: Free Sprint for Students](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Supreme Court rules geofence warrants need warrants](https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision) ⭐️ 9.0/10

The US Supreme Court ruled that geofence warrants require constitutional protections under the Fourth Amendment, limiting warrantless access to location data. The decision was issued on June 29, 2026. This landmark ruling significantly impacts privacy rights and law enforcement practices by requiring probable cause for broad location data searches. It sets a precedent for digital privacy in the era of mass surveillance. The case involved Google providing location data from devices near a bank robbery, with information shared in three tranches. The Court held that geofence warrants are general warrants prohibited by the Fourth Amendment.

hackernews · cdrnsf · Jun 29, 15:54 · [Discussion](https://news.ycombinator.com/item?id=48720924)

**Background**: A geofence warrant is a search warrant that allows law enforcement to obtain location data of all mobile devices within a specific geographic area during a certain time period. The Fourth Amendment protects against unreasonable searches and seizures, and geofence warrants have been controversial as digital analogs to general warrants.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Geofence_warrant">Geofence warrant - Wikipedia</a></li>
<li><a href="https://www.congress.gov/crs-product/LSB11274">Geofence Warrants and the Fourth Amendment | Congress.gov | Library of Congress</a></li>
<li><a href="https://harvardlawreview.org/blog/2025/02/much-ado-about-geofence-warrants/">Much Ado About Geofence Warrants - Harvard Law Review</a></li>

</ul>
</details>

**Discussion**: Commenters noted historical examples like the Paula Broadwell case to illustrate alternative identification methods. Some expressed surprise that Justice Barrett joined the minority, while others asked about practical implications, such as whether police now need probable cause for a specific suspect before obtaining location data.

**Tags**: `#privacy`, `#supreme court`, `#geofence warrants`, `#law enforcement`, `#constitutional law`

---

<a id="item-2"></a>
## [Google's AI Peer-Reviewer Handles ~10K Papers, Catches 34% More Errors](https://www.reddit.com/r/MachineLearning/comments/1uio9rb/googles_agentic_peerreviewer_handled_10k_papers/) ⭐️ 9.0/10

Google deployed an agentic AI peer-reviewer at ICML and STOC, processing approximately 10,000 papers with a 30-minute turnaround, and a formal paper reports it catches 34% more mathematical errors than zero-shot prompting. This sets a precedent for AI-assisted scientific review at conference scale, potentially accelerating the peer-review process and improving error detection in mathematical content, which could transform how top CS conferences handle submissions. The system uses an agentic workflow that goes beyond simple zero-shot prompting, enabling iterative reasoning and verification. The 34% improvement in error detection is specifically for mathematical errors, and the system achieved a 30-minute average review time per paper.

reddit · r/MachineLearning · /u/Justgototheeffinmoon · Jun 29, 10:05

**Background**: Peer review is a critical but time-consuming process in academic publishing, often taking months. Zero-shot prompting asks an AI to perform a task without any examples, which is less effective for complex tasks like mathematical verification. Agentic AI systems use multi-step reasoning and tool use to improve accuracy.

<details><summary>References</summary>
<ul>
<li><a href="https://paperreview.ai/tech-overview">Tech Overview - Stanford Agentic Reviewer</a></li>
<li><a href="https://medium.com/data-science-in-your-pocket/andrew-ngs-agentic-reviewer-ai-for-research-paper-reviews-1c2d9cda8086">Andrew NG’s Agentic Reviewer : AI for Research Paper Reviews | by Mehul Gupta | Data Science in Your Pocket | Medium</a></li>

</ul>
</details>

**Discussion**: Reddit comments generally praised the speed and scale, with some noting that even imperfect AI review can accelerate research by providing rapid feedback. Others raised concerns about over-reliance on AI and potential biases, but overall sentiment was positive about the formal documentation of results.

**Tags**: `#AI`, `#peer review`, `#machine learning`, `#conference`, `#automation`

---

<a id="item-3"></a>
## [llama.cpp b9840 Adds DeepSeek V4 Support](https://github.com/ggml-org/llama.cpp/releases/tag/b9840) ⭐️ 8.0/10

llama.cpp release b9840 adds support for the DeepSeek V4 model architecture, including both Pro and Flash variants, with optimizations such as flash attention, graph reuse, and padding for efficient inference. This release enables local inference of DeepSeek V4, a state-of-the-art Mixture-of-Experts model with up to 1.6 trillion parameters, on consumer hardware via CPU and GPU backends, democratizing access to cutting-edge LLM technology. The release includes contributions from multiple developers, featuring Sinkhorn algorithm adjustments, KV-cache reservation, and support for multi-sequence inference. The DeepSeek V4 model uses a hybrid attention mechanism combining Compressed Sparse Attention and Heavily Compressed Attention.

github · github-actions[bot] · Jun 29, 10:25

**Background**: llama.cpp is an open-source C++ library for efficient LLM inference on CPUs and GPUs, using the GGUF format for model storage. DeepSeek V4 is a Mixture-of-Experts model series with up to 1.6 trillion total parameters, featuring a hybrid attention architecture for long-context processing up to one million tokens.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro">deepseek-ai/DeepSeek-V4-Pro · Hugging Face</a></li>
<li><a href="https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond">The Complete Guide to DeepSeek Models: V3, R1, V4 and Beyond</a></li>

</ul>
</details>

**Tags**: `#llama.cpp`, `#DeepSeek V4`, `#LLM inference`, `#open source`

---

<a id="item-4"></a>
## [Ornith-1.0: Open-Weight LLM for Agentic Coding](https://simonwillison.net/2026/Jun/29/ornith/#atom-everything) ⭐️ 8.0/10

DeepReinforce released Ornith-1.0, a family of open-weight LLMs (MIT license) for agentic coding, available in 9B, 31B, 35B MoE, and 397B MoE variants, built on Gemma 4 and Qwen 3.5. It achieves state-of-the-art performance among open-source models of comparable size on coding benchmarks. This release advances open-source agentic coding by providing a permissively licensed, high-performing model that can autonomously plan, write, test, and modify code. It lowers barriers for developers and researchers to build autonomous coding agents without relying on proprietary models. The model uses a self-scaffolding technique where the LLM generates explicit step-by-step decompositions to handle complex coding tasks. Early tests show it can proficiently run an agent harness over many tool calls, and the 35B GGUF quantized version runs locally at 103 tokens/second.

rss · Simon Willison · Jun 29, 16:17

**Background**: Agentic coding refers to AI-assisted software development where autonomous AI agents plan, write, test, and modify code with minimal human intervention. Self-scaffolding is a technique that exploits LLMs' ability to articulate memorized algorithmic procedures by having them generate explicit step-by-step decompositions. Mixture of Experts (MoE) models use multiple smaller expert networks activated per input, enabling efficient scaling.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=48709744">Ornith-1.0: Self - Scaffolding LLMs for Agentic Coding | Hacker News</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agentic_coding">Agentic coding</a></li>
<li><a href="https://cloud.google.com/discover/what-is-agentic-coding">What is agentic coding? How it works and use cases | Google Cloud</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#coding`, `#open-source`, `#agentic`, `#model release`

---

<a id="item-5"></a>
## [Jon Udell: Flip 'Human in the Loop' to 'Agent in the Loop'](https://simonwillison.net/2026/Jun/28/jon-udell/#atom-everything) ⭐️ 8.0/10

Jon Udell proposes reframing the dominant narrative from 'human in the loop' to 'agent in the loop,' arguing that humans should retain agency and invite AI agents as team members rather than being excluded from the loop. This reframing shifts the power dynamic in AI-assisted software development, emphasizing human oversight and collaboration over black-box automation, which could lead to more trustworthy and reviewable agent-generated code. Udell's argument is part of a blog post titled 'Doctor, it hurts when agents create unreviewable PRs. Don't do that,' which warns against large, opaque pull requests from AI agents and advocates for small, reviewable diffs.

rss · Simon Willison · Jun 28, 21:57

**Background**: The term 'human in the loop' (HITL) traditionally describes systems where a human must approve or intervene in AI actions. Udell's 'agent in the loop' flips this, positioning humans as the primary decision-makers who recruit AI agents as collaborators. This aligns with best practices in agentic software development, such as keeping diffs small and requiring human review.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.jonudell.net/2026/06/28/doctor-it-hurts-when-agents-create-unreviewable-prs-dont-do-that/">“Doctor, it hurts when agents create unreviewable PRs .” “Don’t do that.”</a></li>
<li><a href="https://timdeschryver.dev/blog/keep-agentic-ai-simple-a-practical-workflow-for-software-development">Keep Agentic AI Simple: A Practical Workflow for Software Development</a></li>
<li><a href="https://cloud.google.com/discover/what-is-agentic-coding">What is agentic coding? How it works and use cases | Google Cloud</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#software development`, `#human-AI collaboration`, `#agentic development`

---

<a id="item-6"></a>
## [ChatGPT Disproves Chen Lijie's 7-Year Conjecture](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&mid=2652709773&idx=2&sn=68bde762eb0070f5bd61518728971232) ⭐️ 8.0/10

ChatGPT, building on OpenAI's solution to the Erdős conjecture, has reportedly disproved a core computational geometry conjecture that Chen Lijie had worked on for seven years. This demonstrates AI's growing capability to tackle long-standing mathematical problems, potentially accelerating research in computational geometry and related fields. The disproof leverages OpenAI's recent solution to the Erdős conjecture, though specific details of the computational geometry conjecture and the disproof method are not yet publicly available.

rss · 新智元 · Jun 29, 05:01

**Background**: Chen Lijie is a renowned Chinese computer scientist known for his work in computational complexity and geometry. The Erdős conjecture is a famous unsolved problem in number theory. OpenAI recently announced a solution to the Erdős conjecture, which provided a foundation for this new result.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Erdős_conjecture">Erdős conjecture</a></li>
<li><a href="https://chen-lijie.github.io/">Lijie Chen</a></li>

</ul>
</details>

**Tags**: `#AI`, `#computational geometry`, `#ChatGPT`, `#OpenAI`, `#research breakthrough`

---

<a id="item-7"></a>
## [OpenAI Report Maps AI Impact on EU Jobs](https://openai.com/index/mapping-ai-jobs-transition-eu) ⭐️ 7.0/10

OpenAI released a report analyzing how AI could automate, augment, or transform occupations across the European Union, providing data-driven insights into workforce transitions. This report offers valuable guidance for policymakers and businesses in the EU to prepare for AI-driven labor market changes, potentially influencing workforce planning and retraining initiatives. The report maps which occupations are most exposed to automation, which may see growth, and which will undergo workflow changes, though specific numbers or models are not detailed in the summary.

rss · OpenAI Blog · Jun 29, 07:00

**Background**: AI technologies like large language models are increasingly capable of performing tasks traditionally done by humans, raising questions about job displacement and skill shifts. The EU has been proactive in AI regulation, making such reports timely for policy discussions.

**Tags**: `#AI`, `#labor market`, `#EU`, `#automation`, `#policy`

---

<a id="item-8"></a>
## [Hack Your Summer: Free Sprint for Students](https://simonwillison.net/2026/Jun/28/hack-your-summer/#atom-everything) ⭐️ 6.0/10

Hack Your Summer, a free 4-week production sprint for students affected by the internship shortage, has opened applications for its second cohort starting July 13, 2026, with a deadline of July 8. This initiative provides an alternative pathway for students who missed out on scarce internships, helping them build real projects and professional networks during a tough job market. The program is currently limited to U.S.-based students due to time zone coordination, but organizers hope to expand internationally in the future. It also seeks volunteer mentors.

rss · Simon Willison · Jun 28, 19:26

**Background**: A production sprint is a short, time-boxed period (typically 1-4 weeks) during which a team works intensively to produce a tangible outcome, inspired by agile software development sprints. The internship crisis refers to a severe shortage of internship positions relative to the number of students seeking them, exacerbated by reduced corporate hiring in 2025-2026.

<details><summary>References</summary>
<ul>
<li><a href="https://www.hackyoursummer.org/">Hack Your Summer</a></li>
<li><a href="https://www.hackyoursummer.org/details">Details — Hack Your Summer</a></li>
<li><a href="https://www.cnn.com/2026/04/06/business/job-market-internships-squeeze">The job market is so tough, young people are struggling just to land internships | CNN Business</a></li>

</ul>
</details>

**Tags**: `#education`, `#internships`, `#student-programs`, `#summer-sprint`

---