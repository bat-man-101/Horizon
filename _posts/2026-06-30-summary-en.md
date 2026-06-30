---
layout: default
title: "Horizon Summary: 2026-06-30 (EN)"
date: 2026-06-30
lang: en
---

> From 127 items, 14 important content pieces were selected

---

1. [Supreme Court rules geofence warrants need constitutional protections](#item-1) ⭐️ 9.0/10
2. [Google's AI Peer Reviewer Handles ~10K Papers at ICML/STOC](#item-2) ⭐️ 9.0/10
3. [vLLM v0.24.0 Adds MiniMax-M3 Support and DeepSeek-V4 Optimizations](#item-3) ⭐️ 8.0/10
4. [Ornith-1.0: Open-Weight Self-Scaffolding LLMs for Coding](#item-4) ⭐️ 8.0/10
5. [MiCA deadline may force 10M EU crypto users off platforms](#item-5) ⭐️ 7.0/10
6. [BNY Mellon Expands Stablecoin Services with USDC](#item-6) ⭐️ 7.0/10
7. [BIS warns AI spending boom risks financial instability](#item-7) ⭐️ 7.0/10
8. [OpenAI Maps AI's Impact on EU Jobs](#item-8) ⭐️ 6.0/10
9. [Private Key Hacks Cause 40% of $16B Crypto Losses](#item-9) ⭐️ 6.0/10
10. [White House Pushes Crypto Clarity Act with Law Enforcement](#item-10) ⭐️ 6.0/10
11. [J.P. Morgan Expands Blockchain Settlement Network](#item-11) ⭐️ 6.0/10
12. [Vitalik Buterin: Crypto's Most Powerful Idea Not Ready Yet](#item-12) ⭐️ 6.0/10
13. [Breez SDK enables Bitcoin-to-stablecoin payments across 30+ chains](#item-13) ⭐️ 6.0/10
14. [Vitalik Buterin: Obfuscation Could Enable Private Onchain Voting](#item-14) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Supreme Court rules geofence warrants need constitutional protections](https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision) ⭐️ 9.0/10

The US Supreme Court ruled that geofence warrants, which allow law enforcement to obtain location data of all devices within a specific area, require constitutional protections under the Fourth Amendment. This landmark decision significantly limits law enforcement's ability to conduct mass digital surveillance without individualized suspicion, strengthening privacy rights for all Americans in the digital age. The case involved a bank robbery where Google provided location data of 19 devices near the crime scene; the Court held that such warrants must meet traditional probable cause and particularity requirements.

hackernews · cdrnsf · Jun 29, 15:54 · [Discussion](https://news.ycombinator.com/item?id=48720924)

**Background**: A geofence warrant is a search warrant that compels a company like Google to identify all mobile devices within a defined geographic area over a specific time period. These warrants have been controversial because they can sweep up data from innocent bystanders, raising Fourth Amendment concerns about unreasonable searches.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Geofence_warrant">Geofence warrant</a></li>

</ul>
</details>

**Discussion**: Commenters noted the Court's use of sources in the opinion and discussed historical examples like the Paula Broadwell case, where location data was used to identify a suspect. Some questioned whether the ruling would extend to other surveillance tools like Flock cameras.

**Tags**: `#privacy`, `#supreme court`, `#digital rights`, `#law enforcement`, `#geolocation`

---

<a id="item-2"></a>
## [Google's AI Peer Reviewer Handles ~10K Papers at ICML/STOC](https://www.reddit.com/r/MachineLearning/comments/1uio9rb/googles_agentic_peerreviewer_handled_10k_papers/) ⭐️ 9.0/10

Google deployed an agentic AI peer-reviewer at ICML and STOC that processed approximately 10,000 papers with a 30-minute turnaround, and the formal research paper shows it catches 34% more mathematical errors than zero-shot prompting. This sets a precedent for AI-automated scientific review at conference scale, potentially transforming the peer review process by improving error detection and reducing reviewer burden. The agentic AI system was deployed at two top computer science conferences, ICML and STOC, and the formal paper is available on arXiv (2606.28277). The 34% improvement in catching mathematical errors is measured against zero-shot prompting baselines.

reddit · r/MachineLearning · /u/Justgototheeffinmoon · Jun 29, 10:05

**Background**: Peer review is a critical but time-consuming process in scientific publishing, often struggling with reviewer shortages and inconsistency. Zero-shot prompting refers to asking an AI model to perform a task without any examples, while agentic AI systems can autonomously plan and execute multi-step tasks. Google's approach uses an agentic framework to conduct thorough reviews, including mathematical verification.

<details><summary>References</summary>
<ul>
<li><a href="https://www.wired.com/2017/02/ai-can-solve-peer-review-ai-can-solve-anything/">If AI Can Fix Peer Review in Science, AI Can Do Anything | WIRED</a></li>
<li><a href="https://www.yeschat.ai/gpts-9t55RFv0k6P-AI-Peer-Reviewer">AI Peer Reviewer -Free Automated Peer Review</a></li>
<li><a href="https://huggingface.co/papers/2606.13044">Paper page - No Hidden Prompts Needed! You Can Game AI Peer ...</a></li>

</ul>
</details>

**Discussion**: Reddit discussion is substantive, with users debating the implications for academic integrity, potential biases, and the role of human reviewers. Some express concern about AI replacing human judgment, while others see it as a useful tool to augment reviewers.

**Tags**: `#AI`, `#peer review`, `#machine learning`, `#conference`, `#automation`

---

<a id="item-3"></a>
## [vLLM v0.24.0 Adds MiniMax-M3 Support and DeepSeek-V4 Optimizations](https://github.com/vllm-project/vllm/releases/tag/v0.24.0) ⭐️ 8.0/10

vLLM v0.24.0, released with 571 commits from 256 contributors, adds support for the MiniMax-M3 model and delivers major optimizations for DeepSeek-V4, including a FlashInfer sparse index cache and prefill chunk-planning improvements. This release significantly expands vLLM's model ecosystem and inference performance, enabling efficient serving of cutting-edge models like MiniMax-M3 and DeepSeek-V4, which are critical for coding, agentic tasks, and long-context applications. MiniMax-M3 support includes BF16/FP8 indexer via MSA, MXFP4, FP8 sparse GQA, and extensive AMD/ROCm tuning. DeepSeek-V4 optimizations yield 2-4% TTFT improvement from FlashInfer sparse index cache and 4% end-to-end throughput gain from prefill chunk-planning.

github · khluu · Jun 29, 19:41

**Background**: vLLM is an open-source high-throughput LLM inference engine widely used in production. MiniMax-M3 is a frontier open-weight model with 1M context and strong coding/agentic capabilities, while DeepSeek-V4 is a massive MoE model with up to 1.6T parameters. FlashInfer is a kernel library for LLM serving that provides efficient sparse attention implementations.

<details><summary>References</summary>
<ul>
<li><a href="https://www.minimax.io/models/text/m3">MiniMax M3 - Coding & Agentic Frontier, 1M Context, Multimodal | MiniMax</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro">deepseek-ai/DeepSeek-V4-Pro · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#DeepSeek-V4`, `#MiniMax-M3`, `#open source`

---

<a id="item-4"></a>
## [Ornith-1.0: Open-Weight Self-Scaffolding LLMs for Coding](https://simonwillison.net/2026/Jun/29/ornith/#atom-everything) ⭐️ 8.0/10

DeepReinforce released Ornith-1.0, a family of open-weights (MIT licensed) LLMs ranging from 9B to 397B parameters, built on Gemma 4 and Qwen 3.5, achieving state-of-the-art coding benchmark performance among open-source models of comparable size. This release provides a high-performance, open-source alternative for agentic coding tasks, with a novel self-scaffolding training approach that may improve efficiency and reduce chain-of-thought length, potentially lowering inference costs. The model family includes 9B Dense, 31B Dense, 35B MoE, and 397B MoE variants, all MIT licensed. Early user reports indicate Ornith-1.0 35B is faster than Qwen 3.6 35B due to shorter chain-of-thought, and performs well on complex code modification tasks.

rss · Simon Willison · Jun 29, 16:17

**Background**: Agentic coding refers to AI agents that autonomously plan, write, test, and modify code with minimal human intervention. Self-scaffolding is a training technique where the model learns to generate its own reasoning structure (scaffold) to improve performance on complex tasks, potentially reducing reliance on external prompting frameworks.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/29/ornith/">Ornith-1.0: Self - Scaffolding LLMs for Agentic Coding</a></li>
<li><a href="https://deep-reinforce.com/ornith_1_0.html">Ornith-1.0: Self - Scaffolding LLMs ... | DeepReinforce Blog | Jun. 2026</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agentic_coding">Agentic coding</a></li>

</ul>
</details>

**Discussion**: Community feedback is generally positive: users report Ornith-1.0 35B outperforms Qwen 3.6 35B in speed and code modification tasks, though some note it still struggles with hallucination in chat without tools. Questions remain about the training methodology and the identity of DeepReinforce.

**Tags**: `#LLM`, `#open-source`, `#coding`, `#AI agents`, `#model release`

---

<a id="item-5"></a>
## [MiCA deadline may force 10M EU crypto users off platforms](https://www.coindesk.com/business/2026/06/29/mica-july-1-deadline-could-leave-10-million-crypto-users-searching-for-a-new-platform-in-the-eu) ⭐️ 7.0/10

The MiCA regulation's July 1 deadline could leave approximately 10 million cryptocurrency users in the European Union without access to compliant trading platforms, as many exchanges may fail to obtain necessary licenses in time. This could cause significant market disruption, forcing users to move funds to unregulated venues or exit crypto altogether, while shaping the competitive landscape for crypto exchanges in the EU. The MiCA regulation, which entered into force in June 2023, requires crypto-asset service providers to obtain authorization from national competent authorities by July 1, 2026, or cease operations in the EU.

rss · CoinDesk · Jun 29, 15:03

**Background**: MiCA (Markets in Crypto-Assets) is a comprehensive EU regulatory framework for crypto assets, designed to protect investors and ensure market integrity while fostering innovation. It covers issuers of crypto assets, crypto-asset service providers, and stablecoins. The regulation includes a transitional period during which existing operators can continue serving EU customers while applying for licenses.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Markets_in_Crypto-Assets">Markets in Crypto - Assets - Wikipedia</a></li>
<li><a href="https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica">Markets in Crypto - Assets Regulation (MiCA)</a></li>

</ul>
</details>

**Tags**: `#crypto`, `#regulation`, `#EU`, `#MiCA`

---

<a id="item-6"></a>
## [BNY Mellon Expands Stablecoin Services with USDC](https://www.coindesk.com/business/2026/06/29/wall-street-s-bny-expands-stablecoin-services-for-institutions-starting-with-circle-s-usdc) ⭐️ 7.0/10

BNY Mellon, a major Wall Street bank, is expanding its stablecoin services for institutional clients, starting with Circle's USDC, by adding minting and redemption capabilities to its institutional custody platform. This move signals a significant step in traditional finance embracing crypto, as BNY Mellon is one of the largest custodian banks globally, and its entry into stablecoin services could drive broader institutional adoption of digital assets. The expansion deepens BNY Mellon's existing partnership with Circle, building on its role as the primary custodian of USDC reserves, and allows institutional clients to mint and redeem USDC directly through the bank's platform.

rss · CoinDesk · Jun 29, 14:46

**Background**: Stablecoins like USDC are digital tokens pegged 1:1 to the US dollar, designed to maintain a stable value for transactions and as a store of value. BNY Mellon has been gradually expanding into crypto services, having launched Bitcoin and Ethereum custody in 2022. Minting refers to creating new stablecoin tokens by depositing fiat currency, while redemption is the reverse process of converting tokens back to fiat.

<details><summary>References</summary>
<ul>
<li><a href="https://www.coinbase.com/en-gb/USDC">USDC : The Dollar for the Digital Age | Coinbase</a></li>
<li><a href="https://decrypt.co/111641/bny-mellon-launches-bitcoin-ethereum-custody-services-investment-firms">BNY Mellon Launches Bitcoin, Ethereum Custody Services... - Decrypt</a></li>
<li><a href="https://www.bitgo.com/resources/blog/how-to-build-stablecoins/">Stablecoin Development: How to Build Secure Digital Money | BitGo</a></li>

</ul>
</details>

**Tags**: `#stablecoins`, `#institutional adoption`, `#crypto`, `#finance`, `#blockchain`

---

<a id="item-7"></a>
## [BIS warns AI spending boom risks financial instability](https://cointelegraph.com/news/bis-sounds-alarm-on-ai-exuberance-as-debt-fueled-boom-risks-bust?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) ⭐️ 7.0/10

The Bank for International Settlements (BIS) has warned that excessive AI spending, fueled by debt and leveraged nonbank structures, could lead to global financial consequences. This warning highlights a potential systemic risk in the financial system, as the AI investment surge relies on risky financing that could rapidly unwind, affecting global markets and investors. The BIS report points to enormous debt and highly leveraged nonbank structures, such as hedge funds and private credit, as key financing sources for AI investments that could amplify a bust.

rss · CoinTelegraph · Jun 29, 05:31

**Background**: The Bank for International Settlements is an international financial institution that fosters monetary and financial stability. It regularly monitors systemic risks in the global financial system. Nonbank financial intermediaries (NBFIs) include entities like hedge funds and private equity firms that borrow heavily to invest, increasing leverage and potential contagion.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bank_for_International_Settlements">Bank for International Settlements - Wikipedia</a></li>
<li><a href="https://www.fsb.org/uploads/P090725-1.pdf">Leverage in Nonbank Financial Intermediation: Final report</a></li>
<li><a href="https://www.linkedin.com/posts/francescorosamech_debt-has-entered-the-ai-boom-activity-7393220683910250496-M7SX">Debt Has Entered the A . I . Boom | Francesco Rosa</a></li>

</ul>
</details>

**Tags**: `#AI`, `#finance`, `#systemic risk`, `#investment`

---

<a id="item-8"></a>
## [OpenAI Maps AI's Impact on EU Jobs](https://openai.com/index/mapping-ai-jobs-transition-eu) ⭐️ 6.0/10

OpenAI released a report mapping how AI could automate, augment, or transform occupations across the European Union, identifying which jobs face the highest exposure to AI-driven changes. This report provides a high-level overview of AI's potential impact on the EU labor market, helping policymakers and businesses anticipate workforce transitions and plan for reskilling initiatives. The report categorizes occupations by automation risk, growth potential, and workflow changes, but lacks specific technical details or granular data on individual job roles.

rss · OpenAI Blog · Jun 29, 07:00

**Background**: AI technologies like large language models are increasingly capable of performing tasks traditionally done by humans, raising concerns about job displacement. This report is part of OpenAI's broader effort to study AI's societal impacts.

**Tags**: `#AI`, `#labor market`, `#Europe`, `#automation`

---

<a id="item-9"></a>
## [Private Key Hacks Cause 40% of $16B Crypto Losses](https://www.coindesk.com/tech/2026/06/29/private-keys-not-smart-contracts-caused-40-of-crypto-s-usd16-billion-hack-losses-here-s-whats-being-done) ⭐️ 6.0/10

A new report reveals that 40% of the $16 billion in cryptocurrency hack losses are due to private key compromises, not smart contract vulnerabilities, prompting industry initiatives to improve key management. This finding shifts the security focus from code audits to key custody, affecting how exchanges, protocols, and individual users protect assets. Improved key management could significantly reduce future losses. Private key compromises include phishing, server breaches, and poor storage practices, often bypassing robust smart contract security. The report emphasizes that even audited protocols remain vulnerable if keys are mishandled.

rss · CoinDesk · Jun 29, 15:45

**Background**: In cryptocurrency, a private key is a secret string that proves ownership of funds, similar to a password. Smart contracts are self-executing code on blockchain, but hacks often target key storage rather than code flaws. Many users rely on custodians or hardware wallets for key security.

<details><summary>References</summary>
<ul>
<li><a href="https://www.investopedia.com/terms/p/private-key.asp">Understanding Private Keys: How They Work and Secure Storage Tips</a></li>
<li><a href="https://www.coinbase.com/learn/crypto-basics/what-is-a-private-key">What is a private key? | Coinbase</a></li>
<li><a href="https://www.gemini.com/cryptopedia/public-private-keys-cryptography">Public and Private Keys: What Are They? | Gemini</a></li>

</ul>
</details>

**Tags**: `#cryptocurrency`, `#security`, `#private keys`, `#hacks`

---

<a id="item-10"></a>
## [White House Pushes Crypto Clarity Act with Law Enforcement](https://www.coindesk.com/policy/2026/06/29/white-house-to-speak-with-law-enforcement-groups-to-push-crypto-s-clarity-act) ⭐️ 6.0/10

The White House is meeting with law enforcement groups to advocate for the Crypto's Clarity Act, a bill aimed at establishing clear federal regulations for cryptocurrencies. This engagement signals a strategic push to gain law enforcement support, which could accelerate the bill's passage and bring regulatory clarity to the crypto industry, affecting exchanges, investors, and users. The Clarity Act has faced opposition from various groups, including Catholic leaders, and its passage depends on key Senate Democrats. The White House's outreach aims to counter opposition and build bipartisan support.

rss · CoinDesk · Jun 29, 15:23

**Background**: The Crypto's Clarity Act is a proposed U.S. federal law that would define which digital assets are securities and which are commodities, assigning regulatory authority to the SEC or CFTC. Currently, crypto regulation in the U.S. is fragmented, with agencies issuing conflicting guidance. The bill seeks to resolve this uncertainty, which has been a major hurdle for industry growth.

<details><summary>References</summary>
<ul>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lKekpxNUVSR2RYMXlKekJSTXNTZ0FQAQ?hl=en-US&gl=US&ceid=US:en">Google News - News about CLARITY Act - Overview</a></li>
<li><a href="https://decrypt.co/371923/crypto-clarity-act-new-enemy-catholic-leaders">Crypto ’ s Clarity Act Has a New Enemy: Catholic Leaders - Decrypt</a></li>
<li><a href="https://coinunited.io/learn/en/opinions-&-insights/crypto-s-clarity-act-showdown-will-the-financial-future-be-forged-or-forgotten">Cryptos Clarity Act Showdown: Will the Financial... - CoinUnited.io</a></li>

</ul>
</details>

**Tags**: `#cryptocurrency`, `#regulation`, `#policy`, `#law enforcement`

---

<a id="item-11"></a>
## [J.P. Morgan Expands Blockchain Settlement Network](https://www.coindesk.com/business/2026/06/29/j-p-morgan-broadens-blockchain-settlement-network-as-banks-modernize-cross-border-payments) ⭐️ 6.0/10

J.P. Morgan has expanded its Kinexys blockchain settlement network, which has processed over $4 trillion in transactions, to deepen its reach in the Asia-Pacific region for modernizing cross-border payments. This expansion signals growing adoption of blockchain for core banking infrastructure, potentially reducing costs and settlement times for cross-border payments, which have traditionally been slow and expensive. Kinexys is a bank-led blockchain platform offering programmable payments, asset tokenization, and near-real-time settlement. The latest expansion focuses on the Asia-Pacific region, a key area for cross-border trade.

rss · CoinDesk · Jun 29, 15:23

**Background**: Cross-border payments traditionally rely on a network of correspondent banks, leading to delays and high fees. Blockchain technology enables direct, transparent, and faster settlement by using a shared ledger. J.P. Morgan's Kinexys is one of the largest bank-led blockchain networks, processing trillions in transactions.

<details><summary>References</summary>
<ul>
<li><a href="https://www.jpmorgan.com/kinexys/index">Kinexys: Enterprise Bank-Led Blockchain Solutions</a></li>
<li><a href="https://www.coindesk.com/business/2026/06/29/j-p-morgan-broadens-blockchain-settlement-network-as-banks-modernize-cross-border-payments">J . P . Morgan broadens Kinexys blockchain settlement network as...</a></li>
<li><a href="https://www.paymentsjournal.com/a-look-at-blockchain-in-cross-border-payments/">A Look at Blockchain in Cross - Border Payments - PaymentsJournal</a></li>

</ul>
</details>

**Tags**: `#blockchain`, `#banking`, `#cross-border payments`, `#J.P. Morgan`

---

<a id="item-12"></a>
## [Vitalik Buterin: Crypto's Most Powerful Idea Not Ready Yet](https://www.coindesk.com/tech/2026/06/29/vitalik-buterin-says-crypto-s-most-powerful-idea-is-still-nowhere-near-ready) ⭐️ 6.0/10

Vitalik Buterin stated that a foundational crypto concept, widely considered the most powerful idea in the space, is still far from being ready for practical use. This commentary from Ethereum's co-founder highlights the gap between theoretical potential and real-world readiness, affecting expectations for blockchain innovation and investment. The specific idea was not named in the summary, but the discussion likely refers to concepts like full decentralization, zero-knowledge proofs, or sharding, which face scalability and security hurdles.

rss · CoinDesk · Jun 29, 11:52

**Background**: Vitalik Buterin is the co-founder of Ethereum, a leading blockchain platform. His views often influence the crypto industry. The 'most powerful idea' likely refers to a core crypto principle that promises transformative change but requires further development.

**Tags**: `#cryptocurrency`, `#blockchain`, `#Vitalik Buterin`, `#technology readiness`

---

<a id="item-13"></a>
## [Breez SDK enables Bitcoin-to-stablecoin payments across 30+ chains](https://cointelegraph.com/news/breez-bitcoin-wallets-send-usdc-usdt-without-holding-stablecoins?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) ⭐️ 6.0/10

Breez has launched a new SDK feature that allows developers to route payments from Bitcoin balances to recipients in USDC and USDT across more than 30 blockchains, without requiring users to hold stablecoins. This simplifies cross-chain payments by letting Bitcoin users send stablecoins directly, potentially increasing Bitcoin's utility in everyday transactions and DeFi. It also reduces friction for developers building payment applications that need stablecoin settlement. The feature is part of the Breez SDK, which is trusted by over 75 teams and enables non-custodial Bitcoin and Lightning Network integrations. The cross-chain routing likely uses atomic swap technology to ensure trustless settlement.

rss · CoinTelegraph · Jun 29, 13:00

**Background**: Breez is known for its Bitcoin and Lightning Network payment infrastructure. Stablecoins like USDC and USDT are widely used for their price stability, but typically require users to hold them directly. This SDK bridges Bitcoin and stablecoin ecosystems without requiring users to manage multiple assets.

<details><summary>References</summary>
<ul>
<li><a href="https://cryptobriefing.com/breez-bitcoin-stablecoin-payments-30-blockchains/">Breez launches Bitcoin -to- stablecoin payments across 30 blockchains</a></li>
<li><a href="https://breez.technology/sdk/">Breez SDK | Add Bitcoin to Any App or Service</a></li>
<li><a href="https://en.coin-turk.com/breez-launched-direct-usdc-and-usdt-transfers-from-bitcoin-balances-across-more-than-30-blockchains/">COINTURK NEWS - Bitcoin , Blockchain and Cryptocurrency News...</a></li>

</ul>
</details>

**Tags**: `#Bitcoin`, `#Stablecoins`, `#Cross-chain`, `#Payments`, `#SDK`

---

<a id="item-14"></a>
## [Vitalik Buterin: Obfuscation Could Enable Private Onchain Voting](https://cointelegraph.com/news/vitalik-buterin-private-onchain-voting-obfuscation?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) ⭐️ 6.0/10

Ethereum co-founder Vitalik Buterin stated that indistinguishability obfuscation (iO) could eventually enable private, collusion-resistant onchain voting without trusted committees, though the technology remains impractical for now. If realized, iO-based voting could revolutionize blockchain governance by ensuring voter privacy and preventing collusion, addressing key limitations of current onchain voting systems that rely on transparency or trusted third parties. Indistinguishability obfuscation hides a program's implementation while allowing it to run, but current candidates are extremely impractical—for example, obfuscating a simple 32-bit AND function produces a program nearly 12 gigabytes in size.

rss · CoinTelegraph · Jun 29, 10:53

**Background**: Onchain voting is used by DAOs and blockchain protocols for governance, but it typically lacks privacy because votes are publicly visible. Indistinguishability obfuscation is a cryptographic primitive that makes any two programs computing the same function indistinguishable, enabling secure execution without revealing internal logic. However, iO is still far from practical deployment due to enormous computational and storage overhead.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Indistinguishability_obfuscation">Indistinguishability obfuscation</a></li>
<li><a href="https://docs.tally.xyz/user-guides/governance-concepts/onchain-vs.-offchain-voting">Onchain vs. Offchain Voting | Prod site - docs.tally.xyz</a></li>

</ul>
</details>

**Tags**: `#cryptography`, `#voting`, `#privacy`, `#blockchain`

---