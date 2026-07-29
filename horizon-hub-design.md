# Horizo​​nHub产品设计文档

## 定位

**一句话定位**: The information source marketplace for the Horizon ecosystem—driven by real community usage data for discovery, recommendation, and quality assessment.

**与竞争对手的差异**:

| Product | What it does | What it doesn't do |
|---|---|---|
| RSSHub | Turns websites without RSS into RSS (Pipe) | No quality assessment, no recommendations |
| Feedly | RSS Reader with discovery features | No AI filtering, no personalized recommendations |
| HN / Reddit | Community-driven content aggregation | Fixed sources, user cannot customize |
| **地平线枢纽** | **数据驱动的来源推荐和质量评估** | **没有内容托管，没有读者** |

**核心护城河**: The daily operation of every Horizon user generates quality data for information sources (AI scores, signal-to-noise ratio, output frequency). When aggregated in the Hub, this data forms a **动态质量概况** that no static recommendation list can provide.

---

## 系统架构

```
┌──────────────────────────────────────────────────┐
│                    User Local                    │
│                                                  │
│  horizon-wizard (TUI)       Horizon CLI          │
│  ┌────────────────┐         ┌────────────────┐   │
│  │ Browse/Search  │         │ Fetch -> AI    │   │
│  │ Add/Remove     │──Write─▶│ Score ->       │   │
│  │ Recommend      │         │ Gen Summary    │   │
│  └───────┬────────┘         └───────┬────────┘   │
│          │                          │            │
└──────────┼──────────────────────────┼────────────┘
           │ Report Ops Events        │ Report Quality Data
           ▼                          ▼
┌──────────────────────────────────────────────────┐
│                 HorizonHub Server                │
│                                                  │
│  ┌───────────┐  ┌─────────────┐  ┌────────────┐  │
│  │ Source DB │  │ Rank Engine │  │ Recommender│  │
│  └───────────┘  └─────────────┘  └────────────┘  │
│                        │                         │
│               ┌────────▼────────┐                │
│               │   Hub Web UI    │                │
│               │ (Market / Rank) │                │
│               └─────────────────┘                │
└──────────────────────────────────────────────────┘
```

Two core components:
- **集线器服务器**: Data center + Web frontend, receiving reports, storing statistics, providing APIs and web pages.
- **本地客户端（地平线向导）**: The sole entry point for users to manage information sources; every operation naturally generates data.

---

## Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

### 客源市场（浏览）

The core interface users see when opening the Hub website.

**页面结构**:

- **顶部仪表板**: A row of statistics cards.
  - Total Sources | Field Categories | Contributors | Active Users

- **源卡瀑布**: Each source has a card.
  - Source Name + Type Tags (RSS / Reddit / GitHub / Telegram / Twitter)
  - Color-coded Field Tags (AI Purple, Systems Blue, Security Red...)
  - One-sentence Bio (CN/EN)
  - Key Metrics: Users · AI Avg Score · Signal-to-Noise Ratio
  - Contributor Avatars
  - Badges: 🔥 Hot / ✨ New / ⚠️ Quality Dropped

- **过滤和排序**:
  - Filter by field / language / type
  - Sort by Popularity (Users) / Quality (AI Avg) / SNR / Latest Added
  - Keyword Search

### 来源简介

The detail page for each source, showing a complete data-driven profile.

**包含数据**:

| Metric | Description | Data Source |
|---|---|---|
| Active Users | Number of users using this source in the past 30 days | Telemetry |
| AI Avg Score | Average AI score of content produced by this source | Telemetry |
| SNR | Percentage of items passing AI filtering vs. total fetched | Telemetry |
| Avg Daily Output| Average number of items fetched per day | Telemetry |
| Score Trend | Line chart of AI average scores over the last 30 days | Telemetry Aggregation |
| User Trend | Changes in active users over the last 30 days | Telemetry Aggregation |
| Contributor | Who submitted this source | User submission records |
| Date Added | When it was added to the Hub | Submission records |

### 用户提交（贡献）

**提交流程**:

```
User (Hub Web or Local Client)
  → GitHub OAuth Login
  → Fill info: Name, URL, Type, Category, Language, Bio
  → Submit

Hub Server
  → Automatically fetch last 10 items from source
  → AI quality assessment (Avg score, SNR)
  → Quality OK → Auto-online, Status: ✅ Online
  → Quality Poor → Mark pending, notify maintainer for manual review
```

**渠道**:
- Hub Web Form (most intuitive)
- Local Client Submission (one-click via `horizon-wizard`)

### 智能推荐（推荐）

**应用场景**:

1. **新用户冷启动**: Enter interest keywords ("AI", "Linux Kernel") to recommend the best source combination.
2. **补充推荐**: Analyze existing config to recommend sources with complementary coverage and flag high-overlap sources.
3. **协同过滤** (post-scale): "Users with similar tastes also read..."

**Rec 算法的输入**:
- Source field tags
- Content overlap between sources (calculated via deduplication data)
- Usage patterns of user cohorts

### 一键导出（Export）

After users select sources on the Hub website:

- Generate `config.json` snippet → Copy to clipboard
- Download full config file
- Generate `horizon-wizard` command → One-click import via terminal

### 贡献者系统（社区）

**贡献者排行榜**:
- Ranked by number of sources contributed.
- Displays GitHub avatar + link + contribution count.

**贡献者主页**:
- Sources I submitted.
- How many people use my sources in total.
- Average quality score of my sources.

**徽章系统**:

| Badge | Condition |
|---|---|
| 🌱 First Contribution | Submit the first source |
| 🌟 Quality Contributor| Contributed sources have Avg Score ≥ 7.0 |
| 🔥 Popular Contributor| A single source used by ≥ 50 people |
| 👑 Core Contributor | Contributed ≥ 10 sources |

### 源健康监测

**自动衰变检测** (Option A — Passive):

Hub server continuously tracks active user trends for each source. If usage drops continuously (e.g., >30% drop within 30 days), auto-mark with a ⚠️ warning.

**用户反馈收集** (Option B — Active):

When a user deletes or disables a source via `horizon-wizard`, a popup asks for optional feedback:

```
You removed "QbitAI", can you tell us why? (Optional, Enter to skip)
1. Quality dropped
2. Too much overlap with other sources
3. Low update frequency / defunct
4. Doesn't match my interests
>
```

Reported to the Hub, integrated with decay data for comprehensive judgment.

---

## 分布式代理操作系统

### 类比

If the Horizon ecosystem is viewed as a **分布式代理操作系统**.

A single Horizon instance is like a "standalone machine" managing one user's information flow. HorizonHub acts as the **控制平面** that coordinates all users' Agents into a whole, allowing decentralized individual judgments to converge into collective intelligence.

### 为何“出现”？

Each Agent runs independently and is unaware of others, but:
- **多样性**: Different users subscribe to sources in different fields, naturally providing diverse perspectives.
- **独立**: Each Agent's AI scoring is unaffected by other users.
- **聚合**: The Hub aggregates all scores to form a global quality signal more accurate than any single Agent.

This is not designed intelligence, but rather consensus **新兴的** from a large number of independent judgments—mathematically aligned with the Condorcet Jury Theorem.

---
