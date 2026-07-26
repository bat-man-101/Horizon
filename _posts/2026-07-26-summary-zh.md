---
layout: default
title: "Horizon Summary: 2026-07-26 (ZH)"
date: 2026-07-26
lang: zh
---

> 从 94 条内容中筛选出 12 条重要资讯。

---

**🤖 AI 新闻（2）**
  1. [Ruff v0.16.0 默认启用 413 条代码检查规则](#item-1) ⭐️ 8.0/10
  2. [清华与腾讯通过优化 Rollout 分配降低 LLM 后训练成本](#item-2) ⭐️ 6.0/10

**📌 其他（3）**
  3. [Anthropic 更新 Claude 5 系列模型上下文工程规则](#item-3) ⭐️ 7.0/10
  4. [Fly.io 重新聚焦 Sprites 基础设施](#item-4) ⭐️ 7.0/10
  5. [开放权重 AI 正迎来类似 Kubernetes 的普及时刻](#item-5) ⭐️ 7.0/10

**🚀 科技动态（3）**
  6. [揭秘从未被抓获的黑客活动家 Phineas Fisher](#item-6) ⭐️ 6.0/10
  7. [一根坠落电线暴露 AI 数据中心电网响应缺陷](#item-7) ⭐️ 6.0/10
  8. [Monday.com 成为最新以 AI 为由裁员的大型科技公司](#item-8) ⭐️ 3.0/10

**📰 热点新闻（3）**
  9. [OpenAI 遭黑客攻击，超人速度引发 AI 安全担忧](#item-9) ⭐️ 6.0/10
  10. [硅谷在限制中国 AI 合作问题上出现分歧](#item-10) ⭐️ 6.0/10
  11. [DeepSeek 告知潜在投资者暂停本轮融资](#item-11) ⭐️ 5.0/10

**₿ 加密资产（1）**
  12. [Robinhood Chain 真实世界资产增长五倍，代币化股票交易扩大](#item-12) ⭐️ 4.0/10
---

## 🤖 AI 新闻

<a id="item-1"></a>
## [Ruff v0.16.0 默认启用 413 条代码检查规则](https://simonwillison.net/2026/Jul/25/ruff/#atom-everything) ⭐️ 8.0/10

Ruff v0.16.0 于 2026 年 7 月 23 日发布，将默认启用的代码检查规则从 59 条增加到 413 条。这一变更可以捕获更多严重问题，例如语法错误和即时运行时错误，但也导致许多使用未固定版本 Ruff 依赖的现有 CI 配置出现运行失败。 作为被广泛采用的高性能 Python 代码检查工具，这一默认行为的重大变更将影响大量 Python 项目的 CI 流水线和代码库。它可以帮助开发者在没有额外配置的情况下更早捕获更多潜在的运行时错误，从而提升整体代码质量。 自 v0.1.0 以来，Ruff 的可用规则总数已从 708 条增长到 968 条，新的默认规则包含对 datetime 调用缺少时区参数、盲目捕获异常等问题的检查。用户可以通过运行 `uvx ruff@latest check . --fix --unsafe-fixes` 来自动修复大部分新报告的问题。

rss · Simon Willison · 7月25日 22:44

**背景**: Ruff 是一个用 Rust 编写的高性能 Python 代码检查工具和格式化工具，运行速度比 Flake8、Black 等传统工具快 10 到 100 倍。它支持超过 900 条受 Flake8、isort、pyupgrade 等流行工具启发的检查规则，被广泛应用于 Python 项目的 CI 流水线中。CI 配置中的未固定依赖是指没有指定工具的确切版本，当工具发布带有行为变更的新版本时可能导致意外的运行失败。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.astral.sh/ruff/">An extremely fast Python linter and code formatter, written in Rust.</a></li>
<li><a href="https://docs.astral.sh/ruff/rules/">Rules | Ruff - Astral</a></li>
<li><a href="https://pydevtools.com/handbook/explanation/ruff-complete-guide/">Ruff: Complete Guide to Python's Fastest Linter | pydevtools</a></li>

</ul>
</details>

**标签**: `#python`, `#linting`, `#developer-tools`, `#ci-cd`, `#ruff`

---

<a id="item-2"></a>
## [清华与腾讯通过优化 Rollout 分配降低 LLM 后训练成本](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247907199&idx=3&sn=db62b221aeb50a9dfff1af69803b2787) ⭐️ 6.0/10

清华大学与腾讯的研究人员提出了一种基于树的智能体轨迹方法，通过优化 Rollout 预算分配而非均匀分配给每个提示词，来降低 LLM 后训练成本。该方法将智能体交互轨迹视为树形结构，以提升基于强化学习的后训练的计算效率。 该方法解决了 Rollout 生成的高计算成本问题，而 Rollout 生成是在线同策略强化学习 LLM 后训练中占比最高的训练开销。它有望让计算资源有限的组织也能以更低的成本完成 LLM 后训练。 传统的组策略优化方法会为每个提示词生成多个 Rollout 来计算优势值，但常常将预算浪费在奖励分布坍缩的提示词上。所提出的方法专注于将 Rollout 预算分配给对训练效果影响最大的提示词。

rss · 量子位 · 7月25日 04:40

**背景**: 后训练是让大语言模型对齐预期行为的关键阶段，通常使用强化学习（RL）来微调模型输出。在智能体 LLM 场景中，单个任务的交互过程会分支为多个执行路径，形成树形结构的 Token 轨迹而非线性序列。生成这些交互轨迹的 Rollout 过程，是在线同策略强化学习后训练中占比最高的计算成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.26606v1">Spend Your Rollouts Where It Counts: Rollout Allocation for ...</a></li>
<li><a href="https://arxiv.org/abs/2511.00413">[2511.00413] Tree Training: Accelerating Agentic LLMs ...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#post-training`, `#agent trajectory`, `#reinforcement learning`, `#cost optimization`

---

## 📌 其他

<a id="item-3"></a>
## [Anthropic 更新 Claude 5 系列模型上下文工程规则](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) ⭐️ 7.0/10

Anthropic 发布了专门针对新一代 Claude 5 系列模型（包括 Claude Opus 5 和 Claude Fable 5）的上下文工程更新最佳实践。该公司表示，针对这些模型移除了 Claude Code 超过 80% 的系统提示词，且未观察到编码性能的可测量下降。 这些更新指南可帮助开发者优化与最新 Claude 模型的交互，有望降低提示词复杂度与 token 使用量，提升 AI 工作流效率。相关变化也反映了大语言模型设计的整体趋势，即从冗长的手动提示工程转向更精简的上下文管理。 Anthropic 指出，从 Claude Opus 4.8 等早期模型迁移到 Claude Opus 5 可带来整体输出质量的显著提升。但部分用户反馈，与旧版本相比，Claude Opus 5 的 token 使用量更高，任务首次完成的失败率也更高。

hackernews · mellosouls · 7月25日 20:42 · [社区讨论](https://news.ycombinator.com/item?id=49051361)

**背景**: 上下文工程是指在推理过程中，为大语言模型筛选和维护最优信息（token）集合的策略，其范围不限于用户输入的提示词。Claude 是 Anthropic 开发的大语言模型系列，Claude 5 是该系列的最新迭代，包含 Opus 5、Fable 5 等模型。供应商锁定指客户过度依赖特定供应商的工具与生态，导致难以切换到其他竞争对手产品的情况。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models">The new rules of context engineering for Claude 5 generation models | Claude by Anthropic</a></li>
<li><a href="https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents">Effective context engineering for AI agents \ Anthropic</a></li>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/overview">Models overview - Claude Platform Docs</a></li>

</ul>
</details>

**社区讨论**: 社区用户反应不一，有人调侃是否需要用极端提示约束模型，也有人批评新规则是 Anthropic 推动自家工具生态、加剧供应商锁定的手段。多名用户反馈 Claude Opus 5 错误更多、会意外删除文件，且过度依赖隐藏的自动记忆功能，导致用户无法查看模型的推理过程。

**标签**: `#LLM`, `#prompt-engineering`, `#Anthropic`, `#Claude`, `#AI`

---

<a id="item-4"></a>
## [Fly.io 重新聚焦 Sprites 基础设施](https://fly.io/blog/kurt-scott-money-sprites/) ⭐️ 7.0/10

Fly.io 宣布重新聚焦并改进其 Sprites 基础设施，推出了该产品的新迭代版本。这一战略调整将 Sprites 及其旨在解决的核心问题作为公司未来的发展重点。 此次重新聚焦对依赖有状态沙箱环境的开发者来说意义重大，因为这可能会解决长期存在的可靠性问题并提升产品稳定性。这也标志着 Fly.io 在竞争激烈的云基础设施和 DevOps 市场中的战略方向。 Sprites 是具备检查点和恢复功能的有状态沙箱环境，其持久化由 S3 等对象存储提供支持。虽然该产品设计用于快速创建和硬件隔离执行，但社区反馈显示其历史上曾出现数据丢失和连接问题。

hackernews · subarctic · 7月25日 20:43 · [社区讨论](https://news.ycombinator.com/item?id=49051369)

**背景**: Sprites 是 Fly.io 推出的有状态沙箱环境，提供硬件隔离的 Linux 环境用于运行代码，并使用 NVMe 作为对象存储的读穿透缓存。它们旨在为代码执行提供简单解决方案，具备检查点/恢复功能和对象存储支持的持久化能力。该基础设施面向需要隔离、有状态执行环境的用例，包括 AI 代理和任意代码执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fly.io/sprites/">Sprites — Stateful sandbox environments</a></li>
<li><a href="https://fly.io/blog/design-and-implementation/">The Design & Implementation of Sprites · The Fly Blog</a></li>

</ul>
</details>

**社区讨论**: 社区情绪褒贬不一，部分用户在感知到此前 Sprites 缺乏关注后，对此次重新聚焦表示乐观。然而，多位开发者分享了严重历史可靠性问题，包括数据丢失、僵尸 Sprites 以及中断期间状态报告不准确。一些用户甚至因为 Fly.io 无法平衡工程创新与运营稳定性而选择迁移。

**标签**: `#infrastructure`, `#cloud-computing`, `#fly.io`, `#devops`, `#user-experience`

---

<a id="item-5"></a>
## [开放权重 AI 正迎来类似 Kubernetes 的普及时刻](https://tobi.knaup.me/2026-07-25-open-weight-ai-is-having-its-kubernetes-moment/) ⭐️ 7.0/10

文章认为开放权重 AI 正经历向企业广泛普及的转变，这与 Kubernetes 在企业基础设施领域的崛起过程类似。这一类比凸显了开放权重 AI 从小众使用到成为企业核心应用的战略转型。 这一转变标志着开放权重 AI 正成为企业默认工具，将重塑 AI 应用模式并减少对专有模型的依赖。它还会影响整个行业的 AI 政策讨论、定价透明度以及协作开发模式。 开放权重模型仅发布模型参数，不公开训练数据和代码，因此被批评为相比完全开源 AI 属于“开放洗”行为。社区讨论指出，开放权重模型为推理成本提供了基准，有助于稳定 GPT-4 等专有 AI 服务波动较大的定价。

hackernews · tknaup · 7月25日 14:49 · [社区讨论](https://news.ycombinator.com/item?id=49048034)

**背景**: 开放权重 AI 指模型参数（权重）公开可用、可供使用、研究和修改的 AI 模型，但通常不公开训练数据和源代码。Kubernetes 是一个容器编排平台，凭借其灵活性和可扩展性已成为现代企业的默认基础设施选择。这一类比将当前开放权重 AI 的普及过程，与 Kubernetes 从小众工具转向广泛企业标准的过程相提并论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Open-weight_artificial_intelligence">Open-weight artificial intelligence</a></li>
<li><a href="https://portworx.com/blog/kubernetes-enterprise-adoption-trends/">Why Kubernetes is the New Enterprise Default (2026 Data)</a></li>

</ul>
</details>

**社区讨论**: 评论者认为按原产国禁止模型是不可行的，因为权重只是数值，本身没有国家属性。其他人指出开放权重模型为 AI 行业带来了急需的定价透明度，还有人建议要像 Kubernetes 那样真正普及，需要各方协作开发使用公开训练数据的模型。也有讨论提到 OpenAI 现有的开放权重模型，用户希望这些模型能更频繁地更新。

**标签**: `#open-weight AI`, `#AI industry trends`, `#Kubernetes analogy`, `#AI policy`, `#open source`

---

## 🚀 科技动态

<a id="item-6"></a>
## [揭秘从未被抓获的黑客活动家 Phineas Fisher](https://techcrunch.com/2026/07/25/the-hacker-who-humiliated-spyware-makers-and-was-never-caught/) ⭐️ 6.0/10

TechCrunch 于 2026 年 7 月 25 日发布了一篇人物特写，详细介绍了黑客活动家 Phineas Fisher 的活动，其成功入侵了 Gamma Group 和 Hacking Team 等间谍软件供应商且从未被抓获。文章重点提及了 Fisher 在 2014 年 8 月对 Gamma Group 的首次已知攻击，以及后续针对 Hacking Team 的行动。 这篇特写揭示了黑客活动主义领域的一位知名人物，其曝光了向压迫性政权出售监控工具的公司之争议行为，提升了公众对间谍软件滥用的认知。它凸显了隐私倡导者、黑客活动家与商业监控行业之间持续的紧张关系。 Phineas Fisher 于 2014 年 8 月首次公开露面，宣布入侵了 Gamma Group，随后也声称对 Hacking Team 的入侵负责。尽管西班牙国家警察曾拘留过一名被认为是 Fisher 的嫌疑人，但截至目前尚未有确认的逮捕或身份核实。

rss · 36氪 - 科技 · 7月25日 20:24

**背景**: Phineas Fisher 是一位匿名的黑客活动家，以针对向政府开发和销售监控间谍软件的公司而闻名，包括 Gamma Group（FinFisher 的开发商）和 Hacking Team。Gamma Group 和 Hacking Team 因向压迫性政权提供可用于监控活动人士和异见者的工具而受到批评。Fisher 的攻击通常包括泄露目标公司的内部数据和源代码，以曝光其运营情况。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Phineas_Fisher">Phineas Fisher - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gamma_Group">Gamma Group - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/HackingTeam">HackingTeam - Wikipedia</a></li>
<li><a href="https://techcrunch.com/2026/07/25/the-hacker-who-humiliated-spyware-makers-and-was-never-caught/">The hacker who humiliated spyware makers and was never caught | TechCrunch</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#hacktivism`, `#spyware`, `#infosec`, `#privacy`

---

<a id="item-7"></a>
## [一根坠落电线暴露 AI 数据中心电网响应缺陷](https://techcrunch.com/2026/07/25/one-fallen-power-line-exposed-a-growing-ai-data-center-problem-heres-how-to-fix-it/) ⭐️ 6.0/10

弗吉尼亚州北部的一起电线坠落事故暴露了 AI 数据中心在应对电网中断时的严重缺陷。提出的解决方案包括实施有序的顺序断开/重连流程，以及设计能更好吸收电网扰动的数据中心。 随着 AI 数据中心消耗大量电力并导致不可预测的电网波动，其糟糕的中断响应能力威胁着更广泛的电网稳定性。随着更多超大规模设施投运，解决这一问题对保障 AI 可靠运行和可持续电网规划至关重要。 电网运营商建议相邻的数据中心负载应顺序断开或重连，以便制定更完善的预先响应流程。另一种方案是将数据中心设计为能够吸收电网扰动，而非立即切换到备用电源。

rss · 36氪 - 科技 · 7月25日 13:05

**背景**: AI 数据中心支撑着模型训练等高强度工作负载，这类任务每小时成本可达数百万美元，需要高度稳定的电力供应。大规模数据中心接入可能导致不可预测的电力波动，给传统电网运行和可靠性带来挑战。公用事业公司与数据中心开发商正加强协作，模拟设施在扰动期间的行为并共享运行数据，以维护电网稳定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/07/25/one-fallen-power-line-exposed-a-growing-ai-data-center-problem-heres-how-to-fix-it/">One fallen power line exposed a growing AI data center problem. Here's how to fix it. | TechCrunch</a></li>
<li><a href="https://www.techtimes.com/articles/319695/20260704/ai-data-centers-triggered-1800-mw-grid-drop-nerc-issues-highest-alert.htm">AI Data Centers Triggered 1,800 MW Grid Drop: NERC Issues Highest Alert</a></li>
<li><a href="https://www.datacenterknowledge.com/uptime/from-capacity-to-chaos-how-ai-data-centers-challenge-the-grid">From Capacity to Chaos: How AI Data Centers Challenge the Grid</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#data centers`, `#power grid`, `#reliability`, `#systems engineering`

---

<a id="item-8"></a>
## [Monday.com 成为最新以 AI 为由裁员的大型科技公司](https://techcrunch.com/2026/07/25/the-running-list-major-tech-layoffs-in-2026-where-employers-cited-ai/) ⭐️ 3.0/10

Monday.com 在 2026 年宣布了大规模裁员，并将 AI 列为此次裁员的原因之一。这一消息更新了一份按时间倒序排列的清单，该清单记录了今年已宣布类似以 AI 为相关因素裁员的大型科技公司。 这一趋势凸显了科技公司越来越多地将裁员归因于 AI 应用的普遍现象，预示着行业就业结构可能发生转变。它影响了数千名科技行业从业者，也反映了企业在围绕 AI 技术重组运营方式时的广泛变化。 该清单按时间倒序排列，专门收录了在 2026 年裁员公告中明确提及 AI 为相关因素的大型科技公司。这篇文章仅作为汇总追踪资料，并未对裁员事件提供深入的技术或战略分析。

rss · 36氪 - 科技 · 7月26日 01:30

**背景**: 近年来，许多科技公司采用 AI 工具来自动化原本由员工完成的工作，引发了关于 AI 对劳动力影响的广泛讨论。科技行业的裁员通常涉及业务重组以优先发展新科技，企业有时会将 AI 带来的效率提升作为缩减人员规模的理由。这份清单追踪了 2026 年明确将 AI 列为裁员相关因素的具体案例。

**标签**: `#tech industry`, `#AI`, `#layoffs`, `#business news`, `#workforce trends`

---

## 📰 热点新闻

<a id="item-9"></a>
## [OpenAI 遭黑客攻击，超人速度引发 AI 安全担忧](https://www.bbc.co.uk/news/articles/cd9w22n9e4go?at_medium=RSS&at_campaign=rss) ⭐️ 6.0/10

Hugging Face 报告称，近期一起与 OpenAI 相关的黑客攻击是由几乎无需人类指导的 AI 以超人速度完成的。这一事件引发了关于它究竟是真实的安全警告还是公关噱头的争论。 这一事件凸显了人们对 AI 系统被用于发起比人类防御者响应速度更快的网络攻击的日益担忧。它强调了整个科技行业迫切需要更强大的 AI 安全措施。 据 Hugging Face 对攻击速度和自主性的评估，这次黑客攻击据称是在极少人类干预的情况下完成的。BBC 的文章指出，该报道缺乏对所用攻击方法的详细技术分析。

rss · BBC Technology · 7月25日 10:14

**背景**: Hugging Face 是一个开源 AI 平台，提供预训练模型、数据集和构建机器学习应用的工具，常被称为“AI 界的 GitHub”。OpenAI 是一家领先的 AI 研究公司，以开发 GPT-4 等先进 AI 模型而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hugging_Face">Hugging Face - Wikipedia</a></li>
<li><a href="https://www.geeksforgeeks.org/artificial-intelligence/hugging-face-tutorial/">Hugging Face Tutorial - GeeksforGeeks</a></li>
<li><a href="https://www.ibm.com/think/topics/hugging-face">What is Hugging Face? - IBM</a></li>
<li><a href="https://spillhour.com/openai-hack-hugging-face-reports-superhuman-speed/">OpenAI Hack : Hugging Face Reports Superhuman Speed | SpillHour</a></li>

</ul>
</details>

**标签**: `#AI Security`, `#Cybersecurity`, `#OpenAI`, `#AI Safety`, `#News`

---

<a id="item-10"></a>
## [硅谷在限制中国 AI 合作问题上出现分歧](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPMGg1N0lvWXlpTm43VlhleE5IZmNpNDhTTWFZbzBnV1lUY1FCa212cl93ZkVtU00waTNFMnhib0RnaFl1MVBvZEpVbVVwUmlod1FMTV9Qazh4NjVVNThXTnZXN3U0RFBXU1Rwd3JLcjNPSjYxN0gzbzR0bkdUMmg4NElGRVVHZzdDSE5N?oc=5) ⭐️ 6.0/10

《纽约时报》报道称，硅谷在是否限制与中国 AI 项目的跨境合作与竞争这一提议上出现了日益明显的分歧。相关辩论的核心在于是否要实施更严格的边境管控，并限制与中国在 AI 领域的交流。 这一政策辩论可能会通过改变中美之间的人才、研发和投资流动，显著重塑全球 AI 格局。其结果可能影响 AI 创新的步伐，以及全球科技行业的竞争态势。 这篇文章主要关注政策和地缘政治紧张局势，而非 AI 领域的具体技术突破或产品发布。它凸显了科技行业内部在如何平衡国家安全关切与开放合作益处方面缺乏共识。

google_news · The New York Times · 7月25日 20:07

**背景**: 美国和中国目前是人工智能研发领域的两大领先国家，两国都对该技术投入了大量资源。近年来，美国对技术转让、人才流动以及与中国科技实体相关的潜在国家安全风险进行了越来越多的审查和监管讨论。这些紧张局势已经延伸到 AI 领域，因为 AI 被认为对经济和国防应用具有战略重要性。

**标签**: `#AI policy`, `#geopolitics`, `#tech industry`, `#artificial intelligence`, `#regulation`

---

<a id="item-11"></a>
## [DeepSeek 告知潜在投资者暂停本轮融资](https://news.google.com/rss/articles/CBMi9gFBVV95cUxOSDdtS1JkcXdRMTJxV195eUI3MGh6UDhpSktzWXAxZTJVMEtOSk5sNTJsT3RkUW9hNmtCR3RLX2swVnA3MEJaOVh1N0pJWGl3a0Nsc2Y3d0wtUVRxS2JZbno3dWF2LVhMRWh0amtjTTl6UUhkRUdYX0NpUUtOSGlMcXZZTVR1dThzUUFQSmxhVzFVcV9oTHR2bkN0c21YaEItQU52a2ZuMDJjUEM2R0RpX0diNHV0dW11UUFxNHBnb2Q1R3F6SkV6ZU15TFN0cDR0TGZ1ZUpodXpvczJCZFRCdllHVk5sQ21YS3VQNWw1MHQ1bm5Od1HSAfYBQVVfeXFMTkg3bUtSZHF3UTEycVdfeXlCNzBoelA4aUpLc1lwMWUyVTBLTkpObDUybE90ZFFvYTZrQkd0S19rMFZwNzBCWjlYdTdKSVhpd2tDbHNmN3dMLVFUcUtiWW56N3Vhdi1YTEVodGprY005elFIZEVHWF9DaVFLTkhpTHF2WU1UdXU4c1FBUEpsYVcxVXFfaEx0dm5DdHNtWGhCLUFOdmtmbjAyY1BDNkdEaV9HYjR1dHVtdVFBcTRwZ29kNUdxekpFemVNeUxTdHA0dExmdWVKaHV6b3MyQmRUQnZZR1ZObENtWEt1UDVsNTB0NW5uTndR?oc=5) ⭐️ 5.0/10

据彭博新闻社报道，DeepSeek 已告知潜在投资者，将暂停其正在进行的融资轮次。这一进展标志着这家中国 AI 初创公司暂时停止了募资活动。 作为一家开发出可与 OpenAI 的 GPT-4 相媲美的大语言模型的知名企业，DeepSeek 的融资决策受到全球 AI 行业的密切关注。融资暂停可能预示着这家初创公司战略重点的变化，或 AI 投资市场环境的转变。 该报道来自彭博新闻社，由《经济时报》转载，但简短的新闻片段中未详细说明暂停融资的具体原因。此次融资新闻未提及 DeepSeek 现有 AI 模型的技术更新或变动。

google_news · The Economic Times · 7月25日 15:17

**背景**: DeepSeek 是一家中国 AI 初创公司，由梁文锋于 2023 年 7 月创立，专注于开发大语言模型并探索通用人工智能（AGI）。该公司于 2025 年 1 月推出了 DeepSeek-R1 模型，其性能可与 GPT-4 等领先的当代大语言模型相媲美。此前有报道称，DeepSeek 曾洽谈以 710 亿美元估值筹集 15 亿美元资金，并筹备 2027 年上市。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek - Wikipedia</a></li>
<li><a href="https://techcrunch.com/2026/07/14/deepseek-reportedly-in-talks-to-raise-1-5b-then-ipo/">DeepSeek reportedly in talks to raise $1.5B, then IPO</a></li>

</ul>
</details>

**标签**: `#AI`, `#startup`, `#funding`, `#business`, `#DeepSeek`

---

## ₿ 加密资产

<a id="item-12"></a>
## [Robinhood Chain 真实世界资产增长五倍，代币化股票交易扩大](https://www.coindesk.com/business/2026/07/25/robinhood-chain-s-real-world-assets-jump-fivefold-as-tokenized-stocks-start-trading-in-bigger-size) ⭐️ 4.0/10

Robinhood Chain 报告其真实世界资产规模增长五倍，同时代币化股票的交易量也在扩大。这一增长反映了截至 2026 年 7 月 25 日该平台链上金融服务的活跃度上升。 这一增长表明基于区块链的真实世界资产代币化正在主流面向零售的金融平台中获得更多采用。它展示了 Layer-2 基础设施如何支持可扩展且合规的代币化传统证券交易。 Robinhood Chain 是一个基于 Arbitrum Orbit 堆栈构建的无需许可、兼容以太坊的 Layer-2 区块链，专为链上金融服务设计。代币化股票是区块链上的数字资产，代表传统股票的所有权，通常支持 24/7 交易。

rss · CoinDesk · 7月25日 10:00

**背景**: 真实世界资产代币化是指通过区块链上的数字代币来表示实物或传统金融资产的所有权。Robinhood Chain 是由 Robinhood Markets, Inc. 开发的 Layer-2 区块链，用于支持代币化资产的原生发行与交易。代币化股票允许传统股权在链上进行交易，通常具有更广泛的准入性和更长的交易时间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Robinhood_Chain">Robinhood Chain</a></li>
<li><a href="https://robinhood.com/us/en/chain/">Robinhood Chain : Built for onchain finance</a></li>
<li><a href="https://info.arkm.com/research/tokenized-stocks-whats-the-point">Tokenized Stocks : What’s The Point?</a></li>
<li><a href="https://grokipedia.com/page/asset_tokenization">Asset tokenization</a></li>

</ul>
</details>

**标签**: `#blockchain`, `#tokenization`, `#fintech`, `#real-world assets`, `#trading`

---