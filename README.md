# MSCS Admissions Skill

面向北美 CS 硕士申请的证据优先选校技能：GPA 优先，不迎合，不凭单个案例虚高或虚低定位。

第一版包含 Open CS 与 CS Grad 共 278 份文本资料、247 条双维度分档索引，以及动态 DP 抓取、清洗和同人同季结果检索工具。它不是经过校准的录取预测模型。

## 下载源码包

[下载 v0.1.0 完整源码与技能包](mscs-admissions-v0.1.0.zip)。解压后进入 `mscs-admissions/`，下文的本地路径都相对此目录。包内包含技能、278 份上游文档、USC/Cornell/JHU 官方核验、来源清单、脚本和测试；不包含逐人原始 API 数据。

## 安装与使用

将 `skills/mscs-admissions` 整个文件夹复制到你的技能目录（Codex 默认 `~/.codex/skills/`），然后使用 `$mscs-admissions`：

> 我的本科院校是……，专业……，原始 GPA……/……，排名……，申请 27 Fall 授课型 MSCS。请依据可比案例判断冲刺、匹配和相对稳妥项目，给出来源和不确定性。

离线搜索需要 Python 3.9+：

```sh
python3 skills/mscs-admissions/scripts/search.py 'USC'
```

动态 DP 需另行下载到本地；参见 覆盖与准备流程（源码包内 `skills/mscs-admissions/references/coverage.md`）。原始逐人 API 记录不包含在此仓库。静态资料可直接检索，无需先下载 DP。

## 如何避免错误判断

- Open CS 的录取门槛与 CS Grad 的项目价值分别展示，不合并字母档次。
- 在本科背景、专业、原始评分制及申请季语境中优先评估 GPA；不编固定权重和 GPA→档次公式。
- 高背景申请者的低档录取不能作为其定位上限；最好录取也不自动等于稳定匹配。
- 同一个人的多校结果放在同一申请季组合里看，兼看拒绝案例和缺失结果。
- 科研、项目和实习只在有项目证据时影响判断，研究型项目单独评估。
- 不因用户自信而提高定位，不因用户自卑而降低定位。

## 官网检索与文书思路（不代写）

可以请求技能检索项目官网、申请题目、课程实践及潜在导师的研究方向，把这些证据与你已有的经历对应，提供角度、素材问题和结构建议。它区分明确要求、培养特征与推导建议，不为贴合项目而捏造经历，不把研究相关等同于导师愿意接收。

例如：Cornell MPS IS 可探索团队实践、创业或产品经历中的判断与执行；JHU MSE CS 可探索真实科研与教师方向的契合。两者都以当前官方要求为准，参见 核验示例（源码包内 `skills/mscs-admissions/references/program-fit-examples.md`）。实时核验需要运行环境提供网页搜索/浏览能力；离线时仅使用带日期的资料并说明限制。

## 数据和验证

2026-09-14 抓取：1,968 条动态记录，排除 1 条明确测试数据后 1,967 条，来自 256 位申请者。Open CS 独立 SeaTable 链接已失效，其静态代表性 DP 仍保存在原文。详见 来源版本（源码包内 `skills/mscs-admissions/references/sources.json`）、评估方法（源码包内 `skills/mscs-admissions/references/methodology.md`） 和 数据质量摘要（源码包内 `skills/mscs-admissions/references/dp-quality.json`）。

当前验证是工具与数据不变量验证；尚未完成独立 LLM 行为评测或真实申请结果回测。事实性项目要求应在使用时核验当季官网。

## 致谢与许可

文本资料来自 [Open CS Application](https://opencs.app/)（OpenCSApp contributors）和 [CS Grad](https://csgrad.com/)（CS Grad contributors）。感谢其公开资料和数据贡献。本项目不是两站官方产品。

本仓库采用 [CC BY-NC-SA 4.0](LICENSE)。复用内容保留原作者权利和署名，新增索引、技能说明、检索与清洗工具为本项目改编/新增；使用须遵守署名、非商业和相同方式共享要求。每篇来源、提交版本和校验值见 sources.json。第三方外链内容不因此获得再许可。

已知源数据冲突：CS Grad 的 `USC CS37.md` 正文标题为 CS28，已标记待核实，不自动合并。运行工具测试：`python3 -m unittest discover -s tests`。

USC CS28（常规 MSCS 的历史别名）与 CS37（Scientists and Engineers）已按官网明确区分，常规 MSCS 自 Fall 2024 起为 32 学分。详见 官方核验（源码包内 `skills/mscs-admissions/references/usc-official.md`）。
