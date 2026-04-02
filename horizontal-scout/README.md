# horizontal-scout

围绕某个目标产品，研究“销售该产品的卖家类型”以及这些卖家通常还销售哪些其他商品。

这个 skill 的核心不是找联系人，也不是做相邻产品联想，而是做卖家目录横向分析。

## 适用场景

当用户想知道：

- 美国的轮椅客户还卖哪些产品
- 做这个产品的客户通常分成哪些类型
- 这些类型的头部企业通常还有哪些产品线
- 除了显然相关品类外，还有哪些非显然但高频出现的联卖品类

## 它解决什么问题

同一个产品会被不同经营模型的卖家销售。

例如同样销售轮椅的公司，可能是：

- 品牌商
- 批发商 / 分销商
- 专业零售商
- 电商卖家
- 方案型卖家
- 目录型供应商

这些卖家虽然都卖轮椅，但它们的目录扩张逻辑并不相同。

`horizontal-scout` 的目标是：

1. 判断常见卖家类型
2. 找出各类型的头部样本
3. 研究这些样本的目录结构
4. 总结各类型卖家在目标产品之外常卖什么
5. 区分显然联卖与非显然联卖

## 与其他 Skills 的区别

- `b2b-lead-scout`：找公司名单、渠道名单、联系人
- `hidden-buyer-scout`：找非传统买家
- `horizontal-scout`：研究卖家目录结构，回答“卖这个产品的公司通常还卖什么”

如果用户主要想要联系人或销售名单，应优先使用 `b2b-lead-scout`。

## 交互方式

这个 skill 需要兼容自然语言问法，例如：

- `搜索美国的轮椅客户还卖哪些产品`
- `帮我做一下轮椅客户的横向展开`
- `看看卖 IPC 的客户通常还有哪些产品线`
- `这些客户属于什么类型，还会卖什么`

Skill 应先自动提取：

- 目标产品
- 目标市场
- 用户是否更关注分类总结、代表公司、还是联卖品类

如果关键信息不足，只允许进行一轮补问，并尽量一次补齐高价值信息。

默认情况下：

- 输出中文总结
- 以分类总结为主
- 代表公司样本为辅
- 同时覆盖显然联卖与非显然联卖
- 优先查看网络搜索可见度高的头部企业

## 输出

默认支持三种输出：

- `.csv`：用于 Excel / 表格筛选
- `.md`：用于标准研究总结
- `.html`：用于可视化展示

建议文件名：

- `horizontal_[product_slug]_[market_slug]_[YYYY-MM-DD_HHMM].csv`
- `horizontal_[product_slug]_[market_slug]_[YYYY-MM-DD_HHMM].md`
- `horizontal_[product_slug]_[market_slug]_[YYYY-MM-DD_HHMM].html`

### CSV / Excel

CSV 主要用于结构化分析和后续筛选。

建议一行代表：

- 一个代表公司在某个卖家类型下的一条目录观察记录

建议字段包括：

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
- `evidence_url`
- `evidence_excerpt`
- `visibility_level`
- `confidence_score`
- `notes`

CSV 应使用 UTF-8 with BOM，便于 Excel 正确打开中文。

### Markdown

Markdown 以分类总结为主体，建议包含：

1. 搜索任务摘要
2. 总体结论
3. 卖家分类总览
4. 各类卖家分析
5. 代表公司样本表
6. 高价值非显然横向品类
7. 问题点与证据不足

Markdown 输出应与 CSV 共用核心字段，不要在 Markdown 中单独塞入 CSV 没有的关键信息。

### HTML

HTML 用于展示，页面结构应参考用户提供的可折叠分类卡片式页面。

推荐结构：

- 顶部标题区
- 统计卡片区
- 搜索框
- 分类筛选按钮
- 按卖家类型折叠展示
- 每家公司一个信息卡片
- 每类卖家单独附分类结论摘要

HTML 是展示层，不应隐藏低置信度项，也不能省略证据不足的问题点。

## 输出原则

- 不堆砌商品名
- 优先解释为什么这些商品会和目标产品一起出现
- 不把零散临时 SKU 误判为稳定目录
- 证据不足时要明确写出，不要回退成模糊结论
- 不隐藏问题点
