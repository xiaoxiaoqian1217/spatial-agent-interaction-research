# Paper

本目录用于保存**正式论文正文及其直接相关材料**。

## 约定

- 正式论文主文件：`thesis.docx`
- 如学校或期刊提供模板，可将模板文件一并放在本目录。
- 不在此目录存放外部参考论文；外部论文统一放到 `literature/papers/`。
- 论文中的正式插图建议源文件保存在 `assets/figures/`，正文只引用最终版本。

## 为什么正文使用 Word

当前论文更适合以 `.docx` 作为主格式，便于导师批注、学校模板适配、目录与参考文献排版。仓库中的 Markdown 文件主要用于研究过程记录，不作为最终论文排版格式。

## 当前工作题目

**《面向无人系统任务的情境驱动地图动态交互组织方法研究》**

当前研究主线：

```text
Context
→ Task Situation
→ Interaction Need
→ Interaction Strategy
→ Dynamic Map Interaction
```

其中 RQ2 的核心关注是：如何由运行时任务情境识别操作者当前需要 Understand / Assess / Control / Verify 什么；RQ3 再将这些 Need 转换为 Information、Spatial Visualization 和 Initiative Management。

Mixed Initiative 属于 Interaction Strategy 的组成部分，不作为全文唯一主题。

## 当前技术立场

现阶段不将 LLM 作为必要技术条件，也不把“规则驱动”“上下文模型驱动”“需求推理驱动”看作互斥方案。

第一阶段采用：

```text
上下文模型
→ 组织运行时事实

规则 / 状态机
→ 识别任务状态、事件和情境变化

Interaction Need 推理
→ 判断当前需要理解 / 判断 / 控制 / 核查什么

Interaction Strategy
→ 决定信息、地图表达和主动权
```

如果后续发现规则在复杂组合情境或跨任务泛化上存在明确瓶颈，再考虑学习方法或 LLM 扩展。

## 当前写作安排

1. **引言**：围绕“为什么当前任务情境需要不同交互”提出问题，不再把全文写成完整协同系统功能罗列。
2. **相关工作**：按 Situation Awareness、Context-Aware / Adaptive UI、无人系统地图、Mixed Initiative、Dynamic / Generative UI 组织。
3. **任务情境与需求分析**：建立 Context 因素、Situation、IR1—IR5 和 Understand / Assess / Control / Verify。
4. **方法**：写清 Situation → Need → Strategy 的机制，规则/状态机作为第一阶段实现方案。
5. **原型**：实现地图动态组织、协同介入和结果核查；原 M1/M2/M3 作为实现机制保留。
6. **验证**：分别验证推理逻辑、系统功能和用户效果。

## 正文更新注意事项

现有 `thesis.docx` 中已经写入的旧题目、旧版 G1/G2 主线和“面向长时空间任务”的表述，需要在下一轮正文修订时统一调整；不要直接删除已有业务分析和两个重点案例，而是重新挂接到新的 RQ1—RQ3 框架。

两个重点案例继续保留：

- 异常后的自主接替；
- 新增区域后的主动调整。

它们用于验证代表性任务情境，不代表全文只研究这两类事件。

## 正文进度

2026-09-13 已建立 `thesis.docx`，已有“1 引言”和“3 任务场景与需求分析”的初稿。2026-09-16 研究问题完成收敛，下一轮正文应优先同步：

- 题目；
- 总研究问题；
- RQ1—RQ3；
- Context → Situation → Need → Strategy → UI 主线；
- 相关工作章节结构；
- 原 M1/M2/M3 的层级定位。

结果、改善幅度和最终贡献必须在实验后填写，不预写显著性或用户收益。
