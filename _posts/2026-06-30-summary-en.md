---
layout: default
title: "Horizon Summary: 2026-06-30 (EN)"
date: 2026-06-30
lang: en
---

> From 132 items, 16 important content pieces were selected

---

1. [vLLM v0.24.0: MiniMax-M3 Support & DeepSeek-V4 Optimizations](#item-1) ⭐️ 9.0/10
2. [Supreme Court: Geofence warrants need constitutional protections](#item-2) ⭐️ 9.0/10
3. [Google's AI Peer-Reviewer Handles 10K Papers, Catches 34% More Errors](#item-3) ⭐️ 9.0/10
4. [Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding](#item-4) ⭐️ 8.0/10
5. [ChatGPT Overturns Erdős Conjecture Worked on by Chen Lijie for 7 Years](#item-5) ⭐️ 8.0/10
6. [MiCA Deadline May Force 10M EU Crypto Users Off Platforms](#item-6) ⭐️ 7.0/10
7. [BNY Mellon Adds USDC Minting and Redemption to Custody Platform](#item-7) ⭐️ 7.0/10
8. [BIS warns AI spending debt could trigger financial crisis](#item-8) ⭐️ 7.0/10
9. [Pioneering zk-rollup Loopring closes DEX due to low adoption](#item-9) ⭐️ 7.0/10
10. [OpenAI Maps AI Job Shifts Across EU](#item-10) ⭐️ 6.0/10
11. [Securitize to Debut on NYSE After SPAC Merger Approval](#item-11) ⭐️ 6.0/10
12. [Private Key Compromises Drive 40% of $16B Crypto Hack Losses](#item-12) ⭐️ 6.0/10
13. [White House to Lobby Law Enforcement for Crypto Clarity Act](#item-13) ⭐️ 6.0/10
14. [Vitalik Buterin: Crypto's Most Powerful Idea Not Ready Yet](#item-14) ⭐️ 6.0/10
15. [UK Sets 2027 FCA Authorization Deadline for Crypto Firms](#item-15) ⭐️ 6.0/10
16. [Breez SDK enables Bitcoin-to-stablecoin payments across 30+ chains](#item-16) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [vLLM v0.24.0: MiniMax-M3 Support & DeepSeek-V4 Optimizations](https://github.com/vllm-project/vllm/releases/tag/v0.24.0) ⭐️ 9.0/10

vLLM v0.24.0 adds support for the MiniMax-M3 model and delivers major optimizations for DeepSeek-V4, including a FlashInfer sparse index cache and prefill chunk-planning improvements. The release includes 571 commits from 256 contributors. This release significantly expands vLLM's model support and inference performance, benefiting developers deploying cutting-edge LLMs like MiniMax-M3 and DeepSeek-V4. The optimizations improve throughput and latency, making vLLM more competitive for production use. MiniMax-M3 support includes BF16/FP8 indexer via MSA, MXFP4, FP8 sparse GQA, and extensive AMD/ROCm tuning. DeepSeek-V4 optimizations include a FlashInfer sparse index cache (2–4% TTFT improvement), prefill chunk-planning (4% E2E throughput gain), and native DSA indexer decode for next_n > 2 on SM100.

github · khluu · Jun 29, 19:41

**Background**: vLLM is an open-source high-throughput LLM inference engine widely used in production. MiniMax-M3 is a frontier multimodal model with 1M context and MiniMax Sparse Attention (MSA). DeepSeek-V4 is a trillion-parameter MoE model requiring efficient inference optimizations.

<details><summary>References</summary>
<ul>
<li><a href="https://www.minimax.io/blog/minimax-m3">MiniMax M3: Frontier Coding, 1M Context, Native Multimodality — All in One Model - MiniMax Research | MiniMax</a></li>
<li><a href="https://github.com/flashinfer-ai/flashinfer">GitHub - flashinfer -ai/ flashinfer : FlashInfer : Kernel Library for LLM...</a></li>
<li><a href="https://news.skila.ai/article/deepseek-v4-trillion-parameter-multimodal-model">DeepSeek V 4 : Trillion-Parameter Multimodal AI Model | Skila News</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#open-source`, `#model optimization`, `#release`

---

<a id="item-2"></a>
## [Supreme Court: Geofence warrants need constitutional protections](https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision) ⭐️ 9.0/10

The US Supreme Court ruled that geofence warrants, which compel tech companies to identify all devices in a specific area, must comply with Fourth Amendment protections against unreasonable searches and seizures. This landmark decision sets a crucial precedent for digital privacy in the age of ubiquitous surveillance, potentially limiting law enforcement's ability to conduct mass, warrantless location tracking. The case involved a bank robbery where Google provided location data for 19 devices near the crime scene; the Court held that such warrants require probable cause and particularity, similar to traditional search warrants.

hackernews · cdrnsf · Jun 29, 15:54 · [Discussion](https://news.ycombinator.com/item?id=48720924)

**Background**: A geofence warrant, also known as a reverse location warrant, allows police to request from companies like Google a list of all devices within a virtual boundary (geofence) during a specific time. The Fourth Amendment protects against unreasonable searches, but its application to digital data held by third parties has been debated since cases like Carpenter v. United States.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Geofence_warrant">Geofence warrant - Wikipedia</a></li>
<li><a href="https://www.congress.gov/crs-product/LSB11274">Geofence Warrants and the Fourth Amendment | Congress.gov | Library of Congress</a></li>
<li><a href="https://www.nacdl.org/Content/Geofence-Warrants">NACDL - Geofence Warrants</a></li>

</ul>
</details>

**Discussion**: Commenters noted the Court's opinion cited sources and referenced the Riley case, highlighting the pervasive nature of cell phones. Some discussed the practical limits of surveillance, noting that physical wiretapping had resource constraints that digital surveillance lacks, raising concerns about potential abuse.

**Tags**: `#privacy`, `#supreme court`, `#surveillance`, `#law`, `#technology`

---

<a id="item-3"></a>
## [Google's AI Peer-Reviewer Handles 10K Papers, Catches 34% More Errors](https://www.reddit.com/r/MachineLearning/comments/1uio9rb/googles_agentic_peerreviewer_handled_10k_papers/) ⭐️ 9.0/10

Google deployed an agentic AI peer-reviewer at ICML and STOC that processed approximately 10,000 papers with a 30-minute turnaround, and a new formal research paper shows it catches 34% more mathematical errors than zero-shot prompting. This sets a precedent for AI-automated scientific review at conference scale, potentially transforming peer review by improving error detection and reducing turnaround time, affecting researchers, conference organizers, and the broader scientific community. The system achieved a 34% improvement in detecting mathematical errors compared to zero-shot prompting, and the formal paper documenting this work is now available on arXiv (2606.28277).

reddit · r/MachineLearning · /u/Justgototheeffinmoon · Jun 29, 10:05

**Background**: Peer review is a critical but time-consuming process in scientific publishing, often facing delays and inconsistencies. Zero-shot prompting is a technique where an AI model performs tasks without examples, serving as a baseline here. Agentic AI refers to systems that can autonomously plan and execute multi-step tasks, like reviewing papers.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.28277">Towards Automating Scientific Review with Google's Paper Assistant...</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion is highly engaged, with many commenters impressed by the scale and error-detection improvement, though some express concerns about AI replacing human reviewers and potential biases in automated systems.

**Tags**: `#AI`, `#peer review`, `#machine learning`, `#conference`, `#automation`

---

<a id="item-4"></a>
## [Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding](https://simonwillison.net/2026/Jun/29/ornith/#atom-everything) ⭐️ 8.0/10

DeepReinforce released Ornith-1.0, a family of open-weight LLMs (9B to 397B) under MIT license, achieving state-of-the-art coding benchmark performance by learning to generate its own RL scaffolds. This is the first open-source model family that jointly optimizes the agent harness and solution generation, potentially reducing reliance on human-designed scaffolding for coding agents. The model variants include 9B Dense, 31B Dense, 35B MoE (activating ~3B parameters per token), and 397B MoE, built on top of Gemma 4 and Qwen 3.5 (both Apache 2.0).

rss · Simon Willison · Jun 29, 16:17

**Background**: Traditional RL for coding agents uses a fixed human-written harness to guide solution generation. Ornith-1.0's self-scaffolding approach learns to generate both the harness and the solution, enabling the model to discover better search trajectories and improve its own performance.

<details><summary>References</summary>
<ul>
<li><a href="https://deep-reinforce.com/ornith_1_0.html">Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding | DeepReinforce Blog | Jun. 2026</a></li>
<li><a href="https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B">deepreinforce-ai/Ornith-1.0-9B · Hugging Face</a></li>
<li><a href="https://www.marktechpost.com/2026/06/25/deepreinforce-releases-ornith-1-0-an-open-source-coding-model-family-that-learns-its-own-rl-scaffolds/">DeepReinforce Releases Ornith-1.0: An Open-Source Coding Model Family That Learns Its Own RL Scaffolds - MarkTechPost</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed: some praise its coding performance and creative solutions, while others note it performs poorly on chat without tools and exhibits hallucination. There is also skepticism about whether it's just a fine-tuned Qwen or Gemma 4, and concerns about accessibility (e.g., 9B model requires 80GB GPU).

**Tags**: `#LLM`, `#open-source`, `#coding`, `#AI`, `#model release`

---

<a id="item-5"></a>
## [ChatGPT Overturns Erdős Conjecture Worked on by Chen Lijie for 7 Years](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&mid=2652709773&idx=2&sn=68bde762eb0070f5bd61518728971232) ⭐️ 8.0/10

OpenAI's ChatGPT reportedly solved a core computational geometry problem based on an Erdős conjecture, which had been worked on by renowned theorist Chen Lijie for 7 years. This marks a significant milestone in AI-driven mathematics, demonstrating that large language models can contribute to long-standing open problems in theoretical computer science. The problem is related to the unit distance problem, an 80-year-old conjecture in discrete geometry. OpenAI's model reportedly disproved the conjecture, overturning previous assumptions.

rss · 新智元 · Jun 29, 05:01

**Background**: The Erdős conjecture in computational geometry, specifically the unit distance problem, asks for the maximum number of unit distances among n points in the plane. Chen Lijie is a prominent theoretical computer scientist at UC Berkeley known for his work in computational complexity.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/model-disproves-discrete-geometry-conjecture/">An OpenAI model has disproved a central conjecture in... | OpenAI</a></li>
<li><a href="https://interestingengineering.com/ai-robotics/openai-paul-erdos-geometry-problem-cracked">80-year-old geometry puzzle cracked by OpenAI using number theory</a></li>

</ul>
</details>

**Tags**: `#AI`, `#computational geometry`, `#ChatGPT`, `#Erdős conjecture`, `#theoretical computer science`

---

<a id="item-6"></a>
## [MiCA Deadline May Force 10M EU Crypto Users Off Platforms](https://www.coindesk.com/business/2026/06/29/mica-july-1-deadline-could-leave-10-million-crypto-users-searching-for-a-new-platform-in-the-eu) ⭐️ 7.0/10

The July 1, 2026 deadline for full compliance with the EU's Markets in Crypto-Assets (MiCA) regulation could leave approximately 10 million crypto users in the European Union without access to compliant platforms. This deadline represents a major regulatory shift that could disrupt millions of users and reshape the crypto landscape in Europe, potentially driving users to unregulated or non-compliant alternatives. MiCA requires crypto-asset service providers to obtain authorization from an EU member state and comply with strict rules on stablecoins, market abuse, and consumer protection. Platforms that fail to meet these requirements by July 1, 2026 must cease operations in the EU.

rss · CoinDesk · Jun 29, 15:03

**Background**: MiCA is the first comprehensive regulatory framework for crypto-assets in the EU, adopted in April 2023 and fully applicable since December 2024. It aims to protect investors, ensure financial stability, and foster innovation while addressing risks like money laundering and market manipulation. The July 1, 2026 deadline is the final compliance date for all crypto-asset service providers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Markets_in_Crypto-Assets">Markets in Crypto-Assets - Wikipedia</a></li>
<li><a href="https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica">Markets in Crypto-Assets Regulation (MiCA) - ESMA</a></li>

</ul>
</details>

**Tags**: `#crypto regulation`, `#MiCA`, `#EU`, `#blockchain`, `#finance`

---

<a id="item-7"></a>
## [BNY Mellon Adds USDC Minting and Redemption to Custody Platform](https://cointelegraph.com/news/bny-adds-usdc-minting-and-redemption-to-institutional-custody-platform?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) ⭐️ 7.0/10

BNY Mellon has expanded its institutional custody platform to support the minting and redemption of USDC stablecoins, deepening its partnership with Circle. This integration marks a significant step for traditional finance adoption of cryptocurrencies, as a major bank like BNY Mellon directly facilitates stablecoin operations, potentially increasing institutional trust and liquidity in digital assets. BNY Mellon already serves as the primary custodian of USDC reserves, and this new capability allows clients to mint and redeem USDC directly through the bank's platform, streamlining access to the stablecoin.

rss · CoinTelegraph · Jun 29, 16:10

**Background**: USDC is a stablecoin pegged 1:1 to the US dollar, issued by Circle. Minting and redemption refer to the processes of creating new USDC tokens (by depositing USD) and destroying them (to withdraw USD). Institutional custody platforms like BNY Mellon's provide secure storage and management of digital assets for large clients.

<details><summary>References</summary>
<ul>
<li><a href="https://www.circle.com/circle-mint">Circle Mint | Mint USDC, Unlock Business Efficiency | Circle</a></li>
<li><a href="https://help.circle.com/s/article/USDC-on-supported-blockchains-minting-redemption-FAQs?language=en_US">USDC supported blockchains | minting, redemption, & FAQs</a></li>

</ul>
</details>

**Tags**: `#cryptocurrency`, `#institutional custody`, `#USDC`, `#BNY Mellon`, `#blockchain`

---

<a id="item-8"></a>
## [BIS warns AI spending debt could trigger financial crisis](https://cointelegraph.com/news/bis-sounds-alarm-on-ai-exuberance-as-debt-fueled-boom-risks-bust?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) ⭐️ 7.0/10

The Bank for International Settlements (BIS) has warned that excessive AI spending, fueled by debt and leveraged nonbank structures, poses a systemic risk to global financial stability. This warning from a major central bank institution highlights a new source of systemic risk in the financial system, potentially affecting global markets and investors if the AI investment bubble bursts. The BIS report notes that AI investment has relied heavily on debt and highly leveraged nonbank financial institutions, which could rapidly unwind and trigger cascading failures.

rss · CoinTelegraph · Jun 29, 05:31

**Background**: Systemic risk refers to the possibility that a loss at one institution can spread through the financial system, causing widespread failure. Nonbank financial institutions, such as hedge funds and private equity firms, have grown rapidly and now account for nearly 50% of global credit, increasing leverage and interconnectedness.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Non-bank_financial_institution">Non - bank financial institution - Wikipedia</a></li>
<li><a href="https://www.imf.org/en/blogs/articles/2025/09/29/explainer-five-megatrends-shaping-the-rise-of-nonbank-finance">Explainer: Five Megatrends Shaping the Rise of Nonbank Finance</a></li>

</ul>
</details>

**Tags**: `#AI`, `#finance`, `#systemic risk`, `#regulation`

---

<a id="item-9"></a>
## [Pioneering zk-rollup Loopring closes DEX due to low adoption](https://cointelegraph.com/news/pioneering-zk-rollup-loopring-announces-dex-closure-citing-no-adoption?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) ⭐️ 7.0/10

Loopring, a pioneering zk-rollup protocol, announced the closure of its decentralized exchange (DEX) due to lack of adoption, citing the absence of a virtual machine and composability as key limitations. This closure highlights critical limitations of early zk-rollup designs that lack a virtual machine and composability, which are essential for building a vibrant DeFi ecosystem. It signals that Layer 2 solutions must support smart contract composability to attract users and developers. Loopring's DEX closure was announced by the team, who stated that the lack of a virtual machine prevented composability with other DeFi protocols, limiting ecosystem growth. The protocol will continue to operate but the DEX will shut down.

rss · CoinTelegraph · Jun 29, 03:15

**Background**: zk-rollups are Layer 2 scaling solutions that bundle transactions off-chain and submit a validity proof to Ethereum, reducing gas fees and increasing throughput. Composability in DeFi refers to the ability to combine different protocols like Lego blocks, enabling complex financial applications. A virtual machine (e.g., EVM) allows execution of smart contracts, which is crucial for composability.

<details><summary>References</summary>
<ul>
<li><a href="https://chain.link/education-hub/zero-knowledge-rollup">What Are ZK Rollups ? | Chainlink</a></li>
<li><a href="https://ethereum.org/developers/docs/evm/">Ethereum Virtual Machine (EVM) | ethereum.org</a></li>

</ul>
</details>

**Tags**: `#zk-rollup`, `#Layer 2`, `#DeFi`, `#blockchain`, `#scalability`

---

<a id="item-10"></a>
## [OpenAI Maps AI Job Shifts Across EU](https://openai.com/index/mapping-ai-jobs-transition-eu) ⭐️ 6.0/10

OpenAI released a report mapping how AI could reshape occupations across the EU, identifying jobs at risk of automation, those poised for growth, and those undergoing workflow changes. This report provides a data-driven overview of AI's potential impact on the European labor market, helping policymakers, businesses, and workers prepare for workforce transitions. The report covers a wide range of EU occupations but lacks specific technical details on the methodology or granular data per country.

rss · OpenAI Blog · Jun 29, 07:00

**Background**: AI technologies like large language models are increasingly capable of automating cognitive tasks, raising concerns about job displacement but also creating new opportunities. This report aims to quantify those effects across the diverse EU economy.

**Tags**: `#AI`, `#labor market`, `#Europe`, `#automation`, `#OpenAI`

---

<a id="item-11"></a>
## [Securitize to Debut on NYSE After SPAC Merger Approval](https://www.coindesk.com/business/2026/06/29/securitize-heads-to-nyse-debut-after-investors-approve-spac-merger) ⭐️ 6.0/10

Securitize, a leading tokenization platform, is set to debut on the New York Stock Exchange after investors approved its merger with a special-purpose acquisition company (SPAC). This listing marks a significant milestone for the tokenization industry, bringing a compliance-focused real-world asset (RWA) platform to a major public exchange and potentially increasing mainstream adoption of blockchain-based securities. The SPAC merger was approved by investors on June 29, 2026, and Securitize will begin trading on the NYSE under a new ticker symbol. The company specializes in tokenizing real-world assets such as private equity, real estate, and venture capital funds.

rss · CoinDesk · Jun 29, 23:05

**Background**: Securitize is a compliance-first platform that bridges traditional finance and blockchain by issuing digital securities representing ownership of real-world assets. A SPAC is a shell company that raises capital through an IPO to acquire a private company, taking it public faster than a traditional IPO. This merger allows Securitize to access public markets and raise additional capital for growth.

<details><summary>References</summary>
<ul>
<li><a href="https://securitize.io/">Securitize | The Leading Tokenization Platform</a></li>
<li><a href="https://www.okx.com/en-gb/learn/securitize-tokenization-investment-rwa">Securitize Tokenization Investment: Unlocking the Future of... | OKX</a></li>
<li><a href="https://en.wikipedia.org/wiki/Special-purpose_acquisition_company">Special-purpose acquisition company - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#blockchain`, `#tokenization`, `#SPAC`, `#NYSE`

---

<a id="item-12"></a>
## [Private Key Compromises Drive 40% of $16B Crypto Hack Losses](https://www.coindesk.com/tech/2026/06/29/private-keys-not-smart-contracts-caused-40-of-crypto-s-usd16-billion-hack-losses-here-s-whats-being-done) ⭐️ 6.0/10

A recent analysis reveals that 40% of the $16 billion in crypto hack losses are due to private key compromises, not smart contract vulnerabilities, prompting industry efforts to improve key management. This highlights a critical security gap in the crypto ecosystem, as private key compromises are often harder to detect and prevent than smart contract bugs, affecting businesses and individual users alike. In 2024, private key compromise accounted for 43% of crypto stolen, making it ineligible as a finding in competitive audit contests, and blockchain systems cannot inherently detect theft of private keys.

rss · CoinDesk · Jun 29, 15:45

**Background**: Private keys are cryptographic secrets that grant control over crypto assets. Unlike smart contract vulnerabilities, which can be audited, private key compromises often go unnoticed until assets are moved. Key management involves generation, storage, use, and destruction of keys, and solutions like MPC and TEE-based systems are emerging to address this.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.trailofbits.com/2025/06/25/maturing-your-smart-contracts-beyond-private-key-risk/">Maturing your smart contracts beyond private key risk -The Trail of...</a></li>
<li><a href="https://www.nadcab.com/blog/cryptographic-key-lifecycle">Cryptographic Key Lifecycle | From Private Key Generation to Secure...</a></li>
<li><a href="https://blog.tothemoon.com/articles/private-keys-in-crypto-what-businesses-need-to-know">Private Keys in Crypto : What Businesses Need to Know</a></li>

</ul>
</details>

**Tags**: `#cryptocurrency`, `#security`, `#private keys`, `#blockchain`

---

<a id="item-13"></a>
## [White House to Lobby Law Enforcement for Crypto Clarity Act](https://www.coindesk.com/policy/2026/06/29/white-house-to-speak-with-law-enforcement-groups-to-push-crypto-s-clarity-act) ⭐️ 6.0/10

The White House plans to meet with law enforcement groups to advocate for the Crypto's Clarity Act, a regulatory bill aimed at providing legal clarity for digital assets. This engagement signals high-level government support for the bill, potentially accelerating its passage and shaping the regulatory landscape for cryptocurrencies in the U.S. The bill includes provisions that protect software developers from prosecution, which has drawn criticism from Catholic leaders who argue it could enable human trafficking.

rss · CoinDesk · Jun 29, 15:23

**Background**: The Crypto's Clarity Act is a proposed U.S. federal law designed to clarify which digital assets are securities and which are commodities, and to establish regulatory boundaries. It has faced opposition from various groups, including religious organizations concerned about its impact on illicit activities.

<details><summary>References</summary>
<ul>
<li><a href="https://decrypt.co/371923/crypto-clarity-act-new-enemy-catholic-leaders">Crypto ’ s Clarity Act Has a New Enemy: Catholic Leaders - Decrypt</a></li>
<li><a href="https://coinunited.io/learn/en/opinions-&-insights/crypto-s-clarity-act-showdown-will-the-financial-future-be-forged-or-forgotten">Cryptos Clarity Act Showdown: Will the Financial... - CoinUnited.io</a></li>

</ul>
</details>

**Tags**: `#cryptocurrency`, `#regulation`, `#policy`, `#White House`

---

<a id="item-14"></a>
## [Vitalik Buterin: Crypto's Most Powerful Idea Not Ready Yet](https://www.coindesk.com/tech/2026/06/29/vitalik-buterin-says-crypto-s-most-powerful-idea-is-still-nowhere-near-ready) ⭐️ 6.0/10

Ethereum co-founder Vitalik Buterin stated that account abstraction, often considered crypto's most powerful idea, is still not nearly ready for mainstream use. This highlights the gap between theoretical potential and practical implementation in blockchain, affecting developers and users who await simpler, safer wallet experiences. Account abstraction aims to replace externally owned accounts (EOAs) with smart contract wallets, enabling features like social recovery and multi-factor authentication, but faces challenges in security, gas costs, and adoption.

rss · CoinDesk · Jun 29, 11:52

**Background**: Account abstraction is a proposed upgrade to Ethereum that would make user accounts more flexible and secure by allowing them to be controlled by smart contracts. Currently, Ethereum has two account types: externally owned accounts (controlled by private keys) and contract accounts (controlled by code). Account abstraction would blur this distinction, enabling features like transaction batching, sponsored transactions, and recovery mechanisms.

<details><summary>References</summary>
<ul>
<li><a href="https://ethereum.org/roadmap/account-abstraction/">Account abstraction | ethereum .org</a></li>
<li><a href="https://www.theblock.co/post/284908/vitalik-buterin-account-abstraction">Vitalik Buterin highlights account abstraction in security... | The Block</a></li>
<li><a href="https://coinmarketcap.com/academy/article/vitalik-buterin:-account-abstraction-a-"pretty-big-deal"-to-drive-web3-adoption">Vitalik Buterin : Account Abstraction a “Pretty Big...” | CoinMarketCap</a></li>

</ul>
</details>

**Tags**: `#cryptocurrency`, `#blockchain`, `#vitalik buterin`, `#ethereum`

---

<a id="item-15"></a>
## [UK Sets 2027 FCA Authorization Deadline for Crypto Firms](https://cointelegraph.com/news/uk-crypto-rules-2027-fca-authorization-deadline?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) ⭐️ 6.0/10

The UK's Financial Conduct Authority (FCA) has finalized its crypto regulatory framework, requiring all cryptocurrency firms to obtain full authorization by February 2027. This marks a major shift from the current registration regime to a comprehensive, activity-based regulatory framework, aligning crypto with traditional finance and potentially attracting institutional investors. The authorization gateway opens on September 30, 2026, and firms must comply with five core regulated activities under the Financial Services and Markets Act (FSMA).

rss · CoinTelegraph · Jun 29, 23:01

**Background**: Currently, UK crypto firms only need to register with the FCA for anti-money laundering compliance. The new framework introduces full authorization requirements similar to those for traditional financial institutions, covering areas like custody, trading, and lending. The UK aims to become a global crypto hub with these regulations.

<details><summary>References</summary>
<ul>
<li><a href="https://lasmargaritasinc.com/fca-crypto-authorization-requirements-for-exchanges-in">FCA Crypto Authorization Requirements for Exchanges in 2026</a></li>
<li><a href="https://www.ig.com/uk/trading-strategies/fca-crypto-regulation-uk-what-investors-need-to-know-260624">UK FCA crypto regulation: what Bitcoin holders need to know... - IG UK</a></li>
<li><a href="https://www.edgen.tech/news/crypto/uk-targets-crypto-hub-status-with-2027-regulatory-framework">UK Targets Crypto Hub Status With 2027 Regulatory Framework</a></li>

</ul>
</details>

**Tags**: `#cryptocurrency`, `#regulation`, `#UK`, `#FCA`

---

<a id="item-16"></a>
## [Breez SDK enables Bitcoin-to-stablecoin payments across 30+ chains](https://cointelegraph.com/news/breez-bitcoin-wallets-send-usdc-usdt-without-holding-stablecoins?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) ⭐️ 6.0/10

Breez has launched a new SDK feature that allows developers to route payments from Bitcoin balances to recipients in USDC or USDT across more than 30 blockchains, without requiring users to hold stablecoins. This innovation bridges Bitcoin and stablecoin ecosystems, enabling Bitcoin holders to spend their BTC in stablecoin-denominated transactions without converting or holding stablecoins themselves, potentially expanding Bitcoin's utility in everyday payments. The feature is part of the Breez SDK, which is built on Spark, a native Bitcoin Layer 2 solution offering instant settlement and multi-asset support. It supports over 30 blockchains including major networks like Ethereum, Solana, and Polygon.

rss · CoinTelegraph · Jun 29, 13:00

**Background**: Stablecoins like USDC and USDT are cryptocurrencies pegged to fiat currencies, commonly used for payments and DeFi. Bitcoin, while widely held, is less practical for everyday transactions due to volatility and slower settlement. Breez SDK aims to simplify Bitcoin payments by leveraging Lightning Network and now stablecoin routing.

<details><summary>References</summary>
<ul>
<li><a href="https://cryptobriefing.com/breez-bitcoin-stablecoin-payments-30-blockchains/">Breez launches Bitcoin - to - stablecoin payments across 30 blockchains</a></li>
<li><a href="https://breez.technology/sdk/">Breez SDK | Add Bitcoin to Any App or Service</a></li>
<li><a href="https://coincentral.com/breez-launches-bitcoin-to-stablecoin-payments-without-holding-usdc-or-usdt/">Breez Launches Bitcoin - to - Stablecoin Payments Without Holding...</a></li>

</ul>
</details>

**Tags**: `#Bitcoin`, `#stablecoins`, `#payments`, `#SDK`

---