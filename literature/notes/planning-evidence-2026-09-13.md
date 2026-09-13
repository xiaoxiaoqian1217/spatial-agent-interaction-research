# 接替方案比较与计划影响：定向证据核查

日期：2026-09-13。入口：`research/literature-handoff.md`。这是针对计划比较、混合主动规划与调整影响的定向调研，不是系统综述，也不是已开展的用户需求研究。未修改原有笔记或参考文献库。

## 检索与证据边界

检索组合包括：`explainable planning contrastive explanations plan why not plan user study`、`mixed initiative planning replanning interface plan comparison robot operators`、`NASA mixed initiative replanning MAPGEN plan repair preserving plan`、`Unmanned vehicle plan comparison visualizations`。优先出版社全文、作者公开稿与 NASA 官方记录。沿命中论文追查实验章节，而不只采信摘要。下文标明全文/元数据及章节；HTML 使用章节定位，Szafir 使用作者 PDF 页码（不是期刊连续页码）。没有尝试穷尽所有调度算法、专利或商业调度产品。

## 逐篇证据

### 1. Behymer et al. (2015)：直接的候选方案比较先例

Kyle J. Behymer, Elizabeth M. Mersch, Heath A. Ruff, Gloria L. Calhoun, Sarah E. Spriggs. *Unmanned Vehicle Plan Comparison Visualizations for Effective Human-autonomy Teaming*. Procedia Manufacturing 3, 1022–1029. DOI：10.1016/j.promfg.2015.07.162。

已读[作者上传全文](https://www.researchgate.net/publication/283962389_Unmanned_Vehicle_Plan_Comparison_Visualizations_for_Effective_Human-autonomy_Teaming)；[出版社记录](https://www.sciencedirect.com/science/article/pii/S2351978915001638)全文打开报错。§1，pp.1023–1025 已提出比较车辆能力、到达时间及分派对既有任务的影响，呈现 Plot/Matrix/Chart、权重、阈值与总分。§2：12 名基地员工，对三个静态方案、3/5 个指标答题；不是实体接替。§3.1–3.2，p.1027：准确率 >99%；Plot 只在跨方案找最优单指标时显著更快；选择“最佳方案”无格式显著差异；找不可接受方案更慢；计数阈值违规差异不显著（p=.07）。不能照搬摘要为“Plot 全面优于表格”。§4 承认只比较三方案。

项目判断：候选比较、权重及影响维度已有直接先例。应把普通矩阵/排序作为强基线；不能把“多方案比较”作为研究贡献本身。

### 2. Krarup et al. (2021)：反事实计划与差异高亮已有实现和对照

Benjamin Krarup, Senka Krivic, Daniele Magazzeni, Derek Long, Michael Cashmore, David E. Smith. *Contrastive Explanations of Plans Through Model Restrictions*. 已读[arXiv v1 全文](https://arxiv.org/html/2103.15575)，[机构正式出版记录](https://strathprints.strath.ac.uk/88992/)确认 2021 年发表；本次未逐式审计编译证明。

§6.1.1、Fig.22：原计划与假设计划并排，区分新增、删除、时间改变，比较成本及验证报告。§7.2：20 名混合职业志愿者随机分两组；基线同样有两计划，但无差异/成本高亮。解释满意度中位数 4 对 3，作者报告显著；测的是主观解释满意度，不是接替正确率或实时状态识别。§3 主要假设双方共享初始状态、动作与目标，差异集中于约束和偏好。§7.2 未追踪用户模型演变。

项目判断：局部替换、调整前后差异与反事实说明不是空白；失联后的未知执行状态能否改变比较结论，是不同且尚需验证的问题。

### 3. Eifler & Hoffmann (2020)：说明牺牲哪些目标已有计划空间方法

Rebecca Eifler, Jörg Hoffmann. *Iterative Planning with Plan-Space Explanations: A Tool and User Study*. 已读[arXiv 全文](https://arxiv.org/html/2011.09705)；本次以预印本记录，不推定正式期刊发表。

§3：用户选硬目标，界面区分附带满足与未满足软目标，以最小不可满足目标集合解释目标冲突；不是只给单个替代计划。§4：仅六名熟悉框架的本组规划研究者，各组三人；人为赋予偏好效用，最多十轮；作者明确统计推断不适宜。带解释组均达效用9、平均6.3轮；无解释组剔除一名提前退出者后效用8.5、十轮。结果仅为初步趋势，且不能忽略剔除与样本局限。

项目判断：可以借用“满足接替目标需牺牲哪些原目标”的表达基线；真实操作员是否理解此类冲突集合仍待验证。

### 4. Lindsay et al. (2026)：空间任务、资源与优化取舍的近期强近邻

Alan Lindsay, Andrés A. Ramírez-Duque, Bart Craenen, David A. Robb, Emanuele De Pellegrin, Laurence Boé, Andrea Munafò, Ronald P. A. Petrick. *Supporting human-agent communication for explainable planning in spatial-temporal planning problems*. Neural Computing and Applications 38, 370，正式发表 2026-05-06。已读[出版社全文](https://link.springer.com/article/10.1007/s00521-025-11711-7)。注意本文 UAV 指水下自主设备。

§6–8：MAST 中间概念支持距离、邻近时长、对象集合和数值目标查询。§9.6–9.7：12 名硕博，风场模型中减少老电池设备行程、避维修、减少通信受损区域；固定先旧版A后扩展B，探索性访谈反馈更易表达目标及取舍。存在顺序/学习混杂；不是专业操作员异常接替对照。§9.3–9.4：新优化要求并不保证有限求解时间内指标改善。

项目判断：空间语义与任务相关解释也已有先例；不应把“地图＋反事实”当新颖性。算法求解限制和现实状态不确定性应分别标识。

### 5. Szafir, Mutlu & Fong (2017)：新增任务介入已有交互时间线实证

*Designing Planning and Control Interfaces to Support User Collaboration with Flying Robots*. IJRR 36(5–7), 514–542. DOI：10.1177/0278364916688256。已读[作者全文 PDF](https://www.danszafir.com/papers/IJRR17-Szafir.pdf)。

§5–6：交互时间线与三维航点支持计划/执行；对照为保护性遥操作与航点委派。§6.5–6.6，PDF pp.17–18：36 名纳入分析的校园志愿者，主要为新手，单飞行机器人，执行十分钟。§6.8.2，pp.20–21：新增空气检测任务成功人数，遥操作12/12、协作11/12、航点6/12；协作较航点响应快。机器人重对齐请求无需重规划，各组无显著差异。认知负荷假设未获支持。

项目判断：新增任务场景应保留，但不能以普通航点基线较弱证明新界面普遍有效；该研究不是多设备异常接替，也不是长时脱离回路证据。

### 6. MAPGEN：部署成熟度反证线索，全文证据尚未完成

NASA [2004 官方报告记录](https://ntrs.nasa.gov/citations/20040111024)说明为火星车任务开发部署 MAPGEN；[2005 Capabilities and Shortcomings 记录](https://ntrs.nasa.gov/citations/20050184145)可检索。两份 2005 PDF 通过 web 打开报错，本次不据搜索摘要断言具体修复功能、最小扰动效果或操作员绩效。它足以要求后续审查成熟混合主动调度系统，但不足以在本报告认定“已经解决失联接替”。

## 综合判断与收敛建议（本次分析）

已有证据覆盖候选横向比较、阈值/权重、反事实计划、增删/重排差异、目标冲突与空间资源取舍。尚不能声称这些一般能力缺失。不同界面对不同问题的收益也有冲突：快速识别某项优势，不等于更好地识别不可接受方案，更不等于异常处置正确。

较值得验证的切口是：在失联后部分任务状态未确认时，操作员是否知道方案影响计算依赖哪些假设，以及这些假设改变时推荐是否仍适用。但本次没有证据证明这是尚未解决的研究空白；需与透明度、不确定性可视化文献合并判断。

可操作的否定测试：固定同一后台与同一候选集，将“排序矩阵＋原任务延误/冲突摘要＋时间戳/未知标记”设为基线。如果它已经能可靠支持接替范围与方案选择，便不需要复杂反事实交互。若错误主要源自候选不可行或缺失，则应先修数据与后台；若未知状态不会改变任何选择，则不应强行将不确定性解释设为论文主线。

下一轮只需核实三件事：原任务被抽调后到底有哪些业务认可的损失指标；什么回执足以确认步骤完成；未知完成范围在真实案例中是否曾使两个候选方案的优劣翻转。未取得这些证据前，建议保留窄问题进行需求核验，暂不宣称创新成立。
