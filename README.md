# Spatial Agent Interaction Research

> **2026-09-16 研究定位收敛：** 工作题目调整为“面向无人系统任务的情境驱动地图动态交互组织方法研究”。当前主线为 **Context → Situation → Interaction Need → Interaction Strategy → Dynamic Map Interaction**。现阶段不把 LLM 作为必要技术前提，优先研究上下文模型、规则/状态机和需求推理的组合机制。

本仓库用于管理论文研究全过程。正式论文正文与研究过程材料分开管理：论文正文放在 `paper/`，文献、研究框架、实验记录等使用 Markdown 等便于版本管理的格式。

## 当前研究问题

无人系统在持续、多阶段空间任务中会不断发生任务推进、计划变化、异常、风险、Agent主动调整和用户介入。固定或仅按预定义页面组织的界面难以始终对应操作者当前真正需要处理的问题。

本文关注：

> **在无人系统持续执行空间任务的过程中，如何根据运行时任务情境识别操作者当前的交互需求，并据此动态组织地图信息、空间可视表达和人机交互方式？**

当前研究链：

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
```

### 三个研究问题

1. **RQ1 — Task Situation Modeling**：哪些运行时上下文因素影响操作者的交互需求，以及如何组织为可用于交互决策的任务情境？
2. **RQ2 — Interaction Need Inference**：如何由任务情境识别操作者当前需要 Understand / Assess / Control / Verify 什么？
3. **RQ3 — Dynamic Interaction Organization**：如何将交互需求转化为信息组织、空间可视化和 Mixed-Initiative 策略，并通过动态地图界面支持任务理解与人机协同？

Mixed Initiative 属于 RQ3 的 Initiative Management，不作为全文唯一主题。

## 当前技术立场

“上下文模型驱动”“规则/状态机驱动”“需求/意图推理驱动”不是互斥方案，当前按不同层级组合使用：

```text
上下文模型
→ 组织系统当前知道什么

规则 / 状态机
→ 判断当前任务状态、事件和情境变化

Interaction Need 推理
→ 判断用户现在需要理解 / 判断 / 控制 / 核查什么

Interaction Strategy
→ 决定信息、地图表达和主动权如何组织
```

第一阶段优先采用显式、可解释和可复核的方法形成闭环。后续只有在复杂组合情境或跨任务泛化上出现明确瓶颈时，再考虑统计学习或 LLM 扩展。

## 业务背景与边界

业务背景为操作员远程监督空中、地面、四足等异构无人平台及其执行智能体，并由信息处理、态势分析、任务规划等支撑智能体辅助完成空间任务。

研究重点是**任务情境到交互组织的转换机制**，不研制无人平台控制算法、接替推荐算法或通用多智能体编排。

“长时”保留为应用特征，强调任务持续演化、多阶段和多次可能介入；无长期人员实验时，不宣称降低长期疲劳或改善长期警觉性。

## 用户交互需求

当前使用 IR1—IR5 进行设计追踪：

- **IR1** 理解任务进展与空间分布；
- **IR2** 理解关键变化、原因及后续影响；
- **IR3** 准确表达空间调整及约束；
- **IR4** 判断是否需要介入以及介入到什么程度；
- **IR5** 核查调整落实与任务结果。

原 M1/M2/M3 继续保留为具体实现机制：

- **M1 执行信息组织与呈现**；
- **M2 用户与 Agent 协同介入**；
- **M3 执行衔接与反馈**。

它们现在位于 Interaction Strategy / Dynamic Map Interaction 层，不再作为最高层研究主线。

## 仓库结构

```text
paper/
  thesis.docx              # 正式论文正文（后续放入）
  README.md                # 正文管理说明

research/
  outline.md               # 论文结构与章节分工
  research-question.md     # 研究问题、目标、边界
  framework.md             # 情境驱动动态交互框架
  methodology.md           # 研究方法与验证设计
  design-traceability.md   # RQ—IR—机制—实现—评价追踪

literature/
  papers/                  # 阅读/引用的外部论文 PDF
  notes/                   # 文献阅读笔记

experiments/
  protocols/               # 专家评审、用户实验、对照实验方案
  results/                 # 实验结果与分析

prototype/                  # 交互原型、实现说明
assets/
  figures/                  # 论文图表、模型图、实验截图
references/
  references.bib            # 参考文献数据库
data/                       # 非敏感研究数据
```

## 当前验证思路

验证分三层：

1. **推理层**：情境覆盖、状态转换、规则冲突/未匹配、Need 与 Initiative 输出合理性；
2. **系统层**：地图、调整、状态和反馈是否正确运行；
3. **用户层**：与合理常规界面相比，是否改善理解正确率、变化遗漏、判断耗时、漏介入/误介入、空间调整错误和落实判断。

重点业务案例继续使用：

- 异常后的自主接替；
- 新增区域后的主动调整。

案例用于构造可重复情境，不代表论文只研究这两个业务事件。

## 当前阶段

- [x] 确定无人系统 + 地图动态交互研究方向
- [x] 建立论文研究仓库
- [x] 收敛 Context → Situation → Need → Strategy → UI 主线
- [x] 固化 RQ1—RQ3 与 IR1—IR5 的层次
- [ ] 完成相关工作与理论基础定向调研
- [ ] 建立第一版 Context / Situation 数据结构
- [ ] 建立代表性情境集与规则/状态转换表
- [ ] 建立 Need → Information / Spatial / Initiative 策略表
- [ ] 设计并实现低保真及可运行原型
- [ ] 完成功能验证、专家评审与用户实验
- [ ] 分析结果并完成论文

## 研究原则

- 先明确研究问题，再选择实现技术。
- 不把规则、状态机、LLM 或 Agent 框架本身当作研究贡献。
- 每个动态界面变化都应能追溯到 Task Situation、Interaction Need 和 Interaction Strategy。
- 区分系统工程能力和论文研究贡献。
- 论文结论由文献、任务证据、功能验证、专家评审或用户实验支撑。

优先入口： [研究问题](research/research-question.md) → [研究框架](research/framework.md) → [需求追踪](research/design-traceability.md) → [研究方法](research/methodology.md)。
