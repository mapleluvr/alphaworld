# Repository guidance

## 入口与材料

- 通用版 skill 在 `skills/alphaworld/`；根目录 Pi 包清单仍只暴露这一目录。
- SWE 专门化包已迁出为独立公开仓库 [mapleluvr/alphaworld-swe](https://github.com/mapleluvr/alphaworld-swe)，在本仓库之外维护，本仓库不再包含 `packages/`。根目录候选用于追溯讨论，不是运行入口；SWE 主文与附件的后续修改在新仓库进行。
- `archive/template-skill/` 保存早期版本；`research/agent-wings-plan-cases/` 保存原字节稿件与运行审计。不要为匹配新结论或修复来源项目链接而改写这些快照。
- `research/lieflat-less-ai-tone/` 是固定 commit 的研究 submodule，不是本项目的执行 skill。未经相关任务要求，不修改其代码或移动版本。
- 文档使用简体中文，保留清晰的来源、条件和验证范围。构造案例不能改称实际实验；请求参数与实际运行参数分开记录。

## 修改与检查

- 修改现行 skill 时保留用户明确约定，让具体材料与使用情境决定取舍；不要把思想背景另写成每次必须执行的检查流程。
- SWE 专门化不重写 Alphaworld 的思想来路；思想附件沿用原文，仅注明必要的包内差异。原有写作原则与表达取向同样适用于 SWE 内容和 skill 自身的创作与修订。该取向在新仓库继续适用。
- 路径调整后检查现行 skill 和导航文档的相对链接。历史稿件内部的来源项目链接按其记录解释，不据此改写原字节。
- 用 Pi 原生 skill loader 检查可加载性。加载成功、Markdown 检查通过不等于行为效果得到验证。
- 测量探针复现：`git submodule update --init --recursive`，然后 `python -B research/probe_upstream_metrics.py`。它验证上游函数的特定行为，不评估文本自然度。
- 保留比较记录中的参数偏差和未验证项，不为通过检查放宽条件。
- 不提交凭证、完整会话转录或工具缓存。检查拟提交文件后再发布；仓库保持 private，除非用户明确要求改变可见性。
