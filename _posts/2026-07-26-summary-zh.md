---
layout: default
title: "Horizon Summary: 2026-07-26 (ZH)"
date: 2026-07-26
lang: zh
---

> 从 92 条内容中筛选出 12 条重要资讯。

---

**🤖 AI 新闻（2）**
  1. [Ruff v0.16.0 将默认 lint 规则从 59 条大幅扩展至 413 条](#item-1) ⭐️ 8.0/10
  2. [清华与腾讯提出基于 Rollout 的 LLM 后训练降本方法](#item-2) ⭐️ 3.0/10

**📌 其他（3）**
  3. [Anthropic 发布 Claude 5 模型上下文工程新规则](#item-3) ⭐️ 7.0/10
  4. [Fly.io 在新任 CEO Scott Johnston 领导下转向 Sprites](#item-4) ⭐️ 7.0/10
  5. [开放权重 AI 迎来类似 Kubernetes 的企业级采用拐点](#item-5) ⭐️ 7.0/10

**🚀 科技动态（3）**
  6. [一根坠落电线暴露 AI 数据中心电网韧性缺陷](#item-6) ⭐️ 7.0/10
  7. [神秘黑客活动家 Phineas Fisher 人物侧记](#item-7) ⭐️ 6.0/10
  8. [马斯克的 Boring Company 拟以 200 亿美元估值融资](#item-8) ⭐️ 3.0/10

**📰 热点新闻（3）**
  9. [硅谷在限制中国 AI 技术准入问题上产生分歧](#item-9) ⭐️ 6.0/10
  10. [DeepSeek 告知潜在投资者暂停本轮融资](#item-10) ⭐️ 5.0/10
  11. [日本寻求国际 AI 合作以减少对美中依赖](#item-11) ⭐️ 4.0/10

**₿ 加密资产（1）**
  12. [Robinhood Chain 真实世界资产增长五倍，代币化股票交易扩大](#item-12) ⭐️ 4.0/10
---

## 🤖 AI 新闻

<a id="item-1"></a>
## [Ruff v0.16.0 将默认 lint 规则从 59 条大幅扩展至 413 条](https://simonwillison.net/2026/Jul/25/ruff/#atom-everything) ⭐️ 8.0/10

Astral 于 2026 年 7 月 23 日发布了 Ruff v0.16.0，将默认启用的 lint 规则数量从 59 条增加到 413 条。新增规则包含对语法错误和即时运行时错误等严重问题的检查，这些规则此前默认处于关闭状态。 这一默认行为的重大变更将影响大量 Python 开发者和 CI 流水线，因为未固定版本的 Ruff 依赖可能导致现有工作流因新检测出的问题而失败。它在无需额外配置的情况下就能捕获更多严重缺陷，从而显著提升代码质量。 自 v0.1.0 以来，Ruff 的可用规则总数已从 708 条增长到 968 条，用户可以通过 `uvx ruff@latest check .` 命令试用新默认规则。开发者可以使用 `uvx ruff@latest check . --fix --unsafe-fixes` 自动修复大多数违规问题，但部分问题（如 datetime 调用中缺少时区参数）仍需人工审查。

rss · Simon Willison · 7月25日 22:44

**背景**: Ruff 是一款用 Rust 编写的高性能 Python lint 工具和代码格式化工具，运行速度比 Flake8、Black 等传统工具快 10 到 100 倍。Linting（代码检查）是检测源代码中程序性和风格性错误的过程，有助于发现潜在缺陷并提升代码一致性。许多开发团队会将 lint 工具集成到 CI/CD 工作流中，当代码违反预定义规则时阻止合并操作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.astral.sh/ruff/">An extremely fast Python linter and code formatter, written in Rust.</a></li>
<li><a href="https://astral.sh/ruff">Ruff , an extremely fast Python linter | Astral</a></li>
<li><a href="https://www.linkedin.com/pulse/linting-python-anurag-pola">Python Linting 101: A Beginner's Guide to Clean and Consistent Code</a></li>

</ul>
</details>

**标签**: `#python`, `#linting`, `#developer-tools`, `#ci-cd`, `#ruff`

---

<a id="item-2"></a>
## [清华与腾讯提出基于 Rollout 的 LLM 后训练降本方法](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247907199&idx=3&sn=db62b221aeb50a9dfff1af69803b2787) ⭐️ 3.0/10

清华大学与腾讯提出了一种通过优化 Rollout 策略来降低 LLM 后训练高昂成本的方法。该方法将 Agent 轨迹视为树结构，不再为所有 prompt 均摊 Rollout 预算。 基于强化学习的 LLM 后训练计算成本极高，低效的 Rollout 分配会在低价值 prompt 上浪费大量资源。该方法有望降低企业微调大模型的训练成本，并提升样本利用效率。 该方法根据不同 prompt 提供的训练信号价值分配 Rollout 预算，而非为每个 prompt 设置固定预算。它将 Agent 轨迹构建为树结构，在 Rollout 生成过程中优先分配资源给有潜力的中间状态。

rss · 量子位 · 7月25日 04:40

**背景**: LLM 后训练是指预训练阶段之后，通过监督学习或强化学习对模型进行微调，以提升任务表现和对齐效果的阶段。在 LLM 强化学习中，Rollout 是从 prompt 到终止的完整轨迹，包含中间推理步骤和可选的环境交互。现有许多后训练强化学习方法为每个 prompt 使用固定数量的 Rollout，但不同 prompt 对训练信号的贡献差异很大。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.05606">Cross-Epoch Adaptive Rollout Optimization for RL Post - Training</a></li>
<li><a href="https://themodelwire.com/article/tree-structured-rollouts-improve-sample-efficiency-in-llm-agent-training-01KXYHPFN4WG0DFDVFD1EM3F79">Tree-structured rollouts improve sample efficiency in LLM ...</a></li>
<li><a href="https://arxiv.org/html/2602.11767v3">TSR: Trajectory‑Search Rollouts for Multi‑Turn RL of LLM Agents</a></li>

</ul>
</details>

**标签**: `#LLM`, `#post-training`, `#reinforcement-learning`, `#research-teaser`

---

## 📌 其他

<a id="item-3"></a>
## [Anthropic 发布 Claude 5 模型上下文工程新规则](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) ⭐️ 7.0/10

Anthropic 发布了针对 Claude 5 代模型的最新上下文工程最佳实践指南。该指南提到，为了适配更先进的模型，Claude Code 的系统提示词已移除超过 80%，以优化上下文的整理与维护。 这份官方指南能帮助开发者和用户适应 Claude 5 代模型的行为变化，该系列模型专为更复杂、耗时更长的任务设计。它也将影响整个 AI 社区对最先进大语言模型上下文优化的实践方式。 新规则来源于 Anthropic 在为更先进的 Claude 模型优化其智能体编码工具 Claude Code 过程中积累的经验。部分早期用户反馈显示，与之前的 Opus 版本相比，新版模型的 token 使用量有所增加，且首次完成任务失败的频率更高。

hackernews · mellosouls · 7月25日 20:42 · [社区讨论](https://news.ycombinator.com/item?id=49051361)

**背景**: Claude 是由 Anthropic 开发的大语言模型系列，Anthropic 是一家总部位于旧金山、专注于 AI 安全的公益公司，由前 OpenAI 高管于 2021 年创立。上下文工程指的是在大语言模型推理过程中，整理和维护最优信息（token）集合的策略，包括提示词、检索到的记忆和其他上下文数据。Claude 5 代（也称为 Claude Fable 5）是该模型系列的第五代，专为处理此前版本无法支撑的、耗时数日的复杂异步任务而设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models">The new rules of context engineering for Claude 5 generation ...</a></li>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents">Effective context engineering for AI agents \ Anthropic</a></li>

</ul>
</details>

**社区讨论**: 社区成员讨论新实践是否通过将定制化从可迁移的 markdown 文件转移到 Anthropic 专属工具，从而增加了供应商锁定风险。部分用户反馈 Opus 5 比之前的版本犯更多错误、意外删除文件，且更频繁地绕过钩子控制；还有人批评隐藏的推理轨迹和对 Claude 自动记忆功能的过度依赖。也有评论者调侃不再需要像以前那样用“产生幻觉就害死小猫”这类极端前缀来约束模型。

**标签**: `#LLM`, `#Claude`, `#prompt-engineering`, `#AI`, `#context-engineering`

---

<a id="item-4"></a>
## [Fly.io 在新任 CEO Scott Johnston 领导下转向 Sprites](https://fly.io/blog/kurt-scott-money-sprites/) ⭐️ 7.0/10

Fly.io 宣布进行战略转型，将重点放在新一代 Sprites 产品上，并任命 Scott Johnston 为公司新任 CEO。这一组织和技术的调整旨在适应当前快速变化的人工智能和云基础设施行业格局。 这一举措反映了人工智能的进步正迫使云基础设施公司重新思考其产品战略和组织架构，以保持竞争力。它也凸显了初创公司为应对新兴的人工智能驱动的市场需求而进行转型的更广泛行业趋势。 该公司明确表示将未来的发展重心放在 Sprites 及其旨在解决的具体问题上。一些社区成员对 Sprites 在实际使用场景中的稳定性和可靠性提出了担忧。

hackernews · subarctic · 7月25日 20:43 · [社区讨论](https://news.ycombinator.com/item?id=49051369)

**背景**: Fly.io 是一个以开发者为核心的云基础设施平台，允许用户在靠近最终用户的全球各地部署全栈应用、服务器和数据库。其架构利用运行在 BEAM 虚拟机上的 Elixir 基于参与者的并发模型，以高效管理分布式系统。该平台提供 Anycast 路由、全球负载均衡以及用于有状态应用的快速附加存储等功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fly.io/">Fly.io</a></li>
<li><a href="https://platformchecker.com/blog/fly-io-tech-stack-2026">What Tech Stack Does Fly.io Use in 2026? - Platform Checker</a></li>
<li><a href="https://fwdgrade.com/fly-io">Fly.io — Global Application Hosting Platform for Edge Deployments</a></li>

</ul>
</details>

**社区讨论**: 前用户报告了 Sprites 严重的稳定性问题，包括频繁的数据丢失和无法连接的僵尸实例，这导致他们放弃了该产品。一些评论者对该转型表示怀疑，认为 AI 沙盒市场已经过度拥挤，并担心新任 CEO 可能会优先考虑利润而非创新愿景。还有人指出，这种组织层面的身份危机反映了近期大语言模型进步给许多个人和公司带来的更广泛的不确定性。

**标签**: `#cloud-infrastructure`, `#startup-strategy`, `#AI-impact`, `#devops`, `#fly-io`

---

<a id="item-5"></a>
## [开放权重 AI 迎来类似 Kubernetes 的企业级采用拐点](https://tobi.knaup.me/2026-07-25-open-weight-ai-is-having-its-kubernetes-moment/) ⭐️ 7.0/10

文章认为，开放权重 AI 目前正迎来类似 Kubernetes 的拐点，即将实现大规模企业级采用，这一趋势由成本合理性、协作潜力和相比闭源模型的实用优势共同推动。 这一转变意义重大，它可能像 Kubernetes 改变容器编排领域一样，通过让企业 AI 部署更具成本效益、可控性和协作性，重塑整个 AI 行业的格局。 开放权重 AI 模型开放了模型权重，让用户在托管、业务适配、成本和安全方面拥有更多控制权，但它并非完全开源，因为训练数据和代码通常不会公开。

hackernews · tknaup · 7月25日 14:49 · [社区讨论](https://news.ycombinator.com/item?id=49048034)

**背景**: Kubernetes 是一款容器编排平台，在达到战略拐点后实现了快速的企业级采用，成为许多组织大规模管理容器化应用的首选方案。开放权重 AI 模型是指公开其训练权重的 AI 模型，用户可以在自己的基础设施上运行、修改和部署这些模型。与完全开源的 AI 模型不同，开放权重模型通常不会公开原始训练数据或用于训练模型的完整代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/open-weight-ai-what-we-finally-opened-bonnet-nicolas-pistorio-n3ulf">Open - weight AI : what if we finally opened the bonnet ?</a></li>
<li><a href="https://portworx.com/blog/kubernetes-enterprise-adoption-trends/">Why Kubernetes is the New Enterprise Default (2026 Data)</a></li>

</ul>
</details>

**社区讨论**: 社区成员讨论了禁止中国 AI 模型的可行性，指出模型权重只是数值，无法辨别来源国家，因此这类禁令在技术上不可能实现。还有人提到 GPT-4 等闭源 AI 模型的定价不稳定，而开放权重模型为合理的推理成本提供了基准。部分用户认为开放权重 AI 需要像 Linux 生态那样由多家公司协作开发公开训练数据，另有用户分享了运行 OpenAI 20B 开放权重模型处理日常任务的正面体验。

**标签**: `#open-weight AI`, `#AI infrastructure`, `#Kubernetes`, `#AI economics`, `#open source`

---

## 🚀 科技动态

<a id="item-6"></a>
## [一根坠落电线暴露 AI 数据中心电网韧性缺陷](https://techcrunch.com/2026/07/25/one-fallen-power-line-exposed-a-growing-ai-data-center-problem-heres-how-to-fix-it/) ⭐️ 7.0/10

弗吉尼亚州北部近期发生的一起电线坠落事故，暴露了 AI 数据中心应对电网中断时的严重缺陷。文章提出了提升数据中心在电网中断期间韧性与响应能力的实用改进方案。 随着 AI 算力日益集中在特定区域，此次事件凸显了关键基础设施面临的挑战，也增加了级联故障的风险。提升数据中心的电网韧性对于保障数字经济稳定运行和 AI 持续创新至关重要。 这次险情表明，许多作为数字经济骨干的重要数据中心，即便应对轻微的电网中断也准备不足。配备灵活电力系统的设施可以减少峰值负荷暴露，更高效地接入受限电网。

rss · 36氪 - 科技 · 7月25日 13:05

**背景**: AI 数据中心是承载训练和运行人工智能模型所需计算基础设施的大型设施。这些设施高度依赖稳定的电网连接，而同步是指将频率、相位和电压匹配，以在电源与电网之间安全传输电力。随着 AI 算力向弗吉尼亚州北部等地区集中，局部电网中断可能对全球数字服务构成重大风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://snippora.com/industry/power-grid-vulnerability-threatens-ai-data-center-reliabilit-2718">Power grid vulnerability threatens AI data center reliability — Snippora</a></li>
<li><a href="https://futuresignalnews.com/ai-data-center-resilience-solutions/">AI Data Center Resilience : Solutions for Grid Disruptions</a></li>
<li><a href="https://en.wikipedia.org/wiki/Synchronization_(alternating_current)">Synchronization (alternating current) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#data centers`, `#power grid`, `#reliability`, `#systems engineering`

---

<a id="item-7"></a>
## [神秘黑客活动家 Phineas Fisher 人物侧记](https://techcrunch.com/2026/07/25/the-hacker-who-humiliated-spyware-makers-and-was-never-caught/) ⭐️ 6.0/10

TechCrunch 于 2026 年 7 月 25 日发布了一篇人物侧记，详细介绍了身份不明的黑客活动家 Phineas Fisher 的事迹，他成功入侵并曝光了多家政府间谍软件制造商，且至今未被抓获。 这篇侧记凸显了个体黑客活动家对备受争议的监控行业所能产生的实际影响，让公众关注到政府间谍软件存在的安全风险和伦理问题。 Phineas Fisher 还使用过 Phineas Phisher、Subcowmandante Marcos 等别名，被广泛认为是一名无政府主义黑客活动家，倡导为了社会公益而开展黑客行动。

rss · 36氪 - 科技 · 7月25日 20:24

**背景**: 黑客活动主义（Hacktivism）是指使用基于计算机的黑客技术作为公民不服从的一种形式，以推动政治议程或社会变革。政府间谍软件制造商开发的监控工具通常出售给国家机构用于监视目的，这引发了广泛的隐私和人权担忧。Phineas Fisher 最为人所知的事迹包括入侵 Hacking Team、Gamma International 等间谍软件制造商，并将相关数据泄露给公众。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Phineas_Fisher">Phineas Fisher - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hacktivism">Hacktivism - Wikipedia</a></li>
<li><a href="https://www.androguider.com/2026/07/the-mysterious-hacktivist-unraveling.html">The Mysterious Hacktivist: Unraveling the Legend of Phineas ...</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#hacktivism`, `#privacy`, `#surveillance`, `#infosec`

---

<a id="item-8"></a>
## [马斯克的 Boring Company 拟以 200 亿美元估值融资](https://techcrunch.com/2026/07/25/elon-musks-boring-company-reportedly-raising-funding-at-a-20-billion-valuation/) ⭐️ 3.0/10

据报道，埃隆·马斯克旗下的隧道挖掘初创公司 The Boring Company 正洽谈以 200 亿美元的估值进行新一轮融资。 这一融资轮次表明，尽管该公司未披露详细技术信息，投资者对基础设施和城市交通解决方案的兴趣依然持续。 报道中提到的 200 亿美元估值较此前的融资轮次有显著提升，但目前尚未确认具体的融资金额或领投方。

rss · 36氪 - 科技 · 7月25日 19:23

**背景**: The Boring Company（TBC）是一家由埃隆·马斯克创立的美国基础设施与隧道建设公司，最初于 2017 年作为 SpaceX 的子公司成立，2018 年分拆为独立企业。该公司专注于建设安全、快速且低成本的交通、公用设施和货运隧道，以缓解城市地面交通拥堵问题。其隧道掘进机达到作业深度后，地表产生的噪音和振动比普通行人活动还要小。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/The_Boring_Company">The Boring Company - Wikipedia</a></li>
<li><a href="https://www.boringcompany.com/tunnels">Tunnels — The Boring Company</a></li>
<li><a href="https://www.boringcompany.com/">The Boring Company</a></li>

</ul>
</details>

**标签**: `#startup`, `#funding`, `#transportation`, `#business`

---

## 📰 热点新闻

<a id="item-9"></a>
## [硅谷在限制中国 AI 技术准入问题上产生分歧](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPMGg1N0lvWXlpTm43VlhleE5IZmNpNDhTTWFZbzBnV1lUY1FCa212cl93ZkVtU00waTNFMnhib0RnaFl1MVBvZEpVbVVwUmlod1FMTV9Qazh4NjVVNThXTnZXN3U0RFBXU1Rwd3JLcjNPSjYxN0gzbzR0bkdUMmg4NElGRVVHZzdDSE5N?oc=5) ⭐️ 6.0/10

《纽约时报》报道称，硅谷内部对于美国可能出台的限制中国获取 AI 技术和人才的政策，正出现日益明显的分歧。相关争论的核心在于是否应实施更严格的边境管控，并限制与中国在 AI 领域的跨境合作。 这一政策争论可能会显著重塑全球 AI 格局，影响国际人才流动、科研合作以及中美 AI 产业之间的竞争态势。最终结果可能为科技行业未来应对地缘政治紧张局势树立重要先例。 相关讨论主要围绕 AI 政策和监管的高层行业评论展开，并未涉及技术突破或具体实施细节。文章凸显了行业利益相关方在平衡国家安全关切与开放创新之间的不同立场和矛盾。

google_news · The New York Times · 7月25日 20:07

**背景**: 随着人工智能被全球主要大国视为关键战略技术，AI 政策与地缘政治之间的联系日益紧密。美国和中国目前是 AI 发展的两大领先国家，围绕技术转移、人才流动以及跨境合作对国家安全的影响，相关争论持续不断。

**标签**: `#AI policy`, `#geopolitics`, `#Silicon Valley`, `#AI regulation`, `#industry news`

---

<a id="item-10"></a>
## [DeepSeek 告知潜在投资者暂停本轮融资](https://news.google.com/rss/articles/CBMi9gFBVV95cUxOSDdtS1JkcXdRMTJxV195eUI3MGh6UDhpSktzWXAxZTJVMEtOSk5sNTJsT3RkUW9hNmtCR3RLX2swVnA3MEJaOVh1N0pJWGl3a0Nsc2Y3d0wtUVRxS2JZbno3dWF2LVhMRWh0amtjTTl6UUhkRUdYX0NpUUtOSGlMcXZZTVR1dThzUUFQSmxhVzFVcV9oTHR2bkN0c21YaEItQU52a2ZuMDJjUEM2R0RpX0diNHV0dW11UUFxNHBnb2Q1R3F6SkV6ZU15TFN0cDR0TGZ1ZUpodXpvczJCZFRCdllHVk5sQ21YS3VQNWw1MHQ1bm5Od1HSAfYBQVVfeXFMTkg3bUtSZHF3UTEycVdfeXlCNzBoelA4aUpLc1lwMWUyVTBLTkpObDUybE90ZFFvYTZrQkd0S19rMFZwNzBCWjlYdTdKSVhpd2tDbHNmN3dMLVFUcUtiWW56N3Vhdi1YTEVodGprY005elFIZEVHWF9DaVFLTkhpTHF2WU1UdXU4c1FBUEpsYVcxVXFfaEx0dm5DdHNtWGhCLUFOdmtmbjAyY1BDNkdEaV9HYjR1dHVtdVFBcTRwZ29kNUdxekpFemVNeUxTdHA0dExmdWVKaHV6b3MyQmRUQnZZR1ZObENtWEt1UDVsNTB0NW5uTndR?oc=5) ⭐️ 5.0/10

据彭博新闻社报道，DeepSeek 已告知潜在投资者，其正在进行的融资轮次将暂停。这一进展标志着这家中国 AI 公司暂时停止了当前的募资活动。 作为以 DeepSeek-R1 等高性价比、开放权重 LLM 闻名的高知名度 AI 开发商，融资暂停可能意味着其在竞争激烈的 AI 领域中的扩张战略出现变化。这一举动可能会影响投资者对挑战 OpenAI、Meta 等老牌企业的新兴 AI 初创公司的信心。 该报道由《经济时报》发布，援引彭博新闻社作为信息原始来源。这则简短新闻片段中未披露暂停的具体时间线或该决策背后的原因。

google_news · The Economic Times · 7月25日 15:17

**背景**: DeepSeek 是一家中国 AI 公司，由梁文锋于 2023 年 7 月创立，由对冲基金幻方量化全资持有并提供资金。该公司专注于开发大语言模型（LLM），其 DeepSeek-R1 模型的性能可与 OpenAI 的 GPT-4 媲美，且训练成本大幅降低。该公司开放权重、高性价比的模型曾颠覆 AI 行业，因其较低的算力需求导致英伟达市值大幅下跌。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek</a></li>

</ul>
</details>

**标签**: `#AI`, `#DeepSeek`, `#Venture Capital`, `#Business News`, `#LLM`

---

<a id="item-11"></a>
## [日本寻求国际 AI 合作以减少对美中依赖](https://news.google.com/rss/articles/CBMiWkFVX3lxTE0zREE1YzV6QTRzQTdhMzFXU3ZuQ3dkeG9JOEJwUVI2a3VCTTJiRnlBLXNSX3FWV1lFSVJjZFBzZGJpM2k2WFlhRkloQmZQMmRkZFBocVhCMTU4UQ?oc=5) ⭐️ 4.0/10

日本正积极寻求人工智能领域的国际合作，以减少其在技术上对美国和中国的依赖。这一政策动向由共同社通过其日本电讯服务进行了报道。 此举反映了技术脱钩和多元化的广泛趋势，各国正寻求避免过度依赖主要的人工智能超级大国。这可能会重塑区域技术联盟，并影响全球 AI 供应链的格局。 该倡议被定位为一项旨在实现日本 AI 技术来源多元化的战略政策发展。在最初的报道中，并未提供具体的合作伙伴国家或技术实施细节。

google_news · Japan Wire by Kyodo News · 7月25日 01:23

**背景**: 人工智能已成为国家安全和经济竞争力的关键领域，促使许多国家努力保障自身的供应链安全。目前，美国和中国主导着全球 AI 格局，在硬件、软件和研究方面拥有重大影响力。日本作为主要的科技中心，正寻求在该领域平衡其战略自主性。

**标签**: `#AI`, `#geopolitics`, `#policy`, `#international relations`

---

## ₿ 加密资产

<a id="item-12"></a>
## [Robinhood Chain 真实世界资产增长五倍，代币化股票交易扩大](https://www.coindesk.com/business/2026/07/25/robinhood-chain-s-real-world-assets-jump-fivefold-as-tokenized-stocks-start-trading-in-bigger-size) ⭐️ 4.0/10

截至 2026 年 7 月 25 日，Robinhood Chain 报告其真实世界资产规模增长五倍，同时代币化股票的交易量以更大规模扩大。 这一增长凸显了基于区块链的金融产品日益普及，这类产品为零售用户打通了传统股票与链上基础设施的连接。 Robinhood Chain 是一条基于 Arbitrum Orbit 堆栈构建的无许可、兼容 Ethereum 的 Layer-2 区块链，专注于真实世界资产的原生发行。

rss · CoinDesk · 7月25日 10:00

**背景**: 代币化股票是记录在区块链上的公司股权数字表示形式，用于跟踪真实世界股票的价值。真实世界资产代币化是指通过区块链账本上的数字代币来表示实物或传统资产所有权的行为。Robinhood Chain 是由 Robinhood Markets, Inc.开发的 Layer-2 区块链，旨在支持链上金融服务和真实世界资产交易。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Robinhood_Chain">Robinhood Chain</a></li>
<li><a href="https://www.forbes.com/sites/digital-assets/article/what-are-tokenized-stocks-digital-equities/">What Are Tokenized Stocks? A Complete Guide In March 2026</a></li>
<li><a href="https://grokipedia.com/page/asset_tokenization">Asset tokenization</a></li>

</ul>
</details>

**标签**: `#blockchain`, `#tokenization`, `#fintech`, `#real-world assets`, `#trading`

---