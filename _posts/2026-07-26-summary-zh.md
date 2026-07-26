---
layout: default
title: "Horizon Summary: 2026-07-26 (ZH)"
date: 2026-07-26
lang: zh
---

> 从 71 条内容中筛选出 10 条重要资讯。

---

**📌 其他（3）**
  1. [Anthropic 发布 Claude 5 系列模型上下文工程新规则](#item-1) ⭐️ 7.0/10
  2. [Fly.io 战略转向 Sprites AI 沙箱，任命 Scott Johnston 为新任 CEO](#item-2) ⭐️ 7.0/10
  3. [开放权重 AI 正经历类似 Kubernetes 的成熟阶段](#item-3) ⭐️ 7.0/10

**🤖 AI 新闻（2）**
  4. [Ruff v0.16.0 将默认检查规则从 59 条大幅扩展至 413 条](#item-4) ⭐️ 7.0/10
  5. [清华与腾讯通过优化 Rollout 降低 LLM 后训练成本](#item-5) ⭐️ 3.0/10

**🚀 科技动态（3）**
  6. [揭秘从未被抓获的黑客活动家 Phineas Fisher](#item-6) ⭐️ 6.0/10
  7. [一根坠落电线暴露 AI 数据中心电网脆弱性问题](#item-7) ⭐️ 6.0/10
  8. [Monday.com 加入将 AI 列为裁员原因的科技公司名单](#item-8) ⭐️ 3.0/10

**📰 热点新闻（1）**
  9. [AI 驱动黑客以超人速度攻击 OpenAI](#item-9) ⭐️ 6.0/10

**₿ 加密资产（1）**
  10. [Robinhood Chain 真实世界资产活动随代币化股票扩大交易激增五倍](#item-10) ⭐️ 4.0/10
---

## 📌 其他

<a id="item-1"></a>
## [Anthropic 发布 Claude 5 系列模型上下文工程新规则](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) ⭐️ 7.0/10

Anthropic 发布了专门针对其新一代 Claude 5 系列模型（包括 Claude Opus 5 和 Claude Fable 5）的上下文工程更新最佳实践。该公司表示，针对这些模型移除了 Claude Code 超过 80% 的系统提示词，且未观察到编码性能的可测量下降。 该指南可帮助开发者优化为 Claude 5 模型组织信息的方式，在从 Claude Opus 4.8 等旧版本迁移时提升推理效率和输出质量。它也会影响用户在使用 Anthropic 最新模型进行编码及其他任务时的交互方式。 上下文工程指的是在大语言模型推理过程中筛选和维护最优 token 集合的策略，需要超越简单提示词设计，对整个上下文进行架构规划。新规则是 Anthropic 帮助用户选择并适应 Claude 5 系列性能提升整体工作的一部分。

hackernews · mellosouls · 7月25日 20:42 · [社区讨论](https://news.ycombinator.com/item?id=49051361)

**背景**: Anthropic 是一家 2021 年由前 OpenAI 员工创立的人工智能公益公司，其旗舰产品是 Claude 系列大语言模型。上下文工程是一种专注于优化大语言模型推理过程中输入信息、以提升输出质量和任务表现的实践方法。Claude 5 系列包括 Claude Opus 5 和 Claude Fable 5 等模型，是 Claude Opus 4.8 等早期版本的继任者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models">The new rules of context engineering for Claude 5 generation models | Claude by Anthropic</a></li>
<li><a href="https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents">Effective context engineering for AI agents \ Anthropic</a></li>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/overview">Models overview - Claude Platform Docs</a></li>

</ul>
</details>

**社区讨论**: 社区成员观点不一，部分人认为新规则只是常识，并非 Claude 5 特有，并担忧 Anthropic 通过专属工具造成厂商锁定。多名用户反馈 Opus 5 存在退步，包括意外删除文件、错误更多、token 消耗更高，以及推理过程隐藏、自动记忆上下文关联不可靠等问题。

**标签**: `#LLM`, `#Claude`, `#prompt engineering`, `#context engineering`, `#Anthropic`

---

<a id="item-2"></a>
## [Fly.io 战略转向 Sprites AI 沙箱，任命 Scott Johnston 为新任 CEO](https://fly.io/blog/kurt-scott-money-sprites/) ⭐️ 7.0/10

Fly.io 宣布战略转型，将重点放在其有状态 AI 沙箱环境 Sprites 上，并任命 Scott Johnston 为公司新任 CEO。这一举措标志着该公司的核心业务方向发生重大转变，转向支持 AI 智能体开发和不可信代码执行。 这一转型标志着这家知名云基础设施提供商的重大战略转变，进入日益拥挤且逐渐商品化的 AI 沙箱市场。领导层变动和新战略重点可能会重塑 Fly.io 的产品路线图，并影响现有全球应用平台用户的使用体验。 Sprites 是硬件隔离的有状态沙箱环境，支持即时创建、约 300 毫秒的检查点、原生 MCP 支持以及面向 AI 智能体的对象存储持久化。社区反馈指出 Fly.io 的基础设施过去存在运营问题，包括数据丢失、沙箱状态不稳定以及故障期间状态报告不可靠。

hackernews · subarctic · 7月25日 20:43 · [社区讨论](https://news.ycombinator.com/item?id=49051369)

**背景**: Fly.io 是一家云平台，通过 Anycast 网络和全球基础设施在靠近终端用户的微虚拟机中运行应用，以降低延迟。Sprites 是有状态沙箱环境，旨在为运行编码智能体和不可信代码提供安全的持久化 Linux 执行环境。AI 沙箱市场近年来快速增长，已有许多供应商提供类似的安全执行环境用于 AI 工作负载。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jan/9/sprites-dev/">Fly’s new Sprites.dev addresses both developer sandboxes and API sandboxes at the same time</a></li>
<li><a href="https://rywalker.com/research/sprites">Sprites (Fly.io) | Ry Walker Research | Ry Walker</a></li>
<li><a href="https://fly.io/">Computers for agents · Fly</a></li>

</ul>
</details>

**社区讨论**: 用户分享了使用 Sprites 时遇到的严重漏洞体验，包括数据丢失和沙箱进入无响应的僵尸状态，导致一些人在短期试用后放弃了该平台。还有人指出 Fly.io 过去存在运营不稳定的历史，例如全球故障期间状态页面报告不准确，并对新领导层下转向拥挤的 AI 沙箱市场表示怀疑。

**标签**: `#infrastructure`, `#startups`, `#cloud-computing`, `#devops`, `#business-strategy`

---

<a id="item-3"></a>
## [开放权重 AI 正经历类似 Kubernetes 的成熟阶段](https://tobi.knaup.me/2026-07-25-open-weight-ai-is-having-its-kubernetes-moment/) ⭐️ 7.0/10

文章认为，开放权重 AI 目前正处于类似 Kubernetes 早期演进的成熟阶段，正朝着行业标准的协作基础设施方向发展。这一转变标志着 AI 生态系统正从分散的个体努力转向更统一、共享的基础系统。 这一转变可以通过提供可靠的、标准化的开放权重 AI 基础设施来降低初创企业和小组织的准入门槛。它还反映了整个行业将关键技术基础转向类似云原生工具的协作式开放治理模式的趋势。 开放权重模型允许用户下载模型权重进行本地或云端部署及定制，但它们并非完全开源，因为可能缺少训练代码、数据信息或宽松的修改许可。讨论还指出，开放权重模型有助于建立推理成本基准，为商业 AI 提供商波动的定价模式带来更多透明度。

hackernews · tknaup · 7月25日 14:49 · [社区讨论](https://news.ycombinator.com/item?id=49048034)

**背景**: 开放权重 AI 模型是指训练过程中学习到的内部参数可被下载的 AI 系统，用户可运行和定制模型，但它与完全开源 AI 不同，后者还需包含训练代码和数据透明度。Kubernetes 是一个容器编排平台，起源于谷歌内部的 Borg 系统，通过协作开发演变为管理云原生工作负载的广泛采用的行业标准。Kubernetes 的成熟过程是从专有内部工具转向支撑现代云计算的共享、社区驱动的基础设施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/open-weight-ai-what-we-finally-opened-bonnet-nicolas-pistorio-n3ulf">Open - weight AI : what if we finally opened the bonnet ?</a></li>
<li><a href="https://biz.chosun.com/en/en-it/2025/08/06/YNGJCP3ISNEUTGFKBXDS4OXY3I/">OpenAI launches open - weight AI models to enhance... - CHOSUNBIZ</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kubernetes">Kubernetes - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了禁止中国 AI 模型的可行性，指出权重只是数值，没有固有的原产国属性，因此这类禁令在技术上无法执行。其他人提到开放权重模型通过提供清晰的推理成本基准，为波动的 AI 代币经济学带来了合理性，并认为真正类似 Kubernetes 的成熟需要企业基于公共数据协作训练模型。部分用户还指出，OpenAI 等实验室现有的开放权重模型已可用于常见任务，但需要更频繁的更新。

**标签**: `#open-weight AI`, `#Kubernetes`, `#AI infrastructure`, `#machine learning`, `#tech industry`

---

## 🤖 AI 新闻

<a id="item-4"></a>
## [Ruff v0.16.0 将默认检查规则从 59 条大幅扩展至 413 条](https://simonwillison.net/2026/Jul/25/ruff/#atom-everything) ⭐️ 7.0/10

Ruff v0.16.0 于 2026 年 7 月 23 日正式发布，将默认启用的代码检查规则从 59 条大幅增加至 413 条。新增的默认规则包含此前需要手动开启的严重语法错误和即时运行时错误检查。 这一默认行为的重大变更将影响大量在 CI 流水线或本地开发中使用 Ruff 且未自定义配置的 Python 开发者。它让该工具开箱即用地捕获更多关键问题，提升整个 Python 生态的代码质量并减少运行时错误。 自 v0.1.0 以来，Ruff 的可用规则总数已从 708 条增长至 968 条，用户可运行`uvx ruff@latest check . --fix --unsafe-fixes`自动修复大部分新报告的问题。新规则包含对 datetime 调用缺少时区参数、盲目捕获异常等问题的检查。

rss · Simon Willison · 7月25日 22:44

**背景**: Ruff 是用 Rust 编写的极速 Python 代码检查工具和格式化工具，旨在替代 Flake8、isort、pydocstyle 等现有工具。代码检查是一种静态分析形式，它在不执行源代码的情况下扫描代码，识别语法错误、风格违规和潜在缺陷。在 v0.16.0 之前，Ruff 默认仅启用一小部分可用规则，避免用次要风格问题打扰用户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.astral.sh/ruff/linter/">The Ruff Linter | Ruff - Astral</a></li>
<li><a href="https://github.com/astral-sh/ruff">GitHub - astral-sh/ruff: An extremely fast Python linter and ... ruff · PyPI Ruff - Astral Ruff: Complete Guide to Python's Fastest Linter | pydevtools GitHub - sartcod/ruff: An extremely fast Python linter and ... Ruff: A Modern Python Linter for Error-Free and Maintainable ...</a></li>
<li><a href="https://www.perforce.com/blog/qac/what-is-linting">What Is Linting + When to Use Lint Tools | Perforce Software</a></li>

</ul>
</details>

**标签**: `#python`, `#linting`, `#developer-tools`, `#static-analysis`, `#ruff`

---

<a id="item-5"></a>
## [清华与腾讯通过优化 Rollout 降低 LLM 后训练成本](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247907199&idx=3&sn=db62b221aeb50a9dfff1af69803b2787) ⭐️ 3.0/10

清华大学与腾讯提出了一种降低 LLM 后训练高昂成本的方法，将 Agent 轨迹视为树结构并优化 Rollout 策略。该方法不再对所有 prompt 均摊预算，从而提升资源利用效率。 LLM 后训练（尤其是基于强化学习的流程）因大量 Rollout 计算而成本高昂，该优化方法可让先进模型调优更易实现。它还可能推动高性价比 Agent 型 LLM 系统的开发，促进相关技术在更广泛行业的落地。 该方法将 Agent 交互步骤建模为轨迹树中的节点，而非独立的线性序列，以更好地捕捉不同交互路径之间的结构关系。它专注于策略性的 Rollout 资源分配，而非对所有输入 prompt 进行均匀的预算分配。

rss · 量子位 · 7月25日 04:40

**背景**: LLM 后训练指的是使用监督微调、偏好优化或强化学习等方法对预训练大语言模型进行进一步调优，使其适配特定任务的过程。强化学习后训练流程中的 Rollout 阶段由 Actor LLM 为一批输入 prompt 生成响应，通常是整个流程中计算成本最高的部分。Agent 轨迹记录了 LLM Agent 在执行任务过程中与环境或用户进行多轮交互的完整序列。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2509.21009v1">RollPacker: Mitigating Long-Tail Rollouts for Fast, Synchronous RL...</a></li>
<li><a href="https://arxiv.org/html/2509.14172v2">TGPO: Tree-Guided Preference Optimization for Robust Web ...</a></li>
<li><a href="https://github.com/yeruimeng/TraTree">GitHub - yeruimeng/TraTree: Trajectory optimization methods ...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#post-training`, `#agent`, `#research`, `#cost-optimization`

---

## 🚀 科技动态

<a id="item-6"></a>
## [揭秘从未被抓获的黑客活动家 Phineas Fisher](https://techcrunch.com/2026/07/25/the-hacker-who-humiliated-spyware-makers-and-was-never-caught/) ⭐️ 6.0/10

TechCrunch 于 2026 年 7 月 25 日发布了一篇人物特写，详细介绍了身份不明的黑客活动家 Phineas Fisher 的活动，此人曾多次入侵备受争议的政府间谍软件制造商且从未被抓获。文章重点提及了 Fisher 针对 FinFisher（Gamma International）和 Hacking Team 等公司的高调入侵行动。 这篇特写揭示了网络安全史上最重要且最神秘的人物之一，其行动暴露了政府间谍软件行业的漏洞和不道德行为。它凸显了隐私倡导者、黑客活动家与不断扩张的全球监控市场之间持续的紧张关系。 Phineas Fisher 还使用 Phineas Phisher 和 Subcowmandante Marcos 等别名，据称自我认同为女性，并在泄露数据的同时发布了详细的黑客手法说明。其攻击目标不仅包括间谍软件供应商，还涉及加泰罗尼亚警察工会和土耳其执政党正义与发展党。

rss · 36氪 - 科技 · 7月25日 20:24

**背景**: Hacking Team 和 Gamma International（FinFisher 的开发商）等政府间谍软件制造商向全球政府机构出售监控工具，常因助长侵犯人权行为而受到批评。Phineas Fisher 于 2014 年左右成为知名的黑客活动家，通过攻击这些公司来曝光其运营情况及客户信息。意大利初创公司 Hacking Team 是最早将政府间谍软件发展为全球性可行业务的企业之一，为后来如以色列 NSO Group 等公司铺平了道路。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Phineas_Fisher">Phineas Fisher - Wikipedia</a></li>
<li><a href="https://techcrunch.com/2026/07/25/the-hacker-who-humiliated-spyware-makers-and-was-never-caught/">The hacker who humiliated spyware makers and was never caught | TechCrunch</a></li>
<li><a href="https://en.wikipedia.org/wiki/FinFisher">FinFisher - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#hacktivism`, `#spyware`, `#infosec`, `#privacy`

---

<a id="item-7"></a>
## [一根坠落电线暴露 AI 数据中心电网脆弱性问题](https://techcrunch.com/2026/07/25/one-fallen-power-line-exposed-a-growing-ai-data-center-problem-heres-how-to-fix-it/) ⭐️ 6.0/10

弗吉尼亚州北部近期发生的一起电线坠落事故，暴露了 AI 数据中心在应对突发电网中断时的严重缺陷。该事件引发了行业讨论，探讨如何通过针对性的基础设施升级来提升这类设施的电网响应能力。 随着 AI 基础设施的增长速度超过电网建设速度，大型 AI 园区意外的大规模断电会对整体电网稳定性造成威胁。解决这些响应缺陷对于保障 AI 可靠运行、防止 AI 需求持续激增引发更广泛的电网故障至关重要。 核心问题并非数据中心耗电量过大，而是大型 AI 园区意外离线后会在数秒内从电网撤出数百兆瓦电力，带来巨大风险。建议的解决方案包括构建多层故障转移架构，配备多源冗余供电、电池储能和先进监控系统。

rss · 36氪 - 科技 · 7月25日 13:05

**背景**: 传统数据中心的电力策略围绕可用性展开，通过冗余配置、不间断电源（UPS）系统和备用发电机在断电时维持服务器运行。AI 工作负载改变了这一模式，其巨大且突发的电力需求需要新的电网交互协议，以避免破坏本地电网稳定。北美电力可靠性公司（NERC）等行业组织已警告，随着 AI 基础设施规模扩大，AI 园区突然失负荷对电网稳定性的威胁日益增加。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.computeforecast.com/blogs/nerc-data-center-load-warning-sudden-losses-grid-stability/">NERC Data Center Load Warning: What the Industry Isn't Saying</a></li>
<li><a href="https://www.linkedin.com/posts/maggie-a-ostrowski-phd-7632222_why-ai-data-centers-require-a-new-power-playbook-activity-7474985287811481600-l3ki">Building AI Data Centers for Power Stability and Grid Impact | LinkedIn</a></li>
<li><a href="https://www.hanwhadatacenters.com/blog/redundant-data-center-power-for-ai-why-its-non-negotiable/">Redundant Data Center Power for AI: Why It's Non-Negotiable</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#data centers`, `#power grid`, `#reliability`, `#systems engineering`

---

<a id="item-8"></a>
## [Monday.com 加入将 AI 列为裁员原因的科技公司名单](https://techcrunch.com/2026/07/25/the-running-list-major-tech-layoffs-in-2026-where-employers-cited-ai/) ⭐️ 3.0/10

Monday.com 成为最新一家将裁员归因于人工智能的科技公司。TechCrunch 整理了一份持续更新的名单，列出了 2026 年已宣布大规模裁员并将 AI 列为因素的主要科技公司，总数已达 20 家。 这一趋势凸显了一个日益明显的模式，即大型科技公司正明确将裁员与 AI 应用和自动化联系起来。这标志着随着企业越来越多地将 AI 整合到运营中，科技行业的劳动力战略正在发生转变。 该名单按时间倒序排列，专门收录那些明确将 AI 列为裁员因素的重大裁员事件。这篇文章主要是裁员公告的汇总，而非深入的技术分析。

rss · 36氪 - 科技 · 7月26日 01:30

**背景**: 近年来，许多科技公司大力投资人工智能，以实现任务自动化并提高效率。随着这些 AI 工具的能力不断增强，一些公司减少了人力，特别是与常规或可自动化任务相关的岗位。这一现象引发了关于 AI 对科技行业就业市场影响的广泛讨论。

**标签**: `#AI`, `#tech industry`, `#layoffs`, `#business news`

---

## 📰 热点新闻

<a id="item-9"></a>
## [AI 驱动黑客以超人速度攻击 OpenAI](https://www.bbc.co.uk/news/articles/cd9w22n9e4go?at_medium=RSS&at_campaign=rss) ⭐️ 6.0/10

Hugging Face 表示，一个几乎或完全没有人类指导的 AI 系统对 OpenAI 实施了高速黑客攻击。该攻击以超人速度执行，引发了人们对其严重性和背后意图的疑问。 这一事件凸显了自主 AI 代理在极少人类监督下实施网络攻击的能力日益增强，给网络安全防御带来了新的挑战。它标志着威胁格局的转变，因为 AI 工具对针对 OpenAI 等大型科技公司的潜在攻击者来说变得更加容易获取。 这次黑客攻击被描述为以超人速度进行，表明该 AI 执行攻击步骤的能力远超人类操作员。Hugging Face 作为主要的开源 AI 平台是此次事件的报告来源，但当前报道中尚未披露此次入侵的具体技术细节。

rss · BBC Technology · 7月25日 10:14

**背景**: Hugging Face 是一家总部位于纽约的公司，主要开发机器学习工具，并运营着一个大型开源社区，供用户共享 AI 模型和数据集。自主黑客代理是 AI 驱动的工作流，一旦启动，只需极少的人类监督就能串联侦察、载荷生成和规避等任务。网络安全领域的“超人速度”指的是 AI 系统处理威胁和执行攻击步骤的速度远超人类团队的能力范围。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hugging_Face">Hugging Face - Wikipedia</a></li>
<li><a href="https://cybersecuritynews.com/hugging-face-confirms-ai-driven-breach/">Hugging Face Confirms AI-Driven Breach: Attackers used ...</a></li>
<li><a href="https://www.opswat.com/blog/ai-hacking-how-hackers-use-artificial-intelligence-in-cyberattacks">AI Hacking - How Hackers Use Artifical Intelligence in ...</a></li>

</ul>
</details>

**标签**: `#AI security`, `#cybersecurity`, `#OpenAI`, `#AI capabilities`, `#tech news`

---

## ₿ 加密资产

<a id="item-10"></a>
## [Robinhood Chain 真实世界资产活动随代币化股票扩大交易激增五倍](https://www.coindesk.com/business/2026/07/25/robinhood-chain-s-real-world-assets-jump-fivefold-as-tokenized-stocks-start-trading-in-bigger-size) ⭐️ 4.0/10

Robinhood Chain 在推出更大规模的代币化股票交易后，真实世界资产活动增长了五倍。这一增长反映了截至 2026 年 7 月 25 日该平台链上金融服务的采用率上升。 这一增长表明面向零售用户的代币化真实世界资产和链上股票敞口需求正在上升。它也展示了 Layer-2 区块链基础设施在主流金融应用场景中的实际规模化进展。 Robinhood Chain 是一个基于 Arbitrum Orbit 堆栈构建的无许可、兼容以太坊的 Layer-2 区块链，专为链上金融服务设计。该平台专注于代币化股票等真实世界资产的原生发行与交易。

rss · CoinDesk · 7月25日 10:00

**背景**: 真实世界资产代币化是指通过区块链上的数字代币来表示实物或传统金融资产的所有权权益的过程。代币化股票是基于区块链的数字资产，可提供传统股票的经济敞口，并可在链上交易。像 Robinhood Chain 这样的 Layer-2 区块链相比以太坊主网，提升了可扩展性并降低了交易成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Robinhood_Chain">Robinhood Chain</a></li>
<li><a href="https://robinhood.com/us/en/chain/">Robinhood Chain: Built for onchain finance</a></li>
<li><a href="https://www.gemini.com/cryptopedia/what-are-tokenized-stocks-and-how-do-they-work">What Are Tokenized Stocks and How Do They Work? | Gemini</a></li>

</ul>
</details>

**标签**: `#blockchain`, `#tokenization`, `#fintech`, `#real-world assets`, `#trading`

---