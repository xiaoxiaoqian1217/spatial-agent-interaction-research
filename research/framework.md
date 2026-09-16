# 情境驱动地图交互研究框架

> **2026-09-16 收敛版。** 本框架将原来的 M1 执行信息组织、M2 协同介入、M3 执行衔接与反馈重新放入更上层的研究链：**Context → Situation → Interaction Need → Interaction Strategy → Dynamic Map Interaction**。当前阶段不要求使用 LLM。

## 1. 总体关系

无人系统持续执行空间任务，运行时上下文不断变化。系统首先组织可用上下文，识别当前任务情境，再判断操作者当前需要理解、判断、控制或核查什么，最后决定信息、地图表达和人机主动权如何组织。

```text
Runtime Context
      ↓
Context Model
      ↓
Task Situation
      ↓
Interaction Need
      ↓
Interaction Strategy
      ↓
Dynamic Map Interaction
      ↓
用户操作 / Agent继续执行
      └──────────────→ 新的 Runtime Context
```

这是一个闭环，而不是固定线性流程。正常执行可以长时间保持低干预状态；异常、计划变化、用户主动调整、Agent征询和结果反馈都可能改变当前情境与交互需求。

## 2. Context 与 Task Situation

### 2.1 Runtime Context

Context 表示系统在当前时刻能够获得的事实和状态，包括：

- 任务目标、阶段、计划、进度与约束；
- 平台/Agent状态、能力、当前任务与执行结果；
- 设备、区域、路径、目标点及空间关系；
- 事件、风险、异常、计划变化与反馈；
- 已确认事实、最后报告、当前未知与后续计划；
- 用户当前选区、查看对象、已提交调整和待确认操作。

Context Model 的作用是统一描述“系统现在知道什么”，不是直接决定界面。

### 2.2 Task Situation

Task Situation 是对上下文的任务级解释，回答：

- 当前处于什么任务状态？
- 刚发生了什么变化？
- 哪些对象、区域、路径和任务受到影响？
- 当前是否存在风险、冲突、未知或待决策项？
- Agent 正准备做什么？用户是否需要参与？

候选结构：

```text
Situation =
  Task State
+ Agent / Platform State
+ Spatial State
+ Event
+ Risk / Impact
+ Decision State
+ Evidence State
```

第一阶段优先用显式状态、事件和规则组织情境，不将某种特定形式化方法写死为唯一实现。

## 3. Interaction Need

Interaction Need 是本文连接“任务情境”和“界面组织”的核心中间层。

第一版采用四类需求：

| Need | 操作者当前需要解决的问题 | 示例 |
| --- | --- | --- |
| Understand | 发生了什么、在哪里、当前状态是什么 | 平台失联后谁在接替、当前任务到哪一步 |
| Assess | 变化是否重要、影响什么、方案有何差异 | 接替是否影响原任务、候选路线风险差异 |
| Control | 是否需要介入、能改什么、需确认什么 | 否决接替、修改区域、补充约束、确认计划 |
| Verify | 是否落实、结果是否符合要求、哪些仍未知 | 调整是否被执行、任务是否完成、反馈是否充分 |

多个 Need 可以同时成立。研究重点包括：

- 情境到 Need 的映射依据；
- 多 Need 的优先级与组合；
- 冲突或证据不足时如何处理；
- 哪些情境只需继续监督，不应主动打断用户。

## 4. Interaction Strategy

Interaction Strategy 决定“知道用户需要什么以后，系统应该怎样组织交互”。

```text
Interaction Strategy
├─ Information Organization
├─ Spatial Visualization
└─ Initiative Management
```

### 4.1 Information Organization

围绕“发生什么—为什么—影响什么—还有什么未知”组织信息，并区分：

- 已确认事实；
- 最后报告；
- 当前未知；
- 后续计划；
- 候选方案；
- 执行证据与结果。

### 4.2 Spatial Visualization

根据 Need 决定地图表达，包括但不限于：

- 地图视野与聚焦范围；
- 设备、区域、路径、目标点的显隐与强调；
- 原计划与新计划、计划与实际轨迹的对比；
- 风险区域、受影响范围和候选方案；
- 地图对象与任务过程、变化记录和反馈的联动。

地图不是单纯展示背景，而是用于理解空间变化、表达调整和核查结果的主要交互载体。

### 4.3 Initiative Management

Mixed Initiative 放在这一层，用于决定当前交互由谁发起、Agent 主动到什么程度、用户何时必须参与。

候选级别：

| Level | 方式 | 示例 |
| --- | --- | --- |
| I0 Observe | Agent继续执行，用户按需查看 | 正常稳定执行 |
| I1 Inform | Agent主动告知重要变化 | 路线发生轻微调整 |
| I2 Suggest | Agent提出候选建议 | 建议采用备选路线 |
| I3 Request | Agent请求用户选择或补充信息 | 两个方案需人为取舍 |
| I4 Confirm | 执行前必须人工确认 | 关键任务修改、权限要求 |

“谁发起交互”与“谁拥有执行权限”分开表示。当前不研究根据心理负荷自动改变自动化等级。

## 5. M1—M3 的重新定位

原 M1/M2/M3 保留，但作为 Dynamic Map Interaction 的具体实现机制，不再承担最高层研究主线。

| 实现机制 | 对应 Need / Strategy | 用户问题 | 拟设计交互 |
| --- | --- | --- | --- |
| M1 执行信息组织与呈现 | Understand / Assess；Information + Spatial | 现在怎样、发生了什么、影响什么？ | 地图与任务双向定位、变化联动、历史与后续按需查看 |
| M2 用户与 Agent 协同介入 | Assess / Control；Spatial + Initiative | 是否需要介入、我要改什么、影响什么？ | 选区/对象选择、约束输入、方案比较、影响预览、确认/取消 |
| M3 执行衔接与反馈 | Verify；Information + Spatial | 调整是否落实、结果是否符合要求？ | 调整—计划—执行证据关联、部分落实/失败/未知、后续处理入口 |

## 6. 驱动机制的关系

当前阶段不把“上下文模型驱动”“规则/状态机驱动”“需求/意图推理驱动”当作互斥路线，而是按层级组合：

```text
上下文模型
  → 组织系统当前可用事实

规则 / 状态机
  → 识别任务状态、事件与情境变化

需求推理
  → 将情境转换为 Understand / Assess / Control / Verify

交互策略
  → 决定信息、地图表达与 Mixed Initiative
```

第一阶段优先使用可解释规则、有限状态和显式映射完成原型；后续只有在组合情境、开放事件或跨任务泛化上出现明显瓶颈时，再考虑统计学习或 LLM 扩展。

## 7. 场景层次

系统应用：操作员远程监督异构无人平台完成持续、多阶段的空间任务。

典型协作情境继续保留：

- S1 目标委托与理解确认；
- S2 正常执行与过程监督；
- S3 Agent 主动征询；
- S4 用户主动调整；
- S5 异常处理与协同恢复；
- S6 结果确认与后续衔接。

这些情境用于覆盖检查，不是固定线性阶段，也不是全部实验变量。

重点业务案例继续使用：

1. **异常后的自主接替**：检验 Understand / Assess / Control / Verify 的转换，以及正常监督和必要介入的区别。
2. **新增区域后的主动调整**：检验空间调整表达、约束保持、影响理解和结果核查。

## 8. 共同规则与实现边界

- 任务、对象、调整和反馈保持稳定标识；
- 历史视图必须标明时间；
- 预测、计划与事实区分；
- 下发、接受、开始执行、完成不能合并为一个状态；
- 迟到反馈必须归属对应调整，不能覆盖新要求；
- 已发生动作不能通过编辑历史撤销；
- 前端规则负责确定性显示与操作，后台/Agent负责业务事实与任务执行；
- 缺失接口可使用明确标注的脚本模拟，但不虚构实时能力。

## 9. 研究与评价关系

- **RQ1**：验证 Context / Situation 模型是否覆盖代表性无人系统任务情境。
- **RQ2**：验证 Situation → Interaction Need 的映射是否合理、一致、可解释。
- **RQ3**：验证 Need → Strategy → Dynamic Map Interaction 是否改善用户理解、判断、介入和核查。

对应评价分为：规则与状态逻辑验证、专家一致性/合理性检查、功能验证和用户对照实验。详见[研究方法](methodology.md)及[需求—机制—实现—评价表](design-traceability.md)。
