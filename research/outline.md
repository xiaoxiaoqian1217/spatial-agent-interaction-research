# 论文大纲（2026-09-16 收敛版）

> 工作题目：**面向无人系统任务的情境驱动地图动态交互组织方法研究**。
>
> 全文主线：**Context → Situation → Interaction Need → Interaction Strategy → Dynamic Map Interaction**。
>
> 原 M1 执行信息组织、M2 协同介入、M3 执行衔接与反馈继续保留，但作为具体交互实现机制，不再作为最高层研究问题。

## 研究定位

研究面向操作员监督无人系统执行持续、多阶段、空间分布的任务。论文不研究平台控制、任务规划算法或通用多智能体编排，而研究：**运行时任务情境如何转化为适当的人机交互。**

当前不把 LLM 作为必要前提。第一阶段优先采用显式上下文模型、规则/状态机和可解释的需求推理；后续是否引入学习方法依据实际瓶颈决定。

## 核心研究问题

- **RQ1 — Task Situation Modeling**：哪些运行时上下文因素影响操作者的交互需求，以及如何组织为可用于交互决策的任务情境？
- **RQ2 — Interaction Need Inference**：如何依据任务情境判断当前任务要求界面支持的理解、判断、控制和核查内容，显式需求表示相较直接策略映射有何价值？
- **RQ3 — Dynamic Interaction Organization**：如何将交互需求转化为信息组织、空间可视化和 Mixed-Initiative 策略，并通过动态地图界面支持任务理解与人机协同？

## 论文结构

# 1 引言

## 1.1 研究背景

介绍异构无人平台、Agent 自主执行、持续多阶段任务和操作员在环监督。说明地图既承担态势理解，也承担空间调整与结果核查。

## 1.2 问题提出

分析固定或仅按预定义页面组织的交互在动态任务中的不足：

- 任务阶段和关注对象持续变化；
- 异常、风险和 Agent 行为改变信息优先级；
- 并非所有变化都需要人工介入；
- 同一事件在不同约束和空间关系下可能对应不同交互需求；
- 直接情境适配能否满足需要，以及显式需求表示是否带来额外收益，尚须在本文场景中比较。

提出从 Runtime Context 经 Task Situation、Interaction Need 到 Interaction Strategy 的研究思路。

## 1.3 研究目标与范围

明确 RQ1—RQ3、IR1—IR5、两个重点案例及研究边界。说明“长时”主要作为持续演化和多次情境变化的应用特征，不在无长期实验时宣称疲劳改善。

## 1.4 研究内容与贡献

按实际完成情况组织贡献：

1. 无人系统空间任务的 Context / Situation 表示；
2. Situation → Interaction Need 的可解释推理机制；
3. Need → Information / Spatial / Initiative 的动态交互组织方法；

可运行地图原型与分层验证作为上述方法的支撑证据；组合方法或增加层次不自动构成创新。

# 2 理论基础与相关研究

本章回答“已有研究做到哪里、本文方法建立在什么基础上”。

## 2.1 Situation Awareness 与监督控制

讨论操作者对当前事实、意义和后续趋势的理解需求，以及自动化监督中的信息组织问题。

## 2.2 Context-Aware / Adaptive Interface

梳理上下文模型、自适应界面、状态驱动界面和智能地图研究，重点比较：

- Context 如何定义；
- 是否运行时感知；
- 是否直接 State → UI；
- 是否存在 Interaction Need 中间层。

## 2.3 无人系统地图与空间任务交互

梳理 C2 Map、无人机/无人艇监督、任务阶段地图使用、空间态势和安全界面研究，论证地图为何是核心交互载体。

## 2.4 Mixed-Initiative Human-Agent Interaction

梳理 AIMS / SAMI、Mixed-Initiative Visual Analytics、Agent 主动协助等。强调：

- 谁发起交互与谁拥有执行权限不同；
- Mixed Initiative 在本文中属于 Interaction Strategy 的 Initiative Management；
- 本文不把动态自动化等级本身作为唯一研究问题。

## 2.5 Dynamic / Generative UI

讨论任务进展驱动界面变化、Agent UI、DuetUI、ProactiveVA 等研究。区分“直接生成 UI”和“先推断 Interaction Need 再组织 UI”。

## 2.6 研究不足与本文切入点

形成文献对比矩阵：

| 维度 | 关注点 |
| --- | --- |
| Context 表示 | 是否覆盖任务、Agent、空间、事件、风险、决策和证据 |
| Situation 识别 | 是否解释运行时状态与变化 |
| Interaction Need | 是否表示任务导出的交互支持需求，是否评估该表示的增量价值 |
| Dynamic UI | 是否动态调整信息、地图与操作 |
| Initiative | 是否根据情境调整告知/建议/请求/确认 |
| Validation | 是否有系统、专家或用户实验 |

研究空白最终以实际文献证据收敛，不预先宣称完全无人研究。

# 3 无人系统任务情境与交互需求分析

本章回答 RQ1 的需求来源和分析基础，并为 RQ2 建立标注空间。

## 3.1 系统应用与任务边界

描述操作员、无人平台、执行 Agent、支撑 Agent、任务目标和空间对象，不虚构未核实权限和流程。

## 3.2 协作情境

保留六类覆盖情境：

- S1 目标委托与理解确认；
- S2 正常执行与过程监督；
- S3 Agent 主动征询；
- S4 用户主动调整；
- S5 异常处理与协同恢复；
- S6 结果确认与后续衔接。

这些是覆盖分类，不是固定线性任务阶段。

## 3.3 Interaction Requirements

- IR1 理解任务进展与空间分布；
- IR2 理解关键变化、原因及后续影响；
- IR3 准确表达空间调整及约束；
- IR4 判断是否需要介入以及介入到什么程度；
- IR5 核查调整落实与任务结果。

## 3.4 Context 因素分析

从 Task、Agent/Platform、Spatial、Event、Risk/Impact、Decision、Evidence、User Context 八类因素分析运行时信息。

## 3.5 Interaction Need 定义

定义：

- Understand；
- Assess；
- Control；
- Verify。

说明多标签、优先级、冲突和无介入情境；此分类不是用户心理状态模型，也不等同于三级 SA。

## 3.6 两个重点案例

### C1 异常后的自主接替

重点检验：Understand → Assess → 必要时 Control → Verify。

### C2 新增区域后的主动调整

重点检验：空间要求理解、Assess / Control、方案变化和 Verify。

# 4 情境驱动动态交互组织方法

本章是核心方法章节，对应 RQ1—RQ3。

## 4.1 Context Model

定义运行时数据结构、对象标识、任务/平台/区域/路径关系、时间与证据状态。

## 4.2 Task Situation Recognition

说明如何通过状态、事件和规则识别当前任务情境：

```text
Context Facts
→ Task State
→ Trigger / Change
→ Affected Objects
→ Risk / Impact
→ Decision State
→ Evidence State
```

第一阶段采用上下文模型、有限状态、事件和规则组合，不使用 LLM；这些方法可跨情境识别、需求判断、策略选择及执行环节使用，不固定成一一对应的技术层。

## 4.3 Interaction Need Inference

定义 Situation → Need 的映射：

```text
Task Situation
→ Understand / Assess / Control / Verify
```

研究内容包括：

- 单 Need 和多 Need；
- 主 Need / 次 Need；
- 优先级；
- 规则冲突；
- 未匹配与证据不足；
- 不应打扰用户的正常状态；
- 与直接规则映射比较需求层价值及额外复杂度；
- 开发情境与独立保留情境的划分、标注分歧和反例。

## 4.4 Interaction Strategy

### 4.4.1 Information Organization

组织事实、变化、原因、影响、未知、计划、候选方案和执行证据。

### 4.4.2 Spatial Visualization

动态组织地图视野、对象、区域、路径、风险、原/新计划和实际轨迹。

### 4.4.3 Initiative Management

定义本文原型的交互方式编号（不是标准自动化等级）：

- I0 Observe；
- I1 Inform；
- I2 Suggest；
- I3 Request；
- I4 Confirm。

分别记录发起方、交互方式、业务操作集合和执行权限；允许用户主动发起、修改、拒绝与 Agent 主动建议，避免把自动弹窗等同于 Mixed Initiative。

## 4.5 Dynamic Map Interaction

将策略映射到实际交互：地图聚焦、图层、对象强调、方案比较、信息卡片、调整操作、确认、结果核查。

## 4.6 M1—M3 实现机制

- M1 执行信息组织与呈现；
- M2 用户与 Agent 协同介入；
- M3 执行衔接与反馈。

说明它们如何落实 Need / Strategy，而非作为独立理论。

# 5 原型系统设计与实现

## 5.1 系统架构

描述情境、需求、策略和地图界面的逻辑关系；规则与状态机可跨多个环节实现，逻辑表示不要求拆成多个服务或 Agent。

## 5.2 Context 与状态维护

说明任务、对象、事件、计划、反馈和证据如何维护。

## 5.3 规则与状态机实现

展示第一版代表性情境集、规则表、优先级和冲突处理。

## 5.4 地图动态组织实现

实现视野、对象、区域、路径、风险和方案比较；保留用户选区/拖拽视野，提供恢复全局与取消入口，记录不必要视野切换。

## 5.5 Mixed-Initiative 交互实现

实现 Inform / Suggest / Request / Confirm 等交互。

## 5.6 调整与反馈衔接

记录用户要求、计划变化、执行端接受、实际执行和结果，不把“已接受”当作“已落实”。

## 5.7 真实接口与模拟边界

明确真实数据、模拟事件和未接入能力，避免以模拟冒充真实无人平台验证。

# 6 验证与结果

验证分层进行。

## 6.1 RQ1：Context / Situation 覆盖验证

检查代表性情境是否可被模型表达，记录遗漏和无法表达项。

## 6.2 RQ2：Need 推理验证

候选指标：

- 情境覆盖率；
- 状态转换正确率；
- 规则冲突率；
- 未匹配率；
- Need 输出与专家标注一致性；
- 交互方式与专家判断一致性。

## 6.3 功能验证

覆盖正常执行、重要变化、异常、自动调整、人工确认、用户主动调整、部分落实、失败、未知、连续修改和迟到反馈。

## 6.4 专家评审

检查 Context 因素、Need 分类、规则、主动交互方式和地图信息是否符合任务与权限。

## 6.5 用户对照实验

### 条件与结论边界

- B0：数据实时更新但交互组织固定的常规界面，保留必要信息、操作和告警。
- B1：基于完整任务情境直接选策略的规则动态界面，不包含显式 Need 层。
- P：同样情境与策略能力，经显式 Need 表示组织交互。

先做独立情境上的 B1/P 策略及维护比较，再做小规模 B0/P 用户对照。前者评估需求层增量价值，后者评估整套动态组织效果。只有增加 B1/P 用户对照，才能归因需求层的用户收益。协议见[对照方案](../experiments/protocols/context-driven-comparison.md)。

### 指标

- 理解正确率；
- 变化遗漏；
- 判断耗时；
- 漏介入 / 误介入；
- 对象/范围/约束错误；
- 落实判断正确率；
- 操作耗时；
- 主观负荷、控制感和可用性。

## 6.6 结果分析

区分推理正确、系统正确和用户表现，不用一层证据替代另一层结论。

# 7 讨论

## 7.1 研究问题回答

分别回答 RQ1、RQ2、RQ3。

## 7.2 与已有方法比较

重点比较：

- State → UI；
- Context → Adaptive UI；
- Situation → Need → Strategy → UI。

讨论增加 Interaction Need 中间层是否带来收益、何种收益及复杂度；允许无差异或不利结果，不能把内部架构差异直接解释成用户效果。

## 7.3 Mixed Initiative 的作用与边界

分析何种情境下 Inform / Suggest / Request / Confirm 有益，何时可能造成打扰或过度干预。

## 7.4 规则方法的边界

讨论规则数量、组合情境、跨任务迁移和开放事件。如果实际数据支持，再提出学习方法或 LLM 作为后续方向，而非预设必然需要。

## 7.5 长时与外部有效性

区分长时任务、系统长时间运行和人员长期使用。没有长期人员实验时不推断疲劳或长期警觉性效果。

## 7.6 工程与研究贡献边界

区分地图组件、协议、Agent框架、状态同步等工程能力与论文的交互组织方法贡献。

# 8 结论与展望

总结：

1. Context / Situation 建模；
2. Interaction Need 推理；
3. Information / Spatial / Initiative 动态策略；
4. 无人系统地图原型和验证结果。

后续可探索：

- 更复杂的组合情境；
- 跨任务规则迁移；
- 数据驱动或 LLM 辅助 Need 推理；
- 多操作员、多 Agent 协同；
- 真实无人系统和长期人员实验。

## 当前写作原则

- 先写问题、方法和证据，不预写实验结论；
- 文献综述按问题线组织，不逐篇罗列；
- 主方案 UI 变化追溯到 Situation、Need 和 Strategy；直接映射基线追溯到 Situation 和 Strategy；
- 规则/状态机是当前实现方案，不直接等同于论文创新；
- Mixed Initiative 是 Interaction Strategy 的组成部分，不单独扩大为全文主题；
- 两个重点案例用于验证，不代替整体研究对象。

相关：[研究问题](research-question.md)、[研究框架](framework.md)、[研究方法](methodology.md)、[需求追踪](design-traceability.md)。
