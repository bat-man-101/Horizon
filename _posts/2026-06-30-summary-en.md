---
layout: default
title: "Horizon Summary: 2026-06-30 (EN)"
date: 2026-06-30
lang: en
---

> From 133 items, 11 important content pieces were selected

---

1. [Supreme Court rules geofence warrants need constitutional protections](#item-1) ⭐️ 9.0/10
2. [Google's AI Peer-Reviewer Processes ~10K Papers at ICML/STOC](#item-2) ⭐️ 9.0/10
3. [vLLM v0.24.0: MiniMax-M3 Support, DeepSeek-V4 Optimizations](#item-3) ⭐️ 8.0/10
4. [Ornith-1.0: Open-Weight Coding LLM with Self-Scaffolding](#item-4) ⭐️ 8.0/10
5. [MiCA Deadline May Displace 10M EU Crypto Users](#item-5) ⭐️ 8.0/10
6. [OpenAI Chief Warns: Small Window for AGI Preparation](#item-6) ⭐️ 6.0/10
7. [Private Key Compromises Cause 40% of $16B Crypto Hack Losses](#item-7) ⭐️ 6.0/10
8. [J.P. Morgan Expands Blockchain Settlement Network](#item-8) ⭐️ 6.0/10
9. [BNY Mellon Adds USDC Stablecoin Services for Institutions](#item-9) ⭐️ 6.0/10
10. [Breez SDK Enables Bitcoin-to-Stablecoin Payments Across 30+ Chains](#item-10) ⭐️ 6.0/10
11. [Vitalik: Obfuscation Could Enable Private Onchain Voting](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Supreme Court rules geofence warrants need constitutional protections](https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision) ⭐️ 9.0/10

The US Supreme Court ruled that geofence warrants, which compel tech companies like Google to provide location data of all devices within a certain area, require constitutional protections under the Fourth Amendment. This landmark decision restricts law enforcement's ability to conduct mass location surveillance without individualized suspicion. This ruling sets a critical precedent for digital privacy in the era of ubiquitous surveillance, potentially affecting millions of users whose location data is collected by companies like Google. It may also influence future cases involving other forms of reverse search warrants and bulk data requests. The case involved a bank robbery where Google provided location data of 19 accounts within 150 meters of the bank, leading to the identification of a suspect. The court emphasized that geofence warrants are inherently broad and require a warrant based on probable cause, with specific limitations to protect innocent third parties.

hackernews · cdrnsf · Jun 29, 15:54 · [Discussion](https://news.ycombinator.com/item?id=48720924)

**Background**: A geofence warrant, also known as a reverse location warrant, is a search warrant that allows law enforcement to search a database (e.g., Google's Sensorvault) for all active mobile devices within a defined geographic area during a specific time period. Unlike traditional warrants that target a specific person or device, geofence warrants sweep up data from many innocent individuals, raising significant Fourth Amendment concerns about unreasonable searches.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Geofence_warrant">Geofence warrant</a></li>
<li><a href="https://www.npr.org/2026/06/29/nx-s1-5844697/supreme-court-restricts-use-of-geofence-warrants">Supreme Court restricts use of geofence warrants : NPR</a></li>

</ul>
</details>

**Discussion**: Commenters expressed strong support for the ruling, with some highlighting historical examples of location tracking (e.g., the Petraeus affair) and questioning whether other surveillance tools like Flock license plate readers would now require warrants. Others noted the court's use of factual sources in the opinion, while criticizing dissenting justices Alito, Thomas, and Barrett for favoring government power.

**Tags**: `#privacy`, `#supreme court`, `#surveillance`, `#law`, `#technology`

---

<a id="item-2"></a>
## [Google's AI Peer-Reviewer Processes ~10K Papers at ICML/STOC](https://www.reddit.com/r/MachineLearning/comments/1uio9rb/googles_agentic_peerreviewer_handled_10k_papers/) ⭐️ 9.0/10

Google deployed an agentic AI peer-reviewer at ICML and STOC conferences, reviewing approximately 10,000 papers with a 30-minute turnaround, and a formal paper reports it catches 34% more mathematical errors than zero-shot prompting. This sets a precedent for AI-automated scientific review at conference scale, potentially accelerating the peer-review process and improving error detection in mathematical content, which could transform how research is evaluated. The system achieved a 34% improvement in detecting mathematical errors compared to zero-shot prompting, and processed papers in about 30 minutes each, demonstrating practical scalability for large conferences.

reddit · r/MachineLearning · /u/Justgototheeffinmoon · Jun 29, 10:05

**Background**: Peer review is a critical but time-consuming process in academic publishing, often causing delays. Zero-shot prompting refers to asking an AI model to perform a task without providing examples, which is a common baseline. Agentic AI systems can autonomously plan and execute multi-step tasks, making them suitable for complex review workflows.

**Discussion**: The Reddit community expressed excitement about the potential for AI to reduce reviewer burden, but also raised concerns about fairness, accuracy, and the risk of over-reliance on automated systems for scientific evaluation.

**Tags**: `#AI`, `#peer review`, `#machine learning`, `#conference`, `#automation`

---

<a id="item-3"></a>
## [vLLM v0.24.0: MiniMax-M3 Support, DeepSeek-V4 Optimizations](https://github.com/vllm-project/vllm/releases/tag/v0.24.0) ⭐️ 8.0/10

vLLM v0.24.0 adds support for the MiniMax-M3 model and delivers major optimizations for DeepSeek-V4, including a FlashInfer sparse index cache that improves time-to-first-token by 2-4% and prefill chunk-planning that boosts end-to-end throughput by 4%. The release also introduces a streaming parser engine, DiffusionGemma support, and DeepEP v2 integration for expert parallelism. This release significantly enhances vLLM's ability to serve cutting-edge large language models like MiniMax-M3 and DeepSeek-V4, which are among the most advanced open-weight models available. The performance optimizations and new features (streaming parser, DiffusionGemma) expand vLLM's applicability to agentic workflows, long-context reasoning, and multimodal tasks, benefiting the entire LLM inference ecosystem. The release includes 571 commits from 256 contributors, with 77 first-time contributors. Key technical highlights include Model Runner V2 now supporting quantized models by default, a new streaming parser engine unifying tool-call/reasoning parsing across models, and the integration of DeepEP v2 for expert parallelism. Additionally, vLLM no longer sets CUDA_VISIBLE_DEVICES internally, replacing it with a device_ids argument.

github · khluu · Jun 29, 19:41

**Background**: vLLM is an open-source high-throughput LLM inference engine that uses PagedAttention to manage KV-cache memory efficiently. MiniMax-M3 is a multimodal vision-language model with a 1M-token context window, built on a Mixture-of-Experts architecture with MiniMax Sparse Attention (MSA). DeepSeek-V4 is a large MoE model with up to 1.6T total parameters (49B active), designed for advanced reasoning and agentic tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.minimax.io/models/text/m3">MiniMax M 3 - Coding & Agentic Frontier, 1M Context, Multimodal</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro">deepseek-ai/DeepSeek-V4-Pro · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#open source`, `#performance optimization`, `#model support`

---

<a id="item-4"></a>
## [Ornith-1.0: Open-Weight Coding LLM with Self-Scaffolding](https://simonwillison.net/2026/Jun/29/ornith/#atom-everything) ⭐️ 8.0/10

DeepReinforce released Ornith-1.0, a family of open-weight (MIT licensed) LLMs for agentic coding, with variants from 9B to 397B parameters, built on Gemma 4 and Qwen 3.5. It achieves state-of-the-art performance among open-source models of comparable size on coding benchmarks. This release provides a permissively licensed, high-performance coding model that can run locally and handle complex agentic tasks, potentially accelerating AI-assisted software development. Its self-scaffolding capability allows the model to improve its own reasoning during inference, which is a novel approach. The model family includes 9B Dense, 31B Dense, 35B MoE, and 397B MoE variants, all under MIT license. Early user reports indicate fast inference (e.g., 103 tokens/second) and effective tool use, though some note a tendency to hallucinate in chat without tools.

rss · Simon Willison · Jun 29, 16:17

**Background**: Agentic coding refers to using AI agents to autonomously perform software development tasks like code generation, debugging, and testing. Self-scaffolding LLMs can generate and refine their own reasoning steps or tool calls during inference, improving performance without external prompts. MoE (Mixture of Experts) architecture activates only a subset of parameters per token, enabling larger models with efficient computation.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/29/ornith/">Ornith-1.0: Self - Scaffolding LLMs for Agentic Coding</a></li>
<li><a href="https://deep-reinforce.com/ornith_1_0.html">Ornith-1.0: Self - Scaffolding LLMs ... | DeepReinforce Blog | Jun. 2026</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agentic_coding">Agentic coding</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed but generally positive: some users find Ornith-1.0 slightly better than Qwen-3.6 35B and appreciate its faster inference due to shorter chain-of-thought. Others question whether it's merely a 'benchmaxxed' fine-tune and express skepticism about the lack of transparency from DeepReinforce. A few users report good results on complex coding tasks but note poor performance in chat-only scenarios.

**Tags**: `#LLM`, `#open-source`, `#coding`, `#agentic`, `#model release`

---

<a id="item-5"></a>
## [MiCA Deadline May Displace 10M EU Crypto Users](https://www.coindesk.com/business/2026/06/29/mica-july-1-deadline-could-leave-10-million-crypto-users-searching-for-a-new-platform-in-the-eu) ⭐️ 8.0/10

The Markets in Crypto-Assets (MiCA) regulation's July 1, 2026 deadline could force approximately 10 million cryptocurrency users in the European Union to find new platforms, as many existing exchanges may fail to comply with the new rules. This deadline represents a major regulatory shift that could disrupt the EU crypto market, potentially reducing access for millions of users and reshaping the competitive landscape among exchanges. MiCA was adopted in April 2023 and has been fully applicable since December 2024, but a transitional period ends on July 1, 2026, after which all crypto-asset service providers must be fully authorized under MiCA.

rss · CoinDesk · Jun 29, 15:03

**Background**: MiCA is the first comprehensive EU regulatory framework for crypto-assets, covering issuers, exchanges, and custodians. It aims to protect investors and ensure market integrity while fostering innovation. The regulation applies in two phases, with the final phase requiring full compliance by July 1, 2026.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Markets_in_Crypto-Assets">Markets in Crypto-Assets - Wikipedia</a></li>
<li><a href="https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica">Markets in Crypto-Assets Regulation (MiCA)</a></li>
<li><a href="https://www.nortonrosefulbright.com/en/knowledge/publications/2cec201e/regulating-crypto-assets-in-europe-practical-guide-to-mica">Regulating crypto-assets in Europe: Practical guide to MiCA | Global law firm | Norton Rose Fulbright</a></li>

</ul>
</details>

**Tags**: `#crypto`, `#regulation`, `#EU`, `#MiCA`, `#finance`

---

<a id="item-6"></a>
## [OpenAI Chief Warns: Small Window for AGI Preparation](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&mid=2652710037&idx=2&sn=942dd7ab7358a3a8a5729c96860e9831) ⭐️ 6.0/10

OpenAI's Chief Research Officer, Mark Chen, stated that the window for humanity to prepare for artificial general intelligence (AGI) is small, and that scaling laws remain valid, with pre-training, data engineering, inference training, and longer task chains as the main path to AGI. This warning from a top OpenAI researcher underscores the accelerating pace of AI development and the urgent need for safety and governance measures, affecting policymakers, researchers, and the public. The article lacks technical depth and is considered clickbait, but Chen's remarks confirm OpenAI's continued belief in scaling laws and the importance of inference-time compute.

rss · 新智元 · Jun 30, 04:32

**Background**: Artificial general intelligence (AGI) is a hypothetical AI that matches or surpasses human capabilities across virtually all cognitive tasks. Many AI researchers and prediction markets estimate AGI could arrive within the next decade, with some timelines suggesting 2027-2030 as a possible window.

<details><summary>References</summary>
<ul>
<li><a href="https://eu.36kr.com/en/p/3875321045217288">AGI Countdown: OpenAI's Chief Research Officer Warns Humanity ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Artificial_general_intelligence">Artificial general intelligence - Wikipedia</a></li>
<li><a href="https://aimultiple.com/artificial-general-intelligence-singularity-timing">AGI /Singularity: 9,800 Predictions Analyzed</a></li>

</ul>
</details>

**Tags**: `#AGI`, `#OpenAI`, `#AI safety`

---

<a id="item-7"></a>
## [Private Key Compromises Cause 40% of $16B Crypto Hack Losses](https://www.coindesk.com/tech/2026/06/29/private-keys-not-smart-contracts-caused-40-of-crypto-s-usd16-billion-hack-losses-here-s-whats-being-done) ⭐️ 6.0/10

A new analysis reveals that 40% of the $16 billion in crypto hack losses are due to private key compromises, not smart contract vulnerabilities, prompting the industry to adopt new security measures like multi-party computation (MPC) and hardware security modules (HSMs). This finding shifts the security focus from smart contract audits to key management, which is critical for protecting user funds and restoring trust in the crypto ecosystem. Private key compromises often occur through phishing, malware, social engineering, or weak storage, and once compromised, attackers gain irreversible access to drain wallets and protocol treasuries.

rss · CoinDesk · Jun 29, 15:45

**Background**: In cryptocurrency, private keys are secret codes that allow users to sign transactions and prove ownership of their assets. Unlike smart contract vulnerabilities, which are code bugs, private key compromises directly target the user's control over their funds. The industry has historically focused on auditing smart contracts, but this data highlights the need for better key management practices.

<details><summary>References</summary>
<ul>
<li><a href="https://www.securview.com/ai-security-essentials/private-key-compromise">Private Key Compromise: Definition and Key Concepts</a></li>
<li><a href="https://www.guardrail.ai/common-attack-vectors/private-key-compromises">Guardrail – Protect Your Wallet from Private Key Compromises</a></li>
<li><a href="https://coinsprobe.com/zachxbt-flags-suspected-polymarket-exploit-as-658k-drained-from-uma-ctf-adapter/">Polymarket $520K Drain Was a Compromised Private Key — Not...</a></li>

</ul>
</details>

**Tags**: `#cryptocurrency`, `#security`, `#private keys`, `#hacks`

---

<a id="item-8"></a>
## [J.P. Morgan Expands Blockchain Settlement Network](https://www.coindesk.com/business/2026/06/29/j-p-morgan-broadens-blockchain-settlement-network-as-banks-modernize-cross-border-payments) ⭐️ 6.0/10

J.P. Morgan has expanded its Kinexys blockchain settlement network, which has processed over $4 trillion in transactions, to deepen its reach in the Asia-Pacific region for modernizing cross-border payments. This expansion signals growing adoption of blockchain in traditional banking, potentially reducing costs and settlement times for cross-border payments, which are typically slow and expensive. Kinexys is a permissioned blockchain platform that supports programmable payments, asset tokenization, and near-real-time settlement, and J.P. Morgan selected Base, an Ethereum layer-2 network, for scalable institutional applications.

rss · CoinDesk · Jun 29, 15:23

**Background**: Cross-border payments traditionally rely on a network of correspondent banks, leading to delays and high fees. Blockchain technology offers a more efficient alternative by enabling direct, near-instant settlement. J.P. Morgan's Kinexys is one of the leading bank-led blockchain initiatives, having already processed over $4 trillion in transactions.

<details><summary>References</summary>
<ul>
<li><a href="https://www.jpmorgan.com/kinexys/index">Kinexys: Enterprise Bank-Led Blockchain Solutions</a></li>
<li><a href="https://www.coindesk.com/business/2026/06/29/j-p-morgan-broadens-blockchain-settlement-network-as-banks-modernize-cross-border-payments">J . P . Morgan broadens Kinexys blockchain settlement network as...</a></li>
<li><a href="https://www.binance.com/en/square/post/32457142769777">JPMorgan Ignites a New Era Where... | Decilizer on Binance Square</a></li>

</ul>
</details>

**Tags**: `#blockchain`, `#finance`, `#cross-border payments`, `#J.P. Morgan`

---

<a id="item-9"></a>
## [BNY Mellon Adds USDC Stablecoin Services for Institutions](https://www.coindesk.com/business/2026/06/29/wall-street-s-bny-expands-stablecoin-services-for-institutions-starting-with-circle-s-usdc) ⭐️ 6.0/10

BNY Mellon has expanded its partnership with Circle to offer institutional clients the ability to custody, transfer, mint, and redeem USDC through its Digital Asset Custody platform. This move signals growing institutional adoption of stablecoins and bridges traditional finance with blockchain-based digital assets, potentially increasing liquidity and trust in regulated stablecoin services. BNY Mellon already serves as the primary custodian of USDC reserves; now it adds client-facing stablecoin capabilities, allowing institutions to mint and redeem USDC directly on its platform.

rss · CoinDesk · Jun 29, 14:46

**Background**: Stablecoins like USDC are cryptocurrencies designed to maintain a stable value, typically pegged 1:1 to a fiat currency like the US dollar. BNY Mellon is one of the world's largest custodian banks, and its entry into stablecoin services represents a significant step in integrating digital assets into mainstream finance.

<details><summary>References</summary>
<ul>
<li><a href="https://cryptobriefing.com/bny-mellon-usdc-digital-asset-custody/">BNY adds USDC as first stablecoin on its institutional custody platform</a></li>
<li><a href="https://cryptopotato.com/circles-usdc-becomes-first-stablecoin-supported-by-bny-mellon-for-institutional-clients/">Circle's USDC Becomes First Stablecoin Supported by BNY Mellon for Institutional Clients</a></li>
<li><a href="https://crypto.news/bny-unlocks-usdc-minting-and-redemption-for-clients/">BNY unlocks USDC minting and redemption for institutional clients</a></li>

</ul>
</details>

**Tags**: `#stablecoins`, `#institutional adoption`, `#crypto`, `#finance`

---

<a id="item-10"></a>
## [Breez SDK Enables Bitcoin-to-Stablecoin Payments Across 30+ Chains](https://cointelegraph.com/news/breez-bitcoin-wallets-send-usdc-usdt-without-holding-stablecoins?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) ⭐️ 6.0/10

Breez has launched a new SDK feature that allows developers to route payments from Bitcoin balances to recipients in USDC or USDT across more than 30 blockchain networks, without requiring users to hold stablecoins. This simplifies stablecoin payments for Bitcoin users, enabling them to send stablecoins without managing separate wallets or tokens, which could drive broader adoption of Bitcoin-based payment solutions. The feature is built on Spark, a native Bitcoin Layer 2 with instant settlement and multi-asset support. Over 75 apps, including Deblock, Cake Wallet, and Klever, have already integrated the Breez SDK.

rss · CoinTelegraph · Jun 29, 13:00

**Background**: Stablecoins like USDC and USDT are digital assets pegged to fiat currencies, commonly used for payments and remittances. However, users typically need to acquire and hold these tokens separately. Breez's SDK eliminates that requirement by automatically converting Bitcoin to stablecoins at the time of payment, leveraging its Lightning Network integration and cross-chain routing.

<details><summary>References</summary>
<ul>
<li><a href="https://cryptobriefing.com/breez-bitcoin-stablecoin-payments-30-blockchains/">Breez launches Bitcoin - to - stablecoin payments across 30 blockchains</a></li>
<li><a href="https://breez.technology/sdk/">Breez SDK | Add Bitcoin to Any App or Service</a></li>
<li><a href="https://www.cointrust.com/market-news/breez-enables-bitcoin-to-stablecoin-payments-across-30-blockchains">Breez Enables Bitcoin-to-Stablecoin Payments Across 30 Blockchains</a></li>

</ul>
</details>

**Tags**: `#Bitcoin`, `#stablecoins`, `#payments`, `#SDK`, `#blockchain`

---

<a id="item-11"></a>
## [Vitalik: Obfuscation Could Enable Private Onchain Voting](https://cointelegraph.com/news/vitalik-buterin-private-onchain-voting-obfuscation?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) ⭐️ 6.0/10

Vitalik Buterin stated that indistinguishability obfuscation (iO) could eventually enable private, collusion-resistant onchain voting without the need for trusted committees, though the technology remains impractical for now. If realized, iO-based voting would solve the long-standing tension between transparency and privacy in blockchain governance, allowing votes to be verified without revealing individual choices. This could strengthen decentralized decision-making in DAOs and other crypto communities. Indistinguishability obfuscation is a cryptographic primitive that hides a program's implementation while preserving its functionality, but current candidates are extremely impractical—for example, obfuscating a simple 32-bit AND function produces a program nearly 12 gigabytes in size.

rss · CoinTelegraph · Jun 29, 10:53

**Background**: Onchain voting is a core feature of many decentralized autonomous organizations (DAOs), but it typically exposes how each participant voted, enabling bribery or coercion. Indistinguishability obfuscation, first proposed in 2001, is a powerful but still-theoretical tool that could hide voting choices while allowing public verification of results. However, known constructions are far from practical deployment due to massive size and computational overhead.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Indistinguishability_obfuscation">Indistinguishability obfuscation</a></li>
<li><a href="https://cointelegraph.com/news/vitalik-buterin-private-onchain-voting-obfuscation">Vitalik Details Cryptographic Path To Private Onchain Voting</a></li>

</ul>
</details>

**Tags**: `#cryptography`, `#voting`, `#privacy`, `#blockchain`

---