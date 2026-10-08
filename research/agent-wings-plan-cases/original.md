# Agent Wings 基础设施规划与仓库边界

## 1. 本轮范围

为 Agent Wings 建立三个独立项目：直播展示平台、sandboxing、Wings Ray。当前阶段是仓库初始化、参考实现调研和首版规划，不是服务上线或隔离验收。

确定项：OBS Studio 负责推流；sandboxing 参考 kappa-box 的 Windows 实现但必须独立验证；Wings Ray 基于 New API 建立公开 fork，定制需求单后续提供。赛事既定的 Pi 0.87.1、统一改进包和多目标评分不在本轮改动。

不在本轮执行：安装 OBS/WSL/Docker、创建发行版或虚拟机、修改网络/防火墙/代理、配置密钥、启动服务、付费模型测试。后续用户已授权在 `mapleluvr` 下托管和推送仓库：Wings Ray 为 public fork，其余仓库为 private。

## 2. 三个独立仓库

| 项目 | 本地仓库 | 规划入口 | 职责 |
| --- | --- | --- | --- |
| 直播展示平台 | `D:/Projects/HFUT/agentwings-platform` | [README](../../../agentwings-platform/README.md)、[首版规划](../../../agentwings-platform/docs/PLAN.md) | 可信数据接入、脱敏展示、OBS 专用画面与导播控制。 |
| sandboxing | `D:/Projects/HFUT/agentwings-sandbox` | [README](../../../agentwings-sandbox/README.md)、[首版规划](../../../agentwings-sandbox/docs/PLAN.md)、[Windows 调研](../../../agentwings-sandbox/docs/windows-survey.md) | 隔离实例、运行与回收、材料/产物通道、实际边界证据。 |
| Wings Ray | `D:/Projects/HFUT/wings-ray` | [fork 规划](../../../wings-ray/WINGS_RAY_PLAN.md) | New API fork 的模型接入与相关服务；具体定制等待需求单。 |

上述跨仓文件链接适用于三个仓库与 hfut-projects 并列的本地布局。远端均归 `mapleluvr`：[agentwings-platform](https://github.com/mapleluvr/agentwings-platform)、[agentwings-sandbox](https://github.com/mapleluvr/agentwings-sandbox)、[hfut-projects](https://github.com/mapleluvr/hfut-projects) 为 private；[wings-ray](https://github.com/mapleluvr/wings-ray) 是 `QuantumNous/new-api` 的 public fork。私有仓库链接需要访问权限。

platform 与 sandbox 分别初始化自己的 `.git`、`main` 分支、项目规则、忽略规则和规划文档。Router 保留 New API 完整历史，使用 `upstream` 远端与 `hfut/infra-planning` 工作分支，初始基点为 `bb28f2ccad3f6286a9dc4a0ad9e20f571f57533b`。该基点不是已经验收的生产版本。

hfut-projects 继续只承载赛事与跨项目规划，不作为三个实现的 monorepo，不加入 Git 子模块。各仓库独立审阅、提交与发布；跨仓集成用明确版本对应关系验证，不能假定原子更新。

## 3. 分层与权威来源

```text
可信评测 runner / 评分器（实现及部署归属待明确）
  ├─ 使用 sandbox 生命周期与文件通道 → 隔离环境中的参赛 Agent
  │                                      └─ 受限推理权限 → Wings Ray → 指定模型
  ├─ 收集实际产物、运行/费用记录 → 检查、模型裁判与人工复核
  └─ 发送可公开事实 → 展示平台可信接入层 → OBS 展示页 → OBS Studio → 直播服务
```

| 事实或操作 | 权威归属 | 不能替代它的东西 |
| --- | --- | --- |
| 实例生命周期、资源与网络边界 | sandbox runtime 和真实探针 | 页面状态、配置项或容器产品名。 |
| 模型请求与结算记录 | Router/上游记录及可信对账 | Agent 自报 token、前端估算或随意客户端标签。 |
| rollout 身份、输入版本、起止与样本归属 | 可信 runner 的正式记录 | OBS 时间轴、浏览器计时或导播手工选择。 |
| 正式结果与综合成绩 | 评分器及复核流程 | 暂定分、一次成功、演示回放。 |
| 直播内容与焦点选择 | 展示平台/导播 | 修改实际任务、预算、评分或重跑任务的权限。 |

当前没有把评测编排与评分实现悄悄塞进 sandbox、Router 或展示页，也没有新建第四个仓库。runner/评分器的实现归属是明确的待决项，在真实联调之前必须落实，不能以三个仓库已建立代替这项工作。

## 4. OBS 展示平台的首条路线

推荐专用只读 Web 展示页 + OBS Browser Source，后台导播控制与公开画面分离。先打通一队、一题、一次真实 rollout 的本地录制，再增加并列画面、评分板和授权直播间推流。

展示数据先在可信服务端做白名单、脱敏和发布控制；OBS 不加载队伍提供的任意页面，不共享后台凭据。不可信网页/文档产物要经独立预览或渲染边界。刷新页面、断开 OBS、切换画面均不得影响正式运行。

视频规格、音频、直播服务、延迟、部署拓扑和技术栈待明确。当前没有可运行 UI、录像或推流验收结果。

## 5. Windows sandbox 调研结论

本次只读检查 `D:/Projects/kappa/kappa-box` 的代码、ADR、profile 与历史证据。该仓库 HEAD 为 `d1688eb386fd800b2c7d28d1ccd1a2ff34e04cf3`，runtime 相关文件有未提交修改，本次未改动它们。

- 参考路径为 Windows 控制进程 → 专用 WSL2 → OpenShell → Docker Desktop → Linux sandbox。
- 2026-09-12 的历史摘要证明 `create → ready → exec(id) → stop → delete` 已跑通；profile 仍为 `unverified`，不等于完整隔离通过。
- host 组摘要记录 LSM 列表不可读及 Windows 可见 WSL 共享导致的失败。这是参考项目的验收门槛未通过，不能不加分析地等同为 guest 逃逸结论。
- 文件、网络、资源、凭据、会话与产物快照仍须在比赛目标主机重新验收；不复用 kappa-box 的实例、端口或密钥。
- Windows 宿主上的 Linux workload 不等于原生 Windows workload。明确要求原生 Office/桌面的题目需单独验证 Windows backend，不能静默换成 Linux 替代软件。

因此将 WSL2 路线列为优先验证候选，保留独立虚拟机及原生 Windows backend 的对照研究，不提前宣布选型已经通过。

## 6. Router 的准备边界

已完整克隆 `https://github.com/QuantumNous/new-api.git`，已建立本地开发基线和 `mapleluvr/wings-ray` 公开 fork；没有执行上游 Docker Compose、连接数据库或配置渠道。

收到需求单后，逐项判断“上游配置即可满足 / 接口适配 / 必须改代码”，再确定实现与验收。赛事限定模型和成本归属是集成约束，不自动扩展成 Router 所有用户的产品限制。

保留上游 AGPLv3、NOTICE、作者归属和原项目可见链接要求；正式部署前处理对应源码提供与发布义务。仓库归属与可见性已确定；部署版本仍待指定，公开代码不等于服务上线或运行验收。

## 7. 跨仓接口只先确定语义

在真实样本和 Router 需求单明确前，不冻结 API 路径、JSON schema 或共享 SDK。需要共同解决：

- 队伍、题目、rollout、改进包版本、实例与请求的可信关联，不能靠参赛者可随意修改的标签证明归属。
- 运行开始/结束、失败、取消、重试与后续费用结算的区分，避免展示端重复事件导致重复累计。
- 独立 rollout 的环境重置、缓存口径和版本固定，防止跨任务/跨队污染。
- 原始证据、可公开事件和最终分数分别保存与授权；隐藏评测数据、凭据和私人内容不流入直播。
- sandbox 的受限 Router 数据面与 Router/平台/OBS 管理面的网络分离；“能访问模型”不应同时授权访问管理接口。
- 展示端与控制端断线时，谁继续持有任务、谁决定终止，以及恢复后如何对账。

## 8. 推进顺序与验收门槛

| 阶段 | 重点 | 阶段出口 |
| --- | --- | --- |
| I0：规划与分仓 | 三个独立本地仓库、职责边界、参考调研、Router 上游基点。 | 文件与 Git 边界可检查；不等同于生产能力。 |
| I1：输入与选型 | Router 需求单、任务软件要求、目标主机、直播规格、runner 归属。 | 标出已确认/待定项，为下一步环境变更取得授权。 |
| I2：各自纵向切片 | 真实 sandbox 任务、Router 协议/对账、真实事件进入 OBS 本地录制。 | 每仓记录真实路径证据；mock 只用于开发测试，不当验收。 |
| I3：联合与对抗验证 | 跨队隔离、禁网推理、失败重试、撤销、回收、脱敏与直播断连。 | 各环节证据可关联；任何关键边界未知或失败则不准入正式赛。 |
| I4：演练与发布 | 固定版本、容量实测、独立审阅、完整赛事演练。 | 明确可用范围、回滚方式和故障责任，不用单次演示代替验收。 |

近期优先输入是任务是否要求原生 Windows、实际主机资源与已有服务、OBS 目标规格以及 Router 需求单。并发规模、费用上限、录制规格和接口形状均由这些输入及实测决定，不在规划中编造数值。

## 9. 与赛事规则的关系

- [赛事主草案](../releases/1015/Agent_Wings_PLAN_DRAFT.md)
- [改进包交付说明](../releases/1015/Agent_Wings_DELIVERY_DRAFT.md)
- [评分原则与细则](../releases/1015/Agent_Wings_SCORING_DRAFT.md)

校对阶段提供的环境和依赖说明，是 sandbox 适配与准入的输入；评分细则决定计量口径；平台忠实展示事实。基础设施规划不另设评分权重、rollout 次数或晋级规则。
