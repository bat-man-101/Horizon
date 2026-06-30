---
layout: default
title: "Horizon Summary: 2026-06-30 (EN)"
date: 2026-06-30
lang: en
---

> From 133 items, 10 important content pieces were selected

---

1. [Supreme Court rules geofence warrants need Fourth Amendment protections](#item-1) ⭐️ 9.0/10
2. [vLLM v0.24.0: MiniMax-M3 Support, DeepSeek-V4 Optimizations](#item-2) ⭐️ 8.0/10
3. [llama.cpp b9840 Adds DeepSeek V4 Support](#item-3) ⭐️ 8.0/10
4. [Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding](#item-4) ⭐️ 8.0/10
5. [ChatGPT Overturns Chen Lijie's 7-Year Computational Geometry Problem](#item-5) ⭐️ 8.0/10
6. [MiCA Deadline May Force 10M EU Crypto Users Off Platforms](#item-6) ⭐️ 8.0/10
7. [OpenAI Maps AI's Impact on EU Jobs](#item-7) ⭐️ 6.0/10
8. [J.P. Morgan Expands Blockchain Settlement Network for Cross-Border Payments](#item-8) ⭐️ 6.0/10
9. [Vitalik Buterin: Obfuscation Could Enable Private Onchain Voting](#item-9) ⭐️ 6.0/10
10. [BIS warns AI spending boom risks global financial crisis](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Supreme Court rules geofence warrants need Fourth Amendment protections](https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision) ⭐️ 9.0/10

The US Supreme Court ruled that geofence warrants, which compel tech companies to provide location data of all devices within a specific area, must comply with the Fourth Amendment's probable cause and particularity requirements. The decision in Chatrie v. United States sets a landmark precedent for digital privacy. This ruling curtails law enforcement's ability to conduct mass surveillance via geofence warrants, protecting innocent bystanders from having their location data swept up without judicial oversight. It reinforces Fourth Amendment protections in the digital age and may influence similar cases worldwide. The court held that a geofence warrant is a 'search' under the Fourth Amendment, requiring a warrant based on probable cause and describing with particularity the place to be searched. The opinion, written by Justice Kagan, cited the 2014 Riley v. California decision on cell phone searches.

hackernews · cdrnsf · Jun 29, 15:54 · [Discussion](https://news.ycombinator.com/item?id=48720924)

**Background**: Geofence warrants allow police to demand from companies like Google a list of all devices that were within a virtual boundary (geofence) around a crime scene during a specific time window. Critics argued these warrants were unconstitutional because they effectively search everyone in an area, not just suspects. The case arose from a 2018 bank robbery where Google provided data on 19 devices near the bank.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/04/28/scotus-chatrie-geofence-search-warrant-ruling-arguments/">US Supreme Court appears split over controversial use of ' geofence ...</a></li>
<li><a href="https://www.texaspolicyresearch.com/decision-on-geofence-warrants-a-critical-blow-to-mass-surveillance/">Decision on Geofence Warrants : A Critical... - Texas Policy Research</a></li>
<li><a href="https://www.culawreview.org/journal/mapping-the-future-of-surveillance-geofence-warrants-and-the-risks-of-chatrie">Mapping the Future of Surveillance: Geofence Warrants and the Risks...</a></li>

</ul>
</details>

**Discussion**: Commenters praised the ruling as a win for privacy, with one noting the court's use of sources in the opinion as a positive sign. Another commenter highlighted the historical analogy of wiretapping, noting that physical constraints once limited abuse, but digital surveillance lacks those limits. A third commenter shared an example of how location data can identify individuals even without a phone, illustrating the power of such techniques.

**Tags**: `#privacy`, `#supreme court`, `#geofence warrants`, `#digital rights`, `#law enforcement`

---

<a id="item-2"></a>
## [vLLM v0.24.0: MiniMax-M3 Support, DeepSeek-V4 Optimizations](https://github.com/vllm-project/vllm/releases/tag/v0.24.0) ⭐️ 8.0/10

vLLM v0.24.0 adds support for the MiniMax-M3 model and delivers major optimizations for DeepSeek-V4, including a FlashInfer sparse index cache and prefill chunk-planning improvements. The release also introduces Model Runner V2 with default quantization support, a streaming parser engine, and integration of DeepEP v2 for expert parallelism. This release significantly enhances vLLM's capability to serve cutting-edge models like MiniMax-M3 and DeepSeek-V4, which are at the forefront of coding, agentic reasoning, and long-context tasks. The optimizations improve inference throughput and latency, benefiting the broader AI community that relies on vLLM for efficient LLM serving. The release includes 571 commits from 256 contributors, with 77 new contributors. Key technical additions include MXFP4 support for MiniMax-M3, a cluster-cooperative topK kernel for DeepSeek-V4, and a new Rust frontend with API-key authentication and CORS support. vLLM also changed device selection to no longer set CUDA_VISIBLE_DEVICES internally.

github · khluu · Jun 29, 19:41

**Background**: vLLM is a high-performance open-source library for LLM inference and serving, widely used for its efficient memory management and fast decoding. MiniMax-M3 is a frontier open-weight model with 1M context window and multimodal capabilities, while DeepSeek-V4 is a 1-trillion-parameter Mixture-of-Experts model. FlashInfer is a kernel library for LLM serving that provides efficient attention mechanisms like sparse and paged attention.

<details><summary>References</summary>
<ul>
<li><a href="https://www.minimax.io/models/text/m3">MiniMax M3 - Coding & Agentic Frontier, 1M Context, Multimodal</a></li>
<li><a href="https://deepseek.ai/deepseek-v4">DeepSeek V 4 (2026) — 1T Params, Benchmarks & Pricing</a></li>

</ul>
</details>

**Discussion**: The community comments are not directly about vLLM v0.24.0 but discuss a different model (likely Qwen fine-tune). They express mixed opinions: some find it good for creative coding solutions, while others note hallucinations and limitations on consumer hardware. The comments are not relevant to this release.

**Tags**: `#vLLM`, `#LLM inference`, `#model optimization`, `#open source`, `#AI infrastructure`

---

<a id="item-3"></a>
## [llama.cpp b9840 Adds DeepSeek V4 Support](https://github.com/ggml-org/llama.cpp/releases/tag/b9840) ⭐️ 8.0/10

llama.cpp b9840 introduces support for the DeepSeek V4 model architecture, including conversion scripts, inference graph, and optimizations for both V4-Pro and V4-Flash variants. This update enables local, efficient inference of DeepSeek V4—a state-of-the-art open-weight MoE model—on consumer hardware, expanding access to advanced AI capabilities. The release includes multi-platform binaries (macOS, Linux, Windows, Android) and supports features like flash attention, graph reuse, and partial checkpointing for DeepSeek V4.

github · github-actions[bot] · Jun 29, 10:25

**Background**: llama.cpp is a popular open-source project for running large language models locally on CPUs and GPUs with minimal dependencies. DeepSeek V4 is a mixture-of-experts (MoE) model family released by DeepSeek under the MIT license, featuring up to 1.6 trillion total parameters and a 1M-token context window. The GGUF format is used to store quantized models for efficient inference.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ggml-org/llama.cpp/releases">Releases · ggml-org/ llama . cpp</a></li>
<li><a href="https://www.morphllm.com/deepseek-v4">DeepSeek V4: 1.6T MoE, 1M Context, $0.87/M Output. Architecture ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/GGUF">GGUF - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#llama.cpp`, `#DeepSeek V4`, `#LLM inference`, `#open-source`, `#machine learning`

---

<a id="item-4"></a>
## [Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding](https://simonwillison.net/2026/Jun/29/ornith/#atom-everything) ⭐️ 8.0/10

DeepReinforce released Ornith-1.0, a family of open-weight LLMs (MIT licensed) for agentic coding, with sizes from 9B to 397B, built on Gemma 4 and Qwen 3.5. It achieves state-of-the-art performance on coding benchmarks among open-source models of comparable size. Ornith-1.0 introduces a self-scaffolding training framework where the model learns to generate both solutions and task-specific harnesses, potentially reducing reliance on human-designed agent scaffolds. This could accelerate the development of autonomous coding agents and lower the barrier for open-source agentic coding. The model family includes 9B Dense, 31B Dense, 35B MoE, and 397B MoE variants, all MIT licensed. The 35B MoE variant runs at 103 tokens/second on a single GPU and fits in 20GB with 4-bit quantization. Underlying base models (Gemma 4 and Qwen 3.5) are Apache 2.0 licensed.

rss · Simon Willison · Jun 29, 16:17

**Background**: Agentic coding refers to AI systems that perform multi-step software development tasks with minimal human intervention. Traditional LLM-based coding agents rely on human-written scaffolds (harnesses) to guide tool use and reasoning. Self-scaffolding is a new paradigm where the model learns to generate its own task-specific harnesses, co-evolving with the solution policy.

<details><summary>References</summary>
<ul>
<li><a href="https://deep-reinforce.com/ornith_1_0.html">Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding | DeepReinforce Blog | Jun. 2026</a></li>
<li><a href="https://essamamdani.com/blog/ornith-1-0-self-scaffolding-llm-coding-2026">Ornith-1.0: The Self-Scaffolding LLM That Teaches Itself to Code Better | Essa Mamdani | Essa Mamdani</a></li>
<li><a href="https://www.mindstudio.ai/blog/self-scaffolding-ai-models-ornith-1-0">Self-Scaffolding AI Models: How Ornith 1.0 Writes Its Own Agent Harness | MindStudio</a></li>

</ul>
</details>

**Discussion**: Community comments are mixed: some users report good performance on coding tasks and creative solutions, while others note poor performance on chat without tools and a tendency to hallucinate. There is skepticism about whether this is just a fine-tune of Qwen or Gemma, and concerns about accessibility (e.g., 9B model requires 80GB GPU).

**Tags**: `#LLM`, `#open-source`, `#coding`, `#agentic`, `#model release`

---

<a id="item-5"></a>
## [ChatGPT Overturns Chen Lijie's 7-Year Computational Geometry Problem](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&mid=2652709773&idx=2&sn=68bde762eb0070f5bd61518728971232) ⭐️ 8.0/10

ChatGPT reportedly solved a core computational geometry problem that had stumped renowned researcher Chen Lijie for seven years, building on OpenAI's recent resolution of an Erdős conjecture. This demonstrates AI's growing capability to tackle long-standing mathematical problems, potentially accelerating research in computational geometry and related fields. The problem is a core computational geometry challenge that Chen Lijie had worked on for seven years. The solution builds on OpenAI's earlier resolution of an Erdős conjecture, though specific details of the problem and solution remain undisclosed.

rss · 新智元 · Jun 29, 05:01

**Background**: Computational geometry deals with algorithms for geometric problems, such as point location and range searching. Chen Lijie is a renowned computer scientist known for his work in complexity theory. The Erdős conjecture is a famous unsolved problem in number theory proposed by Paul Erdős.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Computational_geometry">Computational geometry - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI`, `#computational geometry`, `#ChatGPT`, `#OpenAI`, `#breakthrough`

---

<a id="item-6"></a>
## [MiCA Deadline May Force 10M EU Crypto Users Off Platforms](https://www.coindesk.com/business/2026/06/29/mica-july-1-deadline-could-leave-10-million-crypto-users-searching-for-a-new-platform-in-the-eu) ⭐️ 8.0/10

The European Union's Markets in Crypto-Assets (MiCA) regulation faces a July 1 deadline that could leave approximately 10 million crypto users without a compliant platform, as many exchanges have not yet obtained the necessary licenses. This deadline represents a major regulatory shake-up for the EU crypto market, potentially disrupting access for millions of users and forcing exchanges to either comply or exit the region, setting a precedent for global crypto regulation. MiCA entered into force in June 2023 and requires crypto asset service providers to obtain authorization by July 1, 2026; non-compliant platforms face enforcement actions, including potential bans on serving EU customers.

rss · CoinDesk · Jun 29, 15:03

**Background**: MiCA is a comprehensive regulatory framework for crypto assets in the EU, aimed at protecting investors and ensuring market integrity while fostering innovation. It covers issuers of crypto assets, exchanges, and wallet providers, requiring them to meet strict compliance standards such as anti-money laundering (AML) and consumer protection rules. The regulation has a phased implementation, with the full application deadline approaching in July 2026.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Markets_in_Crypto-Assets">Markets in Crypto -Assets - Wikipedia</a></li>
<li><a href="https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica">Markets in Crypto -Assets Regulation ( MiCA )</a></li>
<li><a href="https://aurum.law/newsroom/EU-MiCA-Regulation">EU MiCA Regulation : Crypto Compliance Guide | Aurum</a></li>

</ul>
</details>

**Tags**: `#crypto regulation`, `#MiCA`, `#EU`, `#blockchain`, `#finance`

---

<a id="item-7"></a>
## [OpenAI Maps AI's Impact on EU Jobs](https://openai.com/index/mapping-ai-jobs-transition-eu) ⭐️ 6.0/10

OpenAI released a report mapping how AI could reshape occupations across the European Union, identifying roles at risk of automation, those poised for growth, and workflows likely to change. This report provides a high-level overview that could inform EU policy and workforce planning, highlighting the need for reskilling and adaptation as AI adoption accelerates. The report categorizes occupations into automation, growth, and workflow shifts, but lacks specific technical details or quantitative projections.

rss · OpenAI Blog · Jun 29, 07:00

**Background**: AI technologies like large language models are increasingly capable of performing tasks traditionally done by humans, raising questions about job displacement and transformation. The European Union has been proactive in regulating AI through the AI Act, and understanding labor impacts is crucial for policy-making.

**Tags**: `#AI`, `#labor`, `#EU`, `#automation`, `#workforce`

---

<a id="item-8"></a>
## [J.P. Morgan Expands Blockchain Settlement Network for Cross-Border Payments](https://www.coindesk.com/business/2026/06/29/j-p-morgan-broadens-blockchain-settlement-network-as-banks-modernize-cross-border-payments) ⭐️ 6.0/10

J.P. Morgan has expanded its Kinexys blockchain settlement network, deepening its reach in the Asia-Pacific region, with the platform having processed over $4 trillion in transactions to date. This expansion signals growing adoption of blockchain for core banking infrastructure, potentially reducing costs and settlement times for cross-border payments, which traditionally rely on slower systems like SWIFT. Kinexys is a bank-led blockchain platform offering programmable payments, asset tokenization, and near-real-time settlement. The latest expansion focuses on the Asia-Pacific region, a key area for cross-border trade.

rss · CoinDesk · Jun 29, 15:23

**Background**: Traditional cross-border payments often use correspondent banking networks like SWIFT, which can be slow and costly. Blockchain-based settlement networks offer faster, transparent, and programmable alternatives. J.P. Morgan's Kinexys is one such enterprise-grade solution.

<details><summary>References</summary>
<ul>
<li><a href="https://www.coindesk.com/business/2026/06/29/j-p-morgan-broadens-blockchain-settlement-network-as-banks-modernize-cross-border-payments">J . P . Morgan broadens Kinexys blockchain settlement network as...</a></li>
<li><a href="https://www.jpmorgan.com/kinexys/index">Kinexys: Enterprise Bank-Led Blockchain Solutions</a></li>
<li><a href="https://www.paycio.com/blog/blockchain-cross-border-payments-and-how-do-they-work">Blockchain Cross - border Payments & How Do They Work</a></li>

</ul>
</details>

**Tags**: `#blockchain`, `#finance`, `#cross-border payments`, `#J.P. Morgan`

---

<a id="item-9"></a>
## [Vitalik Buterin: Obfuscation Could Enable Private Onchain Voting](https://cointelegraph.com/news/vitalik-buterin-private-onchain-voting-obfuscation?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) ⭐️ 6.0/10

Ethereum co-founder Vitalik Buterin suggested that indistinguishability obfuscation (iO) could eventually enable private, collusion-resistant onchain voting without trusted committees, though the technology is currently impractical. If realized, iO-based voting could significantly enhance privacy and security in DAO governance and DeFi protocols, reducing reliance on trusted third parties and mitigating collusion risks. Indistinguishability obfuscation is a cryptographic primitive that hides a program's implementation while preserving its functionality, but current candidates are extremely impractical—for example, obfuscating a simple 32-bit AND function produces a program nearly 12 gigabytes in size.

rss · CoinTelegraph · Jun 29, 10:53

**Background**: Indistinguishability obfuscation (iO) is a form of software obfuscation where obfuscated versions of any two programs that compute the same function are computationally indistinguishable. It is considered a 'crypto-complete' primitive because it can be used to construct almost all other cryptographic primitives. However, known iO constructions rely on complex mathematical assumptions and are far from practical deployment.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Indistinguishability_obfuscation">Indistinguishability obfuscation</a></li>
<li><a href="https://coinmarketcap.com/academy/article/vitalik-buterin-obfuscation-private-onchain-voting">Vitalik Buterin Says Obfuscation Could Enable Private On - Chain Voting</a></li>
<li><a href="https://coinfractal.com/vitalik-buterin-indistinguishability-obfuscation-private-onchain-voting/">Vitalik: Obfuscation Could Power Private Onchain Voting</a></li>

</ul>
</details>

**Tags**: `#cryptography`, `#voting`, `#privacy`, `#blockchain`, `#Ethereum`

---

<a id="item-10"></a>
## [BIS warns AI spending boom risks global financial crisis](https://cointelegraph.com/news/bis-sounds-alarm-on-ai-exuberance-as-debt-fueled-boom-risks-bust?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) ⭐️ 6.0/10

The Bank for International Settlements (BIS) has warned that excessive AI spending, fueled by debt and leveraged nonbank structures, could lead to global financial instability. This warning highlights a systemic risk that could affect global financial markets, as a rapid unwinding of leveraged AI investments might trigger a broader financial crisis. The BIS report notes that AI investment financing relies heavily on debt and highly leveraged nonbank structures, which can unwind rapidly and cause systemic disruption.

rss · CoinTelegraph · Jun 29, 05:31

**Background**: The BIS is an international financial institution that acts as a bank for central banks and monitors global financial stability. Systemic risk refers to the risk of disruption to financial services that can have serious negative consequences for the real economy. Leveraged nonbank structures include entities like hedge funds and private equity firms that borrow heavily to invest.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bis.org/publ/othp08.htm">Systemic risk: how to deal with it?</a></li>
<li><a href="https://www.fitchratings.com/research/banks/non-bank-entities-face-greater-us-leveraged-lending-risk-vs-banks-06-03-2020">Non-Bank Entities Face Greater US Leveraged Lending Risk vs Banks</a></li>

</ul>
</details>

**Tags**: `#AI`, `#finance`, `#systemic risk`, `#BIS`

---