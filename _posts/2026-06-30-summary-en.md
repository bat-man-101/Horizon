---
layout: default
title: "Horizon Summary: 2026-06-30 (EN)"
date: 2026-06-30
lang: en
---

> From 127 items, 6 important content pieces were selected

---

1. [Supreme Court Rules Geofence Warrants Need Constitutional Protections](#item-1) ⭐️ 9.0/10
2. [Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding](#item-2) ⭐️ 8.0/10
3. [Washington Post Tests AI Chatbots for Political Bias](#item-3) ⭐️ 8.0/10
4. [BNY Mellon Adds USDC Minting and Redemption for Institutions](#item-4) ⭐️ 7.0/10
5. [Patients Bring AI Tools into Therapy Sessions](#item-5) ⭐️ 7.0/10
6. [Rethinking AI Governance: Key Questions](#item-6) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Supreme Court Rules Geofence Warrants Need Constitutional Protections](https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision) ⭐️ 9.0/10

The US Supreme Court ruled that geofence warrants, which compel tech companies to provide location data of all devices within a specified area, must comply with Fourth Amendment protections against unreasonable searches and seizures. This landmark decision significantly limits law enforcement's ability to conduct mass digital surveillance without individualized suspicion, setting a crucial precedent for privacy rights in the digital age. The case involved a bank robbery where Google provided location data from 19 devices within 150 meters of the bank. The Court held that accessing such historical location data constitutes a Fourth Amendment search requiring a warrant based on probable cause.

hackernews · cdrnsf · Jun 29, 15:54 · [Discussion](https://news.ycombinator.com/item?id=48720924)

**Background**: A geofence warrant, also known as a reverse location warrant, allows law enforcement to search a company's database for all mobile devices within a virtual perimeter (geofence) during a specific time. These warrants have become controversial because they can sweep up data from innocent bystanders. The Fourth Amendment protects against unreasonable searches, and the Supreme Court has previously extended its protections to digital data in cases like Riley v. California and Carpenter v. United States.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Geofence_warrant">Geofence warrant - Wikipedia</a></li>
<li><a href="https://www.brennancenter.org/our-work/policy-solutions/fourth-amendment-digital-age">The Fourth Amendment in the Digital Age | Brennan Center for Justice</a></li>

</ul>
</details>

**Discussion**: Commenters largely praised the ruling as a win for privacy, with some noting the Court's use of factual sources in its opinion. Others raised questions about implications for other surveillance technologies like automated license plate readers, while a few criticized dissenting justices for favoring unlimited government power.

**Tags**: `#privacy`, `#supreme court`, `#surveillance`, `#digital rights`, `#law`

---

<a id="item-2"></a>
## [Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding](https://simonwillison.net/2026/Jun/29/ornith/#atom-everything) ⭐️ 8.0/10

DeepReinforce released Ornith-1.0, a family of open-weight (MIT licensed) LLMs for agentic coding, with sizes from 9B to 397B, built on Gemma 4 and Qwen 3.5. It achieves state-of-the-art performance among open-source models of comparable size on coding benchmarks. Ornith-1.0 introduces a self-scaffolding training framework where the model learns to generate both solution rollouts and task-specific harnesses, enabling self-improvement without human-designed scaffolds. This could significantly advance open-source agentic coding capabilities and make powerful coding assistants accessible on local hardware. The model family includes 9B Dense, 31B Dense, 35B MoE, and 397B MoE variants, all under MIT license. Early user reports indicate it produces shorter chain-of-thought, making it up to 3x faster than comparable models like Qwen 3.6 35B, while maintaining high coding performance.

rss · Simon Willison · Jun 29, 16:17

**Background**: Agentic coding refers to LLMs that can autonomously use tools (e.g., code editors, terminals) to solve programming tasks. Traditional approaches rely on hand-crafted scaffolds (harnesses) to guide the model's tool use. Ornith-1.0's self-scaffolding innovation allows the model to learn its own scaffolding strategy during training, improving both efficiency and effectiveness.

<details><summary>References</summary>
<ul>
<li><a href="https://deep-reinforce.com/ornith_1_0.html">Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding | DeepReinforce Blog | Jun. 2026</a></li>
<li><a href="https://essamamdani.com/blog/ornith-1-0-self-scaffolding-llm-coding-2026">Ornith-1.0: The Self-Scaffolding LLM That Teaches Itself to Code Better | Essa Mamdani | Essa Mamdani</a></li>
<li><a href="https://huggingface.co/deepreinforce-ai">deepreinforce-ai (DeepReinforce)</a></li>

</ul>
</details>

**Discussion**: Community feedback is largely positive: users find Ornith-1.0 more useful than previous local models, with one noting it is the first Qwen fine-tune not immediately rejected. Another user reports it is slightly better than Qwen 3.6 35B and up to 3x faster due to shorter chain-of-thought. Some users question the novelty and ask for more details about the self-improvement mechanism.

**Tags**: `#LLM`, `#open-source`, `#coding`, `#AI agents`, `#model release`

---

<a id="item-3"></a>
## [Washington Post Tests AI Chatbots for Political Bias](https://news.google.com/rss/articles/CBMixwFBVV95cUxNcjNMZk5ZYVBRRHlTbDJrZl85THhCTHJvczVHMzlPcnpUdndRdkV1NGZoNFdvMzNBLVdZaHZpS0tEY1dfWFBYTWtKUXpnQzhFa09vMXBHYmNuOEV3TmJuRWVXeTFvQW1adlNBRDg2R0NBUEhQLXlwdWZHVHNLRUVXYjdRUk9FTjFXSDRGenUyZkZxMkdZelk4OWF5VGI4S2Q4U3lyQUpEWEROTFJLUlM3alNwaEQtV1FveVU4bjV1dW1SM3ZvenFZ?oc=5) ⭐️ 8.0/10

The Washington Post conducted a systematic test of major AI chatbots, including ChatGPT, to evaluate their political bias and published the findings. This investigation highlights potential political bias in widely used AI systems, raising concerns about fairness and trustworthiness in AI-generated content. The test methodology likely involved presenting politically charged prompts to chatbots and analyzing the responses for partisan leanings.

google_news · The Washington Post · Jun 30, 01:23

**Background**: AI chatbots like ChatGPT are trained on large datasets from the internet, which may contain biased or unbalanced political viewpoints. Evaluating and mitigating such bias is a key challenge in AI ethics and responsible deployment.

<details><summary>References</summary>
<ul>
<li><a href="https://www.fluence.network/blog/llm-evaluation-framework/">LLM Evaluation Framework for RAG and AI Agents</a></li>
<li><a href="https://www.langchain.com/resources/how-to-evaluate-llms">Evaluating LLMs and Agents: Benchmarks, Evals & Guardrails</a></li>
<li><a href="https://openfabric.ai/blog/llm-evaluation-methodologies-a-deep-dive-into-llm-evals">LLM Evaluation methodologies : A Deep Dive into LLM Evals</a></li>

</ul>
</details>

**Tags**: `#AI bias`, `#ChatGPT`, `#political bias`, `#AI ethics`, `#LLM evaluation`

---

<a id="item-4"></a>
## [BNY Mellon Adds USDC Minting and Redemption for Institutions](https://www.coindesk.com/business/2026/06/29/wall-street-s-bny-expands-stablecoin-services-for-institutions-starting-with-circle-s-usdc) ⭐️ 7.0/10

BNY Mellon has expanded its Digital Asset Custody platform to support Circle's USDC, allowing institutional clients to store, transfer, mint, and redeem the stablecoin directly through the bank. This move marks a significant step in mainstream adoption of stablecoins by traditional finance, as a major Wall Street custodian now offers integrated stablecoin services to institutional investors. USDC is the first stablecoin available on BNY Mellon's platform, and the bank already serves as the primary custodian of USDC reserves, deepening its partnership with Circle.

rss · CoinDesk · Jun 29, 14:46

**Background**: BNY Mellon, custodian of $46.7 trillion in assets, became the first U.S. bank approved by both the SEC and NY DFS to hold Bitcoin and Ethereum for institutional clients in October 2022. Stablecoins like USDC are digital tokens pegged to fiat currency, enabling efficient on-chain transactions. Minting and redemption refer to the creation and conversion of stablecoins to and from fiat currency.

<details><summary>References</summary>
<ul>
<li><a href="https://cointelegraph.com/news/bny-adds-usdc-minting-and-redemption-to-institutional-custody-platform">BNY adds USDC minting and redemption to institutional custody ...</a></li>
<li><a href="https://tokenmetrics.com/usdc/news/bny-usdc-minting-institutional-custody/">BNY Adds USDC Minting To Institutional Custody Platform</a></li>
<li><a href="https://cryptobriefing.com/bny-mellon-usdc-digital-asset-custody/">BNY Mellon integrates USDC as first stablecoin on Digital Asset...</a></li>

</ul>
</details>

**Tags**: `#stablecoins`, `#institutional crypto`, `#BNY Mellon`, `#USDC`, `#fintech`

---

<a id="item-5"></a>
## [Patients Bring AI Tools into Therapy Sessions](https://news.google.com/rss/articles/CBMibEFVX3lxTE1WWnJKR2tRSjN0dk1PajZUX085VmM3aGxKZWRJWGNnTjVvSHZSZWlnd05oM2llajF6YXBDRV8zOTRFRjV6ZTF2SW5FUUh2UU5OLVNMN0tYX2k2cXZvZHFvU2c5UXF6OHNJY3lieQ?oc=5) ⭐️ 7.0/10

Patients are increasingly using AI tools like chatbots and language models during therapy sessions, a trend highlighted by the American Psychological Association. This trend challenges traditional therapeutic boundaries and raises ethical questions about privacy, efficacy, and the therapist's role, potentially reshaping mental health practice. The APA report notes that some patients use AI for self-diagnosis, emotional support, or to prepare for sessions, while therapists grapple with how to integrate these tools responsibly.

google_news · American Psychological Association (APA) · Jun 30, 07:22

**Background**: AI in mental health is growing, with apps offering therapy-like interactions. However, patients bringing their own AI into formal therapy is a newer phenomenon that blurs the line between professional and self-help.

**Tags**: `#AI in healthcare`, `#mental health`, `#therapy`, `#ethics`, `#AI adoption`

---

<a id="item-6"></a>
## [Rethinking AI Governance: Key Questions](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPaXhGeDlGNzRDMkVFUmlGYmFFamh1SWZoRi1rNl9FeHhSZERYTExoZXNHNHloaTRtbzFEa25WNkRNOG9nN1NoUHdkT2R5T2JpYS1BbGR2bjZBd1B1RmNDSDZqTmk1UzdfWHUyX0IzM1lJWkVlRWlQeTNtNUZHdXg3LWJKMFhudDM1?oc=5) ⭐️ 7.0/10

MIT Sloan Management Review published an article arguing that the central question for AI governance is not about controlling AI but about how to design systems that align with human values and societal goals. This perspective shifts the debate from fear-based regulation to proactive design, influencing how policymakers and organizations approach AI ethics and governance frameworks. The article emphasizes that governance should focus on the purpose and context of AI use, rather than solely on technical capabilities or risks.

google_news · MIT Sloan Management Review · Jun 30, 11:00

**Background**: AI governance refers to the policies, laws, and frameworks that guide the development and deployment of artificial intelligence. Current debates often center on risks like bias, privacy, and job displacement.

**Tags**: `#AI governance`, `#artificial intelligence`, `#policy`, `#ethics`

---