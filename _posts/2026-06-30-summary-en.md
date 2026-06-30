---
layout: default
title: "Horizon Summary: 2026-06-30 (EN)"
date: 2026-06-30
lang: en
---

> From 131 items, 9 important content pieces were selected

---

1. [Supreme Court Rules Geofence Warrants Need Constitutional Protections](#item-1) ⭐️ 9.0/10
2. [vLLM v0.24.0 Adds MiniMax-M3 and DeepSeek-V4 Optimizations](#item-2) ⭐️ 8.0/10
3. [Proposed .self TLD aims to boost self-hosting](#item-3) ⭐️ 8.0/10
4. [BNY Mellon Expands Stablecoin Services with USDC](#item-4) ⭐️ 7.0/10
5. [UK to Lower Stablecoin Capital Buffers, Undercutting EU's MiCA](#item-5) ⭐️ 6.0/10
6. [Private Keys Cause 40% of $16B Crypto Hack Losses](#item-6) ⭐️ 6.0/10
7. [MiCA Deadline May Force 10M EU Crypto Users Off Platforms](#item-7) ⭐️ 6.0/10
8. [Breez SDK Enables Bitcoin-to-Stablecoin Payments Across 30+ Chains](#item-8) ⭐️ 6.0/10
9. [Vitalik Buterin: Obfuscation Could Enable Private Onchain Voting](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Supreme Court Rules Geofence Warrants Need Constitutional Protections](https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision) ⭐️ 9.0/10

The US Supreme Court ruled that geofence warrants, which allow law enforcement to obtain location data of all devices within a specific area, require constitutional protections under the Fourth Amendment. This landmark decision, issued on June 29, 2026, sets a precedent for digital privacy in the context of mass surveillance. This ruling significantly limits law enforcement's ability to conduct warrantless digital dragnets, protecting the privacy of millions of individuals whose location data is collected by tech companies like Google. It reinforces the Fourth Amendment's application to modern surveillance technologies, potentially affecting other data collection practices such as automated license plate readers. The case involved a bank robbery where Google provided location data of 19 devices within 150 meters of the bank. The Court held that accessing such comprehensive location history constitutes a search under the Fourth Amendment, requiring a warrant based on probable cause.

hackernews · cdrnsf · Jun 29, 15:54 · [Discussion](https://news.ycombinator.com/item?id=48720924)

**Background**: Geofence warrants, also known as reverse location warrants, allow law enforcement to request location data from tech companies for all devices within a virtual boundary. The Fourth Amendment protects against unreasonable searches and seizures, and the Supreme Court has previously ruled in cases like Carpenter v. United States that accessing historical cell phone location data requires a warrant. This decision extends that reasoning to geofence warrants.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Geofence_warrant">Geofence warrant - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters expressed strong support for the ruling, with some drawing historical parallels to the identification of Paula Broadwell in the Petraeus affair as an example of how location data can be used without a warrant. Others raised concerns about implications for other surveillance technologies like Flock cameras, and noted that Justices Alito and Thomas dissented, with Barrett joining the minority.

**Tags**: `#privacy`, `#supreme court`, `#geofence warrants`, `#digital rights`, `#law enforcement`

---

<a id="item-2"></a>
## [vLLM v0.24.0 Adds MiniMax-M3 and DeepSeek-V4 Optimizations](https://github.com/vllm-project/vllm/releases/tag/v0.24.0) ⭐️ 8.0/10

vLLM v0.24.0, released with 571 commits from 256 contributors, adds support for the MiniMax-M3 model and delivers major performance optimizations for DeepSeek-V4, including a FlashInfer sparse index cache and cluster-cooperative topK kernel. This release significantly expands vLLM's model ecosystem and inference efficiency, benefiting users of cutting-edge models like MiniMax-M3 and DeepSeek-V4 with faster throughput and lower latency. Notable technical improvements include a new streaming parser engine for unified tool-call/reasoning parsing, Model Runner V2 now supporting quantized models by default, and integration of DeepEP v2 for expert parallelism.

github · khluu · Jun 29, 19:41

**Background**: vLLM is a high-performance, memory-efficient inference engine for large language models (LLMs). It optimizes key operations like KV-cache management and batching to reduce latency and memory usage. DeepSeek-V4 is a Mixture-of-Experts (MoE) model with 1.6 trillion total parameters, while MiniMax-M3 is a multimodal MoE model with a 1M context window.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/docs/inference-endpoints/engines/vllm">vLLM · Hugging Face</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro">deepseek-ai/DeepSeek-V4-Pro - Hugging Face</a></li>
<li><a href="https://huggingface.co/MiniMaxAI/MiniMax-M3">MiniMaxAI/ MiniMax - M 3 · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#DeepSeek-V4`, `#MiniMax-M3`, `#performance optimization`

---

<a id="item-3"></a>
## [Proposed .self TLD aims to boost self-hosting](https://hccf.onmy.cloud/2026/06/21/reclaiming-our-digital-selves-hccfs-vision-for-a-human-centered-top-level-domain/) ⭐️ 8.0/10

A proposal for a new .self top-level domain (TLD) has been published, designed to support self-hosting by offering free subdomains to individuals. The initiative, led by HCCF, envisions a human-centered domain namespace with strict anti-abuse policies. If implemented, .self could lower barriers to self-hosting and foster a decentralized internet, but its success hinges on solving abuse prevention and funding challenges. The proposal has sparked community debate about feasibility and reputation management. The proposal includes a 'one free domain per person' model, but critics note that enforcing this without identity verification is difficult. Abuse prevention mechanisms, such as post-facto domain revocation and challenge systems for inactive domains, are being discussed.

hackernews · HumanCCF · Jun 29, 19:49 · [Discussion](https://news.ycombinator.com/item?id=48724230)

**Background**: A top-level domain (TLD) is the last segment of a domain name, such as .com or .org. Self-hosting refers to individuals running their own servers for websites, email, or other services, rather than relying on third-party providers. The .self TLD aims to create a dedicated namespace for self-hosted services, potentially improving discoverability and trust.

<details><summary>References</summary>
<ul>
<li><a href="https://tldz.com/2026-gtld-guide-how-to-get-your-own-top-level-domain/">2026 gTLD Guide: How to Get Your Own Top-Level Domain</a></li>
<li><a href="https://www.hawkdive.com/apple-self-tld-self-hosting-troubleshooting/">Apple Devices and the New .self TLD: Self-Hosting Issues Fixed</a></li>

</ul>
</details>

**Discussion**: Community comments highlight concerns about abuse and reputation, drawing parallels to the .tk free TLD which became overrun with scammers. Some suggest using reputation systems and challenge mechanisms to mitigate squatting, while others question the financial sustainability of a free TLD.

**Tags**: `#DNS`, `#self-hosting`, `#TLD`, `#decentralization`, `#community`

---

<a id="item-4"></a>
## [BNY Mellon Expands Stablecoin Services with USDC](https://www.coindesk.com/business/2026/06/29/wall-street-s-bny-expands-stablecoin-services-for-institutions-starting-with-circle-s-usdc) ⭐️ 7.0/10

BNY Mellon has upgraded its Digital Asset Custody platform to allow institutional clients to mint, store, transfer, and redeem Circle's USDC stablecoin directly within the regulated banking environment. This move signals growing institutional adoption of stablecoins and bridges traditional finance with digital assets, potentially accelerating mainstream use of USDC for payments and settlements. The service includes minting USDC by depositing dollars, custody, transfers, and redemption back to fiat, all within BNY's existing regulated custody infrastructure, deepening BNY's partnership with Circle.

rss · CoinDesk · Jun 29, 14:46

**Background**: USDC is a dollar-pegged stablecoin issued by Circle, backed 1:1 by reserves and redeemable on demand. BNY Mellon, a major Wall Street custodian bank, already served as the primary custodian of USDC reserves before expanding into minting and redemption services for clients.

<details><summary>References</summary>
<ul>
<li><a href="https://finance.biggo.com/news/0ba2d465-1f22-4869-9395-079606d20a8e">BNY Mellon Lets Institutional Clients Mint and Redeem USDC, Deepening Stablecoin Integration — BigGo Finance</a></li>
<li><a href="https://cointelegraph.com/news/bny-adds-usdc-minting-and-redemption-to-institutional-custody-platform">BNY adds USDC minting and redemption to institutional custody ...</a></li>
<li><a href="https://www.bny.com/corporate/global/en/solutions/platforms/digital-assets/digital-assets-custody.html">Secure Digital Asset Custody for Institutional Investors</a></li>

</ul>
</details>

**Tags**: `#stablecoins`, `#institutional adoption`, `#crypto`, `#finance`, `#BNY Mellon`

---

<a id="item-5"></a>
## [UK to Lower Stablecoin Capital Buffers, Undercutting EU's MiCA](https://www.coindesk.com/policy/2026/06/30/uk-to-lower-stablecoin-capital-buffers-undercutting-eu-s-mica-requirements) ⭐️ 6.0/10

The UK's Financial Conduct Authority (FCA) has finalized crypto rules that lower the required capital buffer for stablecoin issuers from 2% to 1% of the total value of stablecoins issued, diverging from the EU's stricter MiCA regulation. This move makes the UK a more attractive jurisdiction for stablecoin issuers compared to the EU, potentially shifting the center of stablecoin activity and influencing global regulatory standards. The FCA set the authorization deadline for crypto firms for February 2027, and the lower capital buffer applies to stablecoin issuers under the new framework.

rss · CoinDesk · Jun 30, 10:08

**Background**: Stablecoins are cryptocurrencies designed to maintain a stable value, often pegged to a fiat currency like the US dollar. Capital buffers are funds that issuers must hold to cover potential losses and protect users. The EU's Markets in Crypto-Assets (MiCA) regulation, fully applicable since December 2024, requires a 2% capital buffer for significant stablecoins. The UK's decision to lower this requirement represents a regulatory divergence aimed at fostering innovation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.electronicpaymentsinternational.com/news/uk-fca-lowers-planned-stablecoin-capital-buffer/">UK FCA lowers planned stablecoin capital buffer in final crypto rules</a></li>
<li><a href="https://en.wikipedia.org/wiki/Markets_in_Crypto-Assets">Markets in Crypto-Assets - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Stablecoin">Stablecoin - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#crypto regulation`, `#stablecoins`, `#UK policy`, `#MiCA`

---

<a id="item-6"></a>
## [Private Keys Cause 40% of $16B Crypto Hack Losses](https://www.coindesk.com/tech/2026/06/29/private-keys-not-smart-contracts-caused-40-of-crypto-s-usd16-billion-hack-losses-here-s-whats-being-done) ⭐️ 6.0/10

A new report reveals that 40% of the $16 billion in total crypto hack losses are due to private key compromises, not smart contract vulnerabilities, prompting industry efforts to improve key management. This finding shifts the security focus from smart contract audits to private key protection, highlighting a critical vulnerability that affects both individual users and protocols. Attackers steal private keys through phishing, malware, social engineering, and weak storage; once compromised, they can instantly drain wallets and protocol treasuries.

rss · CoinDesk · Jun 29, 15:45

**Background**: Private keys are cryptographic codes that grant ownership and control of cryptocurrency assets, similar to passwords. Smart contracts are self-executing code on blockchain, and their vulnerabilities have been a major security concern. This report highlights that key management is equally, if not more, critical.

<details><summary>References</summary>
<ul>
<li><a href="https://www.coindesk.com/tech/2026/06/29/private-keys-not-smart-contracts-caused-40-of-crypto-s-usd16-billion-hack-losses-here-s-whats-being-done">Private keys, not smart contracts, caused 40% of crypto's $16 ...</a></li>
<li><a href="https://www.guardrail.ai/common-attack-vectors/private-key-compromises">Guardrail – Protect Your Wallet from Private Key Compromises</a></li>
<li><a href="https://www.ccn.com/education/crypto/private-key-security-vs-smart-contract-audits/">Private Key Security vs. Smart Contract Audits: What Matters ...</a></li>

</ul>
</details>

**Tags**: `#cryptocurrency`, `#security`, `#private keys`, `#hacks`

---

<a id="item-7"></a>
## [MiCA Deadline May Force 10M EU Crypto Users Off Platforms](https://www.coindesk.com/business/2026/06/29/mica-july-1-deadline-could-leave-10-million-crypto-users-searching-for-a-new-platform-in-the-eu) ⭐️ 6.0/10

The European Securities and Markets Authority (ESMA) has warned that after the MiCA regulation deadline on July 1, 2026, EU crypto clients must be served through a MiCA-authorized entity, potentially leaving 10 million users without a compliant platform. This deadline could disrupt access for millions of EU crypto users and force major exchanges like Binance to restructure their EU operations, significantly impacting the European crypto market. MiCA (Markets in Crypto-Assets Regulation) has been fully applicable since December 2024, but a transitional period ends July 1, 2026, after which all crypto service providers must be fully authorized under MiCA.

rss · CoinDesk · Jun 29, 15:03

**Background**: MiCA is the first comprehensive EU regulatory framework for crypto-assets, covering issuance, service provision, and market abuse prevention. It aims to protect investors and ensure financial stability while fostering innovation. ESMA is the EU authority responsible for enforcing MiCA rules.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Markets_in_Crypto-Assets">Markets in Crypto-Assets - Wikipedia</a></li>
<li><a href="https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica">Markets in Crypto -Assets Regulation (MiCA)</a></li>

</ul>
</details>

**Tags**: `#crypto`, `#regulation`, `#EU`, `#MiCA`

---

<a id="item-8"></a>
## [Breez SDK Enables Bitcoin-to-Stablecoin Payments Across 30+ Chains](https://cointelegraph.com/news/breez-bitcoin-wallets-send-usdc-usdt-without-holding-stablecoins?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) ⭐️ 6.0/10

Breez has launched a new SDK feature that allows developers to route payments from Bitcoin balances to recipients in USDC and USDT across more than 30 blockchains, without requiring users to hold stablecoins. This innovation bridges Bitcoin and stablecoin ecosystems, enabling Bitcoin holders to transact in stablecoins without converting their BTC, which could increase Bitcoin's utility in everyday payments and DeFi. The SDK is built on Spark, a native Bitcoin Layer 2, and supports instant settlement with no minimum limits. It is non-custodial and trusted by over 75 teams.

rss · CoinTelegraph · Jun 29, 13:00

**Background**: Stablecoins like USDC and USDT are widely used for payments and DeFi, but Bitcoin holders often need to sell BTC to obtain them. Breez SDK's routing feature eliminates that step, allowing direct Bitcoin-to-stablecoin payments via Lightning Network and cross-chain swaps.

<details><summary>References</summary>
<ul>
<li><a href="https://cryptobriefing.com/breez-bitcoin-stablecoin-payments-30-blockchains/">Breez launches Bitcoin - to - stablecoin payments across 30 blockchains</a></li>
<li><a href="https://breez.technology/sdk/">Breez SDK | Add Bitcoin to Any App or Service</a></li>
<li><a href="https://coincentral.com/breez-launches-bitcoin-to-stablecoin-payments-without-holding-usdc-or-usdt/">Breez Launches Bitcoin - to - Stablecoin Payments Without Holding ...</a></li>

</ul>
</details>

**Tags**: `#Bitcoin`, `#stablecoins`, `#payments`, `#SDK`, `#blockchain`

---

<a id="item-9"></a>
## [Vitalik Buterin: Obfuscation Could Enable Private Onchain Voting](https://cointelegraph.com/news/vitalik-buterin-private-onchain-voting-obfuscation?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) ⭐️ 6.0/10

Ethereum co-founder Vitalik Buterin suggested that indistinguishability obfuscation (iO) could eventually enable private, collusion-resistant onchain voting without the need for trusted committees. However, he acknowledged that the technology remains highly impractical for now. If realized, iO-based voting could revolutionize governance in DAOs and DeFi protocols by ensuring voter privacy and preventing collusion, addressing key limitations of current onchain voting systems. This would enhance trust and participation in decentralized decision-making. Indistinguishability obfuscation is a cryptographic primitive that hides a program's implementation while preserving its functionality, making obfuscated versions of equivalent programs indistinguishable. Current iO candidates are extremely impractical; for example, obfuscating a simple 32-bit AND function produces a program nearly 12 gigabytes in size.

rss · CoinTelegraph · Jun 29, 10:53

**Background**: Indistinguishability obfuscation (iO) was first proposed in 2001 and is considered a powerful tool that could theoretically construct almost all cryptographic primitives. However, practical iO remains elusive; even the most efficient known constructions are far too large and slow for real-world use. Onchain voting today often relies on trusted committees or reveals votes, making it vulnerable to collusion or privacy breaches.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Indistinguishability_obfuscation">Indistinguishability obfuscation</a></li>
<li><a href="https://coinfractal.com/vitalik-buterin-indistinguishability-obfuscation-private-onchain-voting/">Vitalik: Obfuscation Could Power Private Onchain Voting</a></li>

</ul>
</details>

**Tags**: `#cryptography`, `#blockchain`, `#voting`, `#privacy`

---