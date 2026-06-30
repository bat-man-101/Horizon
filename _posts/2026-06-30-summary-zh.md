---
layout: default
title: "Horizon Summary: 2026-06-30 (ZH)"
date: 2026-06-30
lang: zh
---

> 从 132 条内容中筛选出 16 条重要资讯。

---

1. [vLLM v0.24.0：支持 MiniMax-M3 并优化 DeepSeek-V4](#item-1) ⭐️ 9.0/10
2. [最高法院：地理围栏搜查令需受宪法保护](#item-2) ⭐️ 9.0/10
3. [谷歌 AI 同行评审处理 1 万篇论文，错误检测率提高 34%](#item-3) ⭐️ 9.0/10
4. [Ornith-1.0：用于智能体编程的自脚手架大语言模型](#item-4) ⭐️ 8.0/10
5. [ChatGPT 推翻陈立杰苦研 7 年的 Erdős 猜想](#item-5) ⭐️ 8.0/10
6. [MiCA 截止日期或迫使 1000 万欧盟加密用户离开平台](#item-6) ⭐️ 7.0/10
7. [BNY Mellon 将 USDC 铸造与赎回纳入托管平台](#item-7) ⭐️ 7.0/10
8. [BIS 警告 AI 投资债务可能引发金融危机](#item-8) ⭐️ 7.0/10
9. [先驱 zk-rollup 项目 Loopring 因采用率低关闭 DEX](#item-9) ⭐️ 7.0/10
10. [OpenAI 绘制欧盟 AI 就业变化图](#item-10) ⭐️ 6.0/10
11. [Securitize 获股东批准 SPAC 合并，即将在纽交所上市](#item-11) ⭐️ 6.0/10
12. [私钥泄露导致 160 亿美元加密黑客损失中的 40%](#item-12) ⭐️ 6.0/10
13. [白宫将游说执法机构支持加密货币清晰法案](#item-13) ⭐️ 6.0/10
14. [Vitalik Buterin：加密货币最强理念尚未成熟](#item-14) ⭐️ 6.0/10
15. [英国设定 2027 年 FCA 加密公司授权截止日期](#item-15) ⭐️ 6.0/10
16. [Breez SDK 实现比特币到稳定币跨链支付](#item-16) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [vLLM v0.24.0：支持 MiniMax-M3 并优化 DeepSeek-V4](https://github.com/vllm-project/vllm/releases/tag/v0.24.0) ⭐️ 9.0/10

vLLM v0.24.0 新增了对 MiniMax-M3 模型的支持，并对 DeepSeek-V4 进行了重大优化，包括 FlashInfer 稀疏索引缓存和预填充分块规划改进。此版本包含来自 256 位贡献者的 571 次提交。 此版本显著扩展了 vLLM 的模型支持和推理性能，使部署 MiniMax-M3 和 DeepSeek-V4 等前沿大语言模型的开发者受益。优化提升了吞吐量和延迟，使 vLLM 在生产环境中更具竞争力。 MiniMax-M3 支持包括通过 MSA 的 BF16/FP8 索引器、MXFP4、FP8 稀疏 GQA 以及广泛的 AMD/ROCm 调优。DeepSeek-V4 优化包括 FlashInfer 稀疏索引缓存（TTFT 提升 2–4%）、预填充分块规划（端到端吞吐量提升 4%）以及在 SM100 上对 next_n > 2 的原生 DSA 索引器解码。

github · khluu · 6月29日 19:41

**背景**: vLLM 是一个开源的高吞吐量大语言模型推理引擎，广泛用于生产环境。MiniMax-M3 是一个前沿的多模态模型，支持 1M 上下文和 MiniMax 稀疏注意力（MSA）。DeepSeek-V4 是一个万亿参数的 MoE 模型，需要高效的推理优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.minimax.io/blog/minimax-m3">MiniMax M3: Frontier Coding, 1M Context, Native Multimodality — All in One Model - MiniMax Research | MiniMax</a></li>
<li><a href="https://github.com/flashinfer-ai/flashinfer">GitHub - flashinfer -ai/ flashinfer : FlashInfer : Kernel Library for LLM...</a></li>
<li><a href="https://news.skila.ai/article/deepseek-v4-trillion-parameter-multimodal-model">DeepSeek V 4 : Trillion-Parameter Multimodal AI Model | Skila News</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#open-source`, `#model optimization`, `#release`

---

<a id="item-2"></a>
## [最高法院：地理围栏搜查令需受宪法保护](https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision) ⭐️ 9.0/10

美国最高法院裁定，要求科技公司识别特定区域内所有设备的地理围栏搜查令，必须遵守第四修正案关于禁止不合理搜查和扣押的保护。 这一里程碑式的裁决为普遍监控时代的数字隐私确立了关键先例，可能限制执法部门进行大规模、无证位置追踪的能力。 该案涉及一起银行抢劫案，谷歌提供了案发地点附近 19 台设备的位置数据；法院认为此类搜查令需要具备可能原因和特定性，类似于传统搜查令。

hackernews · cdrnsf · 6月29日 15:54 · [社区讨论](https://news.ycombinator.com/item?id=48720924)

**背景**: 地理围栏搜查令（又称反向位置搜查令）允许警方要求谷歌等公司提供特定时间段内虚拟边界（地理围栏）内的所有设备列表。第四修正案保护公民免受不合理搜查，但自 Carpenter 诉美国案以来，其对第三方持有的数字数据的适用性一直存在争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Geofence_warrant">Geofence warrant - Wikipedia</a></li>
<li><a href="https://www.congress.gov/crs-product/LSB11274">Geofence Warrants and the Fourth Amendment | Congress.gov | Library of Congress</a></li>
<li><a href="https://www.nacdl.org/Content/Geofence-Warrants">NACDL - Geofence Warrants</a></li>

</ul>
</details>

**社区讨论**: 评论者注意到法院意见引用了来源并提及 Riley 案，强调了手机的普遍性。一些人讨论了监控的实际限制，指出物理窃听有资源限制，而数字监控则没有，引发了对潜在滥用的担忧。

**标签**: `#privacy`, `#supreme court`, `#surveillance`, `#law`, `#technology`

---

<a id="item-3"></a>
## [谷歌 AI 同行评审处理 1 万篇论文，错误检测率提高 34%](https://www.reddit.com/r/MachineLearning/comments/1uio9rb/googles_agentic_peerreviewer_handled_10k_papers/) ⭐️ 9.0/10

谷歌在 ICML 和 STOC 会议上部署了一个代理型 AI 同行评审系统，以 30 分钟的处理时间评审了约 1 万篇论文，新正式研究论文显示，它比零样本提示多检测出 34%的数学错误。 这为会议规模的 AI 自动化科学评审开创了先例，可能通过提高错误检测率和缩短周转时间来改变同行评审流程，影响研究人员、会议组织者和更广泛的科学界。 该系统在检测数学错误方面比零样本提示提高了 34%，记录这项工作的正式论文现已发布在 arXiv 上（2606.28277）。

reddit · r/MachineLearning · /u/Justgototheeffinmoon · 6月29日 10:05

**背景**: 同行评审是科学出版中关键但耗时的过程，常面临延迟和不一致。零样本提示是一种 AI 模型无需示例即可执行任务的技术，在此作为基线。代理型 AI 指能够自主规划和执行多步骤任务的系统，例如评审论文。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.28277">Towards Automating Scientific Review with Google's Paper Assistant...</a></li>

</ul>
</details>

**社区讨论**: Reddit 上的讨论非常热烈，许多评论者对系统的规模和错误检测改进印象深刻，但也有人担心 AI 取代人类评审员以及自动化系统可能存在的偏见。

**标签**: `#AI`, `#peer review`, `#machine learning`, `#conference`, `#automation`

---

<a id="item-4"></a>
## [Ornith-1.0：用于智能体编程的自脚手架大语言模型](https://simonwillison.net/2026/Jun/29/ornith/#atom-everything) ⭐️ 8.0/10

DeepReinforce 发布了 Ornith-1.0，一个基于 MIT 许可证的开源权重大语言模型系列（9B 到 397B），通过学习生成自己的强化学习脚手架，在编程基准上达到了最先进水平。 这是首个联合优化智能体框架和解决方案生成的开源模型系列，可能减少对人工设计编程智能体脚手架的依赖。 模型变体包括 9B Dense、31B Dense、35B MoE（每个 token 激活约 3B 参数）和 397B MoE，基于 Gemma 4 和 Qwen 3.5（均为 Apache 2.0 许可）构建。

rss · Simon Willison · 6月29日 16:17

**背景**: 传统的编程智能体强化学习使用固定的人工编写的框架来指导解决方案生成。Ornith-1.0 的自脚手架方法学习生成框架和解决方案，使模型能够发现更好的搜索轨迹并提升自身性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deep-reinforce.com/ornith_1_0.html">Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding | DeepReinforce Blog | Jun. 2026</a></li>
<li><a href="https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B">deepreinforce-ai/Ornith-1.0-9B · Hugging Face</a></li>
<li><a href="https://www.marktechpost.com/2026/06/25/deepreinforce-releases-ornith-1-0-an-open-source-coding-model-family-that-learns-its-own-rl-scaffolds/">DeepReinforce Releases Ornith-1.0: An Open-Source Coding Model Family That Learns Its Own RL Scaffolds - MarkTechPost</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：一些人称赞其编程性能和创造性解决方案，而另一些人指出它在没有工具的情况下聊天表现不佳且容易产生幻觉。还有人怀疑它是否只是 Qwen 或 Gemma 4 的微调版本，并对可访问性表示担忧（例如，9B 模型需要 80GB GPU）。

**标签**: `#LLM`, `#open-source`, `#coding`, `#AI`, `#model release`

---

<a id="item-5"></a>
## [ChatGPT 推翻陈立杰苦研 7 年的 Erdős 猜想](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&mid=2652709773&idx=2&sn=68bde762eb0070f5bd61518728971232) ⭐️ 8.0/10

据报道，OpenAI 的 ChatGPT 解决了一个基于 Erdős 猜想的计算几何核心问题，该问题曾由著名理论家陈立杰研究了 7 年。 这标志着 AI 驱动数学的重要里程碑，表明大语言模型能够对理论计算机科学中长期未解的难题做出贡献。 该问题与单位距离问题相关，这是一个有 80 年历史的离散几何猜想。据报道，OpenAI 的模型否定了该猜想，推翻了之前的假设。

rss · 新智元 · 6月29日 05:01

**背景**: 计算几何中的 Erdős 猜想，特别是单位距离问题，询问平面上 n 个点之间单位距离的最大数量。陈立杰是加州大学伯克利分校著名的理论计算机科学家，以计算复杂性研究闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/model-disproves-discrete-geometry-conjecture/">An OpenAI model has disproved a central conjecture in... | OpenAI</a></li>
<li><a href="https://interestingengineering.com/ai-robotics/openai-paul-erdos-geometry-problem-cracked">80-year-old geometry puzzle cracked by OpenAI using number theory</a></li>

</ul>
</details>

**标签**: `#AI`, `#computational geometry`, `#ChatGPT`, `#Erdős conjecture`, `#theoretical computer science`

---

<a id="item-6"></a>
## [MiCA 截止日期或迫使 1000 万欧盟加密用户离开平台](https://www.coindesk.com/business/2026/06/29/mica-july-1-deadline-could-leave-10-million-crypto-users-searching-for-a-new-platform-in-the-eu) ⭐️ 7.0/10

2026 年 7 月 1 日欧盟《加密资产市场法案》（MiCA）全面合规的截止日期可能导致约 1000 万欧盟加密用户无法使用合规平台。 这一截止日期代表着重大监管转变，可能扰乱数百万用户并重塑欧洲加密格局，可能将用户推向不受监管或不合规的替代方案。 MiCA 要求加密资产服务提供商获得欧盟成员国授权，并遵守关于稳定币、市场滥用和消费者保护的严格规定。未能在 2026 年 7 月 1 日前满足这些要求的平台必须停止在欧盟运营。

rss · CoinDesk · 6月29日 15:03

**背景**: MiCA 是欧盟首个针对加密资产的全面监管框架，于 2023 年 4 月通过，自 2024 年 12 月起全面适用。它旨在保护投资者、确保金融稳定并促进创新，同时解决洗钱和市场操纵等风险。2026 年 7 月 1 日是所有加密资产服务提供商的最终合规日期。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Markets_in_Crypto-Assets">Markets in Crypto-Assets - Wikipedia</a></li>
<li><a href="https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica">Markets in Crypto-Assets Regulation (MiCA) - ESMA</a></li>

</ul>
</details>

**标签**: `#crypto regulation`, `#MiCA`, `#EU`, `#blockchain`, `#finance`

---

<a id="item-7"></a>
## [BNY Mellon 将 USDC 铸造与赎回纳入托管平台](https://cointelegraph.com/news/bny-adds-usdc-minting-and-redemption-to-institutional-custody-platform?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) ⭐️ 7.0/10

BNY Mellon 扩展其机构托管平台，支持 USDC 稳定币的铸造与赎回，深化了与 Circle 的合作关系。 这一整合标志着传统金融对加密货币采用的重要一步，像 BNY Mellon 这样的大型银行直接参与稳定币操作，可能提升机构对数字资产的信任和流动性。 BNY Mellon 已是 USDC 储备的主要托管人，这一新功能使客户能够直接通过该银行平台铸造和赎回 USDC，简化了稳定币的获取流程。

rss · CoinTelegraph · 6月29日 16:10

**背景**: USDC 是一种与美元 1:1 锚定的稳定币，由 Circle 发行。铸造和赎回分别指通过存入美元创建新的 USDC 代币以及销毁代币以提取美元的过程。BNY Mellon 等机构托管平台为大型客户提供数字资产的安全存储和管理服务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.circle.com/circle-mint">Circle Mint | Mint USDC, Unlock Business Efficiency | Circle</a></li>
<li><a href="https://help.circle.com/s/article/USDC-on-supported-blockchains-minting-redemption-FAQs?language=en_US">USDC supported blockchains | minting, redemption, & FAQs</a></li>

</ul>
</details>

**标签**: `#cryptocurrency`, `#institutional custody`, `#USDC`, `#BNY Mellon`, `#blockchain`

---

<a id="item-8"></a>
## [BIS 警告 AI 投资债务可能引发金融危机](https://cointelegraph.com/news/bis-sounds-alarm-on-ai-exuberance-as-debt-fueled-boom-risks-bust?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) ⭐️ 7.0/10

国际清算银行（BIS）警告称，由债务和高杠杆非银行机构推动的过度 AI 支出对全球金融稳定构成系统性风险。 这一来自主要央行机构的警告凸显了金融体系中新的系统性风险来源，如果 AI 投资泡沫破裂，可能影响全球市场和投资者。 BIS 报告指出，AI 投资严重依赖债务和高杠杆的非银行金融机构，这些机构可能迅速崩溃并引发连锁反应。

rss · CoinTelegraph · 6月29日 05:31

**背景**: 系统性风险是指一家机构的损失可能通过金融体系蔓延，导致大范围崩溃。非银行金融机构（如对冲基金和私募股权公司）迅速增长，目前占全球信贷的近 50%，增加了杠杆率和相互关联性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Non-bank_financial_institution">Non - bank financial institution - Wikipedia</a></li>
<li><a href="https://www.imf.org/en/blogs/articles/2025/09/29/explainer-five-megatrends-shaping-the-rise-of-nonbank-finance">Explainer: Five Megatrends Shaping the Rise of Nonbank Finance</a></li>

</ul>
</details>

**标签**: `#AI`, `#finance`, `#systemic risk`, `#regulation`

---

<a id="item-9"></a>
## [先驱 zk-rollup 项目 Loopring 因采用率低关闭 DEX](https://cointelegraph.com/news/pioneering-zk-rollup-loopring-announces-dex-closure-citing-no-adoption?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) ⭐️ 7.0/10

Loopring，一个先驱性的 zk-rollup 协议，宣布关闭其去中心化交易所（DEX），原因是缺乏采用，并指出缺少虚拟机与可组合性是关键限制。 此次关闭凸显了早期 zk-rollup 设计的关键局限性——缺乏虚拟机和可组合性，而这是构建活跃 DeFi 生态所必需的。这表明 Layer 2 解决方案必须支持智能合约可组合性，才能吸引用户和开发者。 Loopring 团队宣布关闭 DEX，并表示缺少虚拟机导致无法与其他 DeFi 协议进行可组合性交互，限制了生态发展。协议将继续运行，但 DEX 将关闭。

rss · CoinTelegraph · 6月29日 03:15

**背景**: zk-rollup 是一种 Layer 2 扩容方案，将交易打包到链下并向以太坊提交有效性证明，从而降低 Gas 费并提高吞吐量。DeFi 中的可组合性指像乐高积木一样组合不同协议的能力，从而实现复杂的金融应用。虚拟机（如 EVM）允许执行智能合约，这对可组合性至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://chain.link/education-hub/zero-knowledge-rollup">What Are ZK Rollups ? | Chainlink</a></li>
<li><a href="https://ethereum.org/developers/docs/evm/">Ethereum Virtual Machine (EVM) | ethereum.org</a></li>

</ul>
</details>

**标签**: `#zk-rollup`, `#Layer 2`, `#DeFi`, `#blockchain`, `#scalability`

---

<a id="item-10"></a>
## [OpenAI 绘制欧盟 AI 就业变化图](https://openai.com/index/mapping-ai-jobs-transition-eu) ⭐️ 6.0/10

OpenAI 发布了一份报告，描绘了 AI 如何重塑欧盟各职业，识别出面临自动化风险的岗位、有望增长的岗位以及工作流程将发生变化的岗位。 该报告提供了 AI 对欧洲劳动力市场潜在影响的数据驱动概述，有助于政策制定者、企业和工作者为劳动力转型做好准备。 该报告涵盖了欧盟广泛的职业，但缺乏具体的技术细节或按国家划分的详细数据。

rss · OpenAI Blog · 6月29日 07:00

**背景**: 像大型语言模型这样的 AI 技术越来越能够自动化认知任务，引发了关于岗位替代的担忧，但也创造了新的机遇。该报告旨在量化这些影响在多元化的欧盟经济中的表现。

**标签**: `#AI`, `#labor market`, `#Europe`, `#automation`, `#OpenAI`

---

<a id="item-11"></a>
## [Securitize 获股东批准 SPAC 合并，即将在纽交所上市](https://www.coindesk.com/business/2026/06/29/securitize-heads-to-nyse-debut-after-investors-approve-spac-merger) ⭐️ 6.0/10

领先的代币化平台 Securitize 在投资者批准其与特殊目的收购公司（SPAC）合并后，即将在纽约证券交易所上市。 此次上市标志着代币化行业的一个重要里程碑，将一家以合规为重点的现实世界资产（RWA）平台带入主流公开交易所，可能推动基于区块链的证券获得更广泛的主流采用。 投资者于 2026 年 6 月 29 日批准了 SPAC 合并，Securitize 将以新的股票代码在纽交所开始交易。该公司专注于对私募股权、房地产和风险投资基金等现实世界资产进行代币化。

rss · CoinDesk · 6月29日 23:05

**背景**: Securitize 是一个以合规为先的平台，通过发行代表现实世界资产所有权的数字证券，连接传统金融与区块链。SPAC 是一家通过 IPO 筹集资金以收购私营公司的空壳公司，能比传统 IPO 更快地使其上市。此次合并使 Securitize 能够进入公开市场并筹集更多资金用于发展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://securitize.io/">Securitize | The Leading Tokenization Platform</a></li>
<li><a href="https://www.okx.com/en-gb/learn/securitize-tokenization-investment-rwa">Securitize Tokenization Investment: Unlocking the Future of... | OKX</a></li>
<li><a href="https://en.wikipedia.org/wiki/Special-purpose_acquisition_company">Special-purpose acquisition company - Wikipedia</a></li>

</ul>
</details>

**标签**: `#blockchain`, `#tokenization`, `#SPAC`, `#NYSE`

---

<a id="item-12"></a>
## [私钥泄露导致 160 亿美元加密黑客损失中的 40%](https://www.coindesk.com/tech/2026/06/29/private-keys-not-smart-contracts-caused-40-of-crypto-s-usd16-billion-hack-losses-here-s-whats-being-done) ⭐️ 6.0/10

最新分析显示，160 亿美元加密黑客损失中的 40%源于私钥泄露，而非智能合约漏洞，这促使行业努力改进密钥管理。 这凸显了加密生态系统中一个关键的安全漏洞，因为私钥泄露通常比智能合约漏洞更难检测和预防，影响企业和个人用户。 2024 年，私钥泄露占被盗加密货币的 43%，使其无法成为竞争性审计竞赛中的发现项，且区块链系统本身无法检测私钥被盗。

rss · CoinDesk · 6月29日 15:45

**背景**: 私钥是控制加密资产的加密秘密。与可审计的智能合约漏洞不同，私钥泄露通常在资产被转移后才被发现。密钥管理涉及密钥的生成、存储、使用和销毁，基于 MPC 和 TEE 的系统等解决方案正在出现以解决这一问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.trailofbits.com/2025/06/25/maturing-your-smart-contracts-beyond-private-key-risk/">Maturing your smart contracts beyond private key risk -The Trail of...</a></li>
<li><a href="https://www.nadcab.com/blog/cryptographic-key-lifecycle">Cryptographic Key Lifecycle | From Private Key Generation to Secure...</a></li>
<li><a href="https://blog.tothemoon.com/articles/private-keys-in-crypto-what-businesses-need-to-know">Private Keys in Crypto : What Businesses Need to Know</a></li>

</ul>
</details>

**标签**: `#cryptocurrency`, `#security`, `#private keys`, `#blockchain`

---

<a id="item-13"></a>
## [白宫将游说执法机构支持加密货币清晰法案](https://www.coindesk.com/policy/2026/06/29/white-house-to-speak-with-law-enforcement-groups-to-push-crypto-s-clarity-act) ⭐️ 6.0/10

白宫计划与执法团体会面，推动《加密货币清晰法案》，该法案旨在为数字资产提供法律明确性。 此次接触表明政府对法案的高层支持，可能加速其通过，并塑造美国加密货币的监管格局。 该法案包含保护软件开发人员免于起诉的条款，这引起了天主教领袖的批评，他们认为这可能助长人口贩运。

rss · CoinDesk · 6月29日 15:23

**背景**: 《加密货币清晰法案》是一项拟议的美国联邦法律，旨在明确哪些数字资产属于证券、哪些属于商品，并确立监管边界。该法案面临多方反对，包括担心其助长非法活动的宗教组织。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://decrypt.co/371923/crypto-clarity-act-new-enemy-catholic-leaders">Crypto ’ s Clarity Act Has a New Enemy: Catholic Leaders - Decrypt</a></li>
<li><a href="https://coinunited.io/learn/en/opinions-&-insights/crypto-s-clarity-act-showdown-will-the-financial-future-be-forged-or-forgotten">Cryptos Clarity Act Showdown: Will the Financial... - CoinUnited.io</a></li>

</ul>
</details>

**标签**: `#cryptocurrency`, `#regulation`, `#policy`, `#White House`

---

<a id="item-14"></a>
## [Vitalik Buterin：加密货币最强理念尚未成熟](https://www.coindesk.com/tech/2026/06/29/vitalik-buterin-says-crypto-s-most-powerful-idea-is-still-nowhere-near-ready) ⭐️ 6.0/10

以太坊联合创始人 Vitalik Buterin 表示，常被视为加密货币最强理念的账户抽象（account abstraction）仍远未准备好投入主流使用。 这凸显了区块链领域理论潜力与实际实施之间的差距，影响了期待更简单、更安全钱包体验的开发者和用户。 账户抽象旨在用智能合约钱包取代外部拥有账户（EOA），实现社交恢复、多因素认证等功能，但在安全性、Gas 费用和采用方面面临挑战。

rss · CoinDesk · 6月29日 11:52

**背景**: 账户抽象是以太坊的一项拟议升级，通过允许用户账户由智能合约控制，使其更加灵活和安全。目前，以太坊有两种账户类型：外部拥有账户（由私钥控制）和合约账户（由代码控制）。账户抽象将模糊这一区别，实现批量交易、赞助交易和恢复机制等功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ethereum.org/roadmap/account-abstraction/">Account abstraction | ethereum .org</a></li>
<li><a href="https://www.theblock.co/post/284908/vitalik-buterin-account-abstraction">Vitalik Buterin highlights account abstraction in security... | The Block</a></li>
<li><a href="https://coinmarketcap.com/academy/article/vitalik-buterin:-account-abstraction-a-"pretty-big-deal"-to-drive-web3-adoption">Vitalik Buterin : Account Abstraction a “Pretty Big...” | CoinMarketCap</a></li>

</ul>
</details>

**标签**: `#cryptocurrency`, `#blockchain`, `#vitalik buterin`, `#ethereum`

---

<a id="item-15"></a>
## [英国设定 2027 年 FCA 加密公司授权截止日期](https://cointelegraph.com/news/uk-crypto-rules-2027-fca-authorization-deadline?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) ⭐️ 6.0/10

英国金融行为监管局（FCA）已最终确定其加密监管框架，要求所有加密货币公司在 2027 年 2 月前获得全面授权。 这标志着从当前注册制度向全面的、基于活动的监管框架的重大转变，使加密资产与传统金融接轨，并可能吸引机构投资者。 授权门户将于 2026 年 9 月 30 日开放，公司必须遵守《金融服务与市场法》（FSMA）下的五项核心受监管活动。

rss · CoinTelegraph · 6月29日 23:01

**背景**: 目前，英国加密公司只需在 FCA 注册以符合反洗钱要求。新框架引入了类似于传统金融机构的全面授权要求，涵盖托管、交易和借贷等领域。英国旨在通过这些法规成为全球加密中心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lasmargaritasinc.com/fca-crypto-authorization-requirements-for-exchanges-in">FCA Crypto Authorization Requirements for Exchanges in 2026</a></li>
<li><a href="https://www.ig.com/uk/trading-strategies/fca-crypto-regulation-uk-what-investors-need-to-know-260624">UK FCA crypto regulation: what Bitcoin holders need to know... - IG UK</a></li>
<li><a href="https://www.edgen.tech/news/crypto/uk-targets-crypto-hub-status-with-2027-regulatory-framework">UK Targets Crypto Hub Status With 2027 Regulatory Framework</a></li>

</ul>
</details>

**标签**: `#cryptocurrency`, `#regulation`, `#UK`, `#FCA`

---

<a id="item-16"></a>
## [Breez SDK 实现比特币到稳定币跨链支付](https://cointelegraph.com/news/breez-bitcoin-wallets-send-usdc-usdt-without-holding-stablecoins?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) ⭐️ 6.0/10

Breez 推出了新的 SDK 功能，允许开发者将比特币余额中的支付路由到超过 30 个区块链上的 USDC 或 USDT 接收方，而无需用户持有稳定币。 这一创新连接了比特币和稳定币生态系统，使比特币持有者无需转换或持有稳定币即可进行以稳定币计价的交易，可能扩大比特币在日常支付中的实用性。 该功能是 Breez SDK 的一部分，该 SDK 基于 Spark 构建，Spark 是一种原生比特币 Layer 2 解决方案，提供即时结算和多资产支持。它支持超过 30 个区块链，包括以太坊、Solana 和 Polygon 等主要网络。

rss · CoinTelegraph · 6月29日 13:00

**背景**: USDC 和 USDT 等稳定币是与法定货币挂钩的加密货币，常用于支付和 DeFi。比特币虽然被广泛持有，但由于波动性和结算速度较慢，在日常交易中不太实用。Breez SDK 旨在通过利用闪电网络和现在的稳定币路由来简化比特币支付。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cryptobriefing.com/breez-bitcoin-stablecoin-payments-30-blockchains/">Breez launches Bitcoin - to - stablecoin payments across 30 blockchains</a></li>
<li><a href="https://breez.technology/sdk/">Breez SDK | Add Bitcoin to Any App or Service</a></li>
<li><a href="https://coincentral.com/breez-launches-bitcoin-to-stablecoin-payments-without-holding-usdc-or-usdt/">Breez Launches Bitcoin - to - Stablecoin Payments Without Holding...</a></li>

</ul>
</details>

**标签**: `#Bitcoin`, `#stablecoins`, `#payments`, `#SDK`

---