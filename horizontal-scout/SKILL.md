---
name: horizontal-scout
description: 围绕目标产品研究卖家类型、目录结构与横向联卖品类，输出中文分类总结、CSV/Markdown/HTML 结果。
homepage: https://github.com/tonywei49/b2b-skills
user-invocable: true
metadata: {"openclaw":{"emoji":"🧭","homepage":"https://github.com/tonywei49/b2b-skills","always":true}}
---

# Horizontal Scout

## Purpose

使用这个 skill 来研究：

- 某个产品在目标市场有哪些典型卖家类型
- 这些卖家类型的头部企业通常还销售哪些商品
- 哪些联卖品类是显然扩展
- 哪些联卖品类是非显然但高频出现的扩展

这个 skill 的核心是卖家目录横向分析，不是联系人挖掘，也不是简单的产品相邻联想。

---

## When To Use This Skill

当用户提出类似需求时使用：

- 搜索美国的轮椅客户还卖哪些产品
- 帮我做一下这个产品客户的横向展开
- 看看卖 IPC 的公司通常还有什么产品线
- 这些客户属于什么类型
- 销售这个产品的头部公司通常还卖什么
- 按客户类型总结这个产品的联卖品类

当用户主要想知道“卖这个产品的商家通常还卖什么”时，优先使用本 skill。

不要在以下情况优先使用本 skill：

- 用户要联系人、邮箱、职位、开发名单
- 用户只要传统分销商/进口商名单
- 用户要找非传统终端买家

这些情况分别更适合：

- `b2b-lead-scout`
- `hidden-buyer-scout`

---

## Core Boundary

本 skill 研究的是：

- 卖家分型
- 头部样本公司
- 卖家目录结构
- 联卖品类归纳
- 非显然横向品类

本 skill 不负责：

- 大规模联系人补全
- 邮箱挖掘
- 单纯收集公司名单
- 从目标产品直接机械扩展到近邻品类

如果研究过程中发现用户真正要的是名单或联系人，要明确指出边界，并建议切换 skill，不要悄悄把任务改成 lead 搜索。

---

## Natural-Language Input Recognition

用户不会总是使用标准化输入。

本 skill 必须能够从自然表达中识别任务意图，例如：

- `搜索美国的轮椅客户还卖哪些产品`
- `帮我分析卖这个产品的客户结构`
- `看看卖病床的商家通常还有哪些目录`
- `做一下轮椅客户的 horizontal`

从这类输入中，优先自动提取：

- `target_product`
- `market`
- 用户是否要分类总结
- 用户是否要代表公司样本
- 用户是否特别强调非显然联卖品类

不要因为用户没有使用标准模板，就要求重说一遍。

---

## Interaction Rules

### Default Interaction Model

优先直接理解并执行。

如果关键信息不足，只允许进行一轮补问，并尽量一次补齐最影响结果质量的条件。

默认只做：

1. 自动识别已有输入
2. 最多一轮补问
3. 继续执行研究

不要连续多轮追问细节。

### What To Ask In The Single Follow-Up

如果需要补问，优先询问以下高价值信息：

- 目标市场是否准确
- 产品是否需要限定细分，例如手动轮椅、电动轮椅、医用轮椅
- 是否只看某类卖家
- 是否只看头部高可见度卖家
- 是否重点寻找非显然联卖品类

优先使用一条整合式补问，把多项关键条件一次补齐。

例如：

`我会按卖家类型研究美国销售轮椅的客户目录。你这次更想看头部样本公司，还是按客户类型归纳的联卖品类？如果轮椅有细分范围，也可以一起说明。`

### Default Assumptions

如果用户没有补充，则默认：

- 输出语言为中文
- 以分类总结为主
- 代表公司样本为辅
- 同时覆盖显然与非显然联卖品类
- 优先研究网络可见度高的头部卖家
- 只使用公开可见目录和公开证据

---

## Required Inputs

最低需要：

- `target_product`
- `market`

可选输入：

- `product_scope`
- `focus_seller_types`
- `top_players_only`
- `need_company_examples`
- `need_non_obvious_cross_sell`
- `public_catalog_only`
- `output_language`

如果缺失可选输入，应按默认值继续执行，而不是停住。

---

## Seller-Type Framework

默认先按以下六类分析：

- 品牌商（Brand Owner）
- 批发商 / 分销商（Distributor / Wholesaler）
- 专业零售商（Specialty Retailer）
- 电商卖家（Ecommerce Seller）
- 方案型卖家（Solution Provider）
- 目录型供应商（Catalog Supplier）

如行业明显特殊，可补充行业专属类型，但必须说明为什么新增该类型。

不要为了凑分类硬拆。

---

## Research Logic

不要从“这个产品旁边还有什么商品”出发。

要从下面四个问题出发：

1. 这种卖家靠什么经营模型赚钱
2. 它面对的是谁
3. 它的目录是围绕什么逻辑扩张
4. 目标产品在其目录里扮演什么角色

每次总结联卖品类时，应尽量归因到以下一种或多种逻辑：

- `same_customer`
- `same_scenario`
- `same_channel`
- `same_business_model`

如果证据不足，不能硬归因，必须直接标明不确定。

---

## Research Workflow

1. 解析用户输入并提取目标产品与市场
2. 若关键信息不足，进行最多一轮补问
3. 判断该产品在目标市场的主要卖家类型
4. 为每类卖家寻找网络可见度较高的代表样本
5. 研究这些样本的官网目录、分类页、品牌页、解决方案页或产品页
6. 识别目标产品之外的稳定联卖品类
7. 区分显然联卖品类与非显然联卖品类
8. 总结每类卖家的经营逻辑与目录结构
9. 输出 CSV、Markdown，以及在需要时输出 HTML

---

## Evidence Rules

优先使用：

- 官网产品页
- 官网分类页
- 官网品牌页
- 官网解决方案页
- 官网关于我们或业务介绍页

必要时可使用：

- 可信目录页
- 企业介绍页
- 平台店铺页

但要明确区分：

- `official_website`
- `source_url`
- `evidence_url`

如果联卖品类只是搜索结果暗示、没有目录证据，不要把它写成确定结论。

---

## Search Priority

本 skill 不要求必须使用 Tavily，但应遵循固定的检索优先级。

优先级如下：

1. 已安装并配置的 `tavily-search`
2. 浏览器 Google 搜索
3. DuckDuckGo 或其他通用搜索兜底

规则：

- Tavily 是可选加速器，不是硬依赖
- 如果没有 Tavily，不要中断任务，应继续用浏览器搜索完成研究
- 搜索工具只用于发现候选页面与线索，最终判断应回到公开目录、官网分类页、产品页或解决方案页
- 不能只根据搜索摘要判断联卖品类，必须尽量回到证据页验证

---

## Output Requirements

默认支持三种输出：

1. `.csv`
2. `.md`
3. `.html`

如果用户未指定格式，至少输出：

- `.csv`
- `.md`

如果用户要求展示版、网页报告、可筛选页面，或明确要求 HTML，则额外输出 `.html`。

### File Naming

- `horizontal_[product_slug]_[market_slug]_[YYYY-MM-DD_HHMM].csv`
- `horizontal_[product_slug]_[market_slug]_[YYYY-MM-DD_HHMM].md`
- `horizontal_[product_slug]_[market_slug]_[YYYY-MM-DD_HHMM].html`

---

## CSV / Excel Output

CSV 用于结构化分析和筛选。

一行应表示：

- 一个代表公司在某个卖家类型下的一条目录观察记录

固定字段建议为：

- `target_product`
- `market`
- `seller_type`
- `seller_type_cn`
- `company_name`
- `official_website`
- `company_region`
- `company_role_summary`
- `target_product_match`
- `other_products`
- `obvious_cross_sell`
- `non_obvious_cross_sell`
- `assortment_logic`
- `catalog_feature`
- `source_url`
- `evidence_url`
- `evidence_excerpt`
- `visibility_level`
- `confidence_score`
- `notes`

规则：

- CSV 使用 UTF-8 with BOM
- 列顺序必须固定
- 不要因为某列为空就省略字段
- `other_products` 用于保留完整联卖品类串
- `obvious_cross_sell` 与 `non_obvious_cross_sell` 必须分开
- `confidence_score` 必须是确定性的离散评分或一致尺度

如需照顾 Excel 展示，可额外输出 `.xlsx`，但 `.csv` 仍应保留。

---

## Markdown Output

Markdown 以中文分类总结为主，代表公司样本为辅。

建议固定包含以下部分：

1. 搜索任务摘要
2. 总体结论
3. 卖家分类总览
4. 各类卖家分析
5. 代表公司样本表
6. 高价值非显然横向品类
7. 问题点与证据不足

### Markdown Summary Rules

`搜索任务摘要` 至少包含：

- 市场
- 产品
- 产品范围
- 是否限定卖家类型
- 是否优先头部企业
- 输出语言
- 搜索状态

`卖家分类总览` 建议使用总表：

| 卖家类型 | 代表公司数 | 常见联卖方向 | 非显然联卖强度 | 备注 |
|---|---:|---|---|---|

`代表公司样本表` 建议使用固定字段：

| company_name | seller_type | website | target_product_match | other_products | non_obvious_cross_sell | assortment_logic | evidence_url | confidence_score | notes |
|---|---|---|---|---|---|---|---|---:|---|

Markdown 应与 CSV 共用核心字段，不允许把 CSV 中没有的重要判断只写在 Markdown 里。

---

## HTML Output

如果输出 HTML，页面结构应参考用户提供的卡片式分类页面。

推荐页面结构：

- 顶部标题区
- 统计卡片区
- 搜索框
- 分类筛选按钮
- 按卖家类型折叠展示
- 每家公司一个信息卡片
- 每类卖家单独附分类结论摘要

### Recommended HTML Sections

#### Header

显示：

- 标题，例如：`轮椅在美国市场的卖家目录横向分析`
- 日期
- 样本公司数
- 卖家类型数

#### Stats

建议展示：

- 卖家类型数
- 代表公司数
- 显然联卖品类数
- 非显然联卖品类数

#### Filters

建议至少支持：

- 全部
- 品牌商
- 批发商 / 分销商
- 专业零售商
- 电商卖家
- 方案型卖家
- 目录型供应商
- Top 高置信度

#### Category Blocks

每个卖家类型单独一块，可折叠。

分类标题区应显示：

- 分类名称
- 该类代表公司数
- 简短分类说明

#### Company Cards

每张卡片应展示：

- 公司名
- 置信分
- 卖家类型标签
- 地区
- 官网
- 目标产品匹配说明
- 其他主营商品
- 非显然联卖品类
- 目录逻辑说明
- 证据链接

#### Category Conclusion

每个分类块下都应附一段分类结论摘要，至少回答：

- 这一类卖家的目录扩张主要围绕什么逻辑
- 最常见的联卖方向
- 最值得关注的非显然方向

HTML 是展示层，不应隐藏低置信度项目，也不能省略问题点与证据不足。

---

## Quality Rules

- 不要只输出显然近邻品类
- 优先解释“为什么这些商品会一起卖”
- 不要把临时零散 SKU 当成稳定目录
- 对证据薄弱项要明确标注
- 不要为了页面好看而删除弱证据项
- 不要回退成模糊话术掩盖问题

---

## Default Output Direction

当用户未特别指定时，默认：

- 中文输出
- 分类总结为主
- 代表公司样本为辅
- 公开目录证据优先
- 同时包含显然和非显然联卖品类

---

## Final Reminder

这个 skill 的价值不在于多列几十家公司。

真正的价值在于：

- 识别卖家经营模型
- 解释目录为什么这样扩张
- 归纳哪些横向品类值得关注
- 把问题点直接写出来，而不是隐藏掉
