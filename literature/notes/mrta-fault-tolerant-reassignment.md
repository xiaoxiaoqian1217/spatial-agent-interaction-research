# 容错任务重分配算法文献（合并笔记）：MRPF (Kalempa 2021)、Haider 2026、Bolarinwa 2025

## 条目
1. Kalempa, V. C. et al. Multi-Robot Preemptive Task Scheduling with Fault Recovery. Sensors, 2021.（PMC8512959）
2. Haider, M. A. et al. Fault-Tolerant Framework for Dynamic Task Reassignment in Multi-Robot Systems. Eng. Proc., 2026, 120(1): 22.（MDPI，会议论文）
3. Bolarinwa, J. et al. Should we get involved? Impact of human collaboration and intervention on multi-robot teams. Frontiers in Robotics and AI, 2025. DOI: 10.3389/frobt.2025.1526287

## 核心内容
- MRPF：多机器人抢占式调度，机器人故障时与最近的空闲机器人通信替换，故障机进维修；替换可立即或等待空闲；仿真+甘特图验证，替换不阻塞整体进度。
- Haider 2026：MQTT 心跳/断连检测故障 → 标记 failed → 识别其执行中与排队任务 → 按最小执行时间或负载均衡重分配给健康机器人；优先部分完成或临近截止的任务；故障注入场景下 30–40ms 级恢复。纯算法贡献，人在环外。
- Bolarinwa 2025：集中式/分布式多机器人团队架构，任务失败且请求时限未过时由 Planner 按失败概率重分配；GUI 随消息更新；研究人介入程度对团队的影响。

## 与本项目的关系
- 回答"接替对象选择"：自动重分配（按距离、负载、失败概率、截止时间）是成熟算法问题，持续有新工作。
- 这些系统中接替决策由算法做出，操作员最多收到 GUI 状态更新；"让操作员理解并参与接替选择"不是这些工作的目标。若本项目系统可以或已经配备此类自动重分配，则"逐台人工比较"的困难可能由引入成熟调度器直接解决——这是必须向用户核实的关键事实（现有系统为何没有自动接替）。
- 商业侧：Realtime Robotics 宣称其工作站技术支持把维修中机器人的任务方便地转交给其他机器人（厂商博客，非学术证据，仅作工程可行性旁证）。

## 对当前框架的支持或挑战
- 挑战交互创新的必要性预设：如果失败可检测、任务可完整描述、资源充足，算法接替已足够，界面创新空间小；本项目价值更可能存在于"算法不适用或不可信时的人机分工"（状态未知、任务语义不全、权限与责任要求人决策），需要先核实业务条件。
