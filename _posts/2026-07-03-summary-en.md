---
layout: default
title: "Horizon Summary: 2026-07-03 (EN)"
date: 2026-07-03
lang: en
---

> From 170 items, 12 important content pieces were selected

---

**📌 Other（3）**
  1. [U.S. Bans Differential Privacy in Census Data](#item-1) ⭐️ 9.0/10
  2. [Virginia Bans Sale of Precise Geolocation Data](#item-2) ⭐️ 8.0/10
  3. [crustc: Entire rustc Compiler Translated to C](#item-3) ⭐️ 8.0/10

**🤖 AI News（3）**
  4. [Understand to Participate: Key to AI Coding Collaboration](#item-4) ⭐️ 8.0/10
  5. [Simon Willison Releases llm-coding-agent 0.1a0 Alpha](#item-5) ⭐️ 7.0/10
  6. [Using DSPy to Optimize Datasette Agent SQL Prompts](#item-6) ⭐️ 7.0/10

**🔬 Semiconductors（1）**
  7. [ECTC 2026 Roundup: EMIB-T, Custom HBM, HBM4, Microfluidic Cooling, Photonic Interconnects](#item-7) ⭐️ 8.0/10

**₿ Crypto（1）**
  8. [OpenAI reportedly offers US government 5% stake](#item-8) ⭐️ 8.0/10

**🚀 Tech Trends（3）**
  9. [US government hacked again: DHS network breach](#item-9) ⭐️ 8.0/10
  10. [Microsoft Launches AI Deployment Company with $2.5B](#item-10) ⭐️ 8.0/10
  11. [Private Space Pilots Fly Orbital Missions for US Space Force](#item-11) ⭐️ 7.0/10

**📰 Top News（1）**
  12. [China Now Has Half of World's Wind and Solar Capacity](#item-12) ⭐️ 6.0/10
---

## 📌 Other

<a id="item-1"></a>
## [U.S. Bans Differential Privacy in Census Data](https://scottaaronson.blog/?p=9902) ⭐️ 9.0/10

On June 4, 2026, the U.S. Secretary of Commerce issued Directive DAO 216-26, which bans differential privacy and noise infusion in all Census Bureau statistical products, restricting disclosure avoidance to coarsening only. This directive threatens the reliability of public statistics and individual privacy protections, potentially undermining data-driven decisions for infrastructure, funding allocation, and research. The directive explicitly forbids noise infusion, defined as methods that modify data by adding random values, and restricts disclosure avoidance to coarsening, which aggregates data into broader categories.

hackernews · flowercalled · Jul 3, 00:01 · [Discussion](https://news.ycombinator.com/item?id=48768992)

**Background**: Differential privacy is a mathematical framework that adds calibrated noise to data to protect individual privacy while allowing accurate statistical analysis. The U.S. Census Bureau adopted differential privacy for the 2020 Census to enhance privacy protections. Noise infusion has been a common disclosure avoidance technique for decades.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Differential_privacy">Differential privacy - Wikipedia</a></li>
<li><a href="https://epic.org/issues/democracy-free-speech/census-privacy/">Census Privacy – EPIC – Electronic Privacy Information Center</a></li>
<li><a href="https://desfontain.es/blog/banning-noise.html">Banning noise will be a disaster for statistical data products - Ted is writing things</a></li>

</ul>
</details>

**Discussion**: Commenters expressed alarm, with some calling the directive a disaster for statistical data products. There was confusion about the political motivation, and a call to action to contact legislators was shared, along with a link to find representatives.

**Tags**: `#privacy`, `#differential privacy`, `#census`, `#government policy`, `#data integrity`

---

<a id="item-2"></a>
## [Virginia Bans Sale of Precise Geolocation Data](https://www.hunton.com/privacy-and-cybersecurity-law-blog/virginia-bans-sale-of-geolocation-data) ⭐️ 8.0/10

Virginia has enacted a law banning the sale of precise geolocation data, defined as data that can locate an individual within 1,750 feet, effective July 1. This regulation significantly impacts data brokers and tech companies that rely on location data for advertising and analytics, setting a precedent for state-level privacy protections. The ban applies to precise geolocation data with a threshold of 1,750 feet, meaning data that identifies location within that radius cannot be sold. The law went into effect on July 1, 2025.

hackernews · toomuchtodo · Jul 2, 21:03 · [Discussion](https://news.ycombinator.com/item?id=48767347)

**Background**: Precise geolocation data refers to information that identifies the physical location of an individual or device with high accuracy, often within a radius of 1,000 to 1,750 feet. Such data is commonly collected by mobile apps and sold to data brokers for targeted advertising. Virginia's law is part of a growing trend of state-level privacy regulations in the U.S., following similar actions by California.

<details><summary>References</summary>
<ul>
<li><a href="https://www.law.cornell.edu/cfr/text/28/202.242">28 CFR § 202.242 - Precise geolocation data. | Electronic Code of Federal Regulations (e-CFR) | US Law | LII / Legal Information Institute</a></li>
<li><a href="https://www.lawinsider.com/dictionary/precise-geolocation">Precise geolocation Definition | Law Insider</a></li>

</ul>
</details>

**Discussion**: Commenters noted that the ban only applies to precise data, allowing sale of fuzzy geolocation data. Some questioned enforcement against out-of-state companies, while others praised the law but called for stronger enforcement.

**Tags**: `#privacy`, `#geolocation`, `#regulation`, `#data protection`

---

<a id="item-3"></a>
## [crustc: Entire rustc Compiler Translated to C](https://github.com/FractalFir/crustc) ⭐️ 8.0/10

A project called crustc has successfully translated the entire Rust compiler (rustc) into C code, enabling bootstrapping on platforms without LLVM or GCC support. This achievement could significantly improve Rust's portability to obscure or legacy hardware, and also opens up possibilities for verifying the Rust compiler's integrity through diverse double-compiling (DDC) techniques. The project is the 14th known attempt to compile Rust to C, and it aims to support platforms that lack LLVM or GCC backends. The translated C code can be compiled by any standard C compiler, such as GCC.

hackernews · Philpax · Jul 2, 22:57 · [Discussion](https://news.ycombinator.com/item?id=48768464)

**Background**: Bootstrapping a compiler typically requires an existing compiler for the same language. For Rust, building rustc from source currently requires a working Rust compiler, which creates a chicken-and-egg problem for new platforms. Translating rustc to C breaks this dependency, as C compilers are available on almost every platform.

<details><summary>References</summary>
<ul>
<li><a href="https://dev.to/tamizuddin/decoding-crustc-translating-the-rust-compiler-to-c-and-its-impact-on-systems-programming-3djc">Decoding ` crustc `: Translating the Rust Compiler to... - DEV Community</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bootstrapping_(compilers)">Bootstrapping (compilers) - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The community expressed admiration for the project's dedication and technical merit. Some commenters discussed using crustc for diverse double-compiling (DDC) to check for backdoors in the official rustc, while others compared it to LLVM's C backend, noting that crustc takes a different approach by transpiling the entire compiler.

**Tags**: `#rust`, `#compilers`, `#bootstrapping`, `#transpilation`, `#systems-programming`

---

## 🤖 AI News

<a id="item-4"></a>
## [Understand to Participate: Key to AI Coding Collaboration](https://simonwillison.net/2026/Jul/2/understand-to-participate/#atom-everything) ⭐️ 8.0/10

Simon Willison highlights Geoffrey Litt's concept of 'understand to participate' for collaborating with coding agents without accumulating cognitive debt. This concept addresses a critical challenge in AI-assisted coding: maintaining human understanding to avoid cognitive debt, which can hinder long-term productivity and code quality. Geoffrey Litt presented this idea at the AIE conference, arguing that developers must understand code deeply enough to actively participate with AI agents, rather than passively accepting changes.

rss · Simon Willison · Jul 2, 17:07

**Background**: Cognitive debt refers to the erosion of shared understanding in a software project, making it harder for developers to reason about and safely modify code. As AI coding agents generate larger changes, developers risk losing comprehension, accumulating cognitive debt. The 'understand to participate' principle emphasizes maintaining fluency to remain an effective collaborator.

<details><summary>References</summary>
<ul>
<li><a href="https://margaretstorey.com/blog/2026/02/09/cognitive-debt/">How Generative and Agentic AI Shift Concern from Technical Debt to Cognitive Debt</a></li>
<li><a href="https://arxiv.org/abs/2603.22106">[2603.22106] From Technical Debt to Cognitive and Intent Debt: Rethinking Software Health in the Age of AI</a></li>
<li><a href="https://getdx.com/blog/cognitive-debt-the-hidden-risk-in-ai-driven-software-development/">Cognitive debt: The hidden risk in AI-driven software development</a></li>

</ul>
</details>

**Tags**: `#AI-assisted coding`, `#cognitive debt`, `#software engineering`, `#human-AI collaboration`

---

<a id="item-5"></a>
## [Simon Willison Releases llm-coding-agent 0.1a0 Alpha](https://simonwillison.net/2026/Jul/2/llm-coding-agent/#atom-everything) ⭐️ 7.0/10

Simon Willison released an early alpha (0.1a0) of llm-coding-agent, a coding agent built on his LLM library and inspired by Claude Code. The agent provides tools for reading, editing files, and executing commands, and can be run via 'uvx --prerelease=allow --with llm-coding-agent llm code'. This release marks a significant step in evolving the LLM library into an agent framework, enabling developers to experiment with AI-assisted coding workflows. It lowers the barrier for building custom coding agents by providing a simple Python API and CLI. The agent includes tools like edit_file, execute_command, list_files, read_file, and search_files, with safety features such as timeout and approval mode. The spec and code were largely generated by Claude Code itself, demonstrating a self-referential development process.

rss · Simon Willison · Jul 2, 19:33

**Background**: Simon Willison's LLM library is a Python tool for interacting with large language models, which has recently evolved into an agent framework. Claude Code is an AI coding agent by Anthropic that can read codebases, edit files, and run commands. This release is an experiment to see what a simple coding agent built on the LLM library looks like.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jul/2/llm-coding-agent/">Release: llm -coding- agent 0.1a0 | Simon Willison ’s Weblog</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent , Terminal, IDE</a></li>

</ul>
</details>

**Tags**: `#coding agent`, `#LLM`, `#Python`, `#agent framework`, `#Simon Willison`

---

<a id="item-6"></a>
## [Using DSPy to Optimize Datasette Agent SQL Prompts](https://simonwillison.net/2026/Jul/2/dspy-datasette-agent-prompts/#atom-everything) ⭐️ 7.0/10

Simon Willison used the DSPy framework to automatically evaluate and improve the SQL system prompts of Datasette Agent, identifying specific optimization directions such as including column names in schema listings. This demonstrates a practical workflow for automatically optimizing LLM system prompts, which can reduce manual trial-and-error and improve the reliability of AI agents that generate SQL queries. The experiment used GPT-4.1 mini and nano models via Claude Fable 5, and found that the baseline prompt's advice to avoid calling describe_table caused column-name guessing and error-retry loops.

rss · Simon Willison · Jul 2, 18:25

**Background**: DSPy (Declarative Self-improving Python) is a framework for building AI systems by composing modular programs instead of writing brittle prompts. Datasette Agent is an AI assistant that answers user questions by executing read-only SQL queries against Datasette databases.

<details><summary>References</summary>
<ul>
<li><a href="https://dspy.ai/">DSPy</a></li>
<li><a href="https://github.com/stanfordnlp/dspy">GitHub - stanfordnlp/ dspy : DSPy : The framework for...</a></li>
<li><a href="https://agent.datasette.io/">Datasette Agent : an AI assistant for Datasette to help explore and...</a></li>

</ul>
</details>

**Tags**: `#DSPy`, `#prompt engineering`, `#LLM`, `#Datasette`, `#SQL`

---

## 🔬 Semiconductors

<a id="item-7"></a>
## [ECTC 2026 Roundup: EMIB-T, Custom HBM, HBM4, Microfluidic Cooling, Photonic Interconnects](https://newsletter.semianalysis.com/p/ectc2026) ⭐️ 8.0/10

At ECTC 2026, Intel, TSMC, SK Hynix, Samsung, Micron, Marvell, Lightmatter, and Microsoft presented breakthroughs in semiconductor packaging, including Intel's EMIB-T technology for HBM4, custom HBM solutions, microfluidic cooling, and photonic interconnects. These advancements address critical challenges in high-performance computing and AI hardware, such as power delivery, thermal management, and bandwidth scaling, enabling next-generation accelerators and memory systems. Intel's EMIB-T adds through-silicon vias (TSVs) to the embedded bridge, enabling higher power delivery and larger packages for HBM4. Microfluidic cooling circulates coolant through microscopic channels on chips, while photonic interconnects use light for faster, lower-power data transfer.

rss · Semianalysis · Jul 2, 17:25

**Background**: Advanced packaging technologies like EMIB (Embedded Multi-die Interconnect Bridge) and CoWoS (Chip-on-Wafer-on-Substrate) are critical for integrating chiplets and high-bandwidth memory (HBM) in AI accelerators. HBM4 is the next generation of HBM, offering higher bandwidth and capacity, but poses significant packaging challenges due to increased power and thermal density. Microfluidic cooling and photonic interconnects are emerging solutions to overcome thermal and bandwidth bottlenecks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/cpus/intel-details-new-advanced-packaging-breakthroughs-emib-t-paves-the-way-for-hbm4-and-increased-ucie-bandwidth">Intel details new advanced packaging breakthroughs — EMIB-T paves the way for HBM4 and increased UCIe bandwidth | Tom's Hardware</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/semiconductors/intels-emib-t-heads-for-fab-rollout-this-year">Intel's EMIB-T packaging technology set for fab rollout this year — as TSMC CoWoS capacity remains limited, EMIB-T is preparing for advanced AI accelerator designs | Tom's Hardware</a></li>
<li><a href="https://www.synopsys.com/blogs/chip-design/accelerating-emib-t-packaging-synopsys-intel-foundry.html">Accelerating EMIB-T Packaging Innovation with Intel Foundry | Synopsys</a></li>

</ul>
</details>

**Tags**: `#semiconductor packaging`, `#HBM`, `#photonic interconnects`, `#advanced cooling`, `#ECTC`

---

## ₿ Crypto

<a id="item-8"></a>
## [OpenAI reportedly offers US government 5% stake](https://www.coindesk.com/policy/2026/07/02/openai-reported-to-discuss-offering-u-s-government-a-5-stake) ⭐️ 8.0/10

OpenAI has reportedly discussed offering the U.S. government a 5% equity stake during early Trump administration talks, as part of a proposal to create a sovereign wealth fund that would allow the public to share in AI gains. This development could reshape AI governance by intertwining national security interests with corporate ownership, potentially setting a precedent for how strategic AI companies are regulated and owned. The proposal involves giving equity to a U.S. sovereign wealth fund, not directly to the government, and comes amid heightened scrutiny of AI model oversight by Washington.

rss · CoinDesk · Jul 2, 10:06

**Background**: A sovereign wealth fund is a state-owned investment fund that invests in assets like stocks, bonds, and real estate. OpenAI's current structure includes a nonprofit parent that holds equity, and the company has been transitioning toward a for-profit model. The reported 5% stake would be a significant ownership share in one of the most valuable AI companies.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sovereign_wealth_fund">Sovereign wealth fund</a></li>
<li><a href="https://openai.com/our-structure/">Our structure | OpenAI</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#AI governance`, `#national security`, `#policy`

---

## 🚀 Tech Trends

<a id="item-9"></a>
## [US government hacked again: DHS network breach](https://techcrunch.com/2026/07/02/us-government-says-it-got-hacked-again/) ⭐️ 8.0/10

A top Democrat on the Senate Intelligence Committee warned that a hack of the Homeland Security Information Network (HSIN) may risk national security. This breach of a critical intelligence-sharing network used by government and private sector partners could expose sensitive information and undermine national security. The Homeland Security Information Network is used to share sensitive but unclassified information among government, international, and private sector partners.

rss · 36氪 - 科技 · Jul 2, 14:22

**Background**: The Homeland Security Information Network (HSIN) is a platform for sharing sensitive but unclassified information among federal, state, local, tribal, territorial, international, and private sector partners. It is managed by the Department of Homeland Security (DHS). Previous breaches of government networks have raised concerns about cybersecurity vulnerabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nextgov.com/cybersecurity/2026/06/hackers-breached-dhs-information-sharing-network-people-familiar-say/414534/">Hackers breached DHS information- sharing network ... - Nextgov/FCW</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#government`, `#national security`, `#data breach`

---

<a id="item-10"></a>
## [Microsoft Launches AI Deployment Company with $2.5B](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/) ⭐️ 8.0/10

Microsoft has announced the launch of its own AI deployment company, committing $2.5 billion to the initiative, following similar moves by Amazon, OpenAI, and Anthropic. This significant investment signals Microsoft's strategic push to control AI infrastructure and deployment, intensifying competition among tech giants in the rapidly growing AI market. The announcement lacks specific details about the company's structure or services, but it aligns with industry trends where major players are vertically integrating AI deployment capabilities.

rss · 36氪 - 科技 · Jul 2, 13:53

**Background**: AI deployment companies focus on helping businesses integrate and run AI models in production environments. Microsoft's move follows Amazon's AWS AI services, OpenAI's platform, and Anthropic's deployment partnerships, reflecting a race to dominate the AI value chain.

**Tags**: `#Microsoft`, `#AI`, `#investment`, `#deployment`, `#industry`

---

<a id="item-11"></a>
## [Private Space Pilots Fly Orbital Missions for US Space Force](https://techcrunch.com/2026/07/02/private-space-pilots-are-flying-orbital-missions-for-the-us-space-force/) ⭐️ 7.0/10

Private companies True Anomaly and Rocket Lab are conducting orbital satellite maneuvers for the US Space Force, performing rapid fly-bys and proximity operations similar to aerial dogfights. This marks a paradigm shift in space logistics and defense, demonstrating that private companies can now execute complex military orbital maneuvers, potentially reducing costs and increasing responsiveness for space superiority. Rocket Lab's satellite Puma was fully activated and ready for its first orbital maneuver around True Anomaly's Jackal within 37 hours and 36 minutes of launch, showcasing rapid readiness.

rss · 36氪 - 科技 · Jul 2, 23:01

**Background**: True Anomaly, founded in 2022 by ex-US Space Force members, focuses exclusively on space defense. Rocket Lab's Electron rocket provides dedicated launch services. The Victus Haze mission demonstrates rapid satellite maneuverability for military purposes.

<details><summary>References</summary>
<ul>
<li><a href="https://www.airandspaceforces.com/victus-haze-mission-rapid-maneuvers-satellites/">Satellites Maneuver on Rapid Timelines for Victus Haze Mission</a></li>
<li><a href="https://www.trueanomaly.space/?ref=whatocome.xyz">True Anomaly - Delivering Decisive Capabilities for Space Superiority.</a></li>

</ul>
</details>

**Tags**: `#space`, `#military`, `#private aerospace`, `#satellite operations`

---

## 📰 Top News

<a id="item-12"></a>
## [China Now Has Half of World's Wind and Solar Capacity](https://news.google.com/rss/articles/CBMimwFBVV95cUxQc016a3huazZtWkIxN0ZrRlVKRjEyNjNscVluREtRQUdWYU1kRGtfNkNSZy1MOVRMRHdXeDBtRWg5dXdqX1ZybkY5YWVPd01TVWdXQTFmMS1TX3VkUFZlNU9lMmpxS1RMTWdsMFUxUEJoWjM4ODYwZVhScy1UUnRNbXdoMUhGQk5ESUlCeDJYbXh4cEFUa285TVRuc9IBoAFBVV95cUxPQ3VnMTZPTG5tX1lzWjlPY1hubVFLV0hGUDNnc1F6eGw4bnB3SUhjRVdTRzB6Zl9tWFU3VGtWZE9FeWZ1aHppRXpTWWNKc1ZtcUlIR0tXaUQ3UFBodWRMSmlTTWJwMWV3LTh0SEhjaXQ4U2FFcGpOdUp2YTYtNE15SHZqX1Z1cGtsOEwyNE5xSko1R0NBOWdtRWNEcHl4Tkxj?oc=5) ⭐️ 6.0/10

According to Statista, China now accounts for half of the world's installed wind and solar capacity, a milestone in renewable energy deployment. This dominance underscores China's critical role in global renewable energy expansion and its potential to influence climate change mitigation efforts worldwide. The statistic includes both onshore and offshore wind, as well as utility-scale and distributed solar photovoltaic installations, as of the latest available data.

google_news · Statista · Jul 2, 13:27

**Background**: Wind and solar power are key renewable energy sources that help reduce greenhouse gas emissions. China has aggressively invested in these technologies over the past decade, becoming the world's largest producer of solar panels and wind turbines.

**Tags**: `#renewable energy`, `#China`, `#wind power`, `#solar power`, `#statistics`

---