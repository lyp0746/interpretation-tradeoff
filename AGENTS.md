# AGENTS.md — 本仓库工作约定与工具链（记忆）

> pi 会把本文件作为目录级上下文/记忆自动加载。改动后新会话生效。

## 工具链（本机实测，2026-10）

- **Git**：`D:\Git\cmd\git.exe`（不在 WSL 的 PATH 里，请用绝对路径 `/mnt/d/Git/cmd/git.exe`）
  - remote：`https://github.com/lyp0746/interpretation-tradeoff.git`，默认分支 `main`
  - 凭据已缓存，可直接 `push`；脚本里加 `GIT_TERMINAL_PROMPT=0` 防卡住
- **Python（构建/分析）**：`/mnt/d/0_Code/Iris Series/.venv/Scripts/python.exe`
  - 已装：numpy scipy pandas matplotlib bs4 lxml pypdf requests
  - `.env.build` 的 `PYTHON` 已指向该解释器；路径含空格，务必加引号
- **PDF 生成**：`build_book.py --pdf` 调无头 Chrome（`C:\Program Files\Google\Chrome\Application\chrome.exe`）

## 常用命令

```bash
PY="/mnt/d/0_Code/Iris Series/.venv/Scripts/python.exe"
GIT="/mnt/d/Git/cmd/git.exe"

"$PY" analysis/make_cover.py                  # 生成 assets/svg/cover.svg
"$PY" analysis/audit.py                        # 校对 → 刷新 校对清单.md
"$PY" analysis/preregistration_checkup.py      # 校验 append-only 登记账本
bash scripts/build.sh                          # 校对→印刷PDF→电子阅读PDF→EPUB→Markdown
bash scripts/validate.sh                       # 校对 + EPUB 结构校验
bash scripts/release.sh                        # 组装 release/
```

## 仓库约定

- **`source/*.html` 是唯一权威正文来源**；`output/`、`release/` 是派生产物（见 `.gitignore`）。
- 改正文后顺序：`analysis/audit.py` → `bash scripts/build.sh`。
- 结论标注：证据等级 **A/B/C** 与概念等级 **甲/乙/丙** 双重标注；C 级仅作方向判断。
- **可证伪登记簿**（附录 E 与 `docs/preregistration/`）为 **append-only**：只追加，绝不改写旧行。
- **正文与元数据不含版本号**；日期使用真实完成日期（`source/book.json` 单一来源）。
- 发布包只放读者面文件；不得含 xlsx/csv/json/py（`release.sh` 有守门检查）。
- 一个 release 对应一个 tag（可选 Model B：一个产物一个 tag）。

## 写作风格（重要）

见 skill `academic-book-pipeline` 的 `references/voice.md`。要点：

- **张力，不宿命**：约束是交易的条件，不是判决。禁止把“必然／不可避免／注定／死路”当作结论；
  但“给定某个选择，这笔账必然到来”属于交易句，可用。
- **分级在装置，不在每句**：证据/概念等级放表格与附录；正文一句一个精确限定即可。
- **反例进正文**；**地图只定性**；**负面结果**照实写出。
- 每个硬约束章必须带反向力量：这条限制**使什么成为可能**。
- 结构由论证决定：本书为 工具 → 深度诊断 → 快速诊断 → 元反思 → 边界。

## 本书特有

- **立场（重要）**：诊断不等于判决，但诊断包含判断；“只诊断不评判”是假二分。正文（前言.2、定义 1.1、阅读合约承诺一）把判断显式化，而非假装中立。
- **本书自己的核心（不依赖前书）**：诠释即置信度的分配（第 2.1 节）。
- **四个借来的约束（联系，而非依赖）**：容量、权衡（C-A-T）、时间 τ、区分；对应四本书，但本书结论不依赖其结论（第 2.7 节、附录 H）。
- **诠释诊断**（定义 1.1）：把置信度分配写出来，并作出可反驳的判断。
- **置信度四层**：L1 观察 / L2 推理 / L3 诠释 / L4 因果（定义 2.1）。
- **三档置信度**：高/中/低，序数不是概率（第 6.3 节）；三个陷阱见警告 6.1。
- **C-A-T 史学翻译**：C＝因果清晰度，A＝维度丰富度，T＝细节传递度（表 2.1）。
  **三顶点在史学中不对等**（警告 A.1）；加维候选（验证度/反例抵抗性）见附录 A.5，登记为 O4b。
- **被让出的顶点**：取三档中最低者（规则 A.1）。
- **三种风格**：清晰论（高 C 让 T）、平衡论（高 A 让 C）、细节论（高 T 让 C）。
- **五个应用（由深而广）**：应用一人物与事件（第 6 章）；应用二跨文明制度（第 7 章）；应用三既有争论（第 8—14 章）；应用四理论统摄（第 15 章）；应用五范式流变（第 16 章）。
- **坐标表是序数列**（附录 J.3）：高/中/低不可相加、不可当分数。
- **框架退化**（第 14.5 节）：快速诊断丢 τ，是三维；适用规模警告 14.1；第 14.3 为十场四维深化，14.4 为二十场三维范围预估。
- **自评数值**（第 19.2.1 节）：C≈70% / A≈60% / T≈50%，本书偏向建框架、不适合细节指导；两个“让出 T”的区别见警告 19.1。
- **地板/天花板/阁楼**（定义 19.1）：地板主张不依赖经验结论，是全书最硬的部分。
- **失败记录**（`source/appendix_j_failed.html`）：撤回“坐标可形式化”的强主张，正式内容不得删除；登记为 refuted。
- **开放问题**：O1—O28 + O4b（第 19.4 节、附录 L）；**可检验预测** F1—F5（第 19.3 节、附录 E）。
- **生死线**：O1（四层衰减）、O2（三选二反例）、O3（时间主张）、O4（翻译合法性）、O5（评分稳健）。
- **数据不对称**（第 13.5 节）：气候数据比社会数据更易得，会系统性影响哪派占上风。
- **跨文明警戒线**（警告 5.1）：对象无“因果清晰度”概念、诠释不以文本存在、不区分事实与意义时，框架可能失效。
- **六个深度案例**：第 8—13 章，每章末给出示意性坐标表（B／乙）。
- **应用四（第 15 章）**：统摄 = 定位，不是合并（定义 15.1、方法 15.1）。
- **术语总表**：`source/front_terms.html`（唯一术语总表，含英文原文）；正文不另设重复定义。
- **自评位置**（第 5.4 节与 19.2.1）：本书选 C+A、让出 T；可由 O8 自指一致性检查推翻。

## 版本脉络

见 `versions/CHANGELOG.md`（首版）。
