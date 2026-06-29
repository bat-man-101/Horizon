# Horizon AI 新闻雷达 - 部署指南

## 📋 项目概览

- **项目**: Thysrael/Horizon - AI 驱动的个人新闻雷达
- **本地路径**: `F:\Workbuddy_space\2026-06-30-00-43-08\horizon-ai-news`
- **功能**: 多源采集 → AI 打分过滤 → 去重合并 → 背景补充 → 生成中英双语日报

---

## 两种部署方式对比

| 特性 | GitHub Actions (免费方案) | Docker 部署到 NAS |
|------|--------------------------|-------------------|
| 费用 | 免费 | 无额外费用 |
| 服务器 | 无需 | 需要 NAS/Docker |
| 外网访问 | ✅ GitHub Runner 在海外，无障碍 | ❌ 需自行配置代理 |
| 配置复杂度 | 较低 | 中等 |
| 输出方式 | GitHub Pages + Webhook | 本地文件 + Webhook |

---

## 方式一：GitHub Actions（推荐，免费）

### 你需要提供：

1. **[必须] AI API Key**（选一个即可）
   - **DeepSeek**（推荐，500万免费 Token）：https://platform.deepseek.com/
   - **Google Gemini**（有免费额度）：https://aistudio.google.com/apikey
   - 其他：OpenAI / 阿里通义 / MiniMax 等

2. **[推荐] GitHub Token**
   - 创建地址：https://github.com/settings/tokens
   - 不需要勾选任何权限，直接生成即可
   - 作用：将 GitHub API 速率从 60 次/小时提升到 5000 次/小时

3. **[可选] Webhook URL**（推送到飞书/钉钉/企业微信）
   - 如果你想把日报推送到群聊

### 操作步骤：

**Step 1: Fork 仓库**
1. 打开 https://github.com/Thysrael/Horizon
2. 点击右上角 `Fork` → 选你自己的账号

**Step 2: 添加 GitHub Secrets**
进入你 Fork 的仓库 → `Settings` → `Secrets and variables` → `Actions` → `New repository secret`，创建以下 Secret：

| Secret 名 | 值 | 必填 |
|-----------|-----|------|
| `DEEPSEEK_API_KEY` | 你的 DeepSeek API Key | ✅ |
| `GOOGLE_API_KEY` | 你的 Gemini API Key | 备用方案 |
| `GH_PAT` | 你的 GitHub Token (注意：不能以 GITHUB_ 开头) | ✅ 强烈推荐 |
| `HORIZON_WEBHOOK_URL` | 企业微信/飞书/钉钉 Webhook 地址 | 可选 |

**Step 3: 上传优化后的配置文件**
将本仓库 `data/` 目录下的 `config.github.json` 上传到你的 Fork 仓库的 `data/` 目录。

**Step 4: 手动触发运行**
在你的 Fork 仓库 → `Actions` → `Daily Horizon Summary` → `Run workflow` → 选择 `main` 分支 → 点击 `Run workflow`

**Step 5: 查看结果**
- 首次运行约 5-10 分钟
- 生成的日报在 `docs/` 目录
- 开启 GitHub Pages: `Settings` → `Pages` → Source 设为 `gh-pages` 分支
- 访问 `https://你的用户名.github.io/Horizon/`

**Step 6: 自动化**
项目已预置每日 8:00 (北京时间) 自动运行的 cron 任务，无需额外配置。

---

## 方式二：Docker 部署到你的绿联 NAS

既然你已经有 Docker 环境（Hermes Agent），可以直接在 NAS 上运行。

### Step 1: 上传项目到 NAS

```bash
# 在 NAS 上创建目录
ssh sh22@192.168.31.247 -p 1122
mkdir -p /volume1/docker/horizon
# 退出后从本地复制文件
```

### Step 2: 在 NAS 上配置 .env

```bash
# 编辑 .env 文件，填入 API Key
vi /volume1/docker/horizon/.env
```

### Step 3: 构建并运行

```bash
cd /volume1/docker/horizon
docker compose build
docker compose run --rm horizon --hours 24
```

### Step 4: 设置定时任务

```bash
# 使用 NAS 的 cron 或 Hermes Agent 的定时任务每天执行
docker compose run --rm horizon --hours 24
```

---

## 信息源说明

配置已包含以下信息源：

| 信息源 | 内容 | 是否需要 Key |
|--------|------|-------------|
| Hacker News | 热门技术帖子 | ❌ 免费 |
| Reddit | r/MachineLearning, r/LocalLLaMA 等 | ❌ 免费 |
| RSS | OpenAI 博客、Anthropic 博客、Simon Willison 等 | ❌ 免费 |
| RSS | 量子位、新智元（中文 AI 资讯） | ❌ 免费 |
| GitHub | 热门 AI 项目 Releases | 推荐 Token |
| OSSInsight | GitHub 开源趋势 | ❌ 免费 |
| Google News | AI 关键词新闻 | ❌ 免费 |

---

## 输出与投递

### GitHub Pages（免费网站）
开启后访问：`https://你的用户名.github.io/Horizon/`

### 飞书/钉钉 Webhook
配置 `HORIZON_WEBHOOK_URL` Secret 后，每天早上自动推送到群聊。

### 邮件订阅
如需邮件投递，在 `config.json` 中配置 SMTP/IMAP 凭据。
