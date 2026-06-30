---
layout: default
title: "Horizon Summary: 2026-06-30 (EN)"
date: 2026-06-30
lang: en
---

> From 130 items, 12 important content pieces were selected

---

1. [Supreme Court: Geofence Warrants Need Constitutional Protections](#item-1) ⭐️ 9.0/10
2. [Google's AI Peer-Reviewer Handles ~10K Papers, Catches 34% More Errors](#item-2) ⭐️ 9.0/10
3. [vLLM v0.24.0 Adds MiniMax-M3, DeepSeek-V4 Optimizations](#item-3) ⭐️ 8.0/10
4. [Ornith-1.0: Open-Weight Self-Scaffolding LLMs for Agentic Coding](#item-4) ⭐️ 8.0/10
5. [OpenAI's Chief Research Officer Warns AGI Window Is Small](#item-5) ⭐️ 6.0/10
6. [Private keys cause 40% of $16B crypto hack losses](#item-6) ⭐️ 6.0/10
7. [J.P. Morgan Expands Blockchain Settlement Network](#item-7) ⭐️ 6.0/10
8. [MiCA Deadline May Displace 10 Million EU Crypto Users](#item-8) ⭐️ 6.0/10
9. [BNY Mellon Adds USDC Minting and Redemption for Institutions](#item-9) ⭐️ 6.0/10
10. [UK Sets 2027 FCA Authorization Deadline for Crypto Firms](#item-10) ⭐️ 6.0/10
11. [Breez SDK Enables Bitcoin-to-Stablecoin Payments Across 30+ Chains](#item-11) ⭐️ 6.0/10
12. [Vitalik: Obfuscation could enable private onchain voting](#item-12) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Supreme Court: Geofence Warrants Need Constitutional Protections](https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision) ⭐️ 9.0/10

The US Supreme Court ruled 6-3 that geofence warrants require constitutional protections under the Fourth Amendment, limiting warrantless digital location tracking by law enforcement. This landmark decision strengthens digital privacy rights by requiring law enforcement to obtain a warrant based on probable cause before accessing location data from tech companies like Google, affecting millions of smartphone users. The case involved a bank robbery where police used a geofence warrant to obtain location data from Google, identifying 19 devices near the crime scene; the Court held that such searches are subject to the Fourth Amendment's warrant requirement.

hackernews · cdrnsf · Jun 29, 15:54 · [Discussion](https://news.ycombinator.com/item?id=48720924)

**Background**: A geofence warrant, also known as a reverse location warrant, allows law enforcement to request location data for all devices within a specific geographic area during a certain time period. The Fourth Amendment protects against unreasonable searches and seizures, and the Supreme Court has previously extended its protections to digital location data in cases like Riley v. California and Carpenter v. United States.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Geofence_warrant">Geofence warrant - Wikipedia</a></li>
<li><a href="https://www.congress.gov/crs-product/LSB11274">Geofence Warrants and the Fourth Amendment | Congress.gov | Library of Congress</a></li>
<li><a href="https://www.nacdl.org/Content/Geofence-Warrants">NACDL - Geofence Warrants</a></li>

</ul>
</details>

**Discussion**: Commenters expressed support for the ruling, with some noting the court's use of factual sources in the opinion. Others discussed implications for other surveillance technologies like Flock cameras, and debated the dissenting justices' positions.

**Tags**: `#privacy`, `#supreme court`, `#geofence warrants`, `#digital surveillance`, `#law`

---

<a id="item-2"></a>
## [Google's AI Peer-Reviewer Handles ~10K Papers, Catches 34% More Errors](https://www.reddit.com/r/MachineLearning/comments/1uio9rb/googles_agentic_peerreviewer_handled_10k_papers/) ⭐️ 9.0/10

Google deployed an agentic AI peer-reviewer at ICML and STOC that processed approximately 10,000 papers with a 30-minute turnaround, and a formal research paper shows it catches 34% more mathematical errors than zero-shot prompting. This sets a precedent for AI-automated scientific review at conference scale, potentially transforming the peer-review process by improving error detection and reducing reviewer workload. The system uses an agentic approach, meaning it can take actions like searching for references or performing calculations, rather than just generating text. It was tested on real papers from top machine learning and theory conferences.

reddit · r/MachineLearning · /u/Justgototheeffinmoon · Jun 29, 10:05

**Background**: Peer review is the process where experts evaluate research papers before publication to ensure quality and correctness. Zero-shot prompting asks an AI to perform a task without providing examples, which is a common baseline for AI performance. Agentic AI systems can interact with tools and environments, enabling more complex tasks like verifying mathematical proofs.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zero-shot_prompting">Zero-shot prompting</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion is generally positive, with users impressed by the scale and error-detection improvement. Some express concerns about AI replacing human reviewers, while others see it as a useful assistant. A few commenters question the generalizability to other fields beyond CS.

**Tags**: `#AI`, `#peer review`, `#machine learning`, `#scientific publishing`, `#Google`

---

<a id="item-3"></a>
## [vLLM v0.24.0 Adds MiniMax-M3, DeepSeek-V4 Optimizations](https://github.com/vllm-project/vllm/releases/tag/v0.24.0) ⭐️ 8.0/10

vLLM v0.24.0, released with 571 commits from 256 contributors, adds support for the MiniMax-M3 model and delivers major optimizations for DeepSeek-V4, including a FlashInfer sparse index cache and prefill chunk-planning improvements. This release significantly improves inference performance for two cutting-edge models, enabling faster and more efficient deployment of large language models in production environments. MiniMax-M3 support includes BF16/FP8 indexer via MSA, MXFP4 support, and FP8 sparse GQA; DeepSeek-V4 gains a FlashInfer sparse index cache (2–4% TTFT improvement) and prefill chunk-planning optimization (4% E2E throughput gain).

github · khluu · Jun 29, 19:41

**Background**: vLLM is a high-throughput, memory-efficient inference engine for large language models. MiniMax-M3 uses a novel sparse attention mechanism that requires specialized kernel support, while DeepSeek-V4 employs a complex multi-pool KV cache architecture that benefits from optimized sparse indexing.

<details><summary>References</summary>
<ul>
<li><a href="https://discuss.vllm.ai/t/minimax-m3-support/2689">Minimax m3 support - Model Support - vLLM Forums</a></li>
<li><a href="https://www.lmsys.org/blog/2026-04-25-deepseek-v4/">DeepSeek-V4 on Day 0: From Fast Inference to Verified RL with SGLang and Miles - LMSYS Org</a></li>

</ul>
</details>

**Discussion**: The vLLM community has been actively discussing MiniMax-M3 support, noting that M3 moves away from MLA-style latent compression to full-attention GQA, which required new kernel implementations. The release was well-received for its performance gains and broad model support.

**Tags**: `#vLLM`, `#LLM inference`, `#DeepSeek`, `#MiniMax`, `#performance optimization`

---

<a id="item-4"></a>
## [Ornith-1.0: Open-Weight Self-Scaffolding LLMs for Agentic Coding](https://simonwillison.net/2026/Jun/29/ornith/#atom-everything) ⭐️ 8.0/10

DeepReinforce released Ornith-1.0, a family of MIT-licensed open-weight LLMs for agentic coding, with variants from 9B to 397B parameters, built on Gemma 4 and Qwen 3.5 base models. It achieves state-of-the-art performance among open-source models of comparable size on coding benchmarks. Ornith-1.0 introduces a novel self-scaffolding training framework where the model learns to generate both solution rollouts and the scaffolds that drive them, potentially reducing the need for external orchestration in agentic coding tasks. Its MIT license and strong performance make it highly accessible for developers and researchers. The model family includes 9B Dense, 31B Dense, 35B MoE, and 397B MoE variants, all MIT-licensed. The underlying base models (Gemma 4 and Qwen 3.5) are Apache 2.0 licensed, ensuring license compatibility. Early user reports indicate faster inference than comparable models due to shorter chain-of-thought.

rss · Simon Willison · Jun 29, 16:17

**Background**: Agentic coding refers to AI agents that autonomously plan, write, test, and modify code with minimal human intervention. Traditional LLM-based coding assistants require external scaffolding (e.g., tool-use frameworks) to perform multi-step tasks. Ornith-1.0's self-scaffolding approach aims to internalize this capability, allowing the model to generate its own execution plan and tool calls.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/29/ornith/">Ornith-1.0: Self - Scaffolding LLMs for Agentic Coding</a></li>
<li><a href="https://deep-reinforce.com/ornith_1_0.html">Ornith - 1 . 0 : Self-Scaffolding LLMs... | DeepReinforce Blog | Jun. 2026</a></li>
<li><a href="https://ornith.site/">Ornith 1 . 0 — Open-Source Agentic Coding Models</a></li>

</ul>
</details>

**Discussion**: Community sentiment is mixed: some users report strong coding performance and faster inference, while others note poor performance in chat without tools and a tendency to hallucinate. Some commenters question whether Ornith-1.0 is merely a fine-tuned version of Qwen or Gemma 4, and there is curiosity about the DeepReinforce team's background.

**Tags**: `#LLM`, `#open-source`, `#coding`, `#AI`, `#machine learning`

---

<a id="item-5"></a>
## [OpenAI's Chief Research Officer Warns AGI Window Is Small](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&mid=2652710037&idx=2&sn=942dd7ab7358a3a8a5729c96860e9831) ⭐️ 6.0/10

OpenAI's Chief Research Officer, Mark Chen, stated that the window for humanity to prepare for artificial general intelligence (AGI) is very small, implying that AGI may arrive sooner than many expect. This warning from a key OpenAI figure underscores the urgency of AI safety research and policy development, as AGI could have transformative impacts on society and the global economy. The statement was made without specifying a precise timeline, but it aligns with other predictions that AGI could emerge within the next few years. The comment reflects ongoing internal concerns at OpenAI about the pace of progress.

rss · 新智元 · Jun 30, 04:32

**Background**: Artificial general intelligence (AGI) is a hypothetical AI system that can perform any intellectual task that a human can. Unlike narrow AI, which excels at specific tasks, AGI would possess general cognitive abilities. The timeline for AGI is highly debated, with some experts predicting it within a decade and others arguing it is far off. AI safety is a field focused on ensuring that advanced AI systems are aligned with human values and do not cause harm.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Artificial_general_intelligence">Artificial general intelligence - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_safety">AI safety - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AGI`, `#OpenAI`, `#AI safety`, `#timeline`

---

<a id="item-6"></a>
## [Private keys cause 40% of $16B crypto hack losses](https://www.coindesk.com/tech/2026/06/29/private-keys-not-smart-contracts-caused-40-of-crypto-s-usd16-billion-hack-losses-here-s-whats-being-done) ⭐️ 6.0/10

A recent report reveals that 40% of the $16 billion in crypto hack losses are due to private key compromises, not smart contract vulnerabilities, prompting the industry to develop new mitigation strategies. This finding shifts the security focus from smart contract audits to private key management, affecting how exchanges, wallets, and DeFi protocols protect user assets. The report estimates that about 49.6% of realized crypto losses since 2022 come from private key compromise, phishing, and social engineering, not contract logic failures.

rss · CoinDesk · Jun 29, 15:45

**Background**: Private keys are cryptographic secrets that grant control over crypto assets; if compromised, attackers can steal funds without exploiting smart contract bugs. Historically, the crypto industry has focused heavily on auditing smart contracts, but this data highlights that key management is a larger risk.

<details><summary>References</summary>
<ul>
<li><a href="https://www.coindesk.com/tech/2026/06/29/private-keys-not-smart-contracts-caused-40-of-crypto-s-usd16-billion-hack-losses-here-s-whats-being-done">Private keys, not smart contracts, caused 40% of crypto's $16 billion ...</a></li>
<li><a href="https://cryptodaily.co.uk/2026/06/crypto-audit-gap-private-keys-phishing">The Crypto Audit Gap: Keys , Phishing, and Missed Risks</a></li>
<li><a href="https://blog.trailofbits.com/2025/06/25/maturing-your-smart-contracts-beyond-private-key-risk/">Maturing your smart contracts beyond private key risk - The Trail of Bits Blog</a></li>

</ul>
</details>

**Tags**: `#cryptocurrency`, `#security`, `#private keys`, `#hacks`

---

<a id="item-7"></a>
## [J.P. Morgan Expands Blockchain Settlement Network](https://www.coindesk.com/business/2026/06/29/j-p-morgan-broadens-blockchain-settlement-network-as-banks-modernize-cross-border-payments) ⭐️ 6.0/10

J.P. Morgan has broadened its Kinexys blockchain settlement network, enabling banks to modernize cross-border payments using a permissioned blockchain for near-real-time settlement. This expansion signals growing institutional adoption of blockchain for core banking operations, potentially reducing settlement times from days to minutes and lowering costs for cross-border transactions. The network uses a permissioned blockchain operated by J.P. Morgan, and its JPM Coin (JPMD) is being integrated with the Canton Network to enable public blockchain interoperability.

rss · CoinDesk · Jun 29, 15:23

**Background**: Traditional cross-border payments rely on correspondent banking networks, which can take days and incur high fees. Blockchain-based solutions offer faster, cheaper, and 24/7 settlement by eliminating intermediaries. J.P. Morgan's Kinexys platform is a bank-led blockchain for programmable payments and asset tokenization.

<details><summary>References</summary>
<ul>
<li><a href="https://www.coindesk.com/business/2026/06/29/j-p-morgan-broadens-blockchain-settlement-network-as-banks-modernize-cross-border-payments">J.P. Morgan broadens Kinexys blockchain settlement network as banks modernize cross-border payments</a></li>
<li><a href="https://www.jpmorgan.com/kinexys/index">Kinexys: Enterprise Bank-Led Blockchain Solutions</a></li>
<li><a href="https://blog.digitalasset.com/news/digital-asset-and-kinexys-by-j.p.-morgan-bring-usd-jpm-coin-jpmd-natively-to-canton">Digital Asset and Kinexys by J.P. Morgan announce intention to bring USD JPM Coin (JPMD) natively to the Canton Network</a></li>

</ul>
</details>

**Tags**: `#blockchain`, `#banking`, `#cross-border payments`, `#J.P. Morgan`

---

<a id="item-8"></a>
## [MiCA Deadline May Displace 10 Million EU Crypto Users](https://www.coindesk.com/business/2026/06/29/mica-july-1-deadline-could-leave-10-million-crypto-users-searching-for-a-new-platform-in-the-eu) ⭐️ 6.0/10

The European Union's Markets in Crypto-Assets (MiCA) regulation faces a key deadline on July 1, 2026, which could force approximately 10 million crypto users in the EU to find new platforms if existing providers fail to comply with the new rules. This deadline represents a major regulatory shift that could disrupt access to crypto services for millions of EU residents, potentially driving users to unregulated platforms or reducing market participation, while also setting a precedent for global crypto regulation. The MiCA regulation, fully adopted in 2024, requires all crypto-asset service providers in the EU to obtain authorization and comply with strict rules on transparency, consumer protection, and anti-money laundering. Non-compliant platforms must cease operations by July 1, 2026.

rss · CoinDesk · Jun 29, 15:03

**Background**: MiCA is the world's first comprehensive regulatory framework for digital assets, designed to harmonize crypto rules across EU member states. It covers issuers of crypto-assets, service providers, and stablecoins, aiming to protect investors and ensure market integrity. The July 1 deadline is a transitional period end date for existing crypto businesses to become fully compliant.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Markets_in_Crypto-Assets">Markets in Crypto -Assets - Wikipedia</a></li>
<li><a href="https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica">Markets in Crypto -Assets Regulation ( MiCA )</a></li>
<li><a href="https://ondato.com/blog/mica-regulation/">MiCA Regulation and its Impact on the Crypto Market | Ondato</a></li>

</ul>
</details>

**Tags**: `#crypto`, `#regulation`, `#EU`, `#MiCA`

---

<a id="item-9"></a>
## [BNY Mellon Adds USDC Minting and Redemption for Institutions](https://www.coindesk.com/business/2026/06/29/wall-street-s-bny-expands-stablecoin-services-for-institutions-starting-with-circle-s-usdc) ⭐️ 6.0/10

BNY Mellon has expanded its Digital Asset Custody platform to support Circle's USDC, enabling institutional clients to mint, redeem, store, and transfer the stablecoin directly through the bank. This marks the first stablecoin integration on BNY's institutional custody offering. This move signals growing institutional adoption of stablecoins, bridging traditional finance with digital assets. By offering USDC services, BNY Mellon provides a regulated gateway for institutions to access stablecoin liquidity and settlement, potentially accelerating mainstream crypto integration. BNY Mellon already served as the primary custodian of USDC reserves; this expansion adds client-facing minting and redemption capabilities. USDC is the first stablecoin available on BNY's Digital Asset Custody platform, which launched in October 2022 for Bitcoin and Ethereum.

rss · CoinDesk · Jun 29, 14:46

**Background**: Stablecoins like USDC are cryptocurrencies pegged to a stable asset, typically the US dollar, enabling price stability for transactions and settlements. BNY Mellon's Digital Asset Custody platform allows institutional investors to hold digital assets alongside traditional securities in a regulated environment. This integration deepens BNY's partnership with Circle, the issuer of USDC.

<details><summary>References</summary>
<ul>
<li><a href="https://crypto.news/bny-unlocks-usdc-minting-and-redemption-for-clients/">BNY unlocks USDC minting and redemption for institutional clients</a></li>
<li><a href="https://cryptobriefing.com/bny-mellon-usdc-digital-asset-custody/">BNY Mellon integrates USDC as first stablecoin on Digital Asset...</a></li>
<li><a href="https://tokenmetrics.com/usdc/news/bny-usdc-minting-institutional-custody/">BNY Adds USDC Minting To Institutional Custody Platform</a></li>

</ul>
</details>

**Tags**: `#stablecoins`, `#institutional finance`, `#crypto`, `#BNY Mellon`

---

<a id="item-10"></a>
## [UK Sets 2027 FCA Authorization Deadline for Crypto Firms](https://cointelegraph.com/news/uk-crypto-rules-2027-fca-authorization-deadline?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) ⭐️ 6.0/10

The UK's Financial Conduct Authority (FCA) has published its final crypto regulatory framework, requiring all crypto firms to obtain FCA authorization by February 2027. This regulation brings crypto firms under the same oversight as traditional financial institutions, enhancing consumer protection and market integrity, and positions the UK as a leading crypto hub. Firms currently registered under the Money Laundering Regulations must also apply for full authorization. The new regime is expected to come into force on October 25, 2027.

rss · CoinTelegraph · Jun 29, 23:01

**Background**: The UK has been developing a comprehensive crypto regulatory framework to align digital assets with traditional finance. The FCA is the financial regulator responsible for authorizing and supervising firms. This move aims to provide clarity and legal certainty for crypto businesses operating in the UK.

<details><summary>References</summary>
<ul>
<li><a href="https://www.grantthornton.co.uk/insights/crypto-firms--a-guide-to-fca-authorisation/">Crypto firms – a guide to FCA authorisation | Grant Thornton</a></li>
<li><a href="https://www.fca.org.uk/firms/new-regime-cryptoasset-regulation/authorisation-supervision-enforcement">Cryptoasset firms: Authorisation, supervision and enforcement | FCA</a></li>
<li><a href="https://www.edgen.tech/news/crypto/uk-targets-crypto-hub-status-with-2027-regulatory-framework">UK Targets Crypto Hub Status With 2027 Regulatory Framework</a></li>

</ul>
</details>

**Tags**: `#cryptocurrency`, `#regulation`, `#UK`, `#FCA`

---

<a id="item-11"></a>
## [Breez SDK Enables Bitcoin-to-Stablecoin Payments Across 30+ Chains](https://cointelegraph.com/news/breez-bitcoin-wallets-send-usdc-usdt-without-holding-stablecoins?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) ⭐️ 6.0/10

Breez has launched a new SDK feature that allows developers to route Bitcoin payments to recipients in USDC and USDT across more than 30 blockchains, without requiring users to hold stablecoins. This innovation bridges Bitcoin and stablecoin ecosystems, enabling Bitcoin holders to make payments in widely used stablecoins without converting their holdings, potentially expanding Bitcoin's utility in everyday transactions and DeFi. The feature is part of the Breez SDK, built on Spark, a native Bitcoin Layer 2 with instant settlement and multi-asset support. It supports over 30 blockchains, including major networks like Ethereum, Solana, and Tron.

rss · CoinTelegraph · Jun 29, 13:00

**Background**: Stablecoins like USDC and USDT are digital assets pegged to fiat currencies, commonly used for payments and DeFi. Bitcoin, while valuable, is less practical for everyday transactions due to volatility and slower settlement. Breez SDK is a non-custodial toolkit that lets developers integrate Bitcoin payments into apps. This new feature uses cross-chain routing to convert Bitcoin value into stablecoins at the recipient's end, simplifying the payment experience.

<details><summary>References</summary>
<ul>
<li><a href="https://cryptobriefing.com/breez-bitcoin-stablecoin-payments-30-blockchains/">Breez launches Bitcoin - to - stablecoin payments across 30 blockchains</a></li>
<li><a href="https://breez.technology/sdk/">Breez SDK | Add Bitcoin to Any App or Service</a></li>
<li><a href="https://coincentral.com/breez-launches-bitcoin-to-stablecoin-payments-without-holding-usdc-or-usdt/">Breez Launches Bitcoin - to - Stablecoin Payments Without Holding...</a></li>

</ul>
</details>

**Tags**: `#Bitcoin`, `#Stablecoins`, `#Payments`, `#SDK`, `#Blockchain`

---

<a id="item-12"></a>
## [Vitalik: Obfuscation could enable private onchain voting](https://cointelegraph.com/news/vitalik-buterin-private-onchain-voting-obfuscation?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) ⭐️ 6.0/10

Ethereum co-founder Vitalik Buterin suggested that indistinguishability obfuscation (iO) could eventually enable private, collusion-resistant onchain voting without trusted committees, though the technology remains impractical today. If realized, iO-based voting could transform governance in DAOs and DeFi protocols by ensuring voter privacy and preventing collusion, addressing key limitations of current onchain voting systems. Indistinguishability obfuscation hides a program's implementation while allowing it to be run, but current candidates are extremely impractical—for example, obfuscating a simple 32-bit AND function produces a program nearly 12 gigabytes in size.

rss · CoinTelegraph · Jun 29, 10:53

**Background**: Indistinguishability obfuscation (iO) is a cryptographic primitive that makes two programs computing the same function indistinguishable, effectively hiding their internal logic. It is considered a 'best-possible' obfuscation and can theoretically construct many other cryptographic primitives. However, known iO constructions rely on unproven assumptions and are far from practical deployment.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Indistinguishability_obfuscation">Indistinguishability obfuscation</a></li>
<li><a href="https://coinfractal.com/vitalik-buterin-indistinguishability-obfuscation-private-onchain-voting/">Vitalik: Obfuscation Could Power Private Onchain Voting</a></li>
<li><a href="https://coinmarketcap.com/academy/article/vitalik-buterin-obfuscation-private-onchain-voting">Vitalik Buterin Says Obfuscation Could Enable Private On - Chain Voting</a></li>

</ul>
</details>

**Tags**: `#cryptography`, `#blockchain`, `#voting`, `#privacy`

---