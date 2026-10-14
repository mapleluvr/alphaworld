# 研究与设计记录

本目录保存设计来路、实际改写及有限测量，不是 skill 的常驻输入。通用版见 [Alphaworld](../skills/alphaworld/SKILL.md)；SWE 专门化版本已迁出为独立公开仓库 [Alphaworld-SWE](https://github.com/mapleluvr/alphaworld-swe)，不在本目录。

## 从哪里读

| 材料 | 用途 |
| --- | --- |
| [文档工作变更记录](alphaworld-document-work-change.md) | 读者问题、澄清与偏好指导怎样进入主文件 |
| [SWE 候选评议](alphaworld-swe-candidate-review.md) | 候选首轮修订及当时验证范围 |
| [SWE 独立包评议](alphaworld-swe-package-review.md) | 留存判据、案例合并、独立封装及思想原文恢复的取舍和检查 |
| [Agent Wings 改写记录](agent-wings-plan-cases/README.md) | 原稿、主会话及独立子代理成稿，输入隔离、参数偏差和比较范围 |
| [自然表达研究评阅](lieflat-less-ai-tone-review.md) | 对上游规则和测量实现的检查，以及可借鉴的判断 |
| [测量探针](probe_upstream_metrics.py) / [结果](upstream-metric-probes.json) | 直接调用未修改的上游函数，复现三项测量定义不一致 |

历史记录保留当时的状态与结论，不因现行 skill 后续改变而被改写成成功叙事。`agent-wings-plan-cases/` 的稿件和 JSON 保留原字节；稿件内部相对链接仍按原 HFUT 项目布局解释，JSON 中本机 session 路径只作来源定位。

## 上游材料

`lieflat-less-ai-tone/` 是 [larashero3-dotcom/lieflat-less-ai-tone](https://github.com/larashero3-dotcom/lieflat-less-ai-tone) 的 Git submodule，固定在 `27d29232f10124db904ca9c0536d0b67cb3b2833`，保留上游许可证和原有文件。

```powershell
git submodule update --init --recursive
python -B research/probe_upstream_metrics.py
```

该探针只需要 Git、Python 标准库和固定版本的上游文件。合成样本不代表公开或私有的人机语料，原始研究统计与改写效果仍应按评阅记录中的范围理解。

完整原始会话和独立运行工作目录未纳入本仓库；现有文件不足以在其他机器重建整场模型实验。后续复验应另外固定输入、模型与实际参数，不能把当前 skill 当作旧实验所用版本。
