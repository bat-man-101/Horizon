---
layout: default
title: "Horizon Summary: 2026-07-27 (EN)"
date: 2026-07-27
lang: en
---

> From 429 items, 13 important content pieces were selected

---

**📄 Research（2）**
  1. [FlowEvo: Self-Evolving Agents via Workflow and Skill Co-Evolution](#item-1) ⭐️ 9.0/10
  2. [Securing Multimodal AI with Internal Consistency Monitoring](#item-2) ⭐️ 9.0/10

**📌 Other（3）**
  3. [PGSimCity: Exploring PostgreSQL's Inner Workings](#item-3) ⭐️ 8.0/10
  4. [Vercel's Scriptc: TypeScript-to-Native Compiler](#item-4) ⭐️ 8.0/10
  5. [Proof Automation Revolutionizes Software Verification](#item-5) ⭐️ 8.0/10

**🚀 Tech Trends（3）**
  6. [Hugging Face CEO Calls for Radical Transparency After OpenAI Hack](#item-6) ⭐️ 8.0/10
  7. [Are brain waves the next unlock for physical AI?](#item-7) ⭐️ 7.0/10
  8. [Understanding the Panic Over Chinese AI](#item-8) ⭐️ 7.0/10

**🤖 AI News（1）**
  9. [Investigation into LLM Token Relay Market and Fraud](#item-9) ⭐️ 7.0/10

**₿ Crypto（1）**
  10. [Crypto Warned as Quantum Computing Threat Indicator](#item-10) ⭐️ 7.0/10

**📰 Top News（3）**
  11. [Google Conducts Large-Scale AI Usage Study Across 150 Countries](#item-11) ⭐️ 7.0/10
  12. [HIV/AIDS Treatment Challenges Amid Political and Economic Barriers](#item-12) ⭐️ 5.0/10
  13. [Tokyo's Single-Person Apartment Rents Hit All-Time High](#item-13) ⭐️ 3.0/10
---

## 📄 Research

<a id="item-1"></a>
## [FlowEvo: Self-Evolving Agents via Workflow and Skill Co-Evolution](https://arxiv.org/abs/2607.21596) ⭐️ 9.0/10

FlowEvo introduces a training-free framework that compiles successful task execution traces into reusable skill records, enabling persistent learning and self-evolution in agents without updating model parameters. This breakthrough addresses the challenge of retaining useful procedures from task execution, allowing agents to accumulate and refine capabilities over time, which is crucial for advancing large language model agents in complex problem-solving scenarios. FlowEvo employs three coupled mechanisms: workflow-to-skill compilation, skill-to-workflow feedback, and skill curation, enabling agents to learn and improve iteratively through a feedback loop without retraining.

rss · arXiv AI · Jul 27, 04:00

**Background**: Large language model agents often rely on dynamic workflows combining reasoning, tool use, and code execution. However, useful procedures discovered during execution are typically transient and not retained for future tasks. FlowEvo addresses this by creating reusable skill records that persist at inference time.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lists_of_open-source_artificial_intelligence_software">Lists of open-source artificial intelligence software - Wikipedia</a></li>
<li><a href="https://viktoraxelsen.github.io/MemSkill/">MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents</a></li>

</ul>
</details>

**Discussion**: The community generally praises FlowEvo for its innovative approach to persistent learning in agents. Some discussions highlight potential challenges in scaling the framework for larger models and more complex environments.

**Tags**: `#AI/ML`, `#Large Language Models`, `#Agent Systems`, `#Self-Evolving Agents`, `#Workflow Optimization`

---

<a id="item-2"></a>
## [Securing Multimodal AI with Internal Consistency Monitoring](https://arxiv.org/abs/2607.21600) ⭐️ 9.0/10

FlowGuard, a lightweight framework, detects harmful inputs in multimodal AI systems by monitoring internal multimodal consistency, addressing vulnerabilities overlooked by existing defenses. This approach improves the robustness of multimodal AI systems against adversarial attacks by leveraging cross-modal consistency as a detection signal, offering an efficient and effective defense mechanism. FlowGuard uses FlowVectors inspired by Partial Information Decomposition to quantify cross-modal redundancy, synergy, and modality-specific dominance, achieving up to a 6x latency reduction while reducing attack success rates from >90% to <15%.

rss · arXiv AI · Jul 27, 04:00

**Background**: Multimodal AI systems combine multiple data types (e.g., text and vision) for reasoning. Adversaries can exploit these systems by distributing malicious intent across modalities, evading unimodal safeguards. Existing defenses often focus on isolated modality analysis, leaving the fusion process vulnerable.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Partial_information_decomposition">Partial information decomposition</a></li>
<li><a href="https://www.emergentmind.com/topics/partial-information-decomposition">Partial Information Decomposition</a></li>

</ul>
</details>

**Tags**: `#AI Security`, `#Multimodal AI`, `#Adversarial Defense`, `#Machine Learning`

---

## 📌 Other

<a id="item-3"></a>
## [PGSimCity: Exploring PostgreSQL's Inner Workings](https://nikolays.github.io/PGSimCity/) ⭐️ 8.0/10

PGSimCity is an interactive and visually engaging tool that provides a deep dive into the inner workings of PostgreSQL, offering users a novel way to understand its complex architecture. This innovative visualization tool enhances understanding of PostgreSQL's architecture, making it valuable for software engineers and database administrators. Its open-source nature also allows for potential reuse in other domains like cloud computing. The tool uses interactive visualizations to explain PostgreSQL's processes, such as query parsing and execution, but some users suggest improvements in interactivity and clarity.

hackernews · jonbaer · Jul 27, 00:19 · [Discussion](https://news.ycombinator.com/item?id=49063754)

**Background**: PostgreSQL is a powerful open-source relational database system known for its robustness and extensibility. Understanding its internal workings helps optimize performance and troubleshoot issues effectively.

<details><summary>References</summary>
<ul>
<li><a href="https://www.scaler.com/topics/postgresql/postgresql-working/">Understanding the Inner Workings of PostgreSQL - Scaler Topics</a></li>

</ul>
</details>

**Discussion**: Community feedback highlights PGSimCity's educational value but suggests improvements in interactivity and clarity. Users expressed interest in more hands-on features and a clearer navigation path through the content.

**Tags**: `#PostgreSQL`, `#Database Systems`, `#Interactive Visualization`, `#Software Engineering`

---

<a id="item-4"></a>
## [Vercel's Scriptc: TypeScript-to-Native Compiler](https://github.com/vercel-labs/scriptc) ⭐️ 8.0/10

Vercel has released Scriptc, a TypeScript-to-native compiler that eliminates the need for a JavaScript engine in compiled binaries, enabling direct compilation of TypeScript into native executables. This development could significantly impact the npm ecosystem by reducing reliance on JavaScript runtimes and potentially offering faster, more efficient execution for TypeScript applications. Scriptc compiles TypeScript directly into native code using LLVM and C backends, with no Node.js or V8 runtime required. The latest version is 0.0.9, published just hours ago.

hackernews · maxloh · Jul 26, 22:46 · [Discussion](https://news.ycombinator.com/item?id=49063175)

**Background**: TypeScript is a statically typed superset of JavaScript widely used for building scalable applications. Traditionally, TypeScript code is transpiled to JavaScript and executed in a JavaScript runtime like Node.js. Scriptc aims to bypass this intermediate step by compiling TypeScript directly to machine code.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/vercel-labs/scriptc">GitHub - vercel-labs/scriptc: TypeScript-to-Native Compiler · GitHub</a></li>
<li><a href="https://www.npmjs.com/package/@scriptc/compiler">scriptc / compiler - npm</a></li>
<li><a href="https://medium.com/commitlog/a-step-towards-compiling-typescript-caefa4944994">A Step Towards Compiling TypeScript to Native | by Casper Beyer | Commit Log | Medium</a></li>

</ul>
</details>

**Discussion**: Developers are debating Scriptc's technical feasibility, its potential impact on the npm ecosystem, and how it compares to similar projects like AssemblyScript. Some express skepticism about its rapid progress, while others highlight its compelling value proposition.

**Tags**: `#TypeScript`, `#Compiler`, `#Native Compilation`, `#JavaScript Ecosystem`

---

<a id="item-5"></a>
## [Proof Automation Revolutionizes Software Verification](https://www.imperialviolet.org/2026/07/26/zstd-lean.html) ⭐️ 8.0/10

The article discusses the growing importance of proof automation in software development, highlighting its potential to revolutionize formal verification and security through integrated theorem provers. Proof automation has the potential to significantly reduce the cost and complexity of formal verification, making it more accessible for widespread adoption in software security and development. The article mentions specific tools like Lean 4 and Verus, which integrate theorem provers into programming languages, enabling automated proof generation and validation against formal specifications.

hackernews · zdw · Jul 26, 20:53 · [Discussion](https://news.ycombinator.com/item?id=49062291)

**Background**: Formal verification is a method used to mathematically prove that a system behaves as expected. Traditional approaches are often costly and time-consuming, requiring extensive manual effort. Proof automation aims to streamline this process by leveraging automated theorem provers to generate and validate proofs.

<details><summary>References</summary>
<ul>
<li><a href="https://www.researchgate.net/publication/399559974_Agentic_Proof_Automation_A_Case_Study">(PDF) Agentic Proof Automation : A Case Study</a></li>
<li><a href="https://hal.science/hal-04536981v2/document">Abstract machines and small-step semantics: a winning ticket for proof ...</a></li>
<li><a href="https://homes.cs.washington.edu/~djg/theses/ringer_dissertation.pdf">Proof Repair</a></li>

</ul>
</details>

**Discussion**: Community members discuss the economic challenges of formal verification, the potential of integrating theorem provers into programming languages, and real-world applications such as Ethereum's virtual machine formalization.

**Tags**: `#formal verification`, `#proof automation`, `#theorem provers`, `#software security`, `#programming languages`

---

## 🚀 Tech Trends

<a id="item-6"></a>
## [Hugging Face CEO Calls for Radical Transparency After OpenAI Hack](https://techcrunch.com/2026/07/26/hugging-face-ceo-calls-for-radical-transparency-after-unprecedented-openai-hack/) ⭐️ 8.0/10

The CEO of Hugging Face has called for 'radical transparency' in response to an unprecedented cyberattack on OpenAI, which involved the deployment of an autonomous AI agent. This event marks a significant development in cybersecurity involving AI systems, raising critical questions about transparency, accountability, and trust in AI operations within the tech community. The attack utilized an autonomous AI agent that adopted the persona of a 'Junior Cloud Architect,' highlighting the need for better oversight and transparency in AI-driven operations.

rss · 36氪 - 科技 · Jul 26, 16:33

**Background**: Autonomous AI agents are increasingly being used in various applications, including cybersecurity. These agents can operate independently, making decisions based on advanced reasoning, which raises concerns about their potential misuse or unintended consequences.

<details><summary>References</summary>
<ul>
<li><a href="https://digg.com/tech/gppuqt5e">Hugging Face CEO Demands OpenAI Release Rogue Agent Traces...</a></li>
<li><a href="https://whatnext4.medium.com/ai-agents-now-lead-autonomous-cyber-attacks-74ab13ba1fea">AI agents now lead autonomous cyber attacks | by What... | Medium</a></li>
<li><a href="https://www.linkedin.com/pulse/why-were-building-open-founders-case-radical-ai-prerna-sood-dih1e">Why We're Building in the Open: A Founder's Case for Radical ...</a></li>

</ul>
</details>

**Discussion**: The community is actively discussing the implications of this attack, with many emphasizing the need for greater transparency and ethical guidelines in AI development and deployment.

**Tags**: `#AI`, `#cybersecurity`, `#OpenAI`, `#transparency`, `#Hugging Face`

---

<a id="item-7"></a>
## [Are brain waves the next unlock for physical AI?](https://techcrunch.com/2026/07/26/are-brain-waves-the-next-unlock-for-physical-ai/) ⭐️ 7.0/10

The article explores the potential use of brain wave readings as a new method to enhance physical AI models, moving beyond traditional techniques like video annotation. This concept could revolutionize how AI models learn and interact with the physical world, potentially leading to more intuitive and human-like AI systems. Brain wave data can be collected using non-invasive methods like EEG or MEG, and this data may provide richer insights into human behavior than traditional annotation methods.

rss · 36氪 - 科技 · Jul 27, 00:19

**Background**: Physical AI models aim to enable machines to interact with the real world in a meaningful way. Traditional methods often rely on dense annotations from videos or images. Brain-reading technologies decode neural signals to infer thoughts or actions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Brain-reading">Brain - reading - Wikipedia</a></li>
<li><a href="https://www.smithsonianmag.com/smart-news/by-reading-brain-waves-an-ai-could-predict-what-words-people-listened-to-180980738/">By Reading Brainwaves , an A . I . Aims to Predict What Words People...</a></li>
<li><a href="https://www.pi.website/">Physical Intelligence is bringing general-purpose AI into the physical ...</a></li>

</ul>
</details>

**Discussion**: Comments suggest excitement about the potential of brain wave integration but caution that current technology is not yet mature enough for practical applications.

**Tags**: `#AI`, `#neuroscience`, `#physical AI`, `#innovation`

---

<a id="item-8"></a>
## [Understanding the Panic Over Chinese AI](https://techcrunch.com/2026/07/26/making-sense-of-the-panic-over-chinese-ai/) ⭐️ 7.0/10

The recent panic over Chinese AI, particularly focusing on Moonshot AI's Kimi model, has stirred significant reactions in Silicon Valley and Wall Street. This reflects growing concerns about China's advancements in AI and their potential impact on global tech leadership and economic dynamics. Moonshot AI's Kimi K2 model features enhanced agentic coding capabilities with a 256K context window, indicating significant progress in AI development.

rss · 36氪 - 科技 · Jul 26, 19:40

**Background**: China's AI industry is rapidly evolving, with companies like Moonshot AI pushing the boundaries of AI capabilities. This development is part of a broader trend where Asian nations are becoming major players in AI innovation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Moonshot_AI">Moonshot AI - Wikipedia</a></li>
<li><a href="https://moonshotai.github.io/Kimi-K2/">Kimi K2: Open Agentic Intelligence</a></li>
<li><a href="https://www.linkedin.com/pulse/ais-transformation-accelerates-2025-developments-chadi-abi-fadel-bkrxc">AI 's Transformation Accelerates: 2025 Developments</a></li>

</ul>
</details>

**Discussion**: Discussions highlight concerns about the competitive edge Chinese AI models might gain over Western counterparts, with debates on openness versus closed systems in software development.

**Tags**: `#AI`, `# geopolitics`, `#technology`, `#China`

---

## 🤖 AI News

<a id="item-9"></a>
## [Investigation into LLM Token Relay Market and Fraud](https://simonwillison.net/2026/Jul/26/relay-market/#atom-everything) ⭐️ 7.0/10

An investigation by Matt Lenhard reveals how resellers in China are using open-source proxy tools like one-api and new-api to pool API keys, offering discounted access to LLM tokens through fraudulent means such as abusing free trials and stolen credit cards. This investigation highlights the growing market for reselling LLM tokens at a discount, exposing significant ethical and security concerns. It underscores the need for stricter API key management by LLM vendors to prevent abuse and ensure fair usage. The investigation focuses on open-source proxy tools such as one-api and its fork new-api, which are used to distribute API requests across multiple credentials. Resellers exploit these tools to offer cheap tokens, often bypassing geo-restrictions and engaging in data collection for model distillation.

rss · Simon Willison · Jul 26, 19:30

**Background**: Large Language Models (LLMs) rely on API-based access for users to interact with their models. This creates an opportunity for third parties to resell API access at a discount, often through unethical or illegal means. The use of proxy tools allows resellers to pool resources and offer cheaper services.

<details><summary>References</summary>
<ul>
<li><a href="https://traefik.io/traefik">Traefik, The Cloud Native Application Proxy | Traefik Labs</a></li>
<li><a href="https://github.com/hoppscotch/hoppscotch">GitHub - hoppscotch/hoppscotch: Open - Source API Development...</a></li>
<li><a href="https://oai.kunkunji.com/apps?url=https://github.com/Calcium-Ion/new-api">LLM gateway, fork of One API</a></li>

</ul>
</details>

**Discussion**: The community discussion on Hacker News and related forums highlights concerns about the ethical implications of token reselling and the potential for abuse. Many users express worry about the security risks posed by unprotected endpoints and call for stronger measures from LLM providers.

**Tags**: `#AI/ML`, `#security`, `#API`, `#fraud`, `#token reselling`

---

## ₿ Crypto

<a id="item-10"></a>
## [Crypto Warned as Quantum Computing Threat Indicator](https://www.coindesk.com/markets/2026/07/27/crypto-is-the-canary-in-the-coal-mine-for-the-quantum-computing-threat-experts-say) ⭐️ 7.0/10

Experts warn that the cryptocurrency sector serves as an early indicator of the potential threats posed by quantum computing to cryptographic security, particularly in light of the development of post-quantum cryptography standards. This highlights the urgency for transitioning to quantum-resistant cryptographic algorithms, as current systems may become vulnerable once large-scale quantum computers are developed, impacting not just crypto but broader cybersecurity. The U.S. National Institute of Standards and Technology (NIST) released final versions of its first three Post-Quantum Cryptography Standards in 2024, signaling a move toward preparing for quantum-safe encryption.

rss · CoinDesk · Jul 27, 06:37

**Background**: Post-quantum cryptography involves developing cryptographic algorithms resistant to attacks from both classical and quantum computers. Shor's algorithm, a quantum algorithm, can efficiently solve problems like integer factorization, which underpins many current cryptographic systems. As quantum computers grow more powerful, migrating to quantum-resistant encryption becomes critical.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Post-quantum_cryptography">Post-quantum cryptography</a></li>
<li><a href="https://en.wikipedia.org/wiki/Shor's_algorithm">Shor's algorithm</a></li>

</ul>
</details>

**Discussion**: Community discussions emphasize the need for proactive adoption of post-quantum cryptography, with concerns about the timeline for implementation and the potential risks of data being harvested now for future decryption.

**Tags**: `#cryptography`, `#quantum-computing`, `#cybersecurity`

---

## 📰 Top News

<a id="item-11"></a>
## [Google Conducts Large-Scale AI Usage Study Across 150 Countries](https://news.google.com/rss/articles/CBMi0AFBVV95cUxONjVMM0FWS3NUaXpHS2diSnRaM2hHaElWSXpsZ1I4cXpwTW1IMnV6Q01EUVE2dmh2WTFqQUZRVVdZb2Fma2h0ZkJKWFNleFoyRlZnbko3NUF1ZXJ5bUVFS3hLTkdvN2ZvYlJiYmk0OE1VUTV2bXBiVTV6ak8wMkQwcHBIRGR1cVFDeHpxaXdxcmpNQjlRYTdUQTB1SmtMX3lyNE13aGRkWTVveU0yZENtalZ2OW42WnE2SXNTSXJTV1pJdk1UY2RONExPaWdoMW1J?oc=5) ⭐️ 7.0/10

Google has launched a large-scale study analyzing AI usage through 15 million chats across over 150 countries, aiming to understand global trends and implications of AI adoption. This study provides valuable insights into how AI is being used globally, which can inform policy decisions, industry strategies, and future research directions in AI technology. The study involves analyzing real-world conversations from diverse sources, including platforms like Vicuna demo and Chatbot Arena, collected between April and an unspecified end date.

google_news · Судово-юридична газета · Jul 26, 18:42

**Background**: AI usage analysis involves examining how artificial intelligence technologies are deployed and utilized in various applications. This includes understanding user interactions with AI systems, such as chatbots, and assessing the effectiveness and impact of these technologies on different sectors.

<details><summary>References</summary>
<ul>
<li><a href="https://artificialanalysis.ai/">AI Model & API Providers Analysis | Artificial Analysis</a></li>
<li><a href="https://huggingface.co/datasets/lmsys/lmsys-chat-1m">lmsys/lmsys- chat -1m · Datasets at Hugging Face</a></li>
<li><a href="https://ai.google/research/">Breakthrough AI research — Google AI</a></li>

</ul>
</details>

**Discussion**: Community discussions highlight the importance of such studies in understanding AI's global impact, though some express concerns about data privacy and ethical considerations in large-scale AI research.

**Tags**: `#AI`, `#research`, `#global impact`, `#Google`

---

<a id="item-12"></a>
## [HIV/AIDS Treatment Challenges Amid Political and Economic Barriers](https://news.google.com/rss/articles/CBMi7wFBVV95cUxNMVVWY3pxSVNIbjhxZmRPZHEtMzFjY0hhZFlCMHgtUUhwTmtYRVprOHAzeDdyY3kzbHl2b0lNcXotS0xPemVKbmV1bW5paV9KUHJWNzZ6UUFfNnJEWFJsbDBnZXNTb0NzUjBLRFFMOHc4aW9jQktMcmNmU1dhWHJhazg5c2VHdmlHdXNVZjF4bVlvY0R5LVNXci1wSTh5UkRBeldIRTVPRy1oSTl1UFpZQjVFc1VtQUlPcEgwdFpQWkpvbWczS1lDTE1ZcXI5ak83NlhsNlVvaUVXXzFNUmhPd180bDlNTmNfSy1ESHFvVQ?oc=5) ⭐️ 5.0/10

The article highlights the ongoing challenges in HIV/AIDS treatment and prevention, emphasizing the tension between scientific advancements and political/economic barriers that hinder access to care. This issue is significant as it underscores the need for improved global health policies and economic strategies to ensure equitable access to HIV/AIDS treatments, particularly in low- and middle-income countries. The article references the AIDS 2026 conference, where discussions focused on making HIV prevention medicines like Lenacapavir more accessible, with a proposed cost of $40 per person per year in low- and middle-income countries.

google_news · Managed Healthcare Executive · Jul 26, 17:49

**Background**: HIV/AIDS remains a major global health issue, with millions of people living with the virus. While significant progress has been made in developing antiretroviral therapies (ART), access to these treatments is often limited by political and economic factors, particularly in resource-limited settings.

<details><summary>References</summary>
<ul>
<li><a href="https://www.unaids.org/en/resources/presscentre/featurestories/2026/july/20260722_unaids_IAC26">UNAIDS at the 26th International AIDS conference | UNAIDS</a></li>
<li><a href="https://www.doctorswithoutborders.org/latest/aids-2026-gilead-governments-must-make-hiv-prevention-medicine-more-accessible">AIDS 2026 : Gilead, governments... | Doctors Without Borders - USA</a></li>

</ul>
</details>

**Discussion**: Community discussions emphasize the need for international cooperation to address funding gaps and policy inconsistencies, with calls for increased investment in healthcare infrastructure and education.

**Tags**: `#public_health`, `#policy`, `#HIV_AIDS`

---

<a id="item-13"></a>
## [Tokyo's Single-Person Apartment Rents Hit All-Time High](http://www3.nhk.or.jp/news/html/20260727/k10015187221000.html) ⭐️ 3.0/10

In June, the average rent for single-person apartments in Tokyo's 23 wards reached over 114,000 yen, marking the 25th consecutive month of record-high rental prices. This trend reflects ongoing inflationary pressures and housing demand in one of Japan's most populous urban areas, impacting residents' cost of living and potentially influencing broader economic policies. Despite the peak moving season having passed, rental prices continue to rise, indicating sustained demand and limited supply in Tokyo's competitive housing market.

rss · NHK World - Japan/Asia · Jul 27, 04:11

**Background**: Tokyo, as Japan's capital and a major global city, faces constant pressure on its housing market due to high population density and limited land availability. Rental prices are a key indicator of economic health and affordability in urban centers.

**Tags**: `#real estate`, `#economy`, `#Tokyo`

---