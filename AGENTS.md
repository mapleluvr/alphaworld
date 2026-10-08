# Repository guidance

## 入口与材料

- 现行 skill 在 `skills/alphaworld/`；Pi 的包清单只暴露这一目录。
- `archive/template-skill/` 保存早期版本；`research/agent-wings-plan-cases/` 保存原字节稿件与运行审计。不要为匹配新结论或修复来源项目链接而改写这些快照。
- `research/lieflat-less-ai-tone/` 是固定 commit 的研究 submodule，不是本项目的执行 skill。未经相关任务要求，不修改其代码或移动版本。
- 文档使用简体中文，保留清晰的来源、条件和验证范围。构造案例不能改称实际实验；请求参数与实际运行参数分开记录。

## 修改与检查

- 修改现行 skill 时保留用户明确约定，让具体材料与使用情境决定取舍；不要把思想背景另写成每次必须执行的检查流程。
- 路径调整后检查现行 skill 和导航文档的相对链接。历史稿件内部的来源项目链接按其记录解释，不据此改写原字节。
- 用 Pi 原生 skill loader 检查可加载性。加载成功、Markdown 检查通过不等于行为效果得到验证。
- 测量探针复现：`git submodule update --init --recursive`，然后 `python -B research/probe_upstream_metrics.py`。它验证上游函数的特定行为，不评估文本自然度。
- 保留比较记录中的参数偏差和未验证项，不为通过检查放宽条件。
- 不提交凭证、完整会话转录或工具缓存。检查拟提交文件后再发布；仓库保持 private，除非用户明确要求改变可见性。
