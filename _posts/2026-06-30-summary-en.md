---
layout: default
title: "Horizon Summary: 2026-06-30 (EN)"
date: 2026-06-30
lang: en
---

> From 150 items, 10 important content pieces were selected

---

1. [vLLM v0.24.0 Adds MiniMax-M3, DeepSeek-V4 Optimizations](#item-1) ⭐️ 8.0/10
2. [OpenAI Fixes 18-Year-Old Bug via Core Dump Epidemiology](#item-2) ⭐️ 8.0/10
3. [Tesla Begins Testing Cybercab Without Steering Wheel or Pedals in Austin](#item-3) ⭐️ 8.0/10
4. [Arcturus uses nano-infused copper to halve grid losses](#item-4) ⭐️ 8.0/10
5. [Amazon launches $1B FDE org for AI agent deployment](#item-5) ⭐️ 8.0/10
6. [AI deciphers long-range DNA signals behind RNA splicing](#item-6) ⭐️ 8.0/10
7. [Nasdaq Expands Market Data Distribution to Blockchain](#item-7) ⭐️ 7.0/10
8. [MIT Q&A: Defining Agentic AI Today and Its Future](#item-8) ⭐️ 7.0/10
9. [Chess grandmaster critiques AI visionaries](#item-9) ⭐️ 7.0/10
10. [OpenAI Reports Global Growth in ChatGPT Adoption](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [vLLM v0.24.0 Adds MiniMax-M3, DeepSeek-V4 Optimizations](https://github.com/vllm-project/vllm/releases/tag/v0.24.0) ⭐️ 8.0/10

vLLM v0.24.0 introduces support for the MiniMax-M3 model and major optimizations for DeepSeek-V4, including a FlashInfer sparse index cache and prefill chunk-planning. The release also expands Model Runner V2 to support quantized models by default and integrates DeepEP v2 for expert parallelism. This release significantly enhances vLLM's support for cutting-edge models like MiniMax-M3 and DeepSeek-V4, which are critical for long-context reasoning and agentic tasks. The optimizations improve inference throughput and latency, benefiting the broader AI/ML infrastructure community. The release includes 571 commits from 256 contributors, with new features like a streaming parser engine for tool-call parsing and support for DiffusionGemma. Device selection now uses a new `device_ids` argument instead of setting `CUDA_VISIBLE_DEVICES` internally.

github · khluu · Jun 29, 19:41

**Background**: vLLM is a high-throughput, memory-efficient inference and serving engine for large language models (LLMs), widely used in production AI deployments. MiniMax-M3 is a multimodal vision-language model with a Mixture-of-Experts architecture and up to 1M token context window, while DeepSeek-V4 is a massive MoE model with up to 1.6T total parameters.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm">GitHub - vllm-project/vllm: A high-throughput and memory-efficient inference and serving engine for LLMs · GitHub</a></li>
<li><a href="https://www.minimax.io/blog/minimax-m3">MiniMax M3: Frontier Coding, 1M Context, Native Multimodality — All in One Model - MiniMax Research | MiniMax</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro">deepseek-ai/DeepSeek-V4-Pro · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#DeepSeek`, `#MiniMax`, `#open source`

---

<a id="item-2"></a>
## [OpenAI Fixes 18-Year-Old Bug via Core Dump Epidemiology](https://openai.com/index/core-dump-epidemiology-data-infrastructure-bug) ⭐️ 8.0/10

OpenAI engineers applied large-scale core dump analysis to debug rare infrastructure crashes, uncovering both a hardware fault and an 18-year-old software bug. This demonstrates a novel, epidemiological approach to debugging rare failures in large-scale systems, potentially improving reliability engineering practices across the industry. The bug had persisted for 18 years, and the analysis combined core dump data from thousands of machines to identify the root cause. The fix involved both a hardware replacement and a software patch.

rss · OpenAI Blog · Jun 30, 00:00

**Background**: A core dump is a file containing a snapshot of a process's memory at the time of a crash, commonly used for post-mortem debugging. Large-scale systems generate vast numbers of core dumps, and analyzing them collectively—like an epidemiological study—can reveal patterns that pinpoint elusive bugs.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Core_dump">Core dump - Wikipedia</a></li>
<li><a href="https://sergioprado.blog/linux-core-dump-analysis/">Linux core dump analysis - sergioprado.blog</a></li>
<li><a href="https://dzone.com/articles/debugging-core-dump-files-on-linux-a-detailed-guid">Debugging Linux Core Dump Files: A Detailed Guide</a></li>

</ul>
</details>

**Tags**: `#debugging`, `#infrastructure`, `#reliability`, `#core dump`, `#OpenAI`

---

<a id="item-3"></a>
## [Tesla Begins Testing Cybercab Without Steering Wheel or Pedals in Austin](https://techcrunch.com/2026/06/30/tesla-starts-testing-cybercab-without-pedals-or-a-steering-wheel-in-austin/) ⭐️ 8.0/10

Tesla has started testing its Cybercab robotaxi without a steering wheel or pedals on public roads in Austin, Texas, marking a major step toward a fully autonomous ride-hailing service. This testing brings Elon Musk's long-promised robotaxi network closer to reality and could accelerate the adoption of autonomous vehicles in the ride-hailing industry, challenging competitors like Waymo and Zoox. The Cybercab is a two-passenger electric vehicle designed specifically for autonomy, with a 50-kWh battery pack and an estimated range of nearly 280 miles. Production began in February 2026, and the vehicle is intended to operate without human controls.

rss · 36氪 - 科技 · Jun 30, 15:32

**Background**: Tesla has been developing Full Self-Driving (FSD) software for years, and the Cybercab is a purpose-built vehicle for its robotaxi network. The company launched a limited robotaxi service in Austin in June 2025 using existing Tesla vehicles, but the Cybercab represents a dedicated autonomous platform without manual controls.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Cybercab">Tesla Cybercab</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Robotaxi">Tesla Robotaxi - Wikipedia</a></li>
<li><a href="https://www.caranddriver.com/news/a71590701/tesla-cybercab-specs-epa-documents-revealed/">We Have New Tesla Cybercab Specs Before You're Supposed to See Them Thanks to EPA Documents</a></li>

</ul>
</details>

**Tags**: `#Tesla`, `#autonomous vehicles`, `#robotaxi`, `#self-driving`

---

<a id="item-4"></a>
## [Arcturus uses nano-infused copper to halve grid losses](https://techcrunch.com/2026/06/30/arcturus-could-halve-the-grids-electrical-losses-using-its-nano-infused-copper/) ⭐️ 8.0/10

Stealthy startup Arcturus has developed a laser-based process to infuse carbon nanomaterials into copper, dramatically improving its electrical conductivity and potentially halving electrical grid losses. If successful, this technology could significantly reduce energy waste in power transmission, lowering costs and carbon emissions across the electrical grid. The company claims its nano-infused copper can achieve up to a 30% increase in electrical conductivity in thin films, with potential for bulk conductors to see similar gains.

rss · 36氪 - 科技 · Jun 30, 15:01

**Background**: Electrical grids lose about 5-10% of transmitted energy as heat due to resistance in copper and aluminum conductors. Nanocarbon materials like graphene have exceptional conductivity but are difficult to integrate into metals. Arcturus uses lasers to embed carbon nanomaterials into copper, creating a composite that conducts electricity more efficiently.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/30/arcturus-could-halve-the-grids-electrical-losses-using-its-nano-infused-copper/">Arcturus could halve the grid’s electrical losses using its nano-infused copper | TechCrunch</a></li>
<li><a href="https://www.anl.gov/amd/nanocarboninfused-metallic-conductors">Nanocarbon-infused Metallic Conductors | Argonne National Laboratory</a></li>

</ul>
</details>

**Tags**: `#nanotechnology`, `#energy`, `#materials science`, `#electrical grid`

---

<a id="item-5"></a>
## [Amazon launches $1B FDE org for AI agent deployment](https://techcrunch.com/2026/06/30/amazon-launches-new-1-billion-fde-org-following-openai-and-anthropic/) ⭐️ 8.0/10

Amazon Web Services (AWS) announced a new $1 billion internal organization for forward-deployed engineers (FDEs) who will embed with customers to deploy purpose-built AI agents, following similar moves by OpenAI and Anthropic. This investment signals a major industry trend toward specialized, hands-on AI deployment services, potentially accelerating enterprise adoption of AI agents by providing dedicated engineering support and fostering customer self-sufficiency. Engineers on the new team will focus on fast engagements and customer self-sufficiency, deploying purpose-built agents that are designed for specific jobs rather than general-purpose chatbots. The FDE model was pioneered by Palantir and is increasingly used for AI deployments.

rss · 36氪 - 科技 · Jun 30, 15:00

**Background**: Forward-deployed engineers (FDEs) work closely with clients to develop, customize, and deploy technical solutions in operational environments. Purpose-built AI agents are focused on one specific job and can take action, unlike general-purpose GPT-based tools. Amazon's move follows similar investments by OpenAI and Anthropic, reflecting a growing emphasis on tailored AI solutions.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/30/amazon-launches-new-1-billion-fde-org-following-openai-and-anthropic/">Amazon launches new $1 billion FDE org, following OpenAI and Anthropic | TechCrunch</a></li>
<li><a href="https://en.wikipedia.org/wiki/Forward_Deployed_Engineer">Forward Deployed Engineer - Wikipedia</a></li>
<li><a href="https://www.salesforce.com/blog/autonomous-agents/">Why Purpose-Built Agents are the Future of AI at Work</a></li>

</ul>
</details>

**Tags**: `#Amazon`, `#AI agents`, `#enterprise AI`, `#industry trend`

---

<a id="item-6"></a>
## [AI deciphers long-range DNA signals behind RNA splicing](https://news.google.com/rss/articles/CBMiXEFVX3lxTFAyeGJFZG9KOURQZzdSLUNuZnZfNl9vblRoeUhDWWVyTS05VHlkVzZFaVRPYlRZYnA5dTQ1YWdlR0Q2MDl0RXpCd3k3UHFhenhRZVdWX0RNU1A1dmJa?oc=5) ⭐️ 8.0/10

Researchers have developed an AI model that can identify and interpret long-range DNA signals that regulate RNA splicing, a key process in gene expression. This breakthrough was reported on EurekAlert! and represents a novel application of deep learning to genomics. Understanding long-range DNA signals in RNA splicing could lead to insights into genetic diseases and new therapeutic targets. This work demonstrates AI's potential to unravel complex biological mechanisms that were previously difficult to study. The AI model specifically deciphers signals that are far from the splice sites, which are traditionally hard to capture. The research highlights the importance of non-coding DNA regions in regulating splicing.

google_news · EurekAlert! · Jun 30, 11:17

**Background**: RNA splicing is a process where introns are removed from pre-mRNA and exons are joined to form mature mRNA. Long-range DNA signals are regulatory elements located far from the splice sites that influence splicing efficiency and accuracy. AI models can learn complex patterns in genomic sequences that are not easily detected by traditional methods.

**Tags**: `#AI`, `#genomics`, `#RNA splicing`, `#deep learning`, `#bioinformatics`

---

<a id="item-7"></a>
## [Nasdaq Expands Market Data Distribution to Blockchain](https://www.coindesk.com/markets/2026/06/30/nasdaq-expands-distribution-of-its-market-data-into-blockchain-infrastructure) ⭐️ 7.0/10

Nasdaq announced it will distribute its market data through blockchain infrastructure, integrating traditional financial data with decentralized technology. This move signals growing mainstream adoption of blockchain in traditional finance, potentially increasing transparency and efficiency in market data distribution. The initiative leverages blockchain's immutability and real-time capabilities to provide more secure and timely data access to investors and institutions.

rss · CoinDesk · Jun 30, 13:00

**Background**: Nasdaq is a global stock exchange operator that traditionally distributes market data through centralized systems. Blockchain technology offers a decentralized ledger that can enhance data integrity and reduce latency.

**Tags**: `#blockchain`, `#market data`, `#Nasdaq`, `#fintech`, `#infrastructure`

---

<a id="item-8"></a>
## [MIT Q&A: Defining Agentic AI Today and Its Future](https://news.google.com/rss/articles/CBMidkFVX3lxTE5RM1ZBZHlsbkR4dlJscXJLMkhFUzN1S280eXBsV1hCXzdCOTBraWZ1cUt1SUhqXzBUbThPSnBQdWpKTTI2aXdxQTdHbk9SM1d2NGluUXZ0cWktNzdWeS1xZHRQcVhDcWs5M2R4YXdUTGVvMThCRXc?oc=5) ⭐️ 7.0/10

MIT News published a Q&A article exploring the current definition, capabilities, and desired future of agentic AI systems, featuring expert insights from MIT researchers. This article provides authoritative perspective on agentic AI, a rapidly evolving field that could reshape how AI systems interact with the world, making it essential reading for researchers and practitioners. The Q&A format allows for nuanced discussion of agentic AI's current limitations and potential, including topics like autonomy, goal-directed behavior, and safety considerations.

google_news · MIT News · Jun 30, 15:30

**Background**: Agentic AI refers to AI systems that can act autonomously to achieve goals, as opposed to passive models that only respond to prompts. This concept is central to building AI agents that can plan, reason, and execute tasks in dynamic environments.

**Tags**: `#AI`, `#agentic AI`, `#research`, `#MIT`

---

<a id="item-9"></a>
## [Chess grandmaster critiques AI visionaries](https://news.google.com/rss/articles/CBMikwFBVV95cUxNVmdsYmR1c0hxSGxxN2lLV1RmaEJQSUkxOS1jSW96LWF3NHU0RVVydEhGam1fd285Y2R4ajRVWHZDOUc4LWpVcnpzTzM0NldMdFlfZ0ZPNTl2Z3lRVGhuNm1XQ1gyM3J3bVFVMlpVa0ljN2EzU1BfeWFGNE5xcHJCWGkta0N4OFFta0dhQ2JtX2xpUE0?oc=5) ⭐️ 7.0/10

A chess grandmaster published an opinion piece in The Washington Post arguing that AI visionaries misunderstand key aspects of human intelligence and decision-making. This perspective from a domain where AI has achieved superhuman performance offers a nuanced critique of AI's limitations, challenging the narrative that human cognition can be fully replicated by machines. The grandmaster likely draws on personal experience with chess AI to highlight differences between human intuition and machine calculation, though the full article is behind a paywall.

google_news · The Washington Post · Jun 30, 15:32

**Background**: Chess has been a benchmark for AI since DeepBlue defeated Garry Kasparov in 1997. Modern chess engines like Stockfish and AlphaZero surpass human grandmasters, yet the grandmaster argues that AI still lacks true understanding of the game.

**Tags**: `#AI`, `#chess`, `#opinion`, `#human intelligence`

---

<a id="item-10"></a>
## [OpenAI Reports Global Growth in ChatGPT Adoption](https://openai.com/index/how-chatgpt-adoption-has-expanded) ⭐️ 6.0/10

OpenAI released new Signals data showing that ChatGPT adoption is growing globally, with users increasing usage and exploring more capabilities. This indicates that ChatGPT is becoming more integrated into daily workflows across regions and languages, which could accelerate AI adoption in various industries. The data highlights growth across regions and languages, but the report lacks specific metrics or technical details about the expansion.

rss · OpenAI Blog · Jun 30, 09:00

**Background**: ChatGPT is a conversational AI model developed by OpenAI, launched in late 2022. Its adoption has been tracked through various metrics, and this report provides a high-level overview of global trends.

**Tags**: `#ChatGPT`, `#AI adoption`, `#OpenAI`, `#trends`

---