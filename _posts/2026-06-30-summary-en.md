---
layout: default
title: "Horizon Summary: 2026-06-30 (EN)"
date: 2026-06-30
lang: en
---

> From 151 items, 10 important content pieces were selected

---

1. [vLLM v0.24.0 Adds MiniMax-M3 and DeepSeek-V4 Optimizations](#item-1) ⭐️ 8.0/10
2. [OpenAI Fixes 18-Year-Old Bug via Core Dump Analysis](#item-2) ⭐️ 8.0/10
3. [Tesla Begins Testing Cybercab Without Steering Wheel in Austin](#item-3) ⭐️ 8.0/10
4. [Amazon launches $1B FDE org for AI agent deployment](#item-4) ⭐️ 8.0/10
5. [South Korea pledges $550B+ to ease memory chip shortage](#item-5) ⭐️ 8.0/10
6. [AI deciphers long-range DNA signals in RNA splicing](#item-6) ⭐️ 8.0/10
7. [New York Life's $800B Asset Manager Launches First Tokenized Fund](#item-7) ⭐️ 7.0/10
8. [MIT Q&A Explores Agentic AI Today and Future](#item-8) ⭐️ 7.0/10
9. [Chess grandmaster critiques AI visionaries' blind spots](#item-9) ⭐️ 7.0/10
10. [OpenAI Reports Global Growth in ChatGPT Adoption](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [vLLM v0.24.0 Adds MiniMax-M3 and DeepSeek-V4 Optimizations](https://github.com/vllm-project/vllm/releases/tag/v0.24.0) ⭐️ 8.0/10

vLLM v0.24.0 introduces support for the MiniMax-M3 model and delivers major performance optimizations for DeepSeek-V4, including a FlashInfer sparse index cache and a cluster-cooperative topK kernel. This release significantly boosts inference efficiency for two cutting-edge models, enabling faster and more cost-effective deployment of large language models in production environments. The FlashInfer sparse index cache reduces time-to-first-token (TTFT) by 2–4%, while the cluster-cooperative topK kernel lowers latency for DeepSeek-V4's sparse attention. The release also includes 571 commits from 256 contributors.

github · khluu · Jun 29, 19:41

**Background**: vLLM is a high-throughput, memory-efficient inference engine for large language models. DeepSeek-V4 and MiniMax-M3 are advanced models that require optimized kernels for efficient serving. FlashInfer is a kernel library providing high-performance attention implementations, and the cluster-cooperative topK kernel is a custom kernel for sparse attention index selection.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.flashinfer.ai/api/sparse.html">flashinfer.sparse - FlashInfer 0.6.13 documentation</a></li>
<li><a href="https://github.com/flashinfer-ai/flashinfer">GitHub - flashinfer-ai/flashinfer: FlashInfer: Kernel Library ... flashinfer_sparse - vLLM FlashInfer 0.2 - Efficient and Customizable Kernels for LLM ... FlashInfer: Efficient and Customizable Attention Engine for ... flashinfer/flashinfer/sparse.py at main · flashinfer-ai ... Dissecting FlashInfer - A Systems Perspective on High ...</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#DeepSeek`, `#MiniMax`, `#performance optimization`

---

<a id="item-2"></a>
## [OpenAI Fixes 18-Year-Old Bug via Core Dump Analysis](https://openai.com/index/core-dump-epidemiology-data-infrastructure-bug) ⭐️ 8.0/10

OpenAI engineers conducted large-scale core dump analysis to debug rare infrastructure crashes, uncovering both a hardware fault and an 18-year-old software bug. This demonstrates a novel, data-driven approach to debugging rare failures in large-scale systems, with implications for reliability engineering across the industry. The bug had persisted for 18 years, and the analysis required collecting and examining core dumps from thousands of machines to identify the root cause.

rss · OpenAI Blog · Jun 30, 00:00

**Background**: A core dump is a snapshot of a program's memory at the time of a crash, used for post-mortem debugging. Analyzing core dumps at scale involves aggregating and correlating data from many machines to find common patterns.

<details><summary>References</summary>
<ul>
<li><a href="https://stackoverflow.com/questions/8305866/how-do-i-analyze-a-programs-core-dump-file-with-gdb-when-it-has-command-line-pa">linux - How do I analyze a program's core dump file with GDB ... Code sample</a></li>
<li><a href="https://dzone.com/articles/debugging-core-dump-files-on-linux-a-detailed-guid">Debugging Linux Core Dump Files: A Detailed Guide - DZone</a></li>

</ul>
</details>

**Tags**: `#debugging`, `#infrastructure`, `#reliability`, `#core dump`, `#OpenAI`

---

<a id="item-3"></a>
## [Tesla Begins Testing Cybercab Without Steering Wheel in Austin](https://techcrunch.com/2026/06/30/tesla-starts-testing-cybercab-without-pedals-or-a-steering-wheel-in-austin/) ⭐️ 8.0/10

Tesla has started testing its Cybercab robotaxi without pedals or a steering wheel on public roads in Austin, Texas, marking a major step toward launching a fully autonomous ride-hailing service. This testing brings Elon Musk's long-promised robotaxi network closer to reality, potentially disrupting the transportation industry and intensifying competition with other autonomous vehicle companies like Waymo and Zoox. The Cybercab is a two-passenger, fully autonomous electric vehicle designed without manual controls; it is expected to have a roughly 50-kWh battery pack and an EPA-estimated range of nearly 280 miles.

rss · 36氪 - 科技 · Jun 30, 15:32

**Background**: Tesla first unveiled the Cybercab concept in October 2024 as part of its robotaxi vision. The company's Full Self-Driving (FSD) software underpins the autonomous capabilities, and a limited Tesla Robotaxi service launched in Austin in June 2025 using vehicles with manual controls. Removing the steering wheel and pedals represents a significant leap toward Level 5 autonomy.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Cybercab">Tesla Cybercab - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Robotaxi">Tesla Robotaxi - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#autonomous vehicles`, `#Tesla`, `#robotaxi`, `#transportation`, `#AI`

---

<a id="item-4"></a>
## [Amazon launches $1B FDE org for AI agent deployment](https://techcrunch.com/2026/06/30/amazon-launches-new-1-billion-fde-org-following-openai-and-anthropic/) ⭐️ 8.0/10

Amazon Web Services (AWS) announced a new $1 billion internal organization focused on forward-deployed engineers (FDEs) who will embed with customer companies to deploy custom AI agents. The initiative follows similar moves by OpenAI and Anthropic, emphasizing fast deployment and customer self-sufficiency. This investment signals Amazon's commitment to capturing the enterprise AI agent market, which is rapidly growing as companies seek practical deployment solutions. By embedding engineers directly with clients, Amazon aims to accelerate adoption and reduce deployment friction, potentially setting a new standard for enterprise AI services. The FDE model, pioneered by Palantir, involves engineers working on-site with clients to customize and deploy technical solutions. Amazon's new org will focus on purpose-built AI agents, with engineers embedded in companies for fast engagements and to ensure customers can eventually manage the agents independently.

rss · 36氪 - 科技 · Jun 30, 15:00

**Background**: Forward-deployed engineers (FDEs) are professionals who work closely with client organizations to develop, customize, and deploy technical solutions in operational environments. This model has become increasingly popular for managing AI deployments, as it bridges the gap between product development and real-world application. Amazon, OpenAI, and Anthropic are all investing in this approach to help enterprises adopt AI agents more effectively.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/30/amazon-launches-new-1-billion-fde-org-following-openai-and-anthropic/">Amazon launches new $1 billion FDE org, following OpenAI and Anthropic | TechCrunch</a></li>
<li><a href="https://en.wikipedia.org/wiki/Forward_Deployed_Engineer">Forward Deployed Engineer - Wikipedia</a></li>
<li><a href="https://oodaloop.com/briefs/technology/amazon-launches-new-1-billion-fde-org-following-openai-and-anthropic/">Amazon launches new $1 billion FDE org, following OpenAI and Anthropic — OODAloop</a></li>

</ul>
</details>

**Tags**: `#Amazon`, `#AI agents`, `#enterprise AI`, `#investment`, `#deployment`

---

<a id="item-5"></a>
## [South Korea pledges $550B+ to ease memory chip shortage](https://techcrunch.com/2026/06/29/south-korean-tech-giants-commit-over-550b-to-ease-ramageddon/) ⭐️ 8.0/10

South Korea's top memory chip makers, including Samsung and SK Hynix, have committed over $550 billion to build new fabrication facilities to address the global memory shortage known as 'RAMageddon' and bolster AI capabilities. This massive investment aims to alleviate the severe memory supply shortage that has been impacting consumer and enterprise PC markets since 2025, while also positioning South Korea as a key player in AI infrastructure. The shortage, driven by a structural shift of manufacturing capacity toward high-margin AI data center products, is expected to last until at least 2028, according to industry analysts.

rss · 36氪 - 科技 · Jun 29, 18:07

**Background**: The global memory supply shortage, sometimes called 'RAMageddon' or 'RAMpocalypse', began in 2025 and primarily affects DRAM and NAND flash memory. Unlike the earlier pandemic-era chip shortage, this one is caused by manufacturers prioritizing AI-related chips over consumer memory, leading to scarcity and price hikes.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RAMmageddon">RAMmageddon</a></li>
<li><a href="https://en.wikipedia.org/wiki/2024–present_global_memory_supply_shortage">2025–present global memory supply shortage - Wikipedia</a></li>
<li><a href="https://www.cnet.com/tech/computing/tech-companies-are-freaking-out-about-ramageddon/">Tech Companies Are Freaking Out About RAMageddon - CNET</a></li>

</ul>
</details>

**Tags**: `#memory chips`, `#AI infrastructure`, `#semiconductor investment`, `#South Korea`, `#hardware`

---

<a id="item-6"></a>
## [AI deciphers long-range DNA signals in RNA splicing](https://news.google.com/rss/articles/CBMiXEFVX3lxTFAyeGJFZG9KOURQZzdSLUNuZnZfNl9vblRoeUhDWWVyTS05VHlkVzZFaVRPYlRZYnA5dTQ1YWdlR0Q2MDl0RXpCd3k3UHFhenhRZVdWX0RNU1A1dmJa?oc=5) ⭐️ 8.0/10

Researchers have developed an AI model that can decipher long-range DNA signals that regulate RNA splicing, a key process in gene expression. This breakthrough was reported by EurekAlert! and represents a significant advance in understanding how distant DNA elements influence splicing decisions. This work could transform our understanding of gene regulation and disease mechanisms, as aberrant splicing is linked to many genetic disorders and cancers. The AI approach enables analysis of long-range genomic interactions that were previously difficult to study, potentially leading to new therapeutic targets. The AI model specifically focuses on long-range DNA signals, which are regulatory elements located far from the splice sites they influence. The study likely leverages deep learning to predict splicing outcomes based on genomic sequence context over distances of thousands to millions of base pairs.

google_news · EurekAlert! · Jun 30, 11:17

**Background**: RNA splicing is a process where introns are removed from pre-mRNA and exons are joined together to form mature mRNA. Alternative splicing allows a single gene to produce multiple protein variants, and its regulation involves both nearby and distant DNA elements. Long-range DNA signals, such as enhancers and silencers, can influence splicing by looping to target sites, but identifying these interactions has been challenging.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RNA_splicing">RNA splicing - Wikipedia</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4360811/">Mechanism of alternative splicing and its regulation - PMC</a></li>
<li><a href="https://www.nature.com/articles/s41467-025-65077-4">DNALONGBENCH: a benchmark suite for long-range DNA prediction tasks | Nature Communications</a></li>

</ul>
</details>

**Tags**: `#AI`, `#genomics`, `#RNA splicing`, `#bioinformatics`, `#machine learning`

---

<a id="item-7"></a>
## [New York Life's $800B Asset Manager Launches First Tokenized Fund](https://www.coindesk.com/business/2026/06/29/new-york-life-makes-tokenization-debut-with-onchain-high-yield-bond-fund-with-centrifuge) ⭐️ 7.0/10

New York Life's $800 billion asset manager has launched its first tokenized fund via the Centrifuge platform, marking a major milestone in institutional adoption of blockchain-based asset management. This move signals growing institutional confidence in tokenization, potentially paving the way for more traditional financial giants to integrate blockchain technology into asset management, increasing efficiency and liquidity. The fund is a high-yield bond fund tokenized on Centrifuge's infrastructure, which provides automated compliance, multichain reach, and deep DeFi connectivity. Centrifuge is one of the first and largest tokenization platforms, connecting traditional capital markets to onchain rails.

rss · CoinDesk · Jun 30, 11:20

**Background**: Tokenization is the process of representing shares in a traditional investment fund as digital tokens on a blockchain, replacing traditional transfer agents and brokers. This technology can streamline operations, reduce costs, and enable fractional ownership. Centrifuge is a leading platform for tokenizing real-world assets, including funds, private credit, and real estate.

<details><summary>References</summary>
<ul>
<li><a href="https://centrifuge.io/">Centrifuge | Infrastructure for Onchain Asset Management</a></li>
<li><a href="https://www.gemini.com/cryptopedia/centrifuge-crypto-tinlake-tokenization-real-world-assets">Centrifuge: Tokenization of Real-World Assets | Gemini</a></li>
<li><a href="https://chain.link/article/fund-tokenization">What Is Fund Tokenization? | Chainlink</a></li>

</ul>
</details>

**Tags**: `#tokenization`, `#institutional adoption`, `#DeFi`, `#asset management`, `#blockchain`

---

<a id="item-8"></a>
## [MIT Q&A Explores Agentic AI Today and Future](https://news.google.com/rss/articles/CBMidkFVX3lxTE5RM1ZBZHlsbkR4dlJscXJLMkhFUzN1S280eXBsV1hCXzdCOTBraWZ1cUt1SUhqXzBUbThPSnBQdWpKTTI2aXdxQTdHbk9SM1d2NGluUXZ0cWktNzdWeS1xZHRQcVhDcWs5M2R4YXdUTGVvMThCRXc?oc=5) ⭐️ 7.0/10

MIT News published a Q&A article examining the current state of agentic AI and its desired future direction, featuring expert insights from MIT researchers. This discussion clarifies the evolving definition of agentic AI, which is crucial as AI systems become more autonomous and capable of multi-step tasks, impacting industries from healthcare to finance. The article likely distinguishes agentic AI from generative AI, emphasizing goal-directed behavior, tool use, and limited supervision as key attributes.

google_news · MIT News · Jun 30, 15:30

**Background**: Agentic AI refers to AI systems that can perceive, reason, and act autonomously to achieve specific goals, often using large language models for control. Unlike generative AI, which creates content, agentic AI focuses on task completion with minimal human intervention. The concept has gained prominence as AI agents are deployed in real-world applications like customer service and robotics.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained | MIT Sloan</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-ai">What is Agentic AI? | IBM</a></li>

</ul>
</details>

**Tags**: `#AI`, `#agentic AI`, `#MIT`, `#research`

---

<a id="item-9"></a>
## [Chess grandmaster critiques AI visionaries' blind spots](https://news.google.com/rss/articles/CBMikwFBVV95cUxNVmdsYmR1c0hxSGxxN2lLV1RmaEJQSUkxOS1jSW96LWF3NHU0RVVydEhGam1fd285Y2R4ajRVWHZDOUc4LWpVcnpzTzM0NldMdFlfZ0ZPNTl2Z3lRVGhuNm1XQ1gyM3J3bVFVMlpVa0ljN2EzU1BfeWFGNE5xcHJCWGkta0N4OFFta0dhQ2JtX2xpUE0?oc=5) ⭐️ 7.0/10

A chess grandmaster published an opinion piece in The Washington Post arguing that AI visionaries misunderstand key aspects of human intelligence and decision-making, such as intuition and creativity. This perspective from a high-level human expert challenges the prevailing narrative that AI will soon surpass human cognition in all domains, highlighting enduring limitations of current AI systems. The grandmaster emphasizes that human decision-making relies on pattern recognition, intuition, and contextual understanding that AI models like large language models cannot replicate. The piece is an opinion, not peer-reviewed research, but carries weight due to the author's expertise.

google_news · The Washington Post · Jun 30, 15:32

**Background**: Chess has long been a benchmark for AI progress, from Deep Blue defeating Garry Kasparov in 1997 to AlphaZero mastering the game through self-play. However, grandmasters argue that chess involves more than brute calculation, including psychological factors and creativity that current AI lacks.

**Tags**: `#AI`, `#chess`, `#opinion`, `#human intelligence`

---

<a id="item-10"></a>
## [OpenAI Reports Global Growth in ChatGPT Adoption](https://openai.com/index/how-chatgpt-adoption-has-expanded) ⭐️ 6.0/10

OpenAI released new Signals data showing that ChatGPT adoption is growing globally, with users increasing usage frequency and exploring more capabilities across regions and languages. This indicates that ChatGPT is becoming more deeply integrated into users' workflows, which could drive further investment in AI infrastructure and influence how competitors position their own AI assistants. The report highlights growth across multiple regions and languages, but does not provide specific adoption numbers or breakdowns by industry or use case.

rss · OpenAI Blog · Jun 30, 09:00

**Background**: ChatGPT is a large language model-based chatbot developed by OpenAI, launched in November 2022. Adoption metrics like usage frequency and capability exploration help gauge how users are integrating AI into daily tasks.

**Tags**: `#ChatGPT`, `#AI adoption`, `#OpenAI`, `#LLMs`

---