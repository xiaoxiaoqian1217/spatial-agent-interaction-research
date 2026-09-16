# 情境驱动地图交互：参考路线与差异边界

> 核查日期：2026-09-16。用途是指导当前不使用LLM的工程应用研究，不表示已经复现文献或证明方法新颖性。

## 1. 主方法参考：SAMI

Nathan Brooks，2017，博士论文 *Situational Awareness and Mixed Initiative Markup for Human-Robot Team Plans*，CMU-RI-TR-17-64。

CMU记录说明，研究把态势感知呈现、人机主动权设置和算法选择约束标记到团队计划的具体位置，并通过仿真、无人艇部署和语言可学习性研究评价。适合参考计划情境如何关联交互配置，以及方法、实现和验证如何衔接。[CMU原始记录](https://publications.ri.cmu.edu/situational-awareness-mixed-initiative-markup-human-robot-team-plans)

**对本文的启发（研究判断）**：用显式模型与可追踪配置支持交互，无须把LLM作为前提；借鉴方法组织，不照搬博士论文规模。

**不能直接推出的结论**：不能把SAMI称为固定不变的界面，也不能仅凭摘要断言其不处理运行时情境或不支持复用。其语言学习研究不能替代本文地图交互效果评价。更细的机制差异仍需阅读全文并逐项核对。

## 2. 短篇结构参考：Best of Both Worlds

*Best of Both Worlds: Design and Evaluation of an Adaptive Delegation Interface* 描述AIMS、SAMI任务模型及界面，研究关注任务模型理解与对自动化的信任校准；文中任务模型的态势感知标记也涉及地图聚焦等界面调整。[作者提供的论文全文](https://static1.squarespace.com/static/5a0da796be42d6a3dec58a1a/t/5a0eddc1c830258272006748/1510923713510/Best%2Bof%2BBoth%2BWorlds%2BDesign%2Band%2BEvaluation%2Bof%2Ban%2BAdaptive%2BDelegation%2BInterface.pdf)

**对本文的启发（研究判断）**：参考“问题—架构—关键界面—受控验证”的简洁结构。本文的任务导出需求、策略适切性和空间核查指标须重新设计，不能直接照搬信任实验或套用其结果。

## 3. 本文需要证明的差异

| 候选差异 | 所需证据 | 不能当成证明的内容 |
| --- | --- | --- |
| 多因素任务情境到交互策略的可解释组织 | 明确情境变量、规则依据、组合情境与反例 | 仅罗列字段或画架构图 |
| 显式Need层的价值 | 与同输入、同策略能力的B1直接映射比较 | 增加一层或给规则重新命名 |
| 跨案例复用 | 对相同新增分支比较修改成本与回归问题 | 禁止B1复用，或只展示P的成功例子 |
| 动态地图交互效果 | 相同信息和操作条件下的用户对照 | 仅程序运行正确、专家赞同或文献已有收益 |

上述是待验证的差异，不预先宣称“首次”或“已有方法不能做到”。当前规则/状态机、上下文模型与需求判断可混合使用；LLM只作为未来在出现明确瓶颈时的研究方向。

对应：[研究问题](../../research/research-question.md)、[实验协议](../../experiments/protocols/context-driven-comparison.md)。
