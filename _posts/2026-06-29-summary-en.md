---
layout: default
title: "Horizon Summary: 2026-06-29 (EN)"
date: 2026-06-29
lang: en
---

> From 88 items, 8 important content pieces were selected

---

1. [Google's AI Peer-Reviewer Processes ~10K Papers at Top Conferences](#item-1) ⭐️ 9.0/10
2. [llama.cpp b9840 Adds DeepSeek V4 Support](#item-2) ⭐️ 8.0/10
3. [Rocket Lab Acquires Iridium in Historic Deal](#item-3) ⭐️ 8.0/10
4. [Ornith-1.0: Open-Source LLM Family for Agentic Coding](#item-4) ⭐️ 8.0/10
5. [ChatGPT Disproves Erdős Conjecture, Overturns Chen Lijie's 7-Year Work](#item-5) ⭐️ 8.0/10
6. [Jon Udell: Reframe 'Human in the Loop' as 'Agent in the Loop'](#item-6) ⭐️ 7.0/10
7. [Hack Your Summer: Free 4-Week Sprint for Students](#item-7) ⭐️ 7.0/10
8. [OpenAI Maps AI's Impact on EU Jobs](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Google's AI Peer-Reviewer Processes ~10K Papers at Top Conferences](https://www.reddit.com/r/MachineLearning/comments/1uio9rb/googles_agentic_peerreviewer_handled_10k_papers/) ⭐️ 9.0/10

Google deployed an agentic AI peer-reviewer at ICML and STOC that processed approximately 10,000 papers with a 30-minute turnaround, and the formal research paper shows it catches 34% more mathematical errors than zero-shot prompting. This sets a precedent for AI-automated scientific review at conference scale, potentially transforming the peer-review process by reducing reviewer burden and improving error detection. The system is an agentic AI that mimics aspects of the conference peer-review process, producing structured critiques covering methodology, contribution, clarity, and related work.

reddit · r/MachineLearning · /u/Justgototheeffinmoon · Jun 29, 10:05

**Background**: Zero-shot prompting is a technique where an AI model performs a task without any prior examples, relying solely on its pre-trained knowledge. The agentic reviewer goes beyond this by using multiple reasoning steps and tool use to produce more thorough reviews.

<details><summary>References</summary>
<ul>
<li><a href="https://paperreview.ai/tech-overview">Tech Overview - Stanford Agentic Reviewer - paperreview.ai</a></li>
<li><a href="https://rcgsheffield.github.io/research-ai-landscape/tools/stanford-agentic-reviewer">stanford-agentic-reviewer</a></li>
<li><a href="https://phrasly.ai/blog/zero-shot-prompting/">Zero - Shot Prompting : Definition, Examples & How It Works</a></li>

</ul>
</details>

**Tags**: `#AI`, `#peer review`, `#machine learning`, `#automation`, `#research`

---

<a id="item-2"></a>
## [llama.cpp b9840 Adds DeepSeek V4 Support](https://github.com/ggml-org/llama.cpp/releases/tag/b9840) ⭐️ 8.0/10

llama.cpp release b9840 introduces support for DeepSeek V4, including model conversion, inference, and optimizations such as flash attention and graph reuse. This release enables efficient local inference of DeepSeek V4, a state-of-the-art 1.6 trillion parameter MoE model with million-token context windows, on consumer hardware via llama.cpp. The release includes conversion scripts for DeepSeek V4, flash attention for faster attention computation, and graph reuse to reduce overhead during token generation. It also supports multi-sequence inference and partial checkpointing.

github · github-actions[bot] · Jun 29, 10:25

**Background**: DeepSeek V4 is a Mixture-of-Experts (MoE) model with 1.6 trillion parameters, featuring a hybrid attention architecture combining Compressed Sparse Attention (CSA) and Heavily Compressed Attention (HCA) for long-context efficiency. Flash attention is a memory-efficient algorithm that reduces attention computation time and memory usage. Graph reuse in llama.cpp avoids rebuilding the computational graph for each new token, improving inference speed.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/towardsdev/cracking-the-million-token-barrier-a-deep-dive-into-deepseek-v4s-architecture-3a11c6a87b40">Cracking the Million-Token Barrier: A Deep Dive into DeepSeek-V4’s Architecture | by ArXiv In-depth Analysis | Apr, 2026 | Towards Dev</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro">deepseek-ai/DeepSeek-V4-Pro · Hugging Face</a></li>
<li><a href="https://bentoml.com/llm/kernel-optimization/flashattention">FlashAttention | LLM Inference Handbook</a></li>

</ul>
</details>

**Tags**: `#llama.cpp`, `#DeepSeek V4`, `#LLM inference`, `#open-source`, `#machine learning`

---

<a id="item-3"></a>
## [Rocket Lab Acquires Iridium in Historic Deal](https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-acquire-iridium-historic-deal-creating-fully) ⭐️ 8.0/10

Rocket Lab has announced the acquisition of Iridium Communications, gaining its satellite constellation and spectrum assets to become a fully integrated space company. This deal positions Rocket Lab to compete with SpaceX's Starlink by owning both launch and satellite services, potentially reshaping the satellite communications market. The acquisition includes Iridium's 66 active LEO satellites and its L-band spectrum, providing Rocket Lab with an operational constellation and a steady revenue stream from satellite services.

hackernews · everfrustrated · Jun 29, 14:09 · [Discussion](https://news.ycombinator.com/item?id=48719485)

**Background**: Rocket Lab, founded in New Zealand in 2006, is an end-to-end space company offering launch services and satellite manufacturing. Iridium operates a global LEO satellite constellation for voice and data communications, primarily used for satellite phones and IoT devices.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Iridium_satellite_constellation">Iridium satellite constellation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rocket_Lab">Rocket Lab - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community comments highlight parallels to SpaceX's Starlink model, with some expressing concerns about space debris and the commercialization of space. Others see the acquisition as a smart strategic move to secure launch demand and expand into satellite services.

**Tags**: `#space`, `#acquisition`, `#satellite`, `#Rocket Lab`, `#Iridium`

---

<a id="item-4"></a>
## [Ornith-1.0: Open-Source LLM Family for Agentic Coding](https://simonwillison.net/2026/Jun/29/ornith/#atom-everything) ⭐️ 8.0/10

DeepReinforce released Ornith-1.0, a new open-weight LLM family under MIT license, with variants from 9B to 397B parameters, built on Gemma 4 and Qwen 3.5, achieving state-of-the-art coding performance among open-source models. This release significantly advances open-source agentic coding AI, offering a powerful, permissively licensed alternative to proprietary models, which could accelerate development of autonomous coding agents and democratize access to state-of-the-art coding LLMs. The model family includes 9B Dense, 31B Dense, 35B MoE, and 397B MoE variants, all MIT licensed. Early user reports indicate strong performance in agentic coding tasks, such as navigating codebases and executing multi-step tool calls, with inference speeds up to 103 tokens/second on consumer hardware.

rss · Simon Willison · Jun 29, 16:17

**Background**: Agentic coding refers to AI systems that autonomously perform multi-step software development tasks, such as code generation, debugging, and tool use. Ornith-1.0 is built on top of pretrained models (Gemma 4 and Qwen 3.5) that are Apache 2.0 licensed, ensuring compatibility. The model uses a self-scaffolding approach, where the LLM itself manages its own reasoning and tool-use loops, rather than relying on external orchestration code.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agentic_coding">Agentic coding</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#open-source`, `#coding`, `#AI`, `#agentic`

---

<a id="item-5"></a>
## [ChatGPT Disproves Erdős Conjecture, Overturns Chen Lijie's 7-Year Work](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&mid=2652709773&idx=2&sn=68bde762eb0070f5bd61518728971232) ⭐️ 8.0/10

OpenAI's ChatGPT reportedly solved a long-standing computational geometry problem related to the Erdős conjecture, which renowned theorist Chen Lijie had worked on for seven years. This marks a milestone in AI-driven mathematics, demonstrating that large language models can tackle deep theoretical problems that challenge human experts, potentially accelerating discovery in theoretical computer science. The problem involves the unit distance conjecture in discrete geometry, which Erdős posed over 80 years ago. OpenAI's model not only disproved the conjecture but also provided a constructive counterexample.

rss · 新智元 · Jun 29, 05:01

**Background**: The Erdős conjecture in computational geometry concerns the maximum number of times a given distance can occur among n points in the plane. Chen Lijie, a prominent theorist from Tsinghua's Yao Class and now a professor at UC Berkeley, had made significant progress on related problems. The unit distance problem is a classic open problem in discrete geometry.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/model-disproves-discrete-geometry-conjecture/">An OpenAI model has disproved a central conjecture in... | OpenAI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#computational geometry`, `#ChatGPT`, `#theoretical computer science`, `#Erdős conjecture`

---

<a id="item-6"></a>
## [Jon Udell: Reframe 'Human in the Loop' as 'Agent in the Loop'](https://simonwillison.net/2026/Jun/28/jon-udell/#atom-everything) ⭐️ 7.0/10

Jon Udell proposes reframing 'human in the loop' as 'agent in the loop,' arguing that humans should remain in control and invite AI agents into their existing workflows rather than being subordinated to machines. This perspective shifts the narrative from AI replacing humans to AI augmenting human agency, which could influence how software development teams design agent-assisted processes and maintain human oversight. Udell specifically warns against agents creating 'unreviewable PRs'—pull requests that cannot be properly reviewed due to size or opacity—and advocates for transparent, collaborative agent workflows.

rss · Simon Willison · Jun 28, 21:57

**Background**: The 'human in the loop' (HITL) concept traditionally places a human as a necessary checkpoint in AI decision-making, but critics argue it can reduce humans to passive validators. Udell's 'agent in the loop' flips this: humans own the process and agents are invited participants. Unreviewable PRs are a known pain point in software development, where large or opaque code changes bypass meaningful review.

<details><summary>References</summary>
<ul>
<li><a href="https://vaiotltd.medium.com/human-in-the-loop-vs-human-on-the-loop-880e4538ca65">Human in the Loop vs Human on the Loop | by VAIOT_LTD | Medium</a></li>
<li><a href="https://www.auxiliobits.com/blog/how-to-choose-between-autonomous-and-human-in-the-loop-agents/">Choosing Autonomous vs Human-in-the-Loop Agents</a></li>
<li><a href="https://medium.com/@thepassionatecoder/is-this-pull-request-reviewable-e4a7e1bbff31">Is This Pull Request Reviewable?. Intended Audience: software developers… | by The Passionate Coder | Medium</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#software development`, `#human-AI collaboration`, `#coding agents`

---

<a id="item-7"></a>
## [Hack Your Summer: Free 4-Week Sprint for Students](https://simonwillison.net/2026/Jun/28/hack-your-summer/#atom-everything) ⭐️ 7.0/10

Hack Your Summer, a free 4-week production sprint for undergraduate and graduate students affected by the internship shortage, is launching a second cohort starting July 13th, with applications due July 8th. This initiative provides an alternative path for students who missed out on scarce internships, helping them build real projects and gain mentorship to improve their career prospects. The program is free, runs for 4 weeks, and focuses on high-velocity production sprints where students build tangible, public-facing work. It also accepts volunteer mentors.

rss · Simon Willison · Jun 28, 19:26

**Background**: A 'production sprint' is a time-boxed period used in agile project management, typically 2-4 weeks, where a team works to produce a potentially shippable product increment. DJ Patil, a former U.S. Chief Data Scientist, helped promote this initiative.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Scrum_(software_development)">Scrum (project management) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/DJ_Patil">DJ Patil</a></li>

</ul>
</details>

**Tags**: `#education`, `#internship`, `#career development`, `#student programs`

---

<a id="item-8"></a>
## [OpenAI Maps AI's Impact on EU Jobs](https://openai.com/index/mapping-ai-jobs-transition-eu) ⭐️ 6.0/10

OpenAI released a report analyzing how AI could automate, augment, or transform occupations across the European Union, providing a detailed mapping of potential job shifts. This report offers a data-driven perspective for policymakers and businesses to anticipate AI-driven labor market changes, potentially guiding reskilling and economic strategies across Europe. The report categorizes occupations into those likely to face automation, those that may grow, and those that will see workflow changes, without specifying exact percentages or models used.

rss · OpenAI Blog · Jun 29, 07:00

**Background**: AI technologies like large language models are increasingly capable of performing tasks traditionally done by humans. Understanding which jobs are most exposed helps governments and workers prepare for transitions.

**Tags**: `#AI`, `#labor market`, `#Europe`, `#automation`, `#policy`

---