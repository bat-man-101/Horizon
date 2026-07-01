---
layout: default
title: "Horizon Summary: 2026-07-01 (EN)"
date: 2026-07-01
lang: en
---

> From 184 items, 14 important content pieces were selected

---

**📌 Other（3）**
  1. [Claude Code Steganographically Marks Requests](#item-1) ⭐️ 9.0/10
  2. [US Lifts Export Controls on Anthropic's Claude Fable 5 and Mythos 5](#item-2) ⭐️ 9.0/10
  3. [Anthropic Launches Claude Science for Researchers](#item-3) ⭐️ 8.0/10

**🚀 Tech Trends（3）**
  4. [Realta Fusion claims first direct electricity generation from fusion](#item-4) ⭐️ 9.0/10
  5. [Tesla Begins Testing Cybercab Without Steering Wheel in Austin](#item-5) ⭐️ 8.0/10
  6. [Arcturus uses nano-infused copper to halve grid losses](#item-6) ⭐️ 8.0/10

**🤖 AI News（3）**
  7. [Claude Sonnet 5 Released with Near-Opus Performance](#item-7) ⭐️ 8.0/10
  8. [shot-scraper video: Agents record demos automatically](#item-8) ⭐️ 8.0/10
  9. [ChatGPT Adoption Expands Globally](#item-9) ⭐️ 7.0/10

**🔬 Semiconductors（1）**
  10. [Enterprise Token Spending More Measured Than Hype](#item-10) ⭐️ 7.0/10

**₿ Crypto（1）**
  11. [US Senators Propose Bill to Block AI Tech from Adversaries](#item-11) ⭐️ 7.0/10

**📰 Top News（3）**
  12. [China's Plan to Save Jobs From AI](#item-12) ⭐️ 7.0/10
  13. [Meituan trains trillion-parameter AI model on domestic chips](#item-13) ⭐️ 7.0/10
  14. [Trump's 2025 Financial Report Shows $14B Crypto Income](#item-14) ⭐️ 6.0/10
---

## 📌 Other

<a id="item-1"></a>
## [Claude Code Steganographically Marks Requests](https://thereallo.dev/blog/claude-code-prompt-steganography) ⭐️ 9.0/10

A developer discovered that Anthropic's Claude Code tool (version 2.1.196) silently embeds invisible Unicode steganographic markers into system prompts based on the user's API base URL and timezone, effectively fingerprinting requests without disclosure. This revelation undermines trust in AI service providers, as it shows Anthropic secretly tracking users through their developer tool, potentially violating transparency expectations and raising privacy concerns for developers worldwide. The markers appear designed to flag traffic linked to China, likely to detect model distillation attempts. The technique was discovered by decompiling the local Claude Code install, and Anthropic has not documented or disclosed this behavior.

hackernews · kirushik · Jun 30, 15:44 · [Discussion](https://news.ycombinator.com/item?id=48734373)

**Background**: Steganography is the practice of hiding information within other data, such as invisible Unicode characters in text. Claude Code is a terminal-based AI coding agent from Anthropic that sends prompts to the company's API. The hidden markers are embedded in the system prompt, allowing Anthropic to identify the origin of requests even if routed through a proxy.

<details><summary>References</summary>
<ul>
<li><a href="https://www.aimadetools.com/blog/claude-code-steganography-explained/">Claude Code Is Steganographically Marking Requests: What It Means</a></li>
<li><a href="https://byteiota.com/claude-code-is-marking-requests-what-anthropic-hid/">Claude Code Is Marking Requests: What Anthropic Hid</a></li>
<li><a href="https://aiproductivity.ai/news/claude-code-prompt-steganography-hidden-markers/">Claude Code Prompt Steganography Discovered - aiproductivity.ai</a></li>

</ul>
</details>

**Discussion**: The Hacker News community expressed strong concern, with many criticizing Anthropic's lack of transparency and calling for local AI solutions. Some commenters downplayed the severity, arguing the intent (detecting Chinese model distillation) is clear, while others noted the sloppy implementation and questioned what else might be hidden.

**Tags**: `#AI`, `#security`, `#steganography`, `#Anthropic`, `#developer tools`

---

<a id="item-2"></a>
## [US Lifts Export Controls on Anthropic's Claude Fable 5 and Mythos 5](https://twitter.com/AnthropicAI/status/2072106151890809341) ⭐️ 9.0/10

The US Department of Commerce has lifted export controls on Anthropic's Claude Fable 5 and Mythos 5, allowing global deployment of these advanced AI models starting July 1, 2026. This policy shift signals a more permissive stance on frontier AI exports, but the community debate highlights concerns about business reliance on US AI models and the unpredictability of regulation. Fable 5 will be available globally on Claude Platform, Claude.ai, Claude Code, and Claude Cowork, but initially cannot be used for coding tasks, which will fall back to Opus 4.8.

hackernews · Pragmata · Jun 30, 23:55 · [Discussion](https://news.ycombinator.com/item?id=48740771)

**Background**: Claude Fable 5 and Mythos 5 are Anthropic's most capable models, designed for cybersecurity vulnerability discovery. Export controls were imposed due to safety and misuse concerns, but after negotiations with the US government, Anthropic implemented new classifiers to block cybersecurity tasks, enabling the lift.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/redeploying-fable-5">Redeploying Claude Fable 5 \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable_5">Claude Fable 5</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Mythos">Claude Mythos - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters express skepticism about building business-critical functions on US frontier models due to regulatory unpredictability, with one noting the damage is done. Others highlight that Fable 5 cannot be used for coding initially, and question the process's transparency.

**Tags**: `#AI regulation`, `#export controls`, `#Anthropic`, `#policy`, `#frontier models`

---

<a id="item-3"></a>
## [Anthropic Launches Claude Science for Researchers](https://claude.com/product/claude-science) ⭐️ 8.0/10

Anthropic has launched Claude Science, a specialized AI workbench for scientific research that integrates high-performance computing (HPC) and databases, with a local server and web-based UI. This product addresses a critical need in scientific computing by enabling researchers to run complex analyses on sensitive data within secure environments, potentially accelerating discoveries in fields like bioinformatics and genomics. Claude Science runs a local server and connects via a browser-based UI, making it suitable for locked-down pharma environments. It produces auditable artifacts and integrates with institutional clusters, but is not intended for clinical or diagnostic use.

hackernews · lebovic · Jun 30, 17:07 · [Discussion](https://news.ycombinator.com/item?id=48735770)

**Background**: Scientific research often involves large datasets and complex computational workflows that require HPC resources. Traditional AI tools are not designed to integrate with institutional clusters or handle sensitive data securely. Claude Science bridges this gap by providing a customizable workbench that connects to researchers' existing infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-science-ai-workbench">Claude Science, an AI workbench for scientists \ Anthropic</a></li>
<li><a href="https://claude.com/docs/claude-science/overview">Claude Science - Claude.ai Documentation</a></li>
<li><a href="https://www.technologyreview.com/2026/06/30/1139987/claude-science-is-anthropics-newest-flagship-product/">Claude Science is Anthropic’s newest flagship product</a></li>

</ul>
</details>

**Discussion**: Early users are impressed: one researcher used it to analyze whole genome sequencing data and solved a question about a de novo mutation in about a minute. The founder of a connected HPC tool noted the value of integrations with institutional clusters. Another scientist highlighted how it speeds up bioinformatics workflows but noted the challenge of keeping up with AI-generated models.

**Tags**: `#AI`, `#Science`, `#Bioinformatics`, `#Anthropic`, `#Product Launch`

---

## 🚀 Tech Trends

<a id="item-4"></a>
## [Realta Fusion claims first direct electricity generation from fusion](https://techcrunch.com/2026/06/30/realta-fusion-generates-electricity-directly-from-a-fusion-reaction-an-apparent-first/) ⭐️ 9.0/10

Realta Fusion has achieved a milestone by generating electricity directly from a fusion reaction, using a prototype converter to harvest alpha particles and produce multiple amps at 100 volts, powering lightbulbs. This direct energy conversion could significantly improve the economics of fusion reactors by boosting efficiency, bringing commercial fusion energy closer to reality and potentially transforming global energy production. The startup used a prototype converter attached to its reactor to capture alpha particles from deuterium-tritium fusion, generating enough electricity to power a few lightbulbs. About 20% of fusion energy from deuterium-tritium reactions is carried by alpha particles.

rss · 36氪 - 科技 · Jun 30, 19:12

**Background**: Fusion power aims to replicate the Sun's energy source by fusing light atomic nuclei, releasing vast energy. Traditional designs convert fusion heat into electricity via steam turbines, but direct energy conversion captures charged particles directly, potentially increasing efficiency. Realta Fusion uses a compact, scalable design called CoSMo fusion.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/30/realta-fusion-generates-electricity-directly-from-a-fusion-reaction-an-apparent-first/">Realta Fusion generates electricity directly from a fusion ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Direct_energy_conversion">Direct energy conversion - Wikipedia</a></li>
<li><a href="https://realtafusion.com/technology/">Technology - Realta Fusion</a></li>

</ul>
</details>

**Tags**: `#fusion energy`, `#energy technology`, `#physics`, `#breakthrough`

---

<a id="item-5"></a>
## [Tesla Begins Testing Cybercab Without Steering Wheel in Austin](https://techcrunch.com/2026/06/30/tesla-starts-testing-cybercab-without-pedals-or-a-steering-wheel-in-austin/) ⭐️ 8.0/10

Tesla has started testing its Cybercab, a fully autonomous vehicle without pedals or a steering wheel, on public roads in Austin, Texas, marking a concrete step toward launching a robotaxi network. This testing milestone brings Tesla closer to fulfilling Elon Musk's long-standing promise of a robotaxi network, which could disrupt the ride-hailing industry and accelerate the adoption of autonomous vehicles. The Cybercab is a two-passenger electric vehicle designed for full autonomy, with production starting in February 2026. It has a curb weight of 3,113 lbs, a 219 HP motor, and a 48 kWh battery providing an unadjusted range of 418 miles.

rss · 36氪 - 科技 · Jun 30, 15:32

**Background**: Tesla's robotaxi service, which uses vehicles equipped with Full Self-Driving (FSD) software, launched in a limited capacity in Austin in June 2025. The Cybercab, unveiled as a concept in October 2024, is intended to be the dedicated vehicle for this service, operating without human controls.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Cybercab">Tesla Cybercab - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Robotaxi">Tesla Robotaxi - Wikipedia</a></li>
<li><a href="https://electrek.co/2026/06/15/tesla-cybercab-epa-specs-curb-weight-battery-motor-power/">Tesla Cybercab full specs revealed: 3,113 lbs, 219 HP, 48 kWh</a></li>

</ul>
</details>

**Tags**: `#Tesla`, `#autonomous vehicles`, `#robotaxi`, `#Cybercab`

---

<a id="item-6"></a>
## [Arcturus uses nano-infused copper to halve grid losses](https://techcrunch.com/2026/06/30/arcturus-could-halve-the-grids-electrical-losses-using-its-nano-infused-copper/) ⭐️ 8.0/10

Stealth startup Arcturus emerged from stealth with an $8 million seed round, revealing its laser-based process to infuse carbon nanomaterials into copper, which can dramatically improve electrical conductivity and potentially halve grid electrical losses. If successful, this technology could significantly reduce energy waste in electrical grids and data centers, leading to substantial cost savings and lower carbon emissions, with broad implications for energy infrastructure and sustainability. Arcturus has raised a total of $10 million, with investors including Initialized Capital, Breakthrough Energy Discovery, Toyota Ventures, and Wireframe Ventures. The company has not disclosed the exact composition of the carbon nanomaterials used, but they are likely carbon nanotubes or graphene derivatives.

rss · 36氪 - 科技 · Jun 30, 15:01

**Background**: Electrical grids lose a significant amount of energy as heat due to resistance in conductors like copper. Improving conductivity of existing materials without replacing entire infrastructure is a major challenge. Arcturus uses lasers to embed carbon nanomaterials into copper, enhancing electron flow and reducing resistive losses.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/30/arcturus-could-halve-the-grids-electrical-losses-using-its-nano-infused-copper/">Arcturus could halve the grid’s electrical losses using its ...</a></li>

</ul>
</details>

**Tags**: `#energy`, `#nanotechnology`, `#materials science`, `#electrical grid`, `#startup`

---

## 🤖 AI News

<a id="item-7"></a>
## [Claude Sonnet 5 Released with Near-Opus Performance](https://simonwillison.net/2026/Jun/30/claude-sonnet-5/#atom-everything) ⭐️ 8.0/10

Anthropic released Claude Sonnet 5 on June 30, 2026, claiming its performance is close to Opus 4.8 but at lower prices. The model features a 1 million token context window, 128,000 maximum output tokens, and a new tokenizer that increases token count by about 30% for English text. This release narrows the gap between mid-tier and top-tier models, offering near-flagship performance at a lower cost, which could shift developer adoption patterns. The system card also reveals regulatory considerations, as Sonnet 5 was deemed safe enough to release without government blocking, unlike the more capable Mythos 5. Sonnet 5 drops support for sampling parameters temperature, top_p, and top_k, and enables adaptive thinking by default. Pricing remains the same as Sonnet 4.6 ($3/$15 per million tokens), but the new tokenizer effectively increases costs by ~30% for English text due to higher token counts.

rss · Simon Willison · Jun 30, 21:23

**Background**: Anthropic's Claude model family includes Sonnet (mid-tier) and Opus (flagship) tiers. The company also has a more capable Mythos 5 model, which was only allowed for limited release after government approval due to safety concerns. System cards detail model capabilities and safety evaluations, helping developers and regulators understand risks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-sonnet-5">Introducing Claude Sonnet 5 \ Anthropic</a></li>
<li><a href="https://www-cdn.anthropic.com/480e0bb54327b9622282e9c39a83a4f490ed377e/Claude+Sonnet+5+System+Card.pdf">System Card: Claude Sonnet 5 June 30, 2026 anthropic.com</a></li>
<li><a href="https://llm-stats.com/blog/research/claude-sonnet-5-vs-claude-opus-4-8">Claude Sonnet 5 vs Claude Opus 4.8: The Complete Comparison</a></li>

</ul>
</details>

**Discussion**: Community comments on Hacker News were mixed: some users noted Sonnet 5's performance is comparable to GLM 5.2 but less verbose, while others argued that Opus 4.8 offers better cost-performance at higher effort levels. Some expressed confusion about when to use Sonnet 5 over Opus, given the pricing and tokenizer changes.

**Tags**: `#AI`, `#Claude`, `#Anthropic`, `#LLM`, `#model release`

---

<a id="item-8"></a>
## [shot-scraper video: Agents record demos automatically](https://simonwillison.net/2026/Jun/30/shot-scraper-video/#atom-everything) ⭐️ 8.0/10

Simon Willison released shot-scraper 1.10 with a new 'shot-scraper video' command that uses Playwright to record WebM videos of web application routines defined in a YAML storyboard file. This tool enables coding agents to automatically produce video demos of their work, addressing a key need in agentic workflows for verifying and showcasing agent behavior. The command accepts a storyboard.yml file that specifies server setup, viewport, cursor visibility, JavaScript overrides (e.g., clipboard mocking), and a sequence of scenes with actions like click and pause. It supports authentication via cookies and outputs WebM files.

rss · Simon Willison · Jun 30, 16:54

**Background**: shot-scraper is a command-line tool for taking screenshots and scraping web pages using Playwright. The new video feature extends it to record full sessions, making it easier for AI agents to demonstrate their work without manual screen recording.

<details><summary>References</summary>
<ul>
<li><a href="https://shot-scraper.datasette.io/en/stable/video.html">Recording videos - shot - scraper</a></li>
<li><a href="https://simonwillison.net/2026/Jun/30/shot-scraper-video/">Have your agent record video demos of its work with shot - scraper ...</a></li>
<li><a href="https://github.com/simonw/shot-scraper">GitHub - simonw/ shot - scraper : A command-line utility for taking...</a></li>

</ul>
</details>

**Tags**: `#agentic-ai`, `#testing`, `#developer-tools`, `#playwright`, `#automation`

---

<a id="item-9"></a>
## [ChatGPT Adoption Expands Globally](https://openai.com/index/how-chatgpt-adoption-has-expanded) ⭐️ 7.0/10

OpenAI released new Signals data showing that ChatGPT adoption is growing globally, with users increasing usage, exploring more capabilities, and driving growth across regions and languages. This indicates that ChatGPT is becoming more deeply integrated into daily workflows and cross-cultural contexts, signaling a maturing AI market and expanding user base beyond early adopters. The data comes from OpenAI Signals, which tracks usage patterns, but the announcement lacks specific metrics or regional breakdowns, making it a high-level overview rather than a detailed analysis.

rss · OpenAI Blog · Jun 30, 09:00

**Background**: ChatGPT is a conversational AI model developed by OpenAI, launched in late 2022. Adoption metrics are closely watched as indicators of AI market growth and user acceptance.

**Tags**: `#ChatGPT`, `#AI adoption`, `#OpenAI`, `#market trends`

---

## 🔬 Semiconductors

<a id="item-10"></a>
## [Enterprise Token Spending More Measured Than Hype](https://newsletter.semianalysis.com/p/tokenbudgeting-our-conversations) ⭐️ 7.0/10

Semianalysis reports that enterprise conversations reveal widespread excessive token usage ('TokenMaxxing') is not as prevalent as hyped, with businesses showing more measured spending patterns. This analysis debunks the hype around 'TokenMaxxing' and provides realistic insights into enterprise LLM adoption, helping practitioners and investors understand actual token economics. The article is based on conversations with enterprises and suggests that while some token waste exists, most organizations are budgeting carefully rather than maximizing usage indiscriminately.

rss · Semianalysis · Jun 30, 18:32

**Background**: TokenMaxxing refers to the practice of maximizing AI usage, often measured by token consumption, sometimes seen as productivity theater. Tokens are units of data processed by AI models, and their cost is a key factor in enterprise AI economics.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Token_maxxing">Token maxxing - Wikipedia</a></li>
<li><a href="https://blogs.nvidia.com/blog/ai-tokens-explained/">What Are AI Tokens ? The Language and Currency... | NVIDIA Blog</a></li>

</ul>
</details>

**Tags**: `#AI/ML`, `#enterprise`, `#LLM`, `#token economics`, `#industry analysis`

---

## ₿ Crypto

<a id="item-11"></a>
## [US Senators Propose Bill to Block AI Tech from Adversaries](https://www.coindesk.com/policy/2026/06/30/u-s-senators-seek-to-block-foreign-adversaries-from-ai-technology-in-new-bill) ⭐️ 7.0/10

A bipartisan group of U.S. senators introduced a bill aimed at restricting the transfer of advanced AI technology to foreign adversaries such as China and Russia. This bill could significantly reshape global AI supply chains and technology transfer, impacting both U.S. companies and international AI development. The bill targets AI technologies deemed critical to national security and includes provisions for export controls and investment screening.

rss · CoinDesk · Jun 30, 23:02

**Background**: The U.S. government has increasingly focused on limiting adversaries' access to sensitive technologies, especially AI, which is seen as a dual-use technology with military and civilian applications. Previous actions include export restrictions on advanced semiconductors.

**Tags**: `#AI policy`, `#geopolitics`, `#regulation`, `#technology access`

---

## 📰 Top News

<a id="item-12"></a>
## [China's Plan to Save Jobs From AI](https://news.google.com/rss/articles/CBMigwFBVV95cUxQOERiSFVoaHY5ZkNwWURzMWUyRDV3ZHl1MkpuZDlDcVhQaXN1dEhYQXZhd3oxNFdjYUZFOFFQTW1LdUItQ092ODRSVV9ickRoT1pwYWNJVlQwQ1NNVS0teExQbkM3WkUwSmd2LUlmcy1waFdKSkptcHJpbEM2MV9iZlZtUQ?oc=5) ⭐️ 7.0/10

The New York Times reports on China's strategy to mitigate job losses caused by AI through retraining programs and social safety nets. This policy approach could serve as a model for other nations facing AI-driven job displacement, highlighting the balance between technological progress and social stability. The article discusses specific measures such as government-funded retraining and expanded unemployment benefits, though exact details are not provided in the summary.

google_news · The New York Times · Jul 1, 04:42

**Background**: AI and automation are expected to disrupt labor markets globally, with China facing particular pressure due to its large manufacturing workforce. The Chinese government has historically used state-led interventions to manage economic transitions.

**Tags**: `#AI`, `#labor`, `#China`, `#policy`, `#automation`

---

<a id="item-13"></a>
## [Meituan trains trillion-parameter AI model on domestic chips](https://news.google.com/rss/articles/CBMi2AFBVV95cUxOWEJOc2tfMDNfQll0RHlyRy1uRU1IcWozeHNRTUxJQllWMFJTMXF2X0xhSk92VTZDMXhESi04UEJVWU5tb0EtX014Z3lScmpUd2dMODZFd0JYcjRhWko0V2ZzN195VlU5SUJXYjZYckFUcnV3REttNWVhNkVNVGhHNFZ6SXp2VFZTUWo4UF9OQ2xmMHd0NkRBV1Jwc2xpbWhhTHQyb0Y5dFNsUzh5RXB6NG14TGh4c2VvNGdKMUdOWWs3STBjVVdmV0tPNURyRzRPcEF5cGwzSTHSAd4BQVVfeXFMUEpUaVI2N1Exa25YaEM5Q2YtX19kUEk3N0I0c0x0aDU3MG5jQktnS1BucWoxMW5LTFUycEp6c2c4MEhHa3dwR2RlVXREZzBSa2Q0V09JdUJpdnktdzllWmRzb2dDV1pZYUFsUThPVGQ0NGJnV195ZUo0RENMN2Y0Ym9lTEVfakViVVN4d0E5TE9wOGk3RGg2TVE2Uk0zVUdjMjlsWHRaQzc4UUFOS2xfeTBnUVVLRm9XRFVfUHNRWjA3R0NlSjZ5VXA2LWtiV3VfOFM2ODdDYWt1eC1sV0xR?oc=5) ⭐️ 7.0/10

Meituan announced that its new AI model, LongCat-2.0, with 1.6 trillion parameters, was trained entirely on domestically produced chips, marking the first time a model of this scale has been trained on a domestic compute cluster. This demonstrates China's growing capability to train frontier AI models without relying on Nvidia chips, which are subject to US export restrictions, and could reduce China's dependence on foreign semiconductors. LongCat-2.0 was trained on a 50,000-chip domestic cluster using ASIC superpods, and the model is open-source. The company began exploring domestic chips in 2023.

google_news · The Economic Times · Jun 30, 07:21

**Background**: US export controls have restricted China's access to advanced Nvidia AI chips like the H100 and A100. Most Chinese AI models previously relied on Nvidia hardware for training, while domestic chips were mainly used for inference. Meituan's achievement shows that domestic chips can now handle the most demanding training workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://techxplore.com/news/2026-06-china-meituan-ai-domestic-chips.html">China's Meituan says new AI model trained on domestic chips</a></li>
<li><a href="https://thenextweb.com/news/chinas-meituan-says-its-new-ai-model-was-trained-on-domestic-chips">China’s Meituan says its new AI model was trained on domestic ...</a></li>
<li><a href="https://economictimes.indiatimes.com/tech/artificial-intelligence/chinas-meituan-says-new-ai-model-trained-on-domestic-chips/articleshow/132086878.cms">China's Meituan says new AI model trained on domestic chips</a></li>

</ul>
</details>

**Tags**: `#AI`, `#semiconductors`, `#China`, `#Meituan`, `#hardware`

---

<a id="item-14"></a>
## [Trump's 2025 Financial Report Shows $14B Crypto Income](http://www3.nhk.or.jp/news/html/20260701/k10015166021000.html) ⭐️ 6.0/10

The U.S. government released President Trump's 2025 financial disclosure, revealing that his primary income came from cryptocurrency assets, totaling at least $14 billion (approximately ¥230 billion). This disclosure highlights the growing intersection of high-level politics and cryptocurrency, potentially influencing regulatory attitudes and public perception of digital assets. The reported amount is at least $14 billion, converted to approximately ¥230 billion, and media outlets emphasize that the major earnings are crypto-related.

rss · NHK World - Japan/Asia · Jul 1, 06:40

**Background**: U.S. presidents are required to annually disclose their financial holdings to ensure transparency and avoid conflicts of interest. Cryptocurrency assets, such as Bitcoin and Ethereum, have become increasingly prominent in high-net-worth portfolios.

**Tags**: `#cryptocurrency`, `#politics`, `#finance`

---