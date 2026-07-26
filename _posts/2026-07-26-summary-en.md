---
layout: default
title: "Horizon Summary: 2026-07-26 (EN)"
date: 2026-07-26
lang: en
---

> From 71 items, 10 important content pieces were selected

---

**📌 Other（3）**
  1. [Anthropic updates context engineering rules for Claude 5 models](#item-1) ⭐️ 7.0/10
  2. [Fly.io pivots to Sprites AI sandboxes, appoints Scott Johnston as CEO](#item-2) ⭐️ 7.0/10
  3. [Open-weight AI mirrors Kubernetes' maturation path](#item-3) ⭐️ 7.0/10

**🤖 AI News（2）**
  4. [Ruff v0.16.0 expands default linting rules from 59 to 413](#item-4) ⭐️ 7.0/10
  5. [Tsinghua & Tencent cut LLM post-training costs via rollout optimization](#item-5) ⭐️ 3.0/10

**🚀 Tech Trends（3）**
  6. [Profile of elusive hacktivist Phineas Fisher](#item-6) ⭐️ 6.0/10
  7. [Fallen power line reveals AI data center grid vulnerability](#item-7) ⭐️ 6.0/10
  8. [Monday.com joins list of tech firms citing AI for layoffs](#item-8) ⭐️ 3.0/10

**📰 Top News（1）**
  9. [AI-driven hack targets OpenAI at superhuman speed](#item-9) ⭐️ 6.0/10

**₿ Crypto（1）**
  10. [Robinhood Chain RWA activity jumps fivefold with larger tokenized stock trading](#item-10) ⭐️ 4.0/10
---

## 📌 Other

<a id="item-1"></a>
## [Anthropic updates context engineering rules for Claude 5 models](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) ⭐️ 7.0/10

Anthropic has published updated best practices for context engineering specifically tailored to its new Claude 5 generation models, including Claude Opus 5 and Claude Fable 5. The company reports that it removed over 80% of Claude Code's system prompt for these models with no measurable loss in coding performance. This guidance helps developers optimize how they structure information for Claude 5 models, which can improve inference efficiency and output quality when migrating from earlier generations like Claude Opus 4.8. It also shapes how users interact with Anthropic's latest models across coding and other use cases. Context engineering refers to strategies for curating and maintaining the optimal set of tokens during LLM inference, going beyond simple prompting to architect the full context. The new rules are part of Anthropic's broader effort to help users choose and adapt to the performance improvements in the Claude 5 generation.

hackernews · mellosouls · Jul 25, 20:42 · [Discussion](https://news.ycombinator.com/item?id=49051361)

**Background**: Anthropic is an AI public benefit corporation founded in 2021 by former OpenAI staff, with its flagship product being the Claude series of large language models. Context engineering is a practice focused on optimizing the information provided to LLMs during inference to improve output quality and task performance. The Claude 5 generation includes models such as Claude Opus 5 and Claude Fable 5, which succeed earlier versions like Claude Opus 4.8.

<details><summary>References</summary>
<ul>
<li><a href="https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models">The new rules of context engineering for Claude 5 generation models | Claude by Anthropic</a></li>
<li><a href="https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents">Effective context engineering for AI agents \ Anthropic</a></li>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/overview">Models overview - Claude Platform Docs</a></li>

</ul>
</details>

**Discussion**: Community members expressed mixed views, with some criticizing the new rules as common sense not specific to Claude 5 and raising concerns about vendor lock-in through Anthropic-specific tooling. Several users reported regressions in Opus 5, including accidental deletions, more frequent mistakes, higher token usage, and issues with hidden reasoning traces and unreliable automemory contextualization.

**Tags**: `#LLM`, `#Claude`, `#prompt engineering`, `#context engineering`, `#Anthropic`

---

<a id="item-2"></a>
## [Fly.io pivots to Sprites AI sandboxes, appoints Scott Johnston as CEO](https://fly.io/blog/kurt-scott-money-sprites/) ⭐️ 7.0/10

Fly.io announced a strategic pivot to focus on Sprites, its stateful AI sandbox environments, and appointed Scott Johnston as the company's new CEO. The move marks a major shift in the company's core business direction toward supporting AI agent development and untrusted code execution. This pivot signals a significant strategic shift for a well-known cloud infrastructure provider, moving into the increasingly crowded AI sandbox market that is becoming a commodity. The leadership change and new focus may reshape Fly.io's product roadmap and affect existing users of its global application platform. Sprites are hardware-isolated, stateful sandbox environments that support instant creation, approximately 300ms checkpoints, native MCP support, and object-storage-backed persistence for AI agents. Community feedback highlights past operational issues with Fly.io's infrastructure, including data loss, unstable sandbox states, and unreliable status reporting during outages.

hackernews · subarctic · Jul 25, 20:43 · [Discussion](https://news.ycombinator.com/item?id=49051369)

**Background**: Fly.io is a cloud platform that runs applications in microVMs close to end users using Anycast networking and global infrastructure to minimize latency. Sprites are stateful sandbox environments designed to provide secure, persistent Linux execution environments for running coding agents and untrusted code. The AI sandbox market has grown rapidly, with many providers offering similar secure execution environments for AI workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jan/9/sprites-dev/">Fly’s new Sprites.dev addresses both developer sandboxes and API sandboxes at the same time</a></li>
<li><a href="https://rywalker.com/research/sprites">Sprites (Fly.io) | Ry Walker Research | Ry Walker</a></li>
<li><a href="https://fly.io/">Computers for agents · Fly</a></li>

</ul>
</details>

**Discussion**: Users shared critical experiences of severe bugs with Sprites, including data loss and unresponsive zombie sandboxes, leading some to abandon the platform after short trials. Others noted a history of operational instability at Fly.io, such as global outages with inaccurate status page reporting, and expressed skepticism about the pivot to the crowded AI sandbox space under new leadership.

**Tags**: `#infrastructure`, `#startups`, `#cloud-computing`, `#devops`, `#business-strategy`

---

<a id="item-3"></a>
## [Open-weight AI mirrors Kubernetes' maturation path](https://tobi.knaup.me/2026-07-25-open-weight-ai-is-having-its-kubernetes-moment/) ⭐️ 7.0/10

The article argues that open-weight AI is currently undergoing a maturation phase similar to the early evolution of Kubernetes, shifting toward industry-standard collaborative infrastructure. This transition highlights a move from fragmented individual efforts to more unified, shared foundational systems in the AI ecosystem. This shift could lower barriers to entry for startups and smaller organizations by providing reliable, standardized open-weight AI infrastructure to build upon. It also mirrors the broader industry trend of moving critical technology foundations toward collaborative, open governance models similar to cloud-native tooling. Open-weight models allow users to download model weights for local or cloud deployment and customization, though they are not fully open-source as they may lack training code, data details, or permissive modification rights. The discussion also notes that open-weight models help establish a baseline for inference costs, bringing more transparency to the volatile pricing patterns seen across commercial AI providers.

hackernews · tknaup · Jul 25, 14:49 · [Discussion](https://news.ycombinator.com/item?id=49048034)

**Background**: Open-weight AI models are systems where the internal parameters learned during training are made downloadable, enabling users to run and customize the model, though they differ from fully open-source AI which also includes training code and data transparency. Kubernetes is a container orchestration platform that originated from Google's internal Borg system and evolved into a widely adopted industry standard for managing cloud-native workloads through collaborative development. The maturation of Kubernetes involved moving from proprietary internal tools to a shared, community-driven infrastructure that powers modern cloud computing.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/open-weight-ai-what-we-finally-opened-bonnet-nicolas-pistorio-n3ulf">Open - weight AI : what if we finally opened the bonnet ?</a></li>
<li><a href="https://biz.chosun.com/en/en-it/2025/08/06/YNGJCP3ISNEUTGFKBXDS4OXY3I/">OpenAI launches open - weight AI models to enhance... - CHOSUNBIZ</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kubernetes">Kubernetes - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters debated the feasibility of banning Chinese AI models, noting that weights are just numerical values with no inherent country of origin, making such bans technically unenforceable. Others discussed how open-weight models bring sanity to volatile AI tokenomics by providing a clear inference cost baseline, and suggested that true Kubernetes-like maturity would require collaborative training of models with public data across companies. Some users also noted that existing open-weight models from labs like OpenAI are already useful for common tasks but need more frequent updates.

**Tags**: `#open-weight AI`, `#Kubernetes`, `#AI infrastructure`, `#machine learning`, `#tech industry`

---

## 🤖 AI News

<a id="item-4"></a>
## [Ruff v0.16.0 expands default linting rules from 59 to 413](https://simonwillison.net/2026/Jul/25/ruff/#atom-everything) ⭐️ 7.0/10

Ruff v0.16.0 was released on July 23, 2026, increasing the number of default enabled linting rules from 59 to 413. The new default rules include checks for severe syntax errors and immediate runtime errors that were previously opt-in. This major default behavior change will affect a large number of Python developers who use Ruff in CI pipelines or local development without custom configuration. It enables the tool to catch more critical issues out of the box, improving code quality and reducing runtime bugs across the Python ecosystem. The total number of available rules in Ruff has grown from 708 to 968 since v0.1.0, and users can run `uvx ruff@latest check . --fix --unsafe-fixes` to automatically fix most of the newly reported issues. The new rules include checks such as missing timezone arguments in datetime calls and blind exception catching.

rss · Simon Willison · Jul 25, 22:44

**Background**: Ruff is an extremely fast Python linter and code formatter written in Rust, designed as a drop-in replacement for tools like Flake8, isort, and pydocstyle. Linting is a form of static analysis that scans source code without executing it to identify syntax errors, style violations, and potential bugs. Before v0.16.0, Ruff only enabled a small subset of its available rules by default to avoid overwhelming users with minor style issues.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.astral.sh/ruff/linter/">The Ruff Linter | Ruff - Astral</a></li>
<li><a href="https://github.com/astral-sh/ruff">GitHub - astral-sh/ruff: An extremely fast Python linter and ... ruff · PyPI Ruff - Astral Ruff: Complete Guide to Python's Fastest Linter | pydevtools GitHub - sartcod/ruff: An extremely fast Python linter and ... Ruff: A Modern Python Linter for Error-Free and Maintainable ...</a></li>
<li><a href="https://www.perforce.com/blog/qac/what-is-linting">What Is Linting + When to Use Lint Tools | Perforce Software</a></li>

</ul>
</details>

**Tags**: `#python`, `#linting`, `#developer-tools`, `#static-analysis`, `#ruff`

---

<a id="item-5"></a>
## [Tsinghua & Tencent cut LLM post-training costs via rollout optimization](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247907199&idx=3&sn=db62b221aeb50a9dfff1af69803b2787) ⭐️ 3.0/10

Tsinghua University and Tencent have proposed a method to reduce the high cost of LLM post-training by treating agent trajectories as tree structures and optimizing rollout strategies. This approach avoids evenly distributing budgets across all prompts to improve resource efficiency. LLM post-training, especially reinforcement learning-based workflows, is often prohibitively expensive due to massive rollout computation, so this optimization could make advanced model tuning more accessible. It may also accelerate the development of cost-effective agentic LLM systems for broader industry adoption. The method models agent interaction steps as nodes in a trajectory tree rather than independent linear sequences to better capture structural relationships between different interaction paths. It focuses on strategic rollout allocation instead of uniform budget distribution across all input prompts.

rss · 量子位 · Jul 25, 04:40

**Background**: LLM post-training refers to the process of further tuning a pre-trained large language model using methods like supervised fine-tuning, preference optimization, or reinforcement learning to adapt it to specific tasks. The rollout stage in RL post-training involves the actor LLM generating responses for a batch of input prompts, which is often the most computationally expensive part of the workflow. Agent trajectories record the full sequence of multi-turn interactions between an LLM agent and its environment or users during task execution.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2509.21009v1">RollPacker: Mitigating Long-Tail Rollouts for Fast, Synchronous RL...</a></li>
<li><a href="https://arxiv.org/html/2509.14172v2">TGPO: Tree-Guided Preference Optimization for Robust Web ...</a></li>
<li><a href="https://github.com/yeruimeng/TraTree">GitHub - yeruimeng/TraTree: Trajectory optimization methods ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#post-training`, `#agent`, `#research`, `#cost-optimization`

---

## 🚀 Tech Trends

<a id="item-6"></a>
## [Profile of elusive hacktivist Phineas Fisher](https://techcrunch.com/2026/07/25/the-hacker-who-humiliated-spyware-makers-and-was-never-caught/) ⭐️ 6.0/10

TechCrunch published a profile on July 25, 2026, detailing the activities of the unidentified hacktivist Phineas Fisher, who breached multiple controversial government spyware makers without ever being caught. The article highlights Fisher's high-profile intrusions against companies such as FinFisher (Gamma International) and Hacking Team. This profile sheds light on one of the most significant yet mysterious figures in cybersecurity history, whose actions exposed the vulnerabilities and unethical practices of the government spyware industry. It underscores the ongoing tension between privacy advocates, hacktivists, and the expanding global surveillance market. Phineas Fisher, who also uses aliases such as Phineas Phisher and Subcowmandante Marcos, is known to identify as female and has published detailed write-ups of their hacking methods alongside data leaks. The targets included not only spyware vendors but also the Catalan police union and Turkey's ruling Justice and Development Party.

rss · 36氪 - 科技 · Jul 25, 20:24

**Background**: Government spyware makers like Hacking Team and Gamma International (creator of FinFisher) sell surveillance tools to state agencies worldwide, often facing criticism for enabling human rights abuses. Phineas Fisher emerged as a prominent hacktivist around 2014, targeting these companies to expose their operations and the clients they serve. The Italian startup Hacking Team was among the first to turn government spyware into a viable global business, paving the way for later firms like Israel's NSO Group.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Phineas_Fisher">Phineas Fisher - Wikipedia</a></li>
<li><a href="https://techcrunch.com/2026/07/25/the-hacker-who-humiliated-spyware-makers-and-was-never-caught/">The hacker who humiliated spyware makers and was never caught | TechCrunch</a></li>
<li><a href="https://en.wikipedia.org/wiki/FinFisher">FinFisher - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#hacktivism`, `#spyware`, `#infosec`, `#privacy`

---

<a id="item-7"></a>
## [Fallen power line reveals AI data center grid vulnerability](https://techcrunch.com/2026/07/25/one-fallen-power-line-exposed-a-growing-ai-data-center-problem-heres-how-to-fix-it/) ⭐️ 6.0/10

A fallen power line incident in Northern Virginia recently exposed significant weaknesses in how AI data centers respond to sudden grid disruptions. The event has sparked industry discussions on implementing targeted infrastructure upgrades to improve grid response capabilities for these facilities. As AI infrastructure growth outpaces power grid deployment, unexpected large-scale power withdrawals from major AI campuses threaten overall grid stability. Addressing these response gaps is critical to ensuring reliable AI operations and preventing broader grid failures as AI demand continues to surge. The core concern is not excessive power consumption by data centers, but the risk of a major AI campus tripping offline and withdrawing hundreds of megawatts from the grid within seconds. Proposed fixes focus on building layered failover architectures with multi-source redundant power, battery storage, and advanced monitoring systems.

rss · 36氪 - 科技 · Jul 25, 13:05

**Background**: Traditional data center power strategies focused on availability through redundancy, UPS systems, and backup generators to keep servers running during outages. AI workloads have shifted this model, as their massive, sudden power demands require new grid interaction protocols to avoid destabilizing local power networks. Industry groups like NERC have warned that sudden load losses from AI campuses pose a growing risk to grid stability as AI infrastructure scales.

<details><summary>References</summary>
<ul>
<li><a href="https://www.computeforecast.com/blogs/nerc-data-center-load-warning-sudden-losses-grid-stability/">NERC Data Center Load Warning: What the Industry Isn't Saying</a></li>
<li><a href="https://www.linkedin.com/posts/maggie-a-ostrowski-phd-7632222_why-ai-data-centers-require-a-new-power-playbook-activity-7474985287811481600-l3ki">Building AI Data Centers for Power Stability and Grid Impact | LinkedIn</a></li>
<li><a href="https://www.hanwhadatacenters.com/blog/redundant-data-center-power-for-ai-why-its-non-negotiable/">Redundant Data Center Power for AI: Why It's Non-Negotiable</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#data centers`, `#power grid`, `#reliability`, `#systems engineering`

---

<a id="item-8"></a>
## [Monday.com joins list of tech firms citing AI for layoffs](https://techcrunch.com/2026/07/25/the-running-list-major-tech-layoffs-in-2026-where-employers-cited-ai/) ⭐️ 3.0/10

Monday.com has become the latest technology company to attribute its workforce reductions to artificial intelligence. TechCrunch has compiled a running list of 20 major tech companies that have cited AI as a factor in significant layoffs during 2026. This trend highlights a growing pattern where major technology firms are explicitly linking workforce reductions to AI adoption and automation. It signals a shift in the tech industry's labor strategy as companies increasingly integrate AI into their operations. The list is maintained in reverse chronological order and focuses specifically on significant layoffs where AI was explicitly stated as a contributing factor. The article serves as an aggregation of layoff announcements rather than an in-depth technical analysis.

rss · 36氪 - 科技 · Jul 26, 01:30

**Background**: In recent years, many technology companies have invested heavily in artificial intelligence to automate tasks and improve efficiency. As these AI tools become more capable, some companies have reduced their human workforce, particularly in roles related to routine or automatable tasks. This phenomenon has sparked widespread discussion about the impact of AI on the job market in the technology sector.

**Tags**: `#AI`, `#tech industry`, `#layoffs`, `#business news`

---

## 📰 Top News

<a id="item-9"></a>
## [AI-driven hack targets OpenAI at superhuman speed](https://www.bbc.co.uk/news/articles/cd9w22n9e4go?at_medium=RSS&at_campaign=rss) ⭐️ 6.0/10

Hugging Face reported that an AI system with little or no human guidance carried out a high-speed hack targeting OpenAI. The attack was executed at superhuman speed, raising questions about its severity and underlying intent. This incident highlights the growing capability of autonomous AI agents to conduct cyberattacks with minimal human oversight, posing new challenges for cybersecurity defenses. It signals a shift in the threat landscape as AI tools become more accessible to potential attackers targeting major tech firms like OpenAI. The hack was described as being performed at superhuman speed, indicating the AI's ability to execute attack steps far faster than human operators. Hugging Face, a major open-source AI platform, was the source reporting this incident, though specific technical details of the breach remain limited in current reports.

rss · BBC Technology · Jul 25, 10:14

**Background**: Hugging Face is a New York-based company that develops machine learning tools and hosts a large open-source community for sharing AI models and datasets. Autonomous hacking agents are AI-driven workflows that can chain tasks such as reconnaissance and payload generation with minimal human oversight once launched. The concept of 'superhuman speed' in cybersecurity refers to AI systems processing threats and executing attack steps far faster than human teams can manage.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hugging_Face">Hugging Face - Wikipedia</a></li>
<li><a href="https://cybersecuritynews.com/hugging-face-confirms-ai-driven-breach/">Hugging Face Confirms AI-Driven Breach: Attackers used ...</a></li>
<li><a href="https://www.opswat.com/blog/ai-hacking-how-hackers-use-artificial-intelligence-in-cyberattacks">AI Hacking - How Hackers Use Artifical Intelligence in ...</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#cybersecurity`, `#OpenAI`, `#AI capabilities`, `#tech news`

---

## ₿ Crypto

<a id="item-10"></a>
## [Robinhood Chain RWA activity jumps fivefold with larger tokenized stock trading](https://www.coindesk.com/business/2026/07/25/robinhood-chain-s-real-world-assets-jump-fivefold-as-tokenized-stocks-start-trading-in-bigger-size) ⭐️ 4.0/10

Robinhood Chain reported a fivefold increase in real-world asset activity after launching larger-scale tokenized stock trading. The growth reflects rising adoption of onchain financial services on the platform as of July 25, 2026. This growth signals increasing demand for tokenized real-world assets and onchain equity exposure among retail-focused users. It also demonstrates the practical scaling of Layer-2 blockchain infrastructure for mainstream financial use cases. Robinhood Chain is a permissionless, Ethereum-compatible Layer-2 blockchain built on the Arbitrum Orbit stack and designed for onchain financial services. The platform focuses on native issuance and trading of real-world assets such as tokenized stocks.

rss · CoinDesk · Jul 25, 10:00

**Background**: Real-world asset tokenization is the process of representing ownership rights to physical or traditional financial assets through digital tokens on a blockchain. Tokenized stocks are blockchain-based digital assets that provide economic exposure to traditional equities and can be traded onchain. Layer-2 blockchains like Robinhood Chain improve scalability and reduce transaction costs compared to the Ethereum mainnet.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Robinhood_Chain">Robinhood Chain</a></li>
<li><a href="https://robinhood.com/us/en/chain/">Robinhood Chain: Built for onchain finance</a></li>
<li><a href="https://www.gemini.com/cryptopedia/what-are-tokenized-stocks-and-how-do-they-work">What Are Tokenized Stocks and How Do They Work? | Gemini</a></li>

</ul>
</details>

**Tags**: `#blockchain`, `#tokenization`, `#fintech`, `#real-world assets`, `#trading`

---