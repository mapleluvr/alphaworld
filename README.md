# Alphaworld

面向写作、文档编写与软件工程的 skill。通过具体工作形成可阅读、可使用、可检验的成果，让问题理解与成果结构随材料和反馈发展。

当前版本是一项持续修订的设计，不宣称已经证明对所有模型或任务有效。

## 使用

现行入口是 [skills/alphaworld/SKILL.md](skills/alphaworld/SKILL.md)。三个附件按任务选读：

- [领域示例](skills/alphaworld/references/examples.md)：写作、文档与 SWE 中的工作选择，区分构造案例与实际变更。
- [文档工作情境](skills/alphaworld/references/document-work-cases.md)：怎样澄清读者的问题，以及建立和复用编辑偏好。
- [思想来路与具体化](skills/alphaworld/references/philosophy-and-design.md)：辩证法、德勒兹与阿尔都塞相关讨论怎样进入具体设计。

这是私有仓库，需要具备相应的 GitHub 访问权限。使用 Pi 时，可在准备放置仓库的父目录运行：

```powershell
gh repo clone mapleluvr/alphaworld
pi install ./alphaworld
```

安装后可通过 `/skill:alphaworld` 显式调用。`package.json` 只暴露 `skills/alphaworld/`，不会将归档或上游研究 skill 当作运行入口。普通使用不需要初始化研究 submodule。

也可将完整的 `skills/alphaworld/` 目录复制到支持 Agent Skills 的工具中；请同时保留其 `references/`。

## SWE 专门化包

[Alphaworld-SWE](https://github.com/mapleluvr/alphaworld-swe) 面向软件工程、工程文档与技术协作，使用自己的清单和自包含附件，已迁出为独立公开仓库，在本仓库之外维护：

```powershell
gh repo clone mapleluvr/alphaworld-swe
pi install ./alphaworld-swe
```

通过 `/skill:alphaworld-swe` 显式调用。本仓库不再包含该包；安装本仓库不会加载 SWE skill，运行它也不依赖这里的研究材料。

根目录的 `SKILL-Candidate.md` 与 `document-work-cases-no7.md` 保留为讨论材料，不是继续维护的运行入口。取舍及验证范围见[独立包评议记录](research/alphaworld-swe-package-review.md)。

## 仓库布局

```text
skills/alphaworld/          通用版 skill 与按需附件
archive/template-skill/    早期主文和两个附件的原字节归档
research/                 设计记录、文本对照、测量探针
  agent-wings-plan-cases/  原稿、改写稿和运行审计
  lieflat-less-ai-tone/    固定版本的上游 Git submodule
```

[研究索引](research/README.md)说明各组材料的用途和证据范围。[早期版本说明](archive/template-skill/README.md)记录归档来路；它不是另一个现行入口。

## 复现测量探针

在仓库根目录运行，需要 Git 和 Python 3：

```powershell
git submodule update --init --recursive
python -B research/probe_upstream_metrics.py
```

上游固定在 `27d29232f10124db904ca9c0536d0b67cb3b2833`。探针直接调用该版本未修改的测量函数，使用合成输入检查三项定义不一致，并重写 `research/upstream-metric-probes.json`；它不复现未公开语料，也不测量文风改写收益。

## 证据状态

现有计划改写能用于观察编辑选择，不能单独证明 skill 的因果收益。独立运行采用较早的 skill 快照；其中 Astra 请求 `xhigh`、实际运行 `max` 的差异保留在审计中。通用版的六个文档情境是构造案例，其反馈过程不冒充已发生的实验。迁出的 SWE skill 追加的第七情境未附运行溯源，只按其所述条件分析，不认定为已复现的实际实验。

历史改写稿按原字节保存，内部相对链接仍以来源项目布局为基准；审计中的本地绝对路径用于追溯原运行，不是安装依赖。完整会话日志、凭证和本地缓存不随仓库发布。
