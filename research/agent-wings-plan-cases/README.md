# Agent Wings 计划改写记录

此目录保存 Alphaworld 文档示例的来源与独立改写记录，不作为 skill 常驻材料。

## 父会话的实际改写

- [原文快照](original.md)：来自 `D:/Projects/HFUT/hfut-projects/docs/plans/agent-wings-infrastructure.md`。
- [父会话改写快照](parent-rewrite.md)：来自同目录的 `agent-wings-infrastructure.alphaworld.md`。
- 以上是原字节快照，内部相对链接仍以 HFUT 原项目的目录布局为基准。

| 文件 | UTF-8 文件大小 | SHA-256 |
| --- | ---: | --- |
| original.md | 9,438 bytes | `2A2E5EB09697CA01399BB0826BE65947A018476E73C5A5E0FF0C4E717E9115CF` |
| parent-rewrite.md | 12,885 bytes | `5526076DC0CE7130C2E17E4CBCE9458EE3268C28264839F3F8C1AA8207A6B8C8` |

改写时同时参考了三仓规划、Windows 调研和赛事主草案、交付说明、评分细则。它偏向帮助后续执行者选择下一步；原文还承担仓库边界说明的用途。此次不是控制其他因素的 skill 效果实验。

附件选用的局部变化是等待范围：原文把需求单、环境与直播等输入放在同一阶段，新文补充哪些准备可以独立推进、哪些联调仍需等待。原文未禁止并行工作，所以不能将它记成已经证实的阻塞故障。权限及实际操作范围不因改写扩大。

其他可见变化包括证据与后续用途的配对，以及不同发现对应的修改范围。原文已经要求真实验证、区分运行结束与后续结算、推迟冻结接口；不能将这些已有判断称为本次实验发现。

新版文件体积增加约 36.5%。这是字节计量，不是 token 或阅读耗时测量。前后稿已经形成，尚无读者操作实验或后续执行记录证明收益。skill 附件只收录局部变更及这一证据限定，不要求执行者读取两份完整快照。

## 独立子代理改写

本次用户要求一个子代理不接触父会话改写成品，使用 Alphaworld 独立改写同一原文；父会话同时调整附件。

运行信息：

- Run ID：`076e7a27-9126-41d3-8cec-5f827f94fe79`。
- Mission ID：`7ed49f62-4b03-4ddf-ade3-cd3a568752d5`。
- Agent：`delegate`；运行状态已确认解析为 `Mapleluv/grok-4.7`、`xhigh`。
- Context：显式 `fresh`，无父会话 transcript 分叉。
- 工作目录：`D:/Pi/research/alphaworld-blind-runs/agent-wings-01/workspace`；独立文档快照目录，不是 Git worktree。
- 输入清单：`D:/Pi/research/alphaworld-blind-runs/agent-wings-01/input-manifest.json`，逐文件记录来源、快照路径及 SHA-256。
- 绑定输出：工作目录下 `hfut-projects/docs/plans/agent-wings-infrastructure.independent.md`。

快照仅包含原计划、七份原有参考文档及改动前的 Alphaworld 两文件包，共十个文件。原计划 SHA 与上述原文一致；主 skill SHA 为 `38B2C0F076EA4207BDBC106B56848E8F5C487D0F8859F3293BD19677DF103D0B`，旧附件 SHA 为 `0BEF8D8633AE40C527AD5044EBFE3D1858C3382289CF77E7D1AFDFA200123335`。

委派只规定使用该 skill、原文目标、输入和写入边界；未提供父会话的计划、分析、期望改写结构或本次新增真实案例。显式关闭默认技能注入，通过任务要求先读取快照中的主 skill，其旧附件按需使用。

父会话修改的是原项目中的附件，不同步到子代理快照。父会话主 skill 本次未改；更新后附件 SHA 为 `1F5BEA8E9D8BEFE97543664FDA2613E85BA42051F9A7E4C3FE8EB65A6C718A38`。

隔离方式是 fresh context、独立输入快照和明确读取边界，不是操作系统级文件访问沙箱。运行结束后，应以实际 transcript 核对读取与执行路径，不能只凭子代理自述断言没有污染。

附件调整后，Pi 原生 skill loader 无诊断；三个构造案例和一个实际变更案例的来源标记已检查，引文与父会话快照一致，主 skill 和第一轮十个输入快照的哈希未变。检查脚本首次使用未锚定匹配，将引言中的“来源：构造案例”也计入；改为只匹配独立来源行后通过，没有为了检查结果改写附件。

## 用户追加的指定模型重试

用户指定 `AnyRouter/gpt-6-astra` 和 `Mapleluv/gpt-6.1-sol-pro`，均使用 `xhigh`。

AnyRouter 轮：

- Workflow ID：`6699b78e-1e65-4754-88ce-35612031ef61`。
- Mission ID：`fb485a9b-9608-4a5d-9fae-677b3552a114`。
- 子任务 key：`anyrouter-astra`，`delegate`，显式请求 `AnyRouter/gpt-6-astra:xhigh`，fresh context；最终审计发现实际 thinking 为 `max`，见下方参数偏差。
- 工作目录：`D:/Pi/research/alphaworld-blind-runs/agent-wings-02/workspace`。
- 输入按第一轮 manifest 逐文件复制与哈希核对，共十个；没有复制第一轮输出。
- 任务文本与第一轮相同；唯一输出仍为各自工作目录下 `hfut-projects/docs/plans/agent-wings-infrastructure.independent.md`。

Sol Pro 轮：

- 最初配置缺少精确的 `Mapleluv/gpt-6.1-sol-pro`；未用相近 ID 替代。用户补充定义后，按精确名称确认唯一匹配及 `reasoning: true`。
- Run ID：`1af6f907-acbf-4744-9b4e-9294382e4b8f`。
- Mission ID：`018087c7-5d81-4e67-9923-62f37ad88b96`。
- Agent：`delegate`，`fresh`；运行状态已确认 `gpt-6.1-sol-pro`、`xhigh`。
- 工作目录：`D:/Pi/research/alphaworld-blind-runs/agent-wings-03/workspace`。
- 仅复制第一轮 manifest 的十个输入并核对哈希，不复制任何运行输出；已完成。实际 session 记录精确模型 `Mapleluv/gpt-6.1-sol-pro` 与 `xhigh`，不是相近名称替代。

## 三份成品与机械核查

文档保持子代理原样，不根据父会话偏好润色。这里的“完成”只表示文档已生成，参数符合性与文档效用分别判断。

| 样本 | 实际 thinking | 保存的原样输出 | 文件大小 | 相对原文 | 实际工具调用 |
| --- | --- | --- | ---: | ---: | --- |
| Grok 4.7 | xhigh | [grok-rewrite.md](grok-rewrite.md) | 29,074 bytes | 3.08 倍 | read 14、ls 10、find 1、write 1、edit 2。 |
| AnyRouter Astra | **max，未满足指定 xhigh** | [astra-rewrite.md](astra-rewrite.md) | 23,214 bytes | 2.46 倍 | read 12、ls 3、write 1、edit 2、bash 1。 |
| Sol Pro 6.1 | xhigh | [sol-pro-rewrite.md](sol-pro-rewrite.md) | 27,091 bytes | 2.87 倍 | read 13、ls 3、write 1、grep 1、edit 2、bash 2。 |

原文为 9,438 bytes。文件体积不是 token、账单或阅读耗时，不能仅以变长判定质量下降。

[一致性证据](comparison-evidence.json)从实际 session 提取委派任务正文，三轮任务哈希相同，十文件 manifest 也相同；三十个输入文件均保持原哈希。任务正文一致不表示每个运行器自动注入字段都相同，更不消除模型和实际 effort 差异。

访问核查见 [Grok](grok-access-audit.json)、[Astra](astra-access-audit.json)、[Sol Pro](sol-pro-access-audit.json)。三轮均实际读取主 skill 与旧附件；观察到的读取、目录检查及写入都在各自快照内。Astra 的一个 shell 命令和 Sol Pro 的两个 shell 命令已全文检查，只读取自身输出、计数或检查 cwd 内相对引用，没有网络操作。Grok 有一次读取超过文件末尾的工具错误，随后继续核对并完成，不涉及访问其他目录。此处仍是工具轨迹证据，不是操作系统沙箱证明。

成品分别原样复制到 HFUT 的 `docs/plans/`：

- `agent-wings-infrastructure.alphaworld-grok-4.7.md`
- `agent-wings-infrastructure.alphaworld-astra.md`
- `agent-wings-infrastructure.alphaworld-sol-pro.md`

三个交付副本与运行原件哈希一致。在原 HFUT 布局内，相对链接分别核验 14、10、9 处，均存在；原计划哈希未变。这些字节快照的内部相对链接以原项目布局为基准，不以本研究目录为基准。

### Astra 参数偏差

第一版审计把请求后缀 `xhigh` 记成了 thinking，尚未核对 native session 的等级事件。最终一致性检查因此失败，逐项定位发现：

- launch recovery descriptor 确实记载 `AnyRouter/gpt-6-astra:xhigh` 和 `thinking: xhigh`。
- 实际 session 的 `thinking_level_change` 是 `max`。
- 核查时该模型在 `D:/Pi/runtime/agent/models.json` 中的 `thinkingLevelMap` 只有 `max → max`。Pi 文档说明会将请求等级限制到模型支持范围，与这里的实际记录一致。

已更正审计 JSON 与本记录；`comparison-evidence.json` 保留 `allRequestedEffortsSatisfied: false`，没有放宽条件来宣布三轮均通过。未修改全局模型配置，未静默重跑或更换执行通道。原运行 `743502dc-27d7-4a50-9705-d3e0cc6d0869` 的 cwd 是 `D:/Pi/research/alphaworld-blind-runs/agent-wings-02/workspace`，为非 Git 文档快照，输入未变、完整输出已保存。Astra 可作带参数偏差标记的文本观察，不能作为符合指定 xhigh 的样本；严格重试需先使精确模型定义支持 xhigh。

## 成品体现出的编辑选择

以下比较的是成稿中可见的选择，不复原模型内部思路，也不把句式数量当作自然度。

| 样本 | 与 Alphaworld 指导相符的具体表达 | 仍占较大篇幅的编辑动作 |
| --- | --- | --- |
| Grok | 区分赛事阶段、各仓阶段与跨仓 I0–I4，避免将某仓完成当成联合验收；历史记录与当前证据分开。 | 汇入九项赛事约束与额外阶段对照，原有仓库边界、语义列表和阶段表继续扩写。见 `grok-rewrite.md:29–50,134–153`。 |
| Astra，实际 max | 第 4 节将输入与其决策影响配对；第 69 行明确各条线可以在自己的前置条件满足后推进；第 8 节按准备、运行、结束、结算、发布组织交接。 | 仍扩写各仓限制与赛事规则，保留 I0–I4。见 `astra-rewrite.md:56–69,151–179,181–195`。 |
| Sol Pro | 第 4 节将输入与下一步对应；第 168 行允许独立文档工作继续；第 180 行分别处理隔离、计量与展示故障，使修改范围跟随依赖。 | sandbox 矩阵、Router R0–R4、平台 P0–P4、联合 I0–I4 和赛事说明同时展开，协调入口也承担了各仓规划摘要的职责。见 `sol-pro-rewrite.md:53–102,104–144,166–194`。 |

Astra 与 Sol Pro 的依赖表达比原文更显式；Grok 的主要增量更接近跨资料的约束整合。不能将原文已经存在的真实切片、运行/结算区分、不冻结 API 等判断记成 skill 新产生的发现，也不能因保留阶段表就宣布不符合 Alphaworld。

三份输出共同将读取到的配套材料大量写回协调计划。例如原文第 9 节保留三个赛事入口和一段用途说明；三份成品都加入了约 40 RMB 的额度限定、36 小时提交期限及更多评分/交付细则。保留相应约束有意义，但完整重述是否有助于这个文档的读者，尚未检验。材料用于核对事实，与材料应占据多少正文，是两项不同的编辑判断。

这批样本能支持的有限判断是：依赖关系、证据用途和局部修正的指导在部分段落中得到体现；整体编辑仍主要表现为保留既有框架并补全来源、条件和防误读说明，尚不足以证明 skill 稳定改变了这一主导方式，或降低了交付总成本。

## 结论边界与下一项候选检验

- 三轮均未接触父会话成品及新加案例，不能用来判断新案例的效果。
- 没有无 skill 对照、每条件重复运行或读者实际使用测试，且 Astra 实际 effort 不符。以上不构成 skill 因果收益或普遍模型排名。
- 委派任务包含“保留原材料中的明确要求和事实限定”，可能推动补全；原文和配套材料本来就偏重隔离、合规及验收。它们与模型、skill 共同构成输入条件。
- 父会话先前的版本还受到长期哲学讨论和明确编辑方向影响，不能把它当成只加载 skill 就能稳定重现的效果。

后续最值得检验的不是追加禁用句式，而是文档材料如何取舍：需要被读者据以行动的影响进入正文，其余详细条款保持可追溯引用。可以先形成并核查一项这样的局部修订，再写成有前后证据的变更案例；尚未发生的修订不能包装成成功记录。之后固定任务和模型，比较旧附件与新增案例，而不把希望的改写结论直接写进委派提示。
