# 监督、透明度与状态证据：逐篇核查

2026-09-13。与 [本轮综合报告](01-verified-survey-2026-09-13.md) 配套。正文核查指读取与本问题相关的系统、方法、结果和限制，不指复现实验。以下“项目判断”为本次推论。

## Mercado et al. 2016：最接近的透明度基线

*Intelligent Agent Transparency in Human–Agent Teaming for Multi-UxV Management*. Human Factors 58(3), 401–415. DOI 10.1177/0018720815621206；key `mercado2016transparency`。[出版社全文PDF](https://journals.sagepub.com/doi/pdf/10.1177/0018720815621206)。

pp.403–406、Fig.1–5：30名大学生，模拟异构设备任务，比较推荐A/B；三条件从基本计划逐步增加理由及不确定性。每组八个任务，其中三个最佳选择不是首推。未知以透明度/颜色和文字原因表达，没有概率数值。每任务两分钟，不能把整体到场时间当长时监督。

pp.406–408、Table 1：正确拒绝错误建议随透明度提升；正确采纳只在相对基本条件时显著改善；响应时间无显著差异。pp.409–413讨论负荷、信任及模拟限制。

项目判断：本项目不能宣称首次组合推荐、理由与未知提示。差别须落到缺失执行证据如何改变接替范围；这仍是待检验推论。

## Senaratne et al. 2025：有经验的使用者，但样本并非普遍行业操作员

*A Framework for Dynamic Situational Awareness in Human Robot Teams: An Interview Study*. 本轮以[arXiv v1正文](https://arxiv.org/html/2501.08507v1)定位；key `senaratne2025dynamic`。

§3.1–3.4：16名有重复使用经验者，14名从事机器人研发；半结构访谈。§4.4、Table 5/7记录将不动误判为故障及不理解任务分配；§4.5.1记录扫描界面、暂停/减速和优先处理。§4.5区分已经使用的办法与建议，不能合并成现有功能。

§4.4.6明确没有收到过量SA的具体事例；§5.4提醒非机器人背景实践者不足。项目判断：可指导案例访谈，不证明本业务长期疲劳、接替差错或界面效应；不能用访谈人数推算事故发生率。

## Sidaoui, Daher & Asmar 2021：JISA的作用边界

*Human-Robot Interaction via a Joint-Initiative Supervised Autonomy (JISA) Framework*. [正文](https://arxiv.org/html/2109.04837v1)，[作者元数据](https://arxiv.org/abs/2109.04837)；key `sidaoui2021jisa`。

§III区分机器人自信触发求助与人主动介入；§IV使用AR辅助SLAM，§V通过GUI辅助拼图。§IV-B报告建图耗时较gmapping降低35%–50%；这是任务系统性能，不是操作员负荷效应。§V展示局部匹配与全局纠错。

项目判断：求助/介入已有框架，但该文没有验证失联设备的替代者比较。拼图可删除错误拼接，不代表实体已执行动作可回滚；不以其优越性概括人因结论。

## Epperson et al. 2025：AGDebugger不能替代实体任务证据

*Interactive Debugging and Steering of Multi-Agent AI Systems*. CHI 2025；[正文](https://arxiv.org/html/2503.02068v1)、[正式DOI记录入口](https://arxiv.org/abs/2503.02068)，DOI 10.1145/3706598.3713581；key `epperson2025agdebugger`。

§6：14人的两部分研究，第一部分6人定位错误，第二部分8人交互调试。§6.2两界面错误描述质量相当；§6.3仅2/8最终得到精确正确答案，但重置功能评价较高。

项目判断：偏好或理解提升不能等同任务成功。可借鉴历史导航/反事实调试；对象是开发者、对象状态是消息工作流，不承担本项目操作员需求和实体执行落实论证。

## Kalempa et al. 2021：自动接替有实现，但故障假设必须检查

*Multi-Robot Preemptive Task Scheduling with Fault Recovery: A Novel Approach to Automatic Logistics of Smart Factories*. Sensors 21(19),6536；[出版社全文](https://www.mdpi.com/1424-8220/21/19/6536)，DOI 10.3390/s21196536；key `kalempa2021mrpf`。

§5.3抢占在适当阶段边界发生；§5.4故障设备选择最近可用替代者、移交并前往维修；无空闲者可等待阶段完成。§6以ARENA实体机器人和虚拟货箱展示调度、抢占及恢复。

项目判断：规则明确时无需人工逐台选择；但设备仍可参与恢复的模型不等于完全失联。本篇不是操作员评价，不引用未经核实的毫秒恢复数字。既有bib的第一作者及标题不完整，本次按出版社更正。

## 官方工程资料：动作确认与任务证据不是同一层

- [PX4 Safety](https://docs.px4.io/main/en/config/safety)，Data Link Loss Failsafe节：失联超时、响应及模式例外可配置。证明安全响应有实现；不证明任何特定设备已经暂停，也不证明接替方案最优。key `px4safety2026`。
- [MAVLink Mission Protocol](https://mavlink.io/en/services/mission.html)，Message/Enum Summary及Monitor Mission Progress节：MISSION_ACK确认任务交换操作，MISSION_CURRENT报告当前项等状态，MISSION_ITEM_REACHED报告到达。由此推论，界面应核查协议事件与“业务完成”的映射，不能把上传成功等同执行完成。key `mavlinkmission2026`。

均为2026-09-13访问的动态官方文档，非业务现状或人因实验。

## 访问限制和需要补查的相邻论文

- Roldán 2017：[作者机构PDF](https://orbilu.uni.lu/bitstream/10993/32785/1/sensors-17-01720.pdf)返回25页记录及正文入口，后续读取报错；PMC验证码。本轮不重复旧笔记具体统计，更不把预测监控解释为失联实验证据。
- *Enhanced Teleoperation Interfaces for Multi-Second Latency Conditions: System Design and Evaluation*，IEEE Access 2023，[出版记录](https://ieeexplore.ieee.org/document/10026823/)，DOI 10.1109/ACCESS.2023.3240307：仅核摘要，涉及3秒延迟、预测和牵引丢失。待全文核查，非完全失联/多设备接替。
- *How transparency impacts trust in teleoperated autonomous robots under uncertainty*，[2026出版页](https://www.sciencedirect.com/science/article/pii/S1071581926001527)：仅核摘要，其透明度收益与负荷/绩效取舍值得补查；不能据此得出本项目增量价值。
- *Neuro-cognitive benefits of high agent transparency on operators’ cognitive and affective emergent states in human-agent teaming*，[2026出版页](https://www.sciencedirect.com/science/article/pii/S0003687026000165)：仅核摘要，DOI 10.1016/j.apergo.2026.104738。与上一条不可未经任务和条件核对就合成统一效应。

这些未完成全文条目不新增正式引用条目，也不作为创新依据。

