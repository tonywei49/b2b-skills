---
name: tavily-search
description: >
  Tavily 多功能搜索技能，支持四种模式：
  - search: 网页搜索（基础/深度/快速）
  - research: 深度研究（自动多次搜索+结构化报告）
  - extract: 指定URL内容提取
  - crawl: 站点图爬取
  当用户需要联网搜索、深度调研、提取网页内容时使用此技能。
  比 autoglm-websearch 提供更多控制选项和高级功能。

# Installation / 依赖安装

## 安装后必读

首次使用本 skill 前，**必须运行依赖检查脚本**，确保 Python 3 已安装：

```powershell
# 以管理员身份运行 PowerShell，然后执行：
& "C:\Users\Administrator\.openclaw-autoclaw\skills\tavily-search\check_install_deps.ps1"
```

该脚本会自动：
1. 检测系统是否有 Python 3
2. 若未安装，通过 winget 自动安装 Python 3.11（LTS 版本）
3. 提示手动安装方式（winget 不可用时）

> **注意**：必须以管理员身份运行 PowerShell，否则 winget 安装会失败。

## 系统要求

- Python 3.x（最低支持 3.7）
- urllib（Python 内置，无需单独安装）
- Windows 10/11（使用 winget 安装）
- macOS/Linux：使用 `python3 --version` 检测，手动安装 https://python.org

---

# Tavily Search Skill

支持 search / research / extract / crawl 四种模式。

## 命令行用法

```bash
python tavily.py search "关键词" [--depth basic|advanced|fast|ultra-fast] [--max-results 5] [--topic general|news]
python tavily.py research "研究主题" [--model pro|mini|auto]
python tavily.py extract "URL"
python tavily.py crawl "URL" [--max-depth 2] [--max-urls 10]
```

## 各模式说明

### search — 网页搜索
最常用的搜索模式，等同于 Tavily MCP 工具的核心功能。
- `depth`: advanced(2积分/最精准) / basic(1积分/均衡) / fast / ultra-fast
- `max_results`: 0-20，默认5
- `topic`: general(通用) / news(实时新闻)

### research — 深度研究
自动执行多次搜索、分析来源、生成结构化研究报告。
- `model`: pro(全面深入) / mini(精准高效) / auto(自动选择)
- 会自动探索多个角度，返回完整报告

### extract — 内容提取
从指定URL直接提取网页全文内容，不依赖搜索引擎。
- 适合已知具体网页、需要精准内容时使用

### crawl — 站点爬取
从给定URL出发，自动发现相关页面并抓取内容。
- 先用 /map 发现站点结构，再用 /crawl 批量抓取
- `max_depth`: 爬取深度
- `max_urls`: 最大URL数量

## 积分消耗
- basic/fast/ultra-fast: 1 API Credit
- advanced: 2 API Credits  
- research: 消耗更多（取决于研究深度）

## 返回结果格式
结果以格式化 JSON 输出，包含：
- search: url、title、content(content/snippet)、score
- research: 完整研究报告（多个章节）
- extract: 各URL的原始内容块
- crawl: 发现的所有URL及内容

## 适用场景
- search: 日常快速搜索
- research: 深度报告、市场调研、竞品分析
- extract: 已知文章/文档，需要精确内容
- crawl: 网站全面抓取，信息收集
