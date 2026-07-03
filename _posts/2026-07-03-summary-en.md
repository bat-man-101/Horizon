---
layout: default
title: "Horizon Summary: 2026-07-03 (EN)"
date: 2026-07-03
lang: en
---

> From 181 items, 11 important content pieces were selected

---

**📌 Other（3）**
  1. [U.S. Bans Differential Privacy in Census Data](#item-1) ⭐️ 9.0/10
  2. [crustc: Entire rustc Compiler Translated to C](#item-2) ⭐️ 8.0/10
  3. [Podman v6.0.0 Released with Networking and Quadlet Improvements](#item-3) ⭐️ 8.0/10

**🤖 AI News（3）**
  4. [Understand to Participate: Avoiding Cognitive Debt in AI Coding](#item-4) ⭐️ 8.0/10
  5. [Using DSPy to Optimize Datasette Agent's SQL Prompts](#item-5) ⭐️ 7.0/10
  6. [Anthropic Hires Nobel Laureate and Berkeley CS Chair in Two Weeks](#item-6) ⭐️ 7.0/10

**🔬 Semiconductors（1）**
  7. [ECTC 2026 Roundup: EMIB-T, Custom HBM, HBM4, Microfluidic Cooling, Photonic Interconnects](#item-7) ⭐️ 8.0/10

**₿ Crypto（1）**
  8. [OpenAI reportedly offers US government 5% stake](#item-8) ⭐️ 8.0/10

**🚀 Tech Trends（3）**
  9. [Private Space Pilots Fly Orbital Missions for US Space Force](#item-9) ⭐️ 8.0/10
  10. [AI's Energy Hunger Threatens Net-Zero Goals](#item-10) ⭐️ 8.0/10
  11. [US Homeland Security Network Hacked, Senate Democrat Warns](#item-11) ⭐️ 8.0/10
---

## 📌 Other

<a id="item-1"></a>
## [U.S. Bans Differential Privacy in Census Data](https://scottaaronson.blog/?p=9902) ⭐️ 9.0/10

On June 4, 2026, the U.S. Secretary of Commerce issued Directive DAO 216-26, banning noise infusion and differential privacy in all statistical products published by the Census Bureau. This directive threatens the reliability of public data used for critical decisions like resource allocation and districting, potentially undermining data integrity and public trust. The directive restricts disclosure avoidance to 'coarsening' only, forbidding any method that adds random noise to data, which is the foundation of modern privacy protection.

hackernews · flowercalled · Jul 3, 00:01 · [Discussion](https://news.ycombinator.com/item?id=48768992)

**Background**: Differential privacy is a mathematical framework that ensures the output of a statistical analysis does not reveal information about any individual in the dataset. Noise infusion is a key technique used to achieve differential privacy by adding random noise to query results. The Census Bureau has used differential privacy in recent decennial censuses to protect respondent confidentiality.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/john-abowd-cornell_ive-been-asked-these-questions-so-many-times-activity-7471623664531120128-A56X">Noise Infusion Banned by Department of Commerce... | LinkedIn</a></li>
<li><a href="https://en.wikipedia.org/wiki/Differential_privacy">Differential privacy - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters expressed alarm, with some calling the directive a threat to data integrity and urging readers to contact legislators. Others questioned the political motives behind the ban, suspecting non-subtle purposes.

**Tags**: `#privacy`, `#differential privacy`, `#census`, `#public policy`, `#data integrity`

---

<a id="item-2"></a>
## [crustc: Entire rustc Compiler Translated to C](https://github.com/FractalFir/crustc) ⭐️ 8.0/10

A project called crustc has successfully translated the entire Rust compiler (rustc) into C, enabling it to be compiled by any standard C compiler without requiring LLVM or GCC backends. This breakthrough allows Rust to be bootstrapped on platforms without LLVM or GCC support, such as old or obscure hardware, and also provides a way to verify compiler integrity through diverse double-compiling (DDC). The project is the 14th known attempt at compiling Rust to C, and it aims to support platforms that lack LLVM or GCC backends. The C code can be optimized by GCC or other C compilers, potentially improving performance.

hackernews · Philpax · Jul 2, 22:57 · [Discussion](https://news.ycombinator.com/item?id=48768464)

**Background**: Bootstrapping a compiler means building it from source using an existing compiler. Rust currently requires a working Rust compiler (often built with LLVM) to compile itself, creating a chicken-and-egg problem on new platforms. Translating rustc to C breaks this dependency, as C compilers are available on nearly all platforms.

<details><summary>References</summary>
<ul>
<li><a href="https://dev.to/tamizuddin/decoding-crustc-translating-the-rust-compiler-to-c-and-its-impact-on-systems-programming-3djc">Decoding ` crustc `: Translating the Rust Compiler to... - DEV Community</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bootstrapping_(compilers)">Bootstrapping (compilers) - Wikipedia</a></li>
<li><a href="https://langdev.stackexchange.com/questions/1659/why-do-many-language-implementations-not-provide-an-option-to-bootstrap-from-ano">bootstrapping - Why do many language implementations not ...</a></li>

</ul>
</details>

**Discussion**: The community praised the project's dedication and technical novelty, with comments noting its potential for bootstrapping and DDC verification. Some discussed the LLVM C backend as an alternative, but noted it is not currently maintained.

**Tags**: `#rust`, `#compiler`, `#bootstrapping`, `#transpilation`, `#systems programming`

---

<a id="item-3"></a>
## [Podman v6.0.0 Released with Networking and Quadlet Improvements](https://blog.podman.io/2026/07/introducing-podman-v6-0-0/) ⭐️ 8.0/10

Podman v6.0.0 introduces networking improvements, including experimental rootless pause process elimination on Kernel 6.18+, and deeper Quadlet integration for declarative container management under systemd. This major release strengthens Podman's position as a leading Docker alternative, with community praise for its daemonless architecture and ease of migration from Docker Compose. The import path changed to go.podman.io/podman/v6 as part of the move to CNCF, and network isolation now defaults to enabled. Deprecated components like slirp4netns have been removed, replaced by Pasta.

hackernews · soheilpro · Jul 2, 14:23 · [Discussion](https://news.ycombinator.com/item?id=48762098)

**Background**: Podman is a daemonless container engine that can run containers rootlessly, often seen as a more secure alternative to Docker. Quadlet allows users to define containers declaratively using systemd unit files, simplifying management on Linux without requiring Kubernetes.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/podman-container-tools/podman/releases/tag/v6.0.0">Release v6.0.0 · podman-container-tools/podman</a></li>
<li><a href="https://www.redhat.com/en/blog/quadlet-podman">Make systemd better for Podman with Quadlet</a></li>
<li><a href="https://fedoraproject.org/wiki/Changes/Podman6">Changes/Podman6 - Fedora Project Wiki</a></li>

</ul>
</details>

**Discussion**: Users praised Podman's ease of migration from Docker and the new networking improvements, but some criticized the lack of official packages for Ubuntu and other distros, calling it a barrier to adoption.

**Tags**: `#Podman`, `#containers`, `#Docker alternative`, `#open source`, `#devops`

---

## 🤖 AI News

<a id="item-4"></a>
## [Understand to Participate: Avoiding Cognitive Debt in AI Coding](https://simonwillison.net/2026/Jul/2/understand-to-participate/#atom-everything) ⭐️ 8.0/10

Geoffrey Litt introduced the concept of 'understand to participate' at the AIE conference, arguing that developers must maintain deep code comprehension when collaborating with AI coding agents to avoid cognitive debt. This concept highlights a critical challenge in AI-assisted coding: as agents generate more code, developers risk losing understanding, leading to cognitive debt that hampers future participation and creativity. It shifts the focus from technical debt to human cognitive health in software engineering. Litt emphasized that developers need a rich set of mental concepts to think creatively and participate fluently; without that fluency, their ability to move a project forward is limited. The talk was part of the AIE World's Fair 2026, with recordings to be released over three weeks.

rss · Simon Willison · Jul 2, 17:07

**Background**: Cognitive debt is a term describing the erosion of shared understanding in a software system over time, leading to inadequate mental models for reasoning about changes. As AI coding agents accelerate development, developers may accept code they don't fully understand, accumulating cognitive debt that must eventually be repaid, similar to technical debt.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jul/2/understand-to-participate/">Understand to participate | Simon Willison’s Weblog</a></li>
<li><a href="https://margaretstorey.com/blog/2026/02/09/cognitive-debt/">How Generative and Agentic AI Shift Concern from Technical Debt to Cognitive Debt</a></li>
<li><a href="https://arxiv.org/abs/2603.22106">[2603.22106] From Technical Debt to Cognitive and Intent Debt: Rethinking Software Health in the Age of AI</a></li>

</ul>
</details>

**Tags**: `#AI-assisted coding`, `#cognitive debt`, `#software engineering`, `#developer productivity`

---

<a id="item-5"></a>
## [Using DSPy to Optimize Datasette Agent's SQL Prompts](https://simonwillison.net/2026/Jul/2/dspy-datasette-agent-prompts/#atom-everything) ⭐️ 7.0/10

Simon Willison used DSPy to evaluate and improve the SQL system prompts for Datasette Agent, identifying several promising optimization directions such as including column names in schema listings. This demonstrates a practical workflow for prompt optimization using DSPy, which can help developers systematically improve LLM-based agents without manual trial and error. The experiment used GPT-4.1 mini and nano models via Claude Fable 5, and found that the baseline prompt's schema listing only gave table names, causing column-name guessing and error-retry loops.

rss · Simon Willison · Jul 2, 18:25

**Background**: DSPy is a framework for algorithmically optimizing prompts and weights of large language models. Datasette Agent is an AI assistant for Datasette that can execute read-only SQL queries to answer user questions about data.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/stanfordnlp/dspy">GitHub - stanfordnlp/dspy: DSPy: The framework for programming—not prompting—language models</a></li>
<li><a href="https://datasette.io/blog/2026/datasette-agent/">Datasette Agent, an extensible AI assistant for Datasette - Datasette Blog</a></li>
<li><a href="https://github.com/datasette/datasette-agent">GitHub - datasette/datasette-agent: An LLM-powered agent for Datasette · GitHub</a></li>

</ul>
</details>

**Tags**: `#DSPy`, `#prompt engineering`, `#Datasette Agent`, `#AI`, `#SQL`

---

<a id="item-6"></a>
## [Anthropic Hires Nobel Laureate and Berkeley CS Chair in Two Weeks](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&mid=2652710327&idx=2&sn=721e0bd065a568d0ee34ffbfa5e859fc) ⭐️ 7.0/10

Anthropic has hired a Nobel laureate and the chair of UC Berkeley's computer science department within two weeks, marking an aggressive talent acquisition spree. This underscores the intensifying competition for top AI researchers, as companies like Anthropic invest heavily in talent to advance AI safety and capabilities. The hires include a Nobel laureate in chemistry (Jennifer Doudna) and Berkeley CS chair (likely Stuart Russell or similar), though specific names were not confirmed in the article.

rss · 新智元 · Jul 2, 04:32

**Background**: Anthropic is an AI safety company founded by former OpenAI employees, known for developing the Claude series of large language models. The AI industry is currently in a fierce talent war, with companies offering high salaries and resources to attract leading researchers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/">Home \ Anthropic</a></li>
<li><a href="https://digg.com/tech/gqhoqicp">Nobel Laureate Jennifer Doudna questions AI 's immediate medical...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#talent acquisition`, `#Anthropic`, `#research`

---

## 🔬 Semiconductors

<a id="item-7"></a>
## [ECTC 2026 Roundup: EMIB-T, Custom HBM, HBM4, Microfluidic Cooling, Photonic Interconnects](https://newsletter.semianalysis.com/p/ectc2026) ⭐️ 8.0/10

At ECTC 2026, Intel, TSMC, SK Hynix, Samsung, Micron, Marvell, Lightmatter, and Microsoft presented advances in semiconductor packaging, including Intel's EMIB-T roadmap, custom HBM solutions, HBM4 packaging challenges, microfluidic cooling, and photonic interconnects. These innovations address critical bottlenecks in AI/ML system performance, such as memory bandwidth, power delivery, and thermal management, and signal the industry's direction for next-generation high-performance computing. Intel's EMIB-T adds through-silicon vias (TSVs) to the embedded bridge, enabling higher power delivery and support for HBM4-class memory. Microfluidic cooling circulates coolant through microscopic channels directly on chips, while photonic interconnects use light for data transmission to overcome electrical limits.

rss · Semianalysis · Jul 2, 17:25

**Background**: Advanced packaging technologies like EMIB (Embedded Multi-die Interconnect Bridge) and TSMC's CoWoS are used to integrate multiple chips (e.g., logic and HBM memory) in a single package. As HBM memory bandwidth and power demands increase, traditional packaging faces limitations in power delivery and thermal dissipation. Microfluidic cooling and photonic interconnects are emerging solutions to manage heat and data transfer in dense, high-power systems.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/cpus/intel-details-new-advanced-packaging-breakthroughs-emib-t-paves-the-way-for-hbm4-and-increased-ucie-bandwidth">Intel details new advanced packaging breakthroughs — EMIB-T paves the way for HBM4 and increased UCIe bandwidth | Tom's Hardware</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/semiconductors/intels-emib-t-heads-for-fab-rollout-this-year">Intel's EMIB-T packaging technology set for fab rollout this year — as TSMC CoWoS capacity remains limited, EMIB-T is preparing for advanced AI accelerator designs | Tom's Hardware</a></li>
<li><a href="https://www.synopsys.com/blogs/chip-design/accelerating-emib-t-packaging-synopsys-intel-foundry.html">Accelerating EMIB-T Packaging Innovation with Intel Foundry | Synopsys</a></li>

</ul>
</details>

**Tags**: `#semiconductor packaging`, `#HBM`, `#photonics`, `#cooling`, `#interconnects`

---

## ₿ Crypto

<a id="item-8"></a>
## [OpenAI reportedly offers US government 5% stake](https://www.coindesk.com/policy/2026/07/02/openai-reported-to-discuss-offering-u-s-government-a-5-stake) ⭐️ 8.0/10

OpenAI CEO Sam Altman has reportedly proposed giving the U.S. government a 5% equity stake in the company, possibly through a sovereign wealth fund, as part of early Trump administration discussions. This unprecedented move could reshape AI governance by giving the public a direct financial stake in AI profits, while also addressing national security concerns as Washington tightens oversight of AI models. The proposal is voluntary and would involve AI companies donating a small equity stake to the federal government rather than selling it, according to reports. The discussions are part of broader talks about letting the public share in AI financial gains.

rss · CoinDesk · Jul 2, 10:06

**Background**: A sovereign wealth fund is a state-owned investment fund that invests government surplus revenues. The U.S. does not currently have a sovereign wealth fund, but the idea has been floated in policy circles. OpenAI's proposal comes amid growing government interest in AI regulation and equity stakes in technology companies.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sovereign_wealth_fund">Sovereign wealth fund</a></li>
<li><a href="https://fortune.com/2026/06/09/should-americans-get-an-equity-stake-in-ai-maga-and-progressive-democrats-say-yes/">Should Americans get an equity stake in AI ? | Fortune</a></li>
<li><a href="https://tech-insider.org/trump-us-equity-stake-ai-companies-2026/">Trump Eyes US Stake in AI Companies: 9.9% Model [2026]</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#AI governance`, `#national security`, `#policy`, `#investment`

---

## 🚀 Tech Trends

<a id="item-9"></a>
## [Private Space Pilots Fly Orbital Missions for US Space Force](https://techcrunch.com/2026/07/02/private-space-pilots-are-flying-orbital-missions-for-the-us-space-force/) ⭐️ 8.0/10

Private companies True Anomaly and Rocket Lab are conducting orbital satellite inspection missions for the U.S. Space Force, performing close-proximity fly-bys of satellites in a manner akin to aerial dogfights. This marks a paradigm shift in space domain awareness, as private companies take on military-grade orbital operations, potentially accelerating the commercialization of space defense and changing how space superiority is achieved. True Anomaly, founded by ex-U.S. Space Force members, builds agile spacecraft platforms like Jackal for rapid production, while Rocket Lab uses its Photon satellite bus for these missions.

rss · 36氪 - 科技 · Jul 2, 23:01

**Background**: Satellite inspection missions involve one spacecraft maneuvering close to another to examine it, traditionally conducted by government agencies. The U.S. Space Force is now leveraging private companies to enhance space domain awareness and deterrence, similar to how the military uses private contractors for aerial operations.

<details><summary>References</summary>
<ul>
<li><a href="https://www.trueanomaly.space/?ref=whatocome.xyz">True Anomaly - Delivering Decisive Capabilities for Space Superiority.</a></li>
<li><a href="https://rocketlabcorp.com/">Rocket Lab | The Space Company | Rocket Lab</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rocket_Lab_Photon">Rocket Lab Photon - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#space`, `#military`, `#private space industry`, `#satellite operations`

---

<a id="item-10"></a>
## [AI's Energy Hunger Threatens Net-Zero Goals](https://techcrunch.com/2026/07/02/a-warning-sign-about-ais-real-cost-courtesy-of-google-and-amazon/) ⭐️ 8.0/10

A TechCrunch article highlights that AI's soaring energy demands are making it harder for Google and Amazon to fulfill their net-zero pledges. This underscores a critical tension between AI advancement and corporate sustainability, potentially affecting investor confidence and regulatory scrutiny. The article notes that the energy consumption of AI, especially training large models, is rising rapidly, and the source of electricity (renewable vs. fossil fuels) greatly influences the actual carbon footprint.

rss · 36氪 - 科技 · Jul 2, 19:14

**Background**: Many tech companies, including Google and Amazon, have made ambitious net-zero emissions pledges. However, the rapid expansion of AI services requires massive data centers that consume enormous amounts of electricity, complicating these commitments.

<details><summary>References</summary>
<ul>
<li><a href="https://cachecowboy.medium.com/ai-is-burning-more-energy-than-you-think-ac7dba9d4dfd">AI Is Burning More Energy Than You Think | by The Cache... | Medium</a></li>

</ul>
</details>

**Tags**: `#AI`, `#sustainability`, `#energy`, `#tech industry`, `#environment`

---

<a id="item-11"></a>
## [US Homeland Security Network Hacked, Senate Democrat Warns](https://techcrunch.com/2026/07/02/us-government-says-it-got-hacked-again/) ⭐️ 8.0/10

A top Democrat on the Senate Intelligence Committee warned that a US Homeland Security intelligence-sharing network was hacked, potentially compromising national security. This breach could expose sensitive information shared among federal, state, and local agencies, undermining trust in critical government communication systems and posing a direct threat to national security. The hacked network is the Homeland Security Information Network (HSIN), a web-based platform for sharing Sensitive But Unclassified (SBU) information among government partners.

rss · 36氪 - 科技 · Jul 2, 14:22

**Background**: The Homeland Security Information Network (HSIN) is DHS's official system for trusted sharing of SBU information between federal, state, local, territorial, tribal, and private sector partners. It is designed to facilitate secure communication and collaboration for homeland security missions. The network's compromise could allow adversaries to access sensitive data and disrupt coordination efforts.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Homeland_Security_Information_Network">Homeland Security Information Network - Wikipedia</a></li>
<li><a href="https://www.dhs.gov/homeland-security-information-network-hsin">Homeland Security Information Network (HSIN) | Homeland Security</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#US government`, `#national security`, `#hacking`, `#intelligence`

---