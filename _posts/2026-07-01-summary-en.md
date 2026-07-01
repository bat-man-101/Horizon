---
layout: default
title: "Horizon Summary: 2026-07-01 (EN)"
date: 2026-07-01
lang: en
---

> From 206 items, 13 important content pieces were selected

---

**📌 Other（3）**
  1. [Claude Code Secretly Embeds Steganographic Watermarks](#item-1) ⭐️ 9.0/10
  2. [US Lifts Export Controls on Anthropic's Claude Fable 5 and Mythos 5](#item-2) ⭐️ 9.0/10
  3. [Anthropic Releases Claude Sonnet 5 for Agentic Tasks](#item-3) ⭐️ 8.0/10

**🚀 Tech Trends（3）**
  4. [Realta Fusion achieves first direct electricity from fusion](#item-4) ⭐️ 9.0/10
  5. [Etched hits $5B valuation, $1B in AI chip sales](#item-5) ⭐️ 8.0/10
  6. [Tesla Starts Testing Cybercab Without Pedals or Steering Wheel in Austin](#item-6) ⭐️ 8.0/10

**📰 Top News（3）**
  7. [US Extends Export Controls to Advanced AI Models](#item-7) ⭐️ 8.0/10
  8. [AI Could Revolutionize Vaccine Development](#item-8) ⭐️ 7.0/10
  9. [AI Could Transform Breast Cancer Detection and Recurrence Prediction](#item-9) ⭐️ 7.0/10

**🤖 AI News（2）**
  10. [shot-scraper video records agent demos](#item-10) ⭐️ 7.0/10
  11. [OpenAI Reports Global Growth in ChatGPT Adoption](#item-11) ⭐️ 6.0/10

**🔬 Semiconductors（1）**
  12. [TokenBudgeting: Enterprise AI Cost Management Insights](#item-12) ⭐️ 7.0/10

**₿ Crypto（1）**
  13. [New York Life's $800B asset manager launches tokenized bond fund](#item-13) ⭐️ 7.0/10
---

## 📌 Other

<a id="item-1"></a>
## [Claude Code Secretly Embeds Steganographic Watermarks](https://thereallo.dev/blog/claude-code-prompt-steganography) ⭐️ 9.0/10

Anthropic's Claude Code tool has been found to secretly embed steganographic watermarks in user requests, as revealed by a blog post that reverse-engineered the tool. This raises serious concerns about transparency and trust in AI vendor tooling, as users may unknowingly have their data marked and tracked without consent. The steganographic markers are embedded in the prompts sent to Claude Code, potentially allowing Anthropic to identify the source of requests, such as those from Chinese firms conducting model distillation.

hackernews · kirushik · Jun 30, 15:44 · [Discussion](https://news.ycombinator.com/item?id=48734373)

**Background**: Steganography is the practice of hiding secret data within ordinary files, such as text or images, to avoid detection. Claude Code is Anthropic's agentic coding tool that operates in the terminal to assist developers with code editing and project management.

<details><summary>References</summary>
<ul>
<li><a href="https://topaihubs.com/articles/claude-s-hidden-watermarks-ai-security-and-the-ethics-of-invisible-data">Claude's Hidden Watermarks: AI Security and the Ethics of ...</a></li>
<li><a href="https://www.anthropic.com/product/claude-code">Claude Code | Anthropic's agentic coding system</a></li>

</ul>
</details>

**Discussion**: Community comments are divided: some criticize Anthropic for lack of transparency and sloppy implementation, while others argue the intent (e.g., detecting model distillation by Chinese firms) is understandable. There is also a call for running AI locally to preserve privacy.

**Tags**: `#AI`, `#security`, `#steganography`, `#Anthropic`, `#trust`

---

<a id="item-2"></a>
## [US Lifts Export Controls on Anthropic's Claude Fable 5 and Mythos 5](https://twitter.com/AnthropicAI/status/2072106151890809341) ⭐️ 9.0/10

The US Department of Commerce lifted export controls on Anthropic's Claude Fable 5 and Mythos 5 AI models on June 30, 2026, restoring global access after a three-week ban. This decision marks a significant shift in AI regulation, highlighting the tension between national security concerns and the business dependency on US frontier models, and sets a precedent for future export controls on advanced AI. Claude Fable 5 is Anthropic's most capable widely released model for coding and agentic tasks, while Mythos 5 is a limited-release model for cybersecurity vulnerability discovery; both were disabled on June 12 following an export control order.

hackernews · Pragmata · Jun 30, 23:55 · [Discussion](https://news.ycombinator.com/item?id=48740771)

**Background**: Export controls are government restrictions on the transfer of sensitive technologies to foreign entities. In June 2026, the US government imposed an export ban on Anthropic's most advanced AI models, citing national security risks. The ban was lifted after Anthropic implemented new classifiers to block cybersecurity tasks, though some routine coding tasks now fall back to older models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theguardian.com/technology/2026/jul/01/anthropic-fable-mythos-ai-models-us-export-controls-lifted">Anthropic : US has lifted export controls on Fable and Mythos AI ...</a></li>
<li><a href="https://nypost.com/2026/06/30/business/trump-administration-lifts-export-controls-on-anthropics-most-powerful-ai-models-ending-bitter-standoff/">Trump administration lifts export controls on Anthropic 's most...</a></li>
<li><a href="https://www.euronews.com/2026/07/01/us-lifts-export-controls-on-powerful-ai-models-anthropic-says">US lifts export controls on powerful AI models , Anthropic says</a></li>

</ul>
</details>

**Discussion**: Community comments express concern over the unpredictability of US AI regulation, with some arguing that businesses cannot rely on frontier models for critical functions. Others note that the lifting of controls does not address the lack of clear legal standards, and that the process appears ad hoc.

**Tags**: `#AI regulation`, `#export controls`, `#Anthropic`, `#frontier models`, `#geopolitics`

---

<a id="item-3"></a>
## [Anthropic Releases Claude Sonnet 5 for Agentic Tasks](https://www.anthropic.com/news/claude-sonnet-5) ⭐️ 8.0/10

Anthropic has released Claude Sonnet 5, a new model optimized for agentic tasks such as planning, tool use, and autonomous execution, with pricing at $3/$15 per million tokens. This release highlights the industry trend toward agentic AI, offering a cost-effective option for autonomous workflows, though it shows mixed benchmark results compared to the more expensive Opus model. On some benchmarks, Sonnet 5 matches or exceeds Opus 4.8 at a lower cost, but on others like CyberGym vulnerability discovery, it underperforms compared to Sonnet 4.6 and Opus 4.8. The model also scored 0 on CyberGym when default mitigations were enabled.

hackernews · marinesebastian · Jun 30, 17:59 · [Discussion](https://news.ycombinator.com/item?id=48736605)

**Background**: Agentic AI refers to systems that can autonomously plan, use tools, and execute multi-step tasks with minimal human intervention. Claude Sonnet models are mid-tier offerings from Anthropic, balancing performance and cost, while Opus is the flagship high-end model.

<details><summary>References</summary>
<ul>
<li><a href="https://llm-stats.com/blog/research/claude-sonnet-5-vs-claude-opus-4-8">Claude Sonnet 5 vs Claude Opus 4.8: The Complete Comparison</a></li>
<li><a href="https://codingfleet.com/blog/claude-sonnet-5-vs-claude-opus-4-8/">Claude Sonnet 5 vs Claude Opus 4.8: 93% Power, 60% Price ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community comments express confusion about Sonnet 5's value proposition, noting that Opus often performs better per cost at higher effort levels. Some users highlight regressions in security benchmarks and question the model's pricing strategy.

**Tags**: `#AI`, `#LLM`, `#Anthropic`, `#Claude`, `#model release`

---

## 🚀 Tech Trends

<a id="item-4"></a>
## [Realta Fusion achieves first direct electricity from fusion](https://techcrunch.com/2026/06/30/realta-fusion-generates-electricity-directly-from-a-fusion-reaction-an-apparent-first/) ⭐️ 9.0/10

Realta Fusion has demonstrated the first direct generation of electricity from a fusion reaction, bypassing the traditional steam turbine cycle. The milestone was announced by CEO Kieran Furlong in a TechCrunch interview on June 30, 2026. This breakthrough could dramatically improve the economics and efficiency of fusion power plants, making fusion a more viable clean energy source. It represents a major step toward practical, commercial fusion energy, potentially transforming global energy production. The company used a field-reversed configuration (FRC) reactor, which naturally pulses and allows direct electricity extraction without intermediate heat conversion. Realta Fusion is a spin-out from the University of Wisconsin-Madison and aims to build a fusion device by 2028.

rss · 36氪 - 科技 · Jun 30, 19:12

**Background**: Traditional fusion reactor designs, like tokamaks, rely on heat from fusion to produce steam that drives turbines, similar to conventional power plants. Direct electricity generation from fusion has been a long-sought goal because it eliminates the inefficiency of thermal conversion. Realta Fusion's approach uses a linear FRC reactor with advanced superconducting magnets and plasma physics to achieve this.

<details><summary>References</summary>
<ul>
<li><a href="https://www.msn.com/en-us/technology/renewable-energy/realta-fusion-generates-electricity-directly-from-a-fusion-reaction-an-apparent-first/ar-AA26UNPp">Realta Fusion generates electricity directly from a fusion reaction...</a></li>
<li><a href="https://podmarized.com/episodes/lex-fridman-podcast/david-kirtley-nuclear-fusion-plasma-physics-and-the-future-of-energy-lex-fridman-podcast-485">David Kirtley: Nuclear Fusion , Plasma Physics, and the Future of Energy</a></li>
<li><a href="https://planetforward.org/story/realta-fusion-wisconsin/">UW-Madison startup aims to build fusion energy device by 2028</a></li>

</ul>
</details>

**Tags**: `#fusion energy`, `#clean energy`, `#breakthrough`, `#nuclear fusion`

---

<a id="item-5"></a>
## [Etched hits $5B valuation, $1B in AI chip sales](https://techcrunch.com/2026/06/30/nvidia-competitor-etched-hits-5b-valuation-1b-in-sales-for-ai-chip/) ⭐️ 8.0/10

AI chip startup Etched announced it has secured $1 billion in contracts for its transformer-specific inference systems and achieved a $5 billion valuation, positioning itself as a serious competitor to Nvidia. This milestone signals strong market validation for specialized AI inference chips, potentially challenging Nvidia's dominance in the AI hardware market and accelerating the shift toward purpose-built accelerators. Etched's first-generation chip, Sohu, is an ASIC purpose-built for transformer models, which power large language models like ChatGPT. The company has booked $1 billion under contract for inference systems using Sohu.

rss · 36氪 - 科技 · Jun 30, 18:13

**Background**: Etched is an American semiconductor startup designing custom ASICs for AI workloads. Its chip Sohu is the first purpose-built for transformer AI architecture, focusing on inference rather than training. Nvidia currently dominates the AI chip market with its general-purpose GPUs.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Etched.ai">Etched (company) - Wikipedia</a></li>
<li><a href="https://techcrunch.com/2024/06/25/etched-is-building-an-ai-chip-that-only-runs-transformer-models/">Etched is building an AI chip that only runs one type of... | TechCrunch</a></li>

</ul>
</details>

**Tags**: `#AI hardware`, `#Nvidia competitor`, `#startup funding`, `#AI chips`, `#inference`

---

<a id="item-6"></a>
## [Tesla Starts Testing Cybercab Without Pedals or Steering Wheel in Austin](https://techcrunch.com/2026/06/30/tesla-starts-testing-cybercab-without-pedals-or-a-steering-wheel-in-austin/) ⭐️ 8.0/10

Tesla has begun testing its Cybercab robotaxi without pedals or a steering wheel on public roads in Austin, Texas, marking a major step toward launching a fully autonomous ride-hailing network. This testing represents a critical milestone for Tesla's long-promised robotaxi network, potentially transforming urban transportation by offering driverless rides. If successful, it could accelerate the adoption of autonomous vehicles and disrupt traditional ride-hailing services. The Cybercab is a two-passenger electric vehicle designed exclusively for autonomy, with no manual controls. Tesla unveiled a concept in October 2024 and began production in February 2026, with 20 prototypes initially built.

rss · 36氪 - 科技 · Jun 30, 15:32

**Background**: Tesla has been developing Full Self-Driving (FSD) technology for years, but the Cybercab is its first vehicle purpose-built for robotaxi service without any manual driving controls. The company plans to operate its own ride-hailing network called Tesla Robotaxi, where passengers can summon Cybercabs via an app. This test in Austin brings that vision closer to reality.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Cybercab">Tesla Cybercab - Wikipedia</a></li>
<li><a href="https://www.tesla.com/robotaxi">Robotaxi | Tesla</a></li>

</ul>
</details>

**Tags**: `#Tesla`, `#autonomous vehicles`, `#robotaxi`, `#self-driving`, `#transportation`

---

## 📰 Top News

<a id="item-7"></a>
## [US Extends Export Controls to Advanced AI Models](https://news.google.com/rss/articles/CBMigwJBVV95cUxOWTQzZjJ5VGNUaGtJY3dTaTVwb0dWN01yWFY2RGtZX0gwZEpFVHM5NTZZQWRRZ04yZk1Hc2tCcFplcTg2VkxPZzVyUDhBeElfM21Id25YX3NpSXpRSmpLRVlkdXdkRWUyU1NMVXRydklfYmI4eWFrS1BqdnpNTlFmSnZ0RkZZeG9zYXRBRmdDYWIxOVA3R3E2aENra054OHl6WjhkTDVuWUY3eDdtc0J4WmVSR0lKbXNXaUNlaF9obXV5ajUwU0RNR3pLdjhlbGJYdllmNnZwZjNISUlvZFVUUkRGNTNoRWEyODgtVUQ3WXVKeDRUbHNYMEJXNnNQQWFyVGZN?oc=5) ⭐️ 8.0/10

The US Commerce Department's Bureau of Industry and Security (BIS) has extended export controls to cover advanced AI model weights, while authorizing releases to specific trusted partners under a new framework. This marks a significant escalation in US AI regulation, potentially limiting global access to cutting-edge AI models and reshaping international AI development dynamics. Companies and researchers outside trusted partner networks may face new barriers. The controls apply to advanced AI model weights, and compliance deadlines vary: some changes take effect May 15, 2025, while others are deferred to January 25, 2026. The rule also establishes an 'American AI Exports Program' for trusted partners.

google_news · Mayer Brown · Jul 1, 04:30

**Background**: Export controls on advanced computing items began in October 2022, targeting semiconductor technologies. The new rule extends these controls to AI model weights, which are the parameters that define a model's behavior. Trusted partners are entities deemed low-risk by the US government, such as allied nations or vetted companies.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sidley.com/en/insights/newsupdates/2025/01/new-us-export-controls-on-advanced-computing-items-and-artificial-intelligence-model-weights">New U.S. Export Controls on Advanced Computing Items and Artificial Intelligence Model Weights: Seven Key Takeaways | Insights | Sidley Austin LLP</a></li>
<li><a href="https://www.cov.com/en/news-and-insights/insights/2025/01/us-department-of-commerce-establishes-export-control-framework-limiting-the-diffusion-of-advanced-artificial-intelligence-and-expands-and-clarifies-advanced-computing-controls">U.S. Department of Commerce Establishes Export Control Framework Limiting the Diffusion of Advanced Artificial Intelligence and Expands and Clarifies Advanced Computing Controls | Covington & Burling LLP</a></li>
<li><a href="https://www.federalregister.gov/documents/2025/10/28/2025-19674/american-ai-exports-program">Federal Register :: American AI Exports Program</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#export controls`, `#US policy`, `#AI models`

---

<a id="item-8"></a>
## [AI Could Revolutionize Vaccine Development](https://news.google.com/rss/articles/CBMioAFBVV95cUxPWGlPaUVNdnVRVzc0Y3FzRWQxTWg4UnJSTXhlU0hybGVwYTdiTnkwaXVSVXB3ZU9teGlkamZLLVZfR25MMm1Xc3JUVzdMN2QzOVoxMDhzR3ZybUhVcndZY1pMcFpVOUwxVHhsSi1GbVFueTd1WlFxZEZycjl6T1ZDR0lhcUpGdFhLR0Y0ZWc3N042aDlWdkt6OHdwcnBTc3Zw?oc=5) ⭐️ 7.0/10

A new article from CIDRAP discusses how artificial intelligence could accelerate vaccine discovery and design, potentially transforming the entire vaccine development process. This matters because faster vaccine development can improve pandemic preparedness and enable rapid responses to emerging infectious diseases, ultimately saving lives and reducing economic disruption. AI techniques such as AlphaFold can predict protein structures, aiding in antigen design, while machine learning helps identify optimal vaccine targets and streamline clinical trials.

google_news · CIDRAP · Jun 30, 17:45

**Background**: Traditional vaccine development is slow and costly, often taking years or decades. AI can analyze vast biological datasets to identify patterns and predict immune responses, significantly shortening the timeline. During the COVID-19 pandemic, AI helped rapidly sequence the virus and design mRNA vaccines.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cidrap.umn.edu/covid-19/artificial-intelligence-could-usher-new-era-vaccine-development">Artificial intelligence could usher in a new era of vaccine ... | CIDRAP</a></li>
<li><a href="https://www.gavi.org/vaccineswork/using-ai-lab-jab-how-did-artificial-intelligence-help-us-develop-and-deliver-covid">Using AI from lab to jab: how did artificial intelligence help us develop and deliver COVID-19 vaccines?</a></li>
<li><a href="https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2025.1567116/full">Frontiers | Artificial intelligence in vaccine research and development ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#vaccine development`, `#healthcare`, `#biotechnology`

---

<a id="item-9"></a>
## [AI Could Transform Breast Cancer Detection and Recurrence Prediction](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBPbkVuSFFDbFF2YU9rUHhQZ09qZFg0YzdPYllxbXIxWXdkM3diaGZKNllMVEhMdC1ucWlacDNsdmcybzFScThUMXEtMzZWQ29mYmhHRkhjSW9MQU1p?oc=5) ⭐️ 7.0/10

A recent article on EurekAlert! reports that artificial intelligence shows promise in transforming breast cancer detection and predicting recurrence, potentially improving patient outcomes. This development could lead to earlier and more accurate diagnosis of breast cancer, as well as better prediction of recurrence, ultimately saving lives and reducing healthcare costs. The article highlights AI's ability to analyze mammograms and other imaging data with high accuracy, and to identify patterns associated with cancer recurrence. However, specific models, datasets, or performance metrics are not detailed.

google_news · EurekAlert! · Jun 30, 16:33

**Background**: Breast cancer is one of the most common cancers worldwide, and early detection is critical for successful treatment. Traditional methods like mammography can miss some cancers or yield false positives. AI, particularly deep learning, has been increasingly applied to medical imaging to improve diagnostic accuracy and predict disease progression.

**Tags**: `#AI`, `#healthcare`, `#breast cancer`, `#machine learning`

---

## 🤖 AI News

<a id="item-10"></a>
## [shot-scraper video records agent demos](https://simonwillison.net/2026/Jun/30/shot-scraper-video/#atom-everything) ⭐️ 7.0/10

Simon Willison released shot-scraper 1.10 with a new 'video' command that accepts a storyboard.yml file and uses Playwright to record a video of a web application routine. The tool is designed to let coding agents automatically produce visual demos of their work. This addresses a key challenge in AI-assisted development: proving that agent-generated code actually works. By enabling agents to record reproducible video demos, it increases trust and accountability in automated workflows. The storyboard.yml file defines server startup, URL, viewport, cursor visibility, wait conditions, JavaScript overrides, and a sequence of scenes with actions like pause and click. The command supports --auth for cookie-based authentication and outputs WebM or MP4 video.

rss · Simon Willison · Jun 30, 16:54

**Background**: shot-scraper is a command-line tool for taking screenshots of web pages using Playwright, a browser automation framework. The new video command extends this to full session recording, making it easier for AI agents to create visual proof of their work without manual intervention.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/30/shot-scraper-video/">Have your agent record video demos of its work with shot ...</a></li>
<li><a href="https://letsdatascience.com/news/shot-scraper-launches-video-command-in-110-07962b66">shot-scraper launches video command in 1.10 | Let's Data Science</a></li>
<li><a href="https://playwright.dev/">Fast and reliable end-to-end testing for modern web apps ...</a></li>

</ul>
</details>

**Discussion**: The announcement was well-received, with commenters noting the architectural insight that well-designed --help output can serve as a SKILL.md equivalent for coding agents. Some discussed the potential for integrating with high-performance APIs and the value of reproducible demos.

**Tags**: `#developer-tools`, `#testing`, `#AI-agents`, `#web-automation`

---

<a id="item-11"></a>
## [OpenAI Reports Global Growth in ChatGPT Adoption](https://openai.com/index/how-chatgpt-adoption-has-expanded) ⭐️ 6.0/10

OpenAI released new Signals data showing that ChatGPT adoption is growing globally, with users increasing usage and exploring more capabilities across regions and languages. This indicates that ChatGPT is becoming more deeply integrated into users' daily workflows, which could accelerate AI adoption trends and influence how businesses and individuals leverage AI tools. The data comes from OpenAI's Signals hub, which provides research and analysis on real-world AI use, and highlights growth across multiple regions and languages.

rss · OpenAI Blog · Jun 30, 09:00

**Background**: ChatGPT is a conversational AI model developed by OpenAI, capable of understanding and generating human-like text. Adoption metrics track how many people use the tool and how they engage with it, such as frequency of use and feature exploration.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/signals/">Signals | OpenAI | OpenAI</a></li>
<li><a href="https://openai.com/signals/data/">Signals data | OpenAI | OpenAI</a></li>

</ul>
</details>

**Tags**: `#ChatGPT`, `#AI adoption`, `#OpenAI`, `#trends`

---

## 🔬 Semiconductors

<a id="item-12"></a>
## [TokenBudgeting: Enterprise AI Cost Management Insights](https://newsletter.semianalysis.com/p/tokenbudgeting-our-conversations) ⭐️ 7.0/10

SemiAnalysis published an analysis of enterprise conversations on token spend, questioning whether widespread 'TokenMaxxing' ever truly existed and highlighting the shift toward token budgeting. This matters because enterprises are grappling with rising AI costs, and understanding real usage patterns versus hype can help them adopt more sustainable cost management strategies. TokenMaxxing refers to maximizing AI token usage as a productivity metric, but the article suggests it may have been overhyped; instead, enterprises are focusing on token budgeting to control costs.

rss · Semianalysis · Jun 30, 18:32

**Background**: Token budgeting is an approach where enterprises allocate and monitor AI token usage similarly to how operating systems manage memory, preventing runaway costs. The concept of TokenMaxxing emerged as a way to track AI productivity, but critics argue it encourages wasteful usage.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Token_maxxing">Token maxxing - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/pulse/why-token-budgeting-architecture-missing-layer-enterprise-rama-maddi-lmlsc">Why Token Budgeting Architecture Is the Missing Layer in Enterprise ...</a></li>
<li><a href="https://www.vantage.sh/blog/ai-token-budgeting">Token Budgeting : How To Think About AI Cost Control | Vantage</a></li>

</ul>
</details>

**Tags**: `#AI`, `#enterprise`, `#token economics`, `#cost management`

---

## ₿ Crypto

<a id="item-13"></a>
## [New York Life's $800B asset manager launches tokenized bond fund](https://www.coindesk.com/business/2026/06/29/new-york-life-makes-tokenization-debut-with-onchain-high-yield-bond-fund-with-centrifuge) ⭐️ 7.0/10

New York Life's asset manager, with $800 billion in assets, has launched its first tokenized high-yield bond fund on the Centrifuge platform, marking the firm's debut in blockchain-based asset tokenization. This move signals growing institutional adoption of tokenization, potentially transforming asset management by improving liquidity, transparency, and accessibility for traditionally illiquid assets like bonds. The fund is a high-yield bond fund tokenized on Centrifuge, a platform that has already tokenized over $2 billion in real-world assets and is used by institutions like Apollo and Janus Henderson.

rss · CoinDesk · Jun 30, 11:20

**Background**: Tokenization involves creating digital tokens on a blockchain that represent ownership of real-world assets like bonds or real estate. Centrifuge is a blockchain platform specializing in tokenizing real-world assets and integrating them into decentralized finance (DeFi). This launch represents a major traditional financial institution entering the tokenized asset space.

<details><summary>References</summary>
<ul>
<li><a href="https://centrifuge.io/">Centrifuge | Infrastructure for Onchain Asset Management</a></li>
<li><a href="https://messari.io/project/centrifuge/profile">What is Centrifuge? | Messari</a></li>
<li><a href="https://github.com/centrifuge">Centrifuge · GitHub</a></li>

</ul>
</details>

**Tags**: `#tokenization`, `#blockchain`, `#asset management`, `#DeFi`, `#institutional adoption`

---