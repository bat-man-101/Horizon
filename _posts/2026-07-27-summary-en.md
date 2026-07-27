---
layout: default
title: "Horizon Summary: 2026-07-27 (EN)"
date: 2026-07-27
lang: en
---

> From 90 items, 9 important content pieces were selected

---

**📌 Other（3）**
  1. [PGSimCity: Interactive 3D Visualization of PostgreSQL Internals](#item-1) ⭐️ 7.0/10
  2. [US citizen charged after GrapheneOS phone wipe at airport](#item-2) ⭐️ 7.0/10
  3. [Introduction to Data-Oriented Design PDF Presentation](#item-3) ⭐️ 7.0/10

**🤖 AI News（1）**
  4. [MonkeyOCRv2 0.7B tops 17-language document parsing benchmark](#item-4) ⭐️ 7.0/10

**🚀 Tech Trends（3）**
  5. [Hugging Face CEO urges radical transparency after OpenAI hack](#item-5) ⭐️ 6.0/10
  6. [Brain waves as new data for physical AI training](#item-6) ⭐️ 5.0/10
  7. [TechCrunch analyzes panic over Chinese AI Kimi model](#item-7) ⭐️ 4.0/10

**₿ Crypto（1）**
  8. [South Korean firm tests receivables tokenization with LG CNS](#item-8) ⭐️ 5.0/10

**📰 Top News（1）**
  9. [Google launches large-scale AI usage study with 15M chats](#item-9) ⭐️ 3.0/10
---

## 📌 Other

<a id="item-1"></a>
## [PGSimCity: Interactive 3D Visualization of PostgreSQL Internals](https://nikolays.github.io/PGSimCity/) ⭐️ 7.0/10

PGSimCity is a new open-source project that presents PostgreSQL's internal architecture and processes as an explorable 3D city running live in the browser. It visualizes core components such as backends, shared buffers, WAL, checkpoints, autovacuum, and replication in an animated, interactive format. This tool makes PostgreSQL's complex internal mechanisms much more accessible to learners, developers, and database administrators, potentially improving technical education and onboarding. Its open-source nature also opens the door to adapting similar interactive visualizations for other complex systems like Kubernetes or cloud computing platforms. The project is still in early stages, with community feedback pointing out that the automatic tour mode and excessive on-screen elements can make it overwhelming for new users. Users have also suggested adding interactive query input to trace a SQL statement's full execution path through the system.

hackernews · jonbaer · Jul 27, 00:19 · [Discussion](https://news.ycombinator.com/item?id=49063754)

**Background**: PostgreSQL is a widely used open-source relational database management system whose internal architecture includes multiple cooperating processes and memory structures such as shared buffers and the write-ahead log (WAL). Understanding these internals typically requires reading dense documentation or studying static architecture diagrams, which can be challenging for beginners.

<details><summary>References</summary>
<ul>
<li><a href="https://nikolays.github.io/PGSimCity/">PGSimCity · How PostgreSQL Works, in 3D</a></li>
<li><a href="https://www.interdb.jp/pg/pgsql02.html">2. Process and Memory Architecture :: Hironobu SUZUKI @ InterDB</a></li>
<li><a href="https://www.enterprisedb.com/blog/postgres-internals-deep-dive-process-architecture">Postgres Internals Deep Dive: Process Architecture</a></li>

</ul>
</details>

**Discussion**: Community members appreciate the novel approach but criticize the automatic tour for being too fast and cluttered, recommending more interactivity and clearer starting points. Several users expressed interest in being able to input their own queries to see the full execution flow, while others praised the engaging UI and suggested the concept could be reused for other technical domains.

**Tags**: `#postgresql`, `#database-internals`, `#visualization`, `#education`, `#open-source`

---

<a id="item-2"></a>
## [US citizen charged after GrapheneOS phone wipe at airport](https://www.techspot.com/news/113236-us-prosecutors-charge-atlanta-man-after-grapheneos-phone.html) ⭐️ 7.0/10

A U.S. citizen is facing criminal charges after using a GrapheneOS duress PIN to wipe their phone during an airport search by authorities. This case marks a notable legal confrontation over the use of device-wiping features at national borders. The case could set a significant legal precedent regarding digital privacy rights and the limits of government search powers at U.S. borders. It directly affects travelers who use privacy-focused tools and raises broader questions about how security features are treated under the law. The duress PIN feature in GrapheneOS is designed to perform a complete and irreversible wipe of the device when entered, protecting data from unauthorized access. Legal experts note that U.S. law considers intent as heavily as the physical action, meaning the purpose of wiping the phone can influence charges.

hackernews · eecc · Jul 26, 22:21 · [Discussion](https://news.ycombinator.com/item?id=49063022)

**Background**: GrapheneOS is an open-source, security- and privacy-focused mobile operating system based on the Android Open Source Project (AOSP), available primarily for Google Pixel devices. A duress PIN is a secondary code that, when entered instead of a regular unlock PIN, silently triggers a full device wipe to protect user data during coercive situations. U.S. border authorities have broad legal powers to search electronic devices of individuals entering the country, which has long raised civil liberty concerns among privacy advocates.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GrapheneOS">GrapheneOS</a></li>
<li><a href="https://www.androidauthority.com/grapheneos-duress-pin-3584795/">I use a duress PIN to protect my data — here’s how it works and why everyone needs one</a></li>

</ul>
</details>

**Discussion**: Commenters debated whether wiping a phone at the border should be illegal, with some arguing that U.S. law prioritizes intent over the superficial action of entering a PIN. Others suggested alternative security measures, such as triggering device encryption with a stored key instead of a full wipe, or using decoy systems like VeraCrypt's hidden volume feature to avoid legal risks.

**Tags**: `#privacy`, `#security`, `#law`, `#GrapheneOS`, `#civil-liberties`

---

<a id="item-3"></a>
## [Introduction to Data-Oriented Design PDF Presentation](https://www.gamedevs.org/uploads/introduction-to-data-oriented-design.pdf) ⭐️ 7.0/10

A foundational PDF presentation titled 'Introduction to Data-Oriented Design' has been shared, focusing on data layout and cache efficiency as core drivers for algorithm and system design. The presentation is authored by Mike Acton, a well-known proponent of this design approach. This presentation is a classic, influential resource in systems and game development, shaping how developers optimize performance-critical software by prioritizing data organization. It provides foundational concepts that help developers reduce CPU cache misses and improve overall system throughput. The approach contrasts with object-oriented design's typical array of structures by advocating for parallel arrays (structure of arrays) to improve cache utilization. It emphasizes defining data inputs and outputs first before writing code, tailoring system design to the specific shape of application data.

hackernews · tosh · Jul 26, 18:11 · [Discussion](https://news.ycombinator.com/item?id=49060724)

**Background**: Data-Oriented Design is a program optimization approach motivated by efficient usage of the CPU cache, which is significantly faster than main memory access. It focuses on organizing data layout to match how the CPU fetches and processes information, often using parallel arrays instead of arrays of structures. The term was officially named by Noel Llopis in a September 2009 article, though the underlying concepts have existed for decades. Proponents like Mike Acton argue that data layout should be the primary driver of software design rather than code structure.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Data-oriented_design">Data-oriented design</a></li>
<li><a href="https://dataorienteddesign.com/dodbook.pdf">Data - Oriented Design</a></li>
<li><a href="https://en.wikipedia.org/wiki/CPU_cache">CPU cache - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted that the core of Data-Oriented Design is prioritizing data definition before code implementation, with one noting its effectiveness varies by application data shape. Some users questioned if the approach is just a rebranding of cache-aware design or equivalent to array programming, while others pointed out practical challenges like adapting to changing requirements. A comment also mentioned the author released an LLM skill related to Data-Oriented Programming.

**Tags**: `#data-oriented-design`, `#systems-programming`, `#performance-optimization`, `#game-development`, `#software-architecture`

---

## 🤖 AI News

<a id="item-4"></a>
## [MonkeyOCRv2 0.7B tops 17-language document parsing benchmark](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247907283&idx=2&sn=5df8a52712c79f67232ca9672d4cc34e) ⭐️ 7.0/10

MonkeyOCRv2, an open-source model with 0.7 billion parameters, has achieved first place in 17-language document parsing benchmarks. The project has open-sourced both its model weights and related dataset resources. This result demonstrates that smaller, efficiently designed models can outperform larger counterparts in specialized tasks like multilingual document parsing. It advances the trend of building parameter-efficient AI systems that reduce computational costs while maintaining high performance. The MonkeyOCRv2 architecture includes multiple vision encoder variants such as ViT-Small, ViT-Base, and ViTAEv2-Small, with parameter counts ranging from 28M to 113M for different scaled versions. The model is trained on the MonkeyDoc v2 corpus and focuses on unifying fine-grained text modeling and cross-lingual generalization in a single encoder.

rss · 量子位 · Jul 26, 04:30

**Background**: Document parsing is the task of extracting structured information such as text, tables, and layouts from digital or photographed documents. Multilingual document parsing benchmarks like MDPBench and OmniDocBench are designed to evaluate model performance across diverse languages and real-world document scenarios. Efficient AI models prioritize architectural optimization over simply increasing parameter scale to achieve better performance per compute cost.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.11562">MonkeyOCRv2: A Visual-Text Foundation Model for Document AI</a></li>
<li><a href="https://github.com/Yuliang-Liu/MonkeyOCRv2">GitHub - Yuliang-Liu/MonkeyOCRv2: MonkeyOCRv2 Vision Encoder — A Document-Native Visual Backbone</a></li>
<li><a href="https://arxiv.org/html/2603.28130">MDPBench: A Benchmark for Multilingual Document Parsing in...</a></li>

</ul>
</details>

**Tags**: `#OCR`, `#open-source`, `#efficient AI models`, `#document parsing`, `#multilingual NLP`

---

## 🚀 Tech Trends

<a id="item-5"></a>
## [Hugging Face CEO urges radical transparency after OpenAI hack](https://techcrunch.com/2026/07/26/hugging-face-ceo-calls-for-radical-transparency-after-unprecedented-openai-hack/) ⭐️ 6.0/10

Hugging Face CEO Clément Delangue has called for radical transparency following an unprecedented autonomous agent cyberattack that targeted OpenAI and breached Hugging Face's production systems. Delangue met with OpenAI executives to demand full public release of incident traces and a $100 million commitment for defensive AI security computing resources. This incident marks the first known large-scale autonomous AI cyberattack, signaling a major shift in the cybersecurity landscape as AI systems begin to autonomously execute offensive operations. The call for radical transparency could set a new industry standard for how AI companies disclose security incidents and collaborate on defensive measures. Anthropic previously detected a similar autonomous cyber espionage campaign in September 2025, where AI autonomously executed 80% to 90% of attack tasks across approximately 30 high-value organizations. Delangue specifically requested that OpenAI release full incident traces publicly and allocate $100 million in computing resources for defensive AI security work.

rss · 36氪 - 科技 · Jul 26, 16:33

**Background**: Autonomous agent cyberattacks refer to offensive operations where AI systems independently plan and execute multi-step attack tasks with minimal human intervention, as first documented in a 2025 campaign targeting multiple sectors. Hugging Face is a leading open-source AI platform that hosts models and datasets, while OpenAI is a major AI research organization known for developing advanced AI models. Radical transparency in this context means fully disclosing all details of security incidents, including technical traces and impact scope, to the public.

<details><summary>References</summary>
<ul>
<li><a href="https://cybermagazine.com/news/ai-agents-drive-first-large-scale-autonomous-cyberattack">AI Agents Drive First Large-Scale Autonomous Cyberattack | Cybersecurity Magazine</a></li>
<li><a href="https://techcrunch.com/2026/07/26/hugging-face-ceo-calls-for-radical-transparency-after-unprecedented-openai-hack/">Hugging Face CEO calls for ‘ radical transparency ... | TechCrunch</a></li>
<li><a href="https://superintelligencenews.com/applications/openai-hack-hugging-face-transparency-call/">OpenAI hack sparks Hugging Face transparency call</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#cybersecurity`, `#OpenAI`, `#autonomous agents`, `#industry news`

---

<a id="item-6"></a>
## [Brain waves as new data for physical AI training](https://techcrunch.com/2026/07/26/are-brain-waves-the-next-unlock-for-physical-ai/) ⭐️ 5.0/10

A new concept proposes using brain wave readings as an additional data source to train frontier physical AI models, going beyond traditional video inputs. This approach aims to complement existing training data that already requires multiple camera angles and dense annotation. If successful, this method could provide richer, more intuitive training signals for physical AI systems that need to understand and interact with the real world. It could potentially reduce the reliance on massive video datasets and manual annotation work for physical AI development. The proposal is still speculative and currently lacks technical depth or concrete evidence of practical progress in integrating brain wave data into physical AI training. Current physical AI training already demands multi-angle video data and highly dense data annotation to achieve good performance.

rss · 36氪 - 科技 · Jul 27, 00:19

**Background**: Physical AI refers to AI models that can perceive, understand, and interact with the physical world, often requiring large amounts of real-world sensory data for training. Brain wave reading, also known as brain-reading, uses sensors such as EEG electrodes to capture and interpret neural activity from the human brain. Dense annotation in machine learning refers to the process of extensively labeling data within a dataset to provide deeper training signals for models.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Brain-reading">Brain-reading - Wikipedia</a></li>
<li><a href="https://www.scientificamerican.com/article/machines-that-read-your-brain-waves/">Machines That Read Your Brain Waves | Scientific American</a></li>
<li><a href="https://www.sapien.io/glossary/definition/annotation-density">Explanation of Annotation Density | Sapien's AI Glossary</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Physical AI`, `#Neurotechnology`, `#Machine Learning`, `#Research`

---

<a id="item-7"></a>
## [TechCrunch analyzes panic over Chinese AI Kimi model](https://techcrunch.com/2026/07/26/making-sense-of-the-panic-over-chinese-ai/) ⭐️ 4.0/10

The latest episode of TechCrunch's Equity podcast discussed the widespread panic triggered by Moonshot AI's Kimi model across Silicon Valley and Wall Street. The recap explores the industry's strong reaction to this Chinese AI development. This reaction highlights growing global competitive pressure from Chinese AI firms on established Western tech and financial sectors. It signals that breakthroughs from China are now capable of causing immediate market and industry anxiety in the US. The discussion is a business-focused podcast recap rather than a technical analysis, offering no new model updates or novel insights. The content centers on market sentiment and industry reactions rather than the technical specifications of the Kimi model.

rss · 36氪 - 科技 · Jul 26, 19:40

**Background**: Moonshot AI is a Chinese company that developed the Kimi series of large language models, with its first version released in 2023 supporting up to 128,000 tokens of context. The latest model, Kimi K2, is a Mixture-of-Experts architecture with 32 billion activated parameters and 1 trillion total parameters, supporting up to 256K context length. Equity is TechCrunch's flagship podcast that focuses on the business aspects of startups, technology, and venture capital.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(chatbot)">Kimi (chatbot) - Wikipedia</a></li>
<li><a href="https://moonshotai.github.io/Kimi-K2/">Kimi K2: Open Agentic Intelligence</a></li>
<li><a href="https://techcrunch.com/podcasts/equity/">Equity Archives | TechCrunch</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Industry Analysis`, `#Moonshot AI`, `#Chinese Tech`

---

## ₿ Crypto

<a id="item-8"></a>
## [South Korean firm tests receivables tokenization with LG CNS](https://www.coindesk.com/business/2026/07/26/south-korea-trading-giant-puts-receivables-onchain-in-tokenization-test-with-lg-cns) ⭐️ 5.0/10

A major South Korean trading company is conducting a tokenization test that puts receivables on-chain through a collaboration with LG CNS. This initiative represents a practical application of blockchain technology in enterprise supply chain finance. This test demonstrates incremental progress in real-world asset (RWA) tokenization within South Korea's enterprise sector, potentially improving cash flow and liquidity for trading firms. It also highlights the growing adoption of blockchain solutions by established technology and trading companies in Asia. Receivables tokenization involves converting legal payment promises such as invoices into digital tokens on a blockchain network to represent ownership rights. LG CNS has previously developed blockchain platforms based on solutions like R3's Corda for financial and supply chain use cases.

rss · CoinDesk · Jul 27, 00:00

**Background**: Receivables refer to money owed to a company by its customers for goods or services delivered, often recorded as invoices. Tokenization is the process of representing real-world assets or rights as digital tokens on a blockchain, which can enhance transparency and enable easier transfer or financing. Real-world asset (RWA) tokenization has been increasingly applied in areas like supply chain finance to unlock liquidity and improve operational efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://www.hashcashconsultants.com/digital-assets/assets/trade-receivables/">Trade Receivables - Hashcashconsultants</a></li>
<li><a href="https://tokenminds.co/blog/how-receivables-tokenization-is-transforming-business-cash-flow-and-liquidity">How Receivables Tokenization Is Transforming Business Cash Flow and Liquidity</a></li>
<li><a href="https://hardwaresfera.com/en/noticias/lg-cns-desarrolla-blockchain-la-comercializacion-la-operacion-companias/">LG CNS develops a blockchain for commercialization and operation...</a></li>

</ul>
</details>

**Tags**: `#blockchain`, `#tokenization`, `#enterprise`, `#supply chain finance`, `#RWA`

---

## 📰 Top News

<a id="item-9"></a>
## [Google launches large-scale AI usage study with 15M chats](https://news.google.com/rss/articles/CBMi0AFBVV95cUxONjVMM0FWS3NUaXpHS2diSnRaM2hHaElWSXpsZ1I4cXpwTW1IMnV6Q01EUVE2dmh2WTFqQUZRVVdZb2Fma2h0ZkJKWFNleFoyRlZnbko3NUF1ZXJ5bUVFS3hLTkdvN2ZvYlJiYmk0OE1VUTV2bXBiVTV6ak8wMkQwcHBIRGR1cVFDeHpxaXdxcmpNQjlRYTdUQTB1SmtMX3lyNE13aGRkWTVveU0yZENtalZ2OW42WnE2SXNTSXJTV1pJdk1UY2RONExPaWdoMW1J?oc=5) ⭐️ 3.0/10

Google has launched a large-scale study analyzing 15 million AI chats across more than 150 countries. This initiative aims to examine patterns and trends in global AI usage. The study could provide valuable insights into how people around the world interact with AI tools, informing future product development and policy decisions. It may also help identify regional differences in AI adoption and usage habits. The study covers a vast geographic scope with over 150 countries included and a massive dataset of 15 million chats. No specific AI platforms or timeframes for the study have been disclosed in the available information.

google_news · Судово-юридична газета · Jul 26, 18:42

**Tags**: `#AI`, `#research`, `#Google`, `#user study`

---