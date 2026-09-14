# 数据覆盖与使用（2026-09-14 快照）

- Open CS：公开 Git 仓库的 177 份 Markdown 文档，包括分档和文档内代表性 DP。独立 SeaTable 共享链接当前返回“共享链接不存在”，未取得该库的当日独立完整导出。
- CS Grad：公开 Git 仓库的 101 份 Markdown/MDX 文档；动态公开 API 分 10 页取得 1,968 条记录，剔除 1 条明确自动化测试，保留 1,967 条。共有 256 位申请者，202 位有多条结果（不等同于同申请季多条）。
- 原始 API 记录有 1,908 条带 SeaTable 来源标识，不应把两站历史 DP 视作两套独立样本。
- 两站共 247 条分档索引记录，包含跨类别重复项目，不代表 247 个独立北美 MSCS 项目。
- 本包保存文本知识库（上游原文存储在 corpus.json，以 sources.json 的 document_id 定位），不镜像站点图片、第三方评论、登录内容或网站所有功能。原始相对图片/站点链接可能不在包内，查阅 sources.json 中的原始来源。
- 原始动态 DP 及含完整背景的整理数据保留在研究者本地，GitHub 包不打包这些逐人记录。获取方式如下。公开文档中的作者自述案例随原文保留。

## 本地动态数据准备

需要 Python 3.9+、curl 和网络；从技能目录执行，输出目录自行选择：

```sh
python3 scripts/fetch_dp.py --output /path/to/local/dp-raw
python3 scripts/prepare_dp.py /path/to/local/dp-raw/rows.json --output /path/to/local/dp-prepared
python3 scripts/query_dp.py /path/to/local/dp-prepared/cases.json --school USC --category 985 --scale 4.0 --gpa-min 3.7
```

查询给出匹配者同申请季的全部已知结果，不能将输出中的 CS Grad tier 用作录取门槛。清洗版仅保留学术核心字段；软背景细节必要时在本地原始数据中通过 case_id 查证，不把其缺失视为没有科研或实习。尚未准备动态数据时用静态文档，明确覆盖限制。

脚本分页有上限、限速和重复 ID/总数检查；页面失败、访问受限或数据格式改变时停止并报告，不绕过访问限制。快照总数一致不保证抓取期间记录内容完全不变。更新时保存新目录，以保留旧版本。

## 当前验证范围

验证数据处理不把同人多校、跨季结果或不同 GPA 制度混合，验证源文件校验值和离线检索。尚未做独立模型行为评测、逐项目官方信息核验或录取概率校准。因此这是可用的证据检索与判断流程初版，不是已经证实预测准确的模型。

## 已发现的项目身份冲突

CS Grad 的 `docs/B/USC CS37.md` 文件路径标为 CS37，但正文标题是 `USC CS28`。保留原文，不自行修正；该文作为项目身份待核实证据，不自动与 Open CS CS28 或 CS37 对齐。索引命名、正文和官网冲突时必须先解释冲突再判断。

USC 两个项目身份已通过官网分别核验，详见 [官方核验](usc-official.md)；待核实的是 CS Grad 那一篇文档的归属。常规 MSCS 的 CS28 是历史别名，当前学分随入学年份变化。
