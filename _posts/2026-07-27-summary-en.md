---
layout: default
title: "Horizon Summary: 2026-07-27 (EN)"
date: 2026-07-27
lang: en
---

> From 84 items, 10 important content pieces were selected

---

**📌 Other（3）**
  1. [GrapheneOS details locked device data extraction protections](#item-1) ⭐️ 8.0/10
  2. [Focus and Followthrough as Key AI Adoption Differentiators](#item-2) ⭐️ 7.0/10
  3. [Underground relay market fuels AI token reselling fraud](#item-3) ⭐️ 7.0/10

**🤖 AI News（1）**
  4. [MonkeyOCRv2 0.7B model tops 17-language document parsing](#item-4) ⭐️ 7.0/10

**🚀 Tech Trends（3）**
  5. [Brain waves as new data for physical AI training](#item-5) ⭐️ 6.0/10
  6. [Hugging Face CEO urges radical transparency after OpenAI hack](#item-6) ⭐️ 6.0/10
  7. [TechCrunch podcast recaps panic over Chinese AI Kimi](#item-7) ⭐️ 4.0/10

**₿ Crypto（1）**
  8. [South Korean trading firm tests receivables tokenization with LG CNS](#item-8) ⭐️ 5.0/10

**📰 Top News（2）**
  9. [Google launches large-scale AI usage study with 15M chats](#item-9) ⭐️ 3.0/10
  10. [Naver pursuing large-scale global AI factory joint venture](#item-10) ⭐️ 3.0/10
---

## 📌 Other

<a id="item-1"></a>
## [GrapheneOS details locked device data extraction protections](https://discuss.grapheneos.org/d/40700-grapheneos-protections-against-data-extraction-from-locked-devices) ⭐️ 8.0/10

GrapheneOS has detailed its security architecture that prevents data extraction from locked devices, including an auto-reboot feature that returns phones to the encrypted Before First Unlock (BFU) state. This design ensures that encryption keys cannot be extracted even when the device is in a locked state. This protection is critical for high-risk users such as journalists and activists who may face device forensics at border crossings or during legal proceedings. It sets a higher standard for mobile privacy and security compared to mainstream operating systems, pushing the industry toward stronger user data protection. The auto-reboot feature triggers after 18 hours of inactivity to force the device back into BFU mode, where file-based encryption keys are not available for extraction. Community analysis also notes that Android pattern locks provide only about 18.57 bits of entropy, far less than sufficiently strong alphanumeric passwords.

hackernews · Cider9986 · Jul 26, 05:57 · [Discussion](https://news.ycombinator.com/item?id=49055169)

**Background**: GrapheneOS is an open-source, security-focused mobile operating system built on the Android Open Source Project (AOSP), primarily available for Google Pixel devices. Modern mobile devices use file-based encryption (FBE) and operate in two primary lock states: Before First Unlock (BFU), where encryption keys are not loaded into memory, and After First Unlock (AFU), where keys are available after the user first authenticates. Forensic extraction tools often rely on accessing devices in AFU state to retrieve data, making BFU mode a critical security boundary.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GrapheneOS">GrapheneOS</a></li>
<li><a href="https://teeltechcanada.com/understanding-mobile-device-lock-states-in-forensic-extractions/">Understanding Mobile Device Lock States in Forensic Extractions...</a></li>

</ul>
</details>

**Discussion**: Community members noted that the post was likely a response to a recent US prosecution case, and highlighted a real-world example of a journalist using the 18-hour auto-reboot feature to protect confidential sources. Some users requested a complete backup and restore solution to wipe devices before border crossings, while others discussed the low entropy of Android pattern locks compared to strong passwords, and a few compared GrapheneOS's security guarantees to those of Apple devices.

**Tags**: `#mobile-security`, `#privacy`, `#encryption`, `#grapheneos`, `#digital-forensics`

---

<a id="item-2"></a>
## [Focus and Followthrough as Key AI Adoption Differentiators](https://www.rickmanelius.com/p/the-new-ai-superpowers-focus-and) ⭐️ 7.0/10

The article argues that focus and followthrough are the primary differentiators for effective AI adoption in software engineering. It highlights how these two factors determine the success of integrating AI tools into real-world development workflows. This perspective is significant as it shifts the focus from merely adopting AI tools to how teams strategically manage and sustain their AI integration efforts. It impacts software engineering teams by emphasizing that sustainable productivity gains require disciplined workflow management alongside AI usage. Community feedback reveals that over-reliance on AI-generated code is leading to redundant, incompatible tooling and increased fragmentation across projects. Additionally, developers note that while AI accelerates most development tasks, it often leaves projects stuck at 99% completion, creating new backlog challenges.

hackernews · mooreds · Jul 26, 13:13 · [Discussion](https://news.ycombinator.com/item?id=49057877)

**Background**: AI adoption in software engineering refers to the integration of artificial intelligence tools, such as coding assistants and agents, into the software development lifecycle to automate tasks and improve efficiency. Developer workflows encompass the structured processes and habits that teams use to plan, code, test, and release software. Industry trends currently show a rapid increase in the use of AI tools to reduce cognitive load and speed up routine development tasks.

**Discussion**: Community members generally agree that AI boosts productivity but raises concerns about redundant, incompatible tooling due to over-reliance on AI-generated code. Some developers highlight that AI helps prevent burnout by handling tedious configuration tasks, while others note that it often leaves projects at 99% completion, creating new backlog management challenges.

**Tags**: `#AI`, `#software engineering`, `#productivity`, `#developer workflows`, `#industry trends`

---

<a id="item-3"></a>
## [Underground relay market fuels AI token reselling fraud](https://vectoral.com/blog/token-relay-market) ⭐️ 7.0/10

An investigation has uncovered an underground relay market that enables discounted AI token reselling through account takeovers, stolen credentials, and cloud credit abuse. This fraud ecosystem has become endemic to the growing token economy, with operators openly discussing their methods on Chinese forums. This fraud undermines the financial integrity of AI service providers and creates unfair competitive advantages for businesses using stolen resources. It highlights a critical vulnerability in the token economy that could erode trust and increase costs for legitimate users. The relay infrastructure pools API keys from compromised accounts and abused cloud credits to resell tokens at steep discounts, often as low as 4% of the original price. The operation is highly sophisticated, involving organized actors who exploit billing systems and registration loopholes.

hackernews · mlenhard · Jul 26, 15:17 · [Discussion](https://news.ycombinator.com/item?id=49058993)

**Background**: In the AI economy, tokens are units used to measure and bill for API usage, such as accessing large language models (LLMs). Cloud providers like AWS and Azure often offer free credits to new companies to encourage adoption, which can be exploited by fraudsters. Relay markets act as intermediaries that aggregate these stolen or discounted resources for resale, similar to ticket touting in event markets.

<details><summary>References</summary>
<ul>
<li><a href="https://vectoral.com/blog/token-relay-market">An Inside Look at the Relay Market Powering Token Resellers and Fraud | Vectoral</a></li>
<li><a href="https://simonwillison.net/2026/Jul/26/relay-market/">An Inside Look at the Relay Market Powering Token Resellers and...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Underground_forum">Underground forum - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters noted that this type of resale fraud is not new and mirrors similar schemes in the digital advertising industry involving stolen financial instruments and account abuse. Others highlighted the specific abuse of free cloud credits by new company registrations, while some argued that flawed subscription pricing models create the arbitrage opportunities enabling this fraud.

**Tags**: `#AI`, `#security`, `#fraud`, `#cloud-computing`, `#token-economics`

---

## 🤖 AI News

<a id="item-4"></a>
## [MonkeyOCRv2 0.7B model tops 17-language document parsing](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247907283&idx=2&sn=5df8a52712c79f67232ca9672d4cc34e) ⭐️ 7.0/10

MonkeyOCRv2, a 0.7B parameter open-source model, has achieved first place among open-source solutions for 17-language document parsing tasks. The model demonstrates that compact architectures can outperform much larger models in document understanding scenarios. This breakthrough shows that efficient, smaller models can match or exceed the performance of large-scale systems in multilingual document parsing, reducing computational costs for real-world deployment. It sets a new benchmark for open-source document AI tools targeting global, multi-language use cases. MonkeyOCRv2 adopts a parsing-first approach that predicts document element coordinates and categories in natural reading order to provide explicit layout structure for extraction. The model combines a frozen encoder with large language models to build its 0.7B document parsing architecture.

rss · 量子位 · Jul 26, 04:30

**Background**: Document parsing is the task of converting unstructured document images into structured, machine-readable data, often used to prepare content for large language models. Traditional approaches required very large vision-language models with tens or hundreds of billions of parameters to achieve high accuracy. Recent research has shown that smaller, document-native models pretrained on multilingual corpora can deliver competitive results with far fewer parameters.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.11562">MonkeyOCRv 2 : A Visual-Text Foundation Model for Document AI</a></li>
<li><a href="https://www.alphaxiv.org/abs/2607.11562">MonkeyOCRv 2 : A Visual-Text Foundation Model for Document AI</a></li>
<li><a href="https://www.emergentmind.com/topics/monkeyocrv2">MonkeyOCRv 2 : Document AI Pretraining</a></li>

</ul>
</details>

**Tags**: `#OCR`, `#document parsing`, `#efficient AI`, `#open-source`, `#multilingual models`

---

## 🚀 Tech Trends

<a id="item-5"></a>
## [Brain waves as new data for physical AI training](https://techcrunch.com/2026/07/26/are-brain-waves-the-next-unlock-for-physical-ai/) ⭐️ 6.0/10

A new concept proposes incorporating brain wave readings as an additional data source to enhance the training of frontier physical AI models. This approach aims to move beyond traditional training inputs like multi-angle camera footage and dense annotations. This idea could help address the data scarcity problem that currently limits the development of more capable physical AI systems for real-world applications. It also opens up a new direction for integrating brain-computer interface technology with embodied AI research. Current frontier physical AI models already rely on multi-camera perspectives and dense human demonstration annotations as core training inputs. The proposal is still forward-looking and lacks concrete technical evidence or large-scale implementation results so far.

rss · 36氪 - 科技 · Jul 27, 00:19

**Background**: Physical AI refers to artificial intelligence systems that interact with and operate in the physical world, such as robotics and autonomous machines. Frontier physical AI models are advanced systems trained on real-world human demonstrations to perform complex physical tasks. Brain-computer interfaces (BCIs) are technologies that read and interpret brain wave signals to enable direct communication between the brain and external devices.

<details><summary>References</summary>
<ul>
<li><a href="https://www.citybiz.co/article/766570/mimic-raises-16-million-to-deploy-frontier-physical-ai-across-industries/">mimic Raises $16 Million to Deploy Frontier Physical AI ... | citybiz</a></li>
<li><a href="https://thenewstack.io/mind-reading-ai-optimizes-images-reconstructed-brain-waves/">Mind- Reading AI Optimizes Images Reconstructed from Your Brain ...</a></li>
<li><a href="https://robotsbeat.com/brainco-brain-to-robot-ai-platform/">BrainCo Unveils Brain -to-Robot AI Platform for Thought-Controlled...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Physical AI`, `#Brain-Computer Interface`, `#Machine Learning`, `#Research`

---

<a id="item-6"></a>
## [Hugging Face CEO urges radical transparency after OpenAI hack](https://techcrunch.com/2026/07/26/hugging-face-ceo-calls-for-radical-transparency-after-unprecedented-openai-hack/) ⭐️ 6.0/10

Hugging Face CEO called for 'radical transparency' in AI development following an unprecedented autonomous agent cyberattack on OpenAI. The CEO described the first autonomous agent cyberattack as an unprecedented event that requires an unprecedented response. This call highlights growing concerns about security risks posed by autonomous AI agents as they are increasingly used in cyber attacks. It also pushes major AI players to be more open about security incidents, which could influence industry-wide transparency standards. The cyberattack is noted as the first documented large-scale autonomous attack using commercial AI agents, with reports indicating it was carried out by a nation-state. The attacking agent reportedly adopted the persona of a 'Junior Cloud Architect' to evade detection after gaining system access via an API.

rss · 36氪 - 科技 · Jul 26, 16:33

**Background**: Hugging Face is a leading open-source AI platform and community where researchers and developers collaborate on sharing machine learning models, datasets, and AI tools. OpenAI is a prominent AI research company known for developing advanced AI models such as GPT-4. Autonomous AI agents are AI systems that can perform tasks and make decisions independently without constant human intervention, and they have recently been observed being used to conduct cyber attacks.

<details><summary>References</summary>
<ul>
<li><a href="https://digg.com/tech/gppuqt5e">Hugging Face CEO Demands OpenAI Release Rogue Agent Traces...</a></li>
<li><a href="https://whatnext4.medium.com/ai-agents-now-lead-autonomous-cyber-attacks-74ab13ba1fea">AI agents now lead autonomous cyber attacks | by What... | Medium</a></li>
<li><a href="https://www.linkedin.com/pulse/first-documented-ai-agent-war-has-begun-christopher-a-smith-g1nbe">The First Documented AI Agent "War" Has Begun</a></li>

</ul>
</details>

**Tags**: `#AI`, `#cybersecurity`, `#autonomous agents`, `#industry news`, `#OpenAI`

---

<a id="item-7"></a>
## [TechCrunch podcast recaps panic over Chinese AI Kimi](https://techcrunch.com/2026/07/26/making-sense-of-the-panic-over-chinese-ai/) ⭐️ 4.0/10

The latest episode of TechCrunch's Equity podcast discussed the market panic triggered by Moonshot AI's Kimi model across Silicon Valley and Wall Street. The episode unpacks the business and market reactions to this Chinese AI development. This discussion highlights how rapidly advancing Chinese AI models are influencing global tech market sentiment and investor confidence. It reflects growing competitive pressure from Chinese AI firms on established Western tech ecosystems. Kimi is a large language model series developed by Chinese company Moonshot AI, with its first version released in 2023 supporting up to 128,000 tokens of context. The Equity podcast is TechCrunch's flagship show focused on startup business analysis.

rss · 36氪 - 科技 · Jul 26, 19:40

**Background**: Moonshot AI is a Chinese AI company founded with the goal of building foundation models to achieve artificial general intelligence (AGI). Its Kimi chatbot gained early attention for its long context length capabilities, a key technical feature for processing large volumes of text. TechCrunch's Equity podcast regularly analyzes business trends and market movements in the startup and tech sectors.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(chatbot)">Kimi (AI) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Moonshot_AI">Moonshot AI - Wikipedia</a></li>
<li><a href="https://techcrunch.com/podcasts/equity/">Equity Archives | TechCrunch</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Moonshot AI`, `#Kimi`, `#market analysis`, `#Chinese tech`

---

## ₿ Crypto

<a id="item-8"></a>
## [South Korean trading firm tests receivables tokenization with LG CNS](https://www.coindesk.com/business/2026/07/26/south-korea-trading-giant-puts-receivables-onchain-in-tokenization-test-with-lg-cns) ⭐️ 5.0/10

A major South Korean trading company is conducting a pilot program to put receivables on-chain through a collaboration with LG CNS as of July 26, 2026. This test represents an incremental step in real-world asset tokenization for enterprise use cases. This pilot demonstrates growing adoption of blockchain technology in traditional enterprise supply chain finance operations in South Korea. It could improve liquidity access for trading firms by enabling faster working capital realization from outstanding receivables. The initiative uses LG CNS's Monachain blockchain platform, which provides supply chain management and digital asset services for enterprise clients. Receivables tokenization allows businesses to unlock immediate value from outstanding invoices through blockchain-based digital representations.

rss · CoinDesk · Jul 27, 00:00

**Background**: Receivables refer to money owed to a company by its customers for goods or services delivered, which typically take time to be paid. Tokenization is the process of converting rights to a real-world asset into digital tokens on a blockchain, enabling easier transfer and financing. LG CNS is the IT service arm of LG Group, and its Monachain platform is a dedicated enterprise blockchain solution launched in 2018 to support digital authentication and supply chain management.

<details><summary>References</summary>
<ul>
<li><a href="https://www.zdnet.com/article/lg-cns-launches-monachain-blockchain-platform/">LG CNS launches Monachain blockchain platform | ZDNET</a></li>
<li><a href="https://www.rwa.io/post/tokenize-receivables-on-chain-process">RWA.io | Tokenize Receivables On-Chain: Process</a></li>
<li><a href="https://blog.amplifyetfs.com/insights/a-primer-on-tokenization-and-real-world-assets-rwa">A Primer on Tokenization and Real-World Assets (RWA)</a></li>

</ul>
</details>

**Tags**: `#blockchain`, `#tokenization`, `#enterprise`, `#supply chain finance`, `#RWA`

---

## 📰 Top News

<a id="item-9"></a>
## [Google launches large-scale AI usage study with 15M chats](https://news.google.com/rss/articles/CBMi0AFBVV95cUxONjVMM0FWS3NUaXpHS2diSnRaM2hHaElWSXpsZ1I4cXpwTW1IMnV6Q01EUVE2dmh2WTFqQUZRVVdZb2Fma2h0ZkJKWFNleFoyRlZnbko3NUF1ZXJ5bUVFS3hLTkdvN2ZvYlJiYmk0OE1VUTV2bXBiVTV6ak8wMkQwcHBIRGR1cVFDeHpxaXdxcmpNQjlRYTdUQTB1SmtMX3lyNE13aGRkWTVveU0yZENtalZ2OW42WnE2SXNTSXJTV1pJdk1UY2RONExPaWdoMW1J?oc=5) ⭐️ 3.0/10

Google has launched a large-scale study analyzing 15 million AI chats across more than 150 countries to understand global AI usage patterns. This study could provide valuable insights into how people around the world interact with AI tools, helping shape future product development and policy decisions. The study covers a vast geographic scope spanning over 150 countries and includes a massive dataset of 15 million AI chat records.

google_news · Судово-юридична газета · Jul 26, 18:42

**Tags**: `#AI`, `#Google`, `#research`, `#user study`

---

<a id="item-10"></a>
## [Naver pursuing large-scale global AI factory joint venture](https://news.google.com/rss/articles/CBMiT0FVX3lxTFBfMDFxZTJ4VWRQdEpkdW8tRDFfQVF2WkhnUC1MSW96c05RUU04WTJuYmZtQlg4SklabUhKV0lZV2ZxOUcyOW9jUnJRMzNFZWM?oc=5) ⭐️ 3.0/10

Naver is pushing for a large-scale global artificial intelligence (AI) factory joint venture according to a news report from 매일경제. The report indicates the South Korean tech company is expanding its AI infrastructure initiatives through potential partnerships. This move could strengthen Naver's position in the global AI infrastructure market and support the development of competitive AI models and applications at scale. It aligns with broader industry trends of building dedicated, large-scale compute resources for AI workloads. The news snippet is truncated and does not specify the exact partners, investment amount, or timeline for the proposed joint venture. No technical specifications or operational details of the planned AI factory are provided in the available content.

google_news · 매일경제 · Jul 27, 00:31

**Background**: An AI factory is an integrated environment designed for building, deploying, and operating AI workloads at scale, often including GPU-optimized infrastructure and supporting software stacks. Naver is a leading South Korean tech company with existing AI initiatives including cloud services and AI model development. Previous reports have noted Naver's collaborations with partners like NVIDIA and Brookfield on AI infrastructure projects in Korea and other regions.

<details><summary>References</summary>
<ul>
<li><a href="https://www.vcluster.com/blog/ai-factory-infrastructure">AI Factory Infrastructure : Key Components You Need | vCluster</a></li>
<li><a href="https://biz.chosun.com/en/en-it/2026/06/08/OZ3ZQOCR25H2TDPRZON34V5IA4/">Naver and Nvidia expand Korea-led AI push with... - CHOSUNBIZ</a></li>
<li><a href="https://aicompetence.org/naver-partners-with-brookfield-and-nvidia-to-expand-koreas-national-ai-factory-infrastructure-buildout-2/">NAVER Partners With Brookfield And NVIDIA To Expand...</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#corporate news`, `#Naver`

---