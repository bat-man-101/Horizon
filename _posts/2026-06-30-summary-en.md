---
layout: default
title: "Horizon Summary: 2026-06-30 (EN)"
date: 2026-06-30
lang: en
---

> From 176 items, 11 important content pieces were selected

---

1. [vLLM v0.24.0 Adds MiniMax-M3, DeepSeek-V4 Optimizations](#item-1) ⭐️ 8.0/10
2. [shot-scraper video: Agents record demos via storyboard](#item-2) ⭐️ 8.0/10
3. [OpenAI Launches GeneBench-Pro for Genomics AI](#item-3) ⭐️ 8.0/10
4. [OpenAI Fixes 18-Year-Old Bug via Core Dump Epidemiology](#item-4) ⭐️ 8.0/10
5. [Arcturus uses nano-infused copper to halve grid losses](#item-5) ⭐️ 8.0/10
6. [Amazon launches $1B FDE org for AI agent deployments](#item-6) ⭐️ 8.0/10
7. [South Korea pledges $550B+ to ease memory chip shortage](#item-7) ⭐️ 8.0/10
8. [Hierarchical AI Maps Long-Range DNA Signals in RNA Splicing](#item-8) ⭐️ 8.0/10
9. [AI Could Transform Breast Cancer Detection and Recurrence Prediction](#item-9) ⭐️ 7.0/10
10. [MIT Q&A Explores Agentic AI Today and Future](#item-10) ⭐️ 7.0/10
11. [Nasdaq Expands Market Data to Blockchain via Pyth](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [vLLM v0.24.0 Adds MiniMax-M3, DeepSeek-V4 Optimizations](https://github.com/vllm-project/vllm/releases/tag/v0.24.0) ⭐️ 8.0/10

vLLM v0.24.0 introduces support for the MiniMax-M3 model and delivers major optimizations for DeepSeek-V4, including a FlashInfer sparse index cache and prefill chunk-planning improvements. The release also expands Model Runner V2 to support quantized models by default and adds a new streaming parser engine. This release significantly broadens vLLM's model ecosystem with cutting-edge models like MiniMax-M3 and DeepSeek-V4, which are critical for long-context reasoning and agentic workflows. The performance optimizations, especially for DeepSeek-V4, enable faster and more efficient inference, benefiting the entire AI/ML community. The release includes 571 commits from 256 contributors, with 77 new contributors. Key technical additions include MiniMax Sparse Attention (MSA) support, MXFP4 quantization, FP8 sparse GQA, and extensive AMD/ROCm tuning for MiniMax-M3, as well as a cluster-cooperative topK kernel and native DSA indexer decode for DeepSeek-V4.

github · khluu · Jun 29, 19:41

**Background**: vLLM is a high-performance inference engine for large language models (LLMs), widely used for serving models like GPT and Llama. MiniMax-M3 is a multimodal vision-language model with a Mixture-of-Experts architecture, supporting up to 1M token context windows. DeepSeek-V4 is a series of MoE language models with up to 1.6T parameters, designed for efficient long-context reasoning.

<details><summary>References</summary>
<ul>
<li><a href="https://www.minimax.io/blog/minimax-m3">MiniMax M3: Frontier Coding, 1M Context, Native Multimodality — All in One Model - MiniMax Research | MiniMax</a></li>
<li><a href="https://arxiv.org/abs/2606.19348">[2606.19348] DeepSeek-V4: Towards Highly Efficient Million ...</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#DeepSeek-V4`, `#MiniMax-M3`, `#GPU optimization`

---

<a id="item-2"></a>
## [shot-scraper video: Agents record demos via storyboard](https://simonwillison.net/2026/Jun/30/shot-scraper-video/#atom-everything) ⭐️ 8.0/10

Simon Willison released shot-scraper 1.10 with a new 'video' command that accepts a storyboard.yml file and uses Playwright to record a video of a web application routine, enabling coding agents to produce visual proof of their work. This tool addresses a practical need for AI-assisted development by allowing agents to automatically produce video demos, which helps developers verify that code actually works as intended. It streamlines the feedback loop in agent-driven workflows. The storyboard.yml file defines server setup, viewport size, cursor visibility, wait conditions, JavaScript injection, and a sequence of scenes with actions like pause and click. The command supports authentication via a JSON cookie file and outputs WebM or MP4 videos.

rss · Simon Willison · Jun 30, 16:54

**Background**: shot-scraper is a command-line tool built on Playwright for taking automated screenshots of websites. The new video feature extends this to recording full browser sessions, controlled by a YAML storyboard that scripts user interactions. This is part of a broader trend where coding agents need to demonstrate their output beyond static screenshots.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/30/shot-scraper-video/">Have your agent record video demos of its work with shot ...</a></li>
<li><a href="https://github.com/simonw/shot-scraper">GitHub - simonw/shot-scraper: A command-line utility for ... GitHub - hval/shotscraper: https://www.nettavisen.no · GitHub Simon Willison’s Weblog - vuink.com shot-scraper · PyPI Simon Willison on shot-scraper</a></li>
<li><a href="https://playwright.dev/docs/videos">Videos | Playwright</a></li>

</ul>
</details>

**Tags**: `#developer-tools`, `#playwright`, `#AI-agents`, `#video-recording`, `#automation`

---

<a id="item-3"></a>
## [OpenAI Launches GeneBench-Pro for Genomics AI](https://openai.com/index/introducing-genebench-pro) ⭐️ 8.0/10

OpenAI has introduced GeneBench-Pro, a new benchmark designed to evaluate AI performance in genomics, biology, and scientific research using complex real-world datasets. This benchmark provides a rigorous standard for assessing AI models in genomics, potentially accelerating progress in drug discovery, personalized medicine, and biological research. GeneBench-Pro comprises 129 evaluations across 10 primary domains and 21 subdomains, focusing on multistage statistical reasoning in genomics and translational biomedicine.

rss · OpenAI Blog · Jun 30, 00:00

**Background**: GeneBench-Pro builds on the earlier GeneBench, which tests AI agents for multi-stage inference in scientific workflows. The new benchmark uses more complex, real-world case studies to better reflect practical challenges in genomics research.

<details><summary>References</summary>
<ul>
<li><a href="https://www.biorxiv.org/content/10.64898/2026.06.29.735386v1">GeneBench-Pro: Evaluating Multistage Statistical Reasoning\\in Genomics, Quantitative Biology, and Translational Biomedicine | bioRxiv</a></li>
<li><a href="https://www.startuphub.ai/ai-news/artificial-intelligence/2026/openai-unveils-genebench-pro-benchmark">OpenAI Unveils Genebench-Pro Benchmark | StartupHub.ai</a></li>
<li><a href="https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf">GeneBench: Assessing AI Agents for Multi-Stage Inference ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#benchmark`, `#genomics`, `#scientific research`, `#OpenAI`

---

<a id="item-4"></a>
## [OpenAI Fixes 18-Year-Old Bug via Core Dump Epidemiology](https://openai.com/index/core-dump-epidemiology-data-infrastructure-bug) ⭐️ 8.0/10

OpenAI engineers applied large-scale core dump analysis to debug rare infrastructure crashes, uncovering both a hardware fault and an 18-year-old software bug. This novel debugging methodology, termed 'core dump epidemiology,' demonstrates a scalable approach to diagnosing elusive failures in large-scale AI infrastructure, potentially influencing reliability practices across the industry. The bug had persisted for 18 years, evading detection through conventional debugging. The analysis combined automated core dump collection with statistical correlation to pinpoint root causes across thousands of servers.

rss · OpenAI Blog · Jun 30, 00:00

**Background**: A core dump is a snapshot of a program's memory at the time of a crash, typically generated by the operating system. Analyzing core dumps helps developers understand why a crash occurred. 'Core dump epidemiology' refers to the systematic collection and analysis of core dumps across many machines to identify patterns and root causes of rare failures.

<details><summary>References</summary>
<ul>
<li><a href="https://www.siliconreport.com/openai-details-core-dump-epidemiology-for-infrastructure-debugging-8b6d27b1">OpenAI Details 'Core Dump Epidemiology' for Infrastructure ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Core_dump">Core dump - Wikipedia</a></li>
<li><a href="https://sergioprado.blog/linux-core-dump-analysis/">Linux core dump analysis - sergioprado.blog</a></li>

</ul>
</details>

**Tags**: `#debugging`, `#infrastructure`, `#reliability`, `#core dump`, `#OpenAI`

---

<a id="item-5"></a>
## [Arcturus uses nano-infused copper to halve grid losses](https://techcrunch.com/2026/06/30/arcturus-could-halve-the-grids-electrical-losses-using-its-nano-infused-copper/) ⭐️ 8.0/10

Stealth startup Arcturus has developed a laser-based process to infuse carbon nanomaterials into copper, claiming it can halve electrical losses in the power grid. If verified, this breakthrough could dramatically improve energy efficiency in grid infrastructure, reducing wasted electricity and lowering costs for utilities and consumers worldwide. The company uses lasers to infuse carbon nanomaterials into copper, enhancing its electrical conductivity. However, the claims are currently unverified and lack published technical details.

rss · 36氪 - 科技 · Jun 30, 15:01

**Background**: Electrical grids lose about 5-10% of transmitted energy as heat due to resistance in copper wires. Carbon nanomaterials like graphene have higher conductivity than copper, but integrating them into bulk metals has been challenging. Arcturus' laser infusion technique aims to create a composite that combines the conductivity of carbon with the mechanical properties of copper.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/30/arcturus-could-halve-the-grids-electrical-losses-using-its-nano-infused-copper/">Arcturus could halve the grid’s electrical losses using its nano-infused copper | TechCrunch</a></li>

</ul>
</details>

**Tags**: `#energy`, `#materials science`, `#nanotechnology`, `#grid efficiency`

---

<a id="item-6"></a>
## [Amazon launches $1B FDE org for AI agent deployments](https://techcrunch.com/2026/06/30/amazon-launches-new-1-billion-fde-org-following-openai-and-anthropic/) ⭐️ 8.0/10

Amazon Web Services (AWS) announced a new $1 billion internal organization for forward-deployed engineers (FDEs) focused on deploying purpose-built AI agents within customer companies. Engineers will embed with clients to ensure fast deployments and enable customer self-sufficiency. This move signals a major industry trend where cloud providers invest heavily in hands-on AI deployment services, following similar initiatives by OpenAI and Anthropic. It could accelerate enterprise adoption of AI agents by reducing deployment friction and building customer expertise. The FDE model, pioneered by Palantir, involves engineers working on-site with clients to customize and deploy solutions. Amazon's new org will focus on purpose-built agents—AI systems designed for specific tasks like sales lead nurturing or customer service deflection.

rss · 36氪 - 科技 · Jun 30, 15:00

**Background**: Forward-deployed engineers (FDEs) are professionals who embed with client organizations to develop, customize, and deploy technical solutions in operational environments. Purpose-built agents are AI systems focused on a single job, capable of taking action beyond what general-purpose LLMs can do. This approach has gained popularity as companies seek to integrate AI into their workflows effectively.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Forward_Deployed_Engineer">Forward Deployed Engineer - Wikipedia</a></li>
<li><a href="https://techcrunch.com/2026/06/30/amazon-launches-new-1-billion-fde-org-following-openai-and-anthropic/">Amazon launches new $1 billion FDE org, following OpenAI and Anthropic | TechCrunch</a></li>
<li><a href="https://www.salesforce.com/blog/autonomous-agents/">Why Purpose-Built Agents are the Future of AI at Work</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Amazon`, `#enterprise`, `#agents`, `#investment`

---

<a id="item-7"></a>
## [South Korea pledges $550B+ to ease memory chip shortage](https://techcrunch.com/2026/06/29/south-korean-tech-giants-commit-over-550b-to-ease-ramageddon/) ⭐️ 8.0/10

South Korea's two largest memory chip companies have committed over $550 billion to build new fabrication plants, aiming to alleviate the global memory shortage known as 'RAMageddon' and strengthen AI infrastructure. This massive investment addresses a critical industry shortage that has driven up memory prices and constrained AI data center expansion, positioning South Korea as a key player in the global AI hardware supply chain. The shortage, labeled 'RAMageddon', began in 2025 due to manufacturing capacity being reallocated to high-margin AI memory products, and is expected to last until at least 2027 or 2028 according to industry executives.

rss · 36氪 - 科技 · Jun 29, 18:07

**Background**: Memory chips, such as DRAM and NAND flash, are essential components in computers, servers, and AI systems. The current shortage stems from a structural shift where fabs prioritize high-margin memory for AI data centers over consumer products, leading to supply constraints and price hikes.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RAMmageddon">RAMmageddon</a></li>
<li><a href="https://en.wikipedia.org/wiki/List_of_semiconductor_fabrication_plants">List of semiconductor fabrication plants - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#memory chips`, `#AI infrastructure`, `#semiconductor`, `#investment`, `#South Korea`

---

<a id="item-8"></a>
## [Hierarchical AI Maps Long-Range DNA Signals in RNA Splicing](https://news.google.com/rss/articles/CBMiWEFVX3lxTE55aXEzVDdCTXhTdW5IOGdsUlB0S3gtZ3VSTTdDbE1qeDBJS2I1bW9RejdQYi1OM19pb09GZjY5SGwwRnV0OXZCZXFLOXg4QnBBOTRRZXJnaGM?oc=5) ⭐️ 8.0/10

Researchers developed a hierarchical artificial intelligence model that maps long-range DNA signals regulating RNA splicing, revealing how distant genomic elements influence splice-site selection. This advance provides a deeper understanding of gene regulation, which could improve predictions of genetic variants' effects on splicing and aid in developing therapies for splicing-related diseases. The hierarchical AI model integrates multiple levels of genomic information, from local splice sites to distal regulatory elements, to predict splicing outcomes with high accuracy.

google_news · EurekAlert! · Jun 30, 13:18

**Background**: RNA splicing is a process where introns are removed from pre-mRNA and exons are joined to form mature mRNA. Long-range DNA signals, such as enhancers and silencers located far from splice sites, can influence splicing decisions but are challenging to study. Traditional models often focus on local sequences, missing these distant regulatory effects.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RNA_splicing">RNA splicing - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI`, `#computational biology`, `#RNA splicing`, `#genomics`, `#machine learning`

---

<a id="item-9"></a>
## [AI Could Transform Breast Cancer Detection and Recurrence Prediction](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBPbkVuSFFDbFF2YU9rUHhQZ09qZFg0YzdPYllxbXIxWXdkM3diaGZKNllMVEhMdC1ucWlacDNsdmcybzFScThUMXEtMzZWQ29mYmhHRkhjSW9MQU1p?oc=5) ⭐️ 7.0/10

A new report from EurekAlert! highlights that artificial intelligence shows promise in improving breast cancer detection and predicting recurrence, potentially transforming current diagnostic practices. This advancement could lead to earlier and more accurate diagnosis of breast cancer, reducing false positives and improving patient outcomes, while also enabling personalized recurrence monitoring. The report does not specify particular AI models or datasets, but emphasizes that AI algorithms can analyze mammograms and other imaging data to detect subtle patterns that human radiologists might miss.

google_news · EurekAlert! · Jun 30, 16:33

**Background**: Breast cancer is one of the most common cancers worldwide, and early detection significantly improves survival rates. Traditional screening relies on mammography, which has limitations in sensitivity and specificity. AI, particularly deep learning, has been increasingly applied to medical imaging to enhance diagnostic accuracy.

**Tags**: `#AI`, `#healthcare`, `#breast cancer`, `#machine learning`

---

<a id="item-10"></a>
## [MIT Q&A Explores Agentic AI Today and Future](https://news.google.com/rss/articles/CBMidkFVX3lxTE5RM1ZBZHlsbkR4dlJscXJLMkhFUzN1S280eXBsV1hCXzdCOTBraWZ1cUt1SUhqXzBUbThPSnBQdWpKTTI2aXdxQTdHbk9SM1d2NGluUXZ0cWktNzdWeS1xZHRQcVhDcWs5M2R4YXdUTGVvMThCRXc?oc=5) ⭐️ 7.0/10

MIT News published a Q&A article examining the current state and future aspirations of agentic AI, featuring insights from researchers and practitioners. This discussion helps clarify the evolving definition of agentic AI and its potential impact on industries, as autonomous AI systems become more prevalent. The article likely covers distinctions between agentic AI and generative AI, levels of autonomy, and challenges in building reliable agents.

google_news · MIT News · Jun 30, 15:30

**Background**: Agentic AI refers to AI systems that can autonomously pursue goals, use tools, and take actions with limited human supervision. It represents an evolution beyond generative AI, which primarily produces content. Key concepts include perception, reasoning, planning, and execution.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained - MIT Sloan</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-ai-vs-generative-ai">Agentic AI vs. Generative AI | IBM</a></li>

</ul>
</details>

**Tags**: `#agentic AI`, `#artificial intelligence`, `#MIT`, `#AI research`

---

<a id="item-11"></a>
## [Nasdaq Expands Market Data to Blockchain via Pyth](https://www.coindesk.com/markets/2026/06/30/nasdaq-expands-distribution-of-its-market-data-into-blockchain-infrastructure) ⭐️ 6.0/10

Nasdaq is distributing its TotalView equity data through the Pyth Network blockchain, making real-time market data available to on-chain platforms and tokenized securities. The initiative also involves a partnership with Kraken and powers Ostium's equity perpetuals. This marks a significant step in traditional finance adopting blockchain infrastructure, enabling programmable and decentralized access to Nasdaq's market data. It could accelerate the integration of real-world assets into DeFi and attract more institutional participation. The data is distributed via Pyth Network, a decentralized oracle that already provides price feeds for many DeFi protocols. Nasdaq's TotalView is a premium data product offering detailed order book information.

rss · CoinDesk · Jun 30, 13:00

**Background**: Blockchain oracles like Pyth bridge off-chain data (e.g., stock prices) to on-chain smart contracts. Nasdaq's move follows a broader trend of traditional financial institutions exploring blockchain for efficiency and new revenue streams. The convergence of traditional finance and blockchain is accelerating, with banks and exchanges increasingly integrating distributed ledger technology.

<details><summary>References</summary>
<ul>
<li><a href="https://cryptobriefing.com/nasdaq-blockchain-market-data-distribution/">Nasdaq expands market data distribution into blockchain ...</a></li>
<li><a href="https://www.coindesk.com/markets/2026/06/30/nasdaq-expands-distribution-of-its-market-data-into-blockchain-infrastructure">Nasdaq expands distribution of its market data into ...</a></li>
<li><a href="https://tradersunion.com/news/cryptocurrency-news/show/2530960-nasdaq-market-data-pyth-blockchain/">Nasdaq expands market data distribution through Pyth ...</a></li>

</ul>
</details>

**Tags**: `#blockchain`, `#market data`, `#finance`, `#Nasdaq`

---