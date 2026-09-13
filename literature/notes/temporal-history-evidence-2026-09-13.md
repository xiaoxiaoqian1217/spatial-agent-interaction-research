# 任务历史、空间状态与持续监督：交互证据

2026-09-13，用户纠偏后的定向核查。问题是用户如何联系任务过程与空间对象，不以算法、推荐或失联不确定性为主线。页码为论文页码；注明PDF页时从1计数。仅将正文的作者结果写作证据，其余标为本次判断。

## Scott et al. 2006：事件时间线与历史地图

Stacey D. Scott, Stéphane Mercier, M. L. Cummings, Enlie Wang. *Assisting Interruption Recovery in Supervisory Control of Multiple UAVs*. HFES 2006。[作者全文](https://www.eng.uwaterloo.ca/~s9scott/wiki/uploads/Main/scott_hfes2006.pdf)，key `scott2006recovery`。

- PDF pp.1–2：事件书签按设备/区域分类；点击书签显示当时地图并高亮对象。另一条件加入可选时间区间的加速动画。当前地图仍在另一显示屏上。
- p.3：9名大学生、四设备仿真、35分钟内六次约两分钟中断。复杂题需要历史变化辅助判断。恢复时间的辅助类型主效应不显著（p=.632）。原文称简单决策“显著”，却列p=.102、α=.1，两者不一致，本报告不采信该显著性表述。
- pp.4–5：观察提示书签拥挤、历史与当前关系不清；叠加历史痕迹是作者建议，非已验证结果。

本次判断：时间线联动地图已有先例；可研究关联质量，不能把回放本身当创新。中断实验不证明本业务长时任务必有中断。

## St. John, Smallman & Manes 2005：变化表与地图双向联动

*Recovery from Interruptions to a Dynamic Monitoring Task: The Beguiling Utility of Instant Replay*. HFES Annual Meeting，473–477。[作者上传全文](https://www.researchgate.net/publication/250360673_Recovery_from_Interruptions_to_a_Dynamic_Monitoring_Task_The_Beguiling_Utility_of_Instant_Replay)，key `stjohn2005replay`。

pp.473–475，Method、Table 1：35人，五种条件比较动态地图变化检测。CHEX将变化列成表，选择条目高亮地图对象，也支持反向关联；回放不是唯一历史呈现办法。pp.475–476，Results：CHEX报告变化更快、误报更少；Basic Replay在部分分析中慢于无辅助。Discussion说明仅标出“哪里变化”不足以说明“变了什么”。

本次判断：应以变化表＋联动作为强基线，不用纯日志和纯回放制造薄弱对照。任务是识别变化，不能外推为用户更能制定调整或理解后续影响。该实验同时改变显式变化信息，不能将全部收益归因于双向高亮。

## Porathe 2014：跨日航程、地图与时间尺度

Thomas Porathe. *Remote Monitoring and Control of Unmanned Vessels – The MUNIN Shore Control Centre*. COMPIT 2014，460–467。[作者全文](https://thomaspo.folk.ntnu.no/webbprofil/hfunmanned/Porathe%20COMPIT%202014.pdf)，key `porathe2014munin`。

§4.1–4.4，pp.463–465：空间概览用可缩放海图；时间概览按天/小时展开，事件同时在时间视图和海图出现；区分船端/岸端时区。趋势图以当前时刻分开历史测量和未来预测。作者明确这里展示监控界面，控制界面另论。

§5，p.466：首次用户测试尚在计划中。故这篇提供长航程、多时间尺度设计先例，不提供效率或长期使用效果。不能将未来概念方案称为已部署验证系统。

## Kristensson et al. 2009：时空一体表达并非总优于二维

*An Evaluation of Space Time Cube Representation of Spatiotemporal Patterns*. IEEE TVCG 15(4)，696–702，DOI 10.1109/TVCG.2008.194。[论文全文存档](https://uncharted.software/assets/GeoTime_Method_Evaluation_TVCG_09_published.pdf)，key `kristensson2009spacetime`。存档位于GeoTime相关厂商网站，证据来自论文正文，不用厂商推广文字。

§4–5：30名校园招募的可视化新手，组间比较二维与时空立方体，回答人物移动问题；复杂整体时空题平均响应121秒对60秒，错误率差异不显著；部分简单时点题二维错误更少。§6：地图熟悉度、二维基线文字标记等限制外推。

本次判断：依据用户具体查询选择表达，不能预设三维、叠加全部轨迹或展示全部历史更好。这是已结束数据的分析，不是执行中设备控制实验。

## QGroundControl：常规空间操作下限

官方[Plan View](https://docs.qgroundcontrol.com/master/en/qgc-user-guide/plan_view/plan_view.html)（UI Overview、Mission Stats / Terrain Panel）和[Fly View](https://docs.qgroundcontrol.com/master/en/qgc-user-guide/fly_view/fly_view.html)（Actions associated with a map position、Pause），2026-09-13访问master文档。key `qgcinteraction2026`。

已有地图选点/拖动航点、任务条目编辑、路线及距离/估计时长呈现；飞行视图提供位置相关操作和确认。它说明基本地图编辑与任务指标关联已有工程能力，不证明本业务采用该系统，也不提供跨设备影响理解的人因效果。

## 检索记录与限制

实际查询：`human robot interface mission history timeline map situation awareness temporal visualization`；`robot supervisory control history replay interface situation awareness`；`Temporal Overview robot interface mission`；`An Evaluation of Space Time Cube Kristensson pdf`；`Recovery from Interruptions Beguiling pdf`；`robot map timeline user study 2025 interface`。

纳入理由：可明确指出用户看到什么、操作什么、如何在时间与空间间关联，且能查到原始论文/官方功能资料。这里包含基础论文，不能据年代早便判定如今仍未解决。检索命中2025–2026机器人编程/任务说明与地图时间线工作，但不把开发者编程任务当持续监督证据；最新部署与长期用户研究尚未穷尽。无数据库全量筛选，不声称系统综述。
