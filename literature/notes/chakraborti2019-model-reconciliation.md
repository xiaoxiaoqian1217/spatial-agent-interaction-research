# Chakraborti et al. (2017/2019) 计划解释作为模型调和（含实证研究）

- 理论出处：Plan Explanations as Model Reconciliation: Moving Beyond Explanation as Soliloquy, IJCAI 2017（arXiv:1701.08317）。
- 实证出处：Chakraborti, Sreedharan, Grover & Kambhampati, Plan Explanations as Model Reconciliation: An Empirical Study, HRI 2019, pp. 258–266。
- 基础文献：Sreedharan et al., Foundations of Explanations as Model Reconciliation, Artificial Intelligence, 2021（S0004370221001090）。

## 研究问题
当机器人/计划器的模型与人的心理模型不一致时，解释应被视为"模型调和问题"：给出最小完备解释（MCE），使人更新自己的模型后，原计划在人更新后的模型中也是最优的。

## 方法与结论
- 形式化了多模型（机器人模型 M_R、人的模型 M^h_R）与解释生成；2019 HRI 论文报告了以人为对象的用户研究，验证模型调和解释的可用性。
- 相关扩展：处理模型不确定性/多模型的解释（ICAPS 2018）、explicable planning（让计划本身更贴近期望）。

## 与本项目的关系
- 回应"推荐理由/解释"的理论基础：解释的目的是调和双方模型差异，而非罗列信息。对本项目候选设计中"说明推荐依据"提供理论语言和评价视角（解释是否最小、是否针对模型差异）。
- 但该谱系工作在 Fetch 机器人单人交互/经典规划域验证，未涉及多设备失联接替、长时任务和真实操作员。

## 对当前框架的支持或挑战
- 支持解释机制的设计理论；同时表明"解释规划决策"是 2017 年以来系统发展的成熟方向，不能作为创新点提出；可作为解释质量的评价框架。
