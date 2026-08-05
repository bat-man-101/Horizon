---
layout: default
title: Scoring System
---

# 评分系统

After fetching content from all sources, Horizon uses an AI model to score each item on a 0-10 scale. This determines what appears in the daily summary.

## 管道

1. **批量处理** — Items are scored in batches of 10 with a progress bar. Failed items receive a score of 0.
2. **内容准备** — For each item, the content is truncated (800 chars if comments are present, 1000 otherwise) and engagement metrics are assembled from metadata (HN score, Reddit upvote ratio, etc.).
3. **人工智能分析** — The prepared content is sent to the configured AI model (temperature 0.3) with a system prompt defining the scoring criteria.
4. **响应解析** — The AI response is parsed as JSON (with fallbacks for code-block-wrapped JSON). Each item gets: `ai_score` (float), `ai_reason` (string), `ai_summary` (string), and `ai_tags` (list).
5. **重试** — Failed AI calls are retried up to 3 times with exponential backoff (2-10 seconds).

## 评分标准

| Score | Tier | Description |
|-------|------|-------------|
| 9-10 | Groundbreaking | Major breakthroughs, paradigm shifts, major version releases, significant research breakthroughs |
| 7-8 | High Value | Important developments, technical deep-dives, novel approaches, insightful analysis, valuable tools |
| 5-6 | Interesting | Incremental improvements, useful tutorials, moderate community interest |
| 3-4 | Low Priority | Minor updates, common knowledge, overly promotional |
| 0-2 | Noise | Spam, off-topic, trivial updates |

## 评分因素

The AI evaluates each item based on:

- **技术深度和新颖性** — original ideas, new techniques, research contributions
- **潜在影响** — how broadly this affects software engineering, AI/ML, or systems research
- **写作/演讲质量** — clarity, structure, thoroughness
- **社区讨论** — insightful comments, diverse viewpoints, substantive debates
- **参与信号** — high upvotes/favorites paired with substantive discussion (not just raw numbers)

Engagement metadata is source-specific: HN provides score and comment count, Reddit provides upvote ratio and comment count.

## 过滤

After scoring, items are filtered by `filtering.ai_score_threshold` (default: `7.0`) and sorted by score descending. Optional balanced digest quotas are then applied before enrichment.

```json
{
  "filtering": {
    "ai_score_threshold": 7.0,
    "time_window_hours": 24,
    "max_items": 20,
    "category_groups": {
      "ai": {
        "limit": 5,
        "categories": ["ai-news", "ai-tools", "machine-learning"]
      }
    }
  }
}
```

`category_groups` limits each configured category group independently.
`max_items` caps the merged result. Both fields are optional; without them,
scoring and filtering behave as before.

Items scoring 9.0 or above are featured in the "Today's Highlights" section of the summary.

## 丰富

Items that pass the score threshold and any balanced digest limits go through a second AI pass for enrichment (`src/ai/enricher.py`):

1. **概念提取** — AI identifies 1-3 technical concepts in the item that may need explanation.
2. **网页搜索** — Each concept is searched via DuckDuckGo to gather grounding context.
3. **结构化分析** — The item content and search results are sent to AI, which produces:
   - `whats_new` — what specifically happened or changed
   - `why_it_matters` — significance and impact
   - `key_details` — notable technical details or caveats
   - `background` — background knowledge for readers without deep domain expertise

These fields are combined into a `detailed_summary` stored in the item's metadata and used in the final daily summary.
