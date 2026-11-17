# 研究来源与取舍 / Sources and design choices

[中文正文](../README.md) · [English article](../README.en.md)

查阅日期 / Checked: **2026-11-17**。文档和默认分支会变化；下列记录说明本次写作吸收了什么，以及哪些结论仍需在实际环境中验证。论文标明本次阅读版本。外部文章中的性能数字没有移植为本工作流的成绩。

Documentation and default branches can change. These notes identify what informed this article and what still requires local validation. Paper versions identify the editions read. Performance figures from other systems are not results of this workflow.

## Context and recovery

<a id="s01"></a>
**[1] OpenAI — [Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/).**

吸收：短入口、可导航的仓库知识、让 Agent 能访问并使用实际工程依据。取舍：文中的具体审查循环、合并策略和基础设施属于其团队条件；我们没有把它们写成每个任务的固定门禁。

Adopted: short entry points, navigable repository knowledge, and engineering evidence agents can access and use. Boundary: that team's review loops, merge policy, and infrastructure depend on its workload. They are not mandatory gates here.

<a id="s02"></a>
**[2] Anthropic — [Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents).**

吸收：按需获取、外部笔记、压缩与子代理各有适用场景。取舍：摘要要保留可追溯入口；仅有摘要不能代替原始依据，也不能保证不丢信息。

Adopted: retrieval on demand, external notes, compaction, and subagents serve different needs. Boundary: a summary should retain paths to evidence; it cannot replace original evidence or guarantee lossless recovery.

<a id="s03"></a>
**[3] Anthropic — [Effective harnesses for long-running agents](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents).**

吸收：让后继会话能从明确产物和进度继续，区分局部进展与目标完成。取舍：初始化 Agent、功能清单和会话安排是其实现，本文只吸收可接续的原则。

Adopted: leave explicit artifacts and progress for successors; distinguish partial progress from goal completion. Boundary: the initializer, feature list, and session arrangement are one implementation, not a universal template.

## Content and execution interfaces

<a id="s04"></a>
**[4] Agent Skills — [Specification](https://agentskills.io/specification).**

吸收：以清晰触发说明和可按需展开的文件封装程序性知识。取舍：格式兼容不等于所有宿主的工具、脚本依赖、权限和加载行为相同。本文没有导出任何私有 Skill。

Adopted: package procedural knowledge with clear activation descriptions and files that can be expanded on demand. Boundary: format compatibility does not establish equivalent host tools, script dependencies, permissions, or loading. No private skills are exported here.

<a id="s05"></a>
**[5] Model Context Protocol — [Architecture](https://modelcontextprotocol.io/docs/learn/architecture).**

吸收：在宿主、客户端和能力服务之间复用明确接口。取舍：MCP 本身不承担项目规划、任务可靠投递或业务结果验收。

Adopted: reuse defined interfaces between hosts, clients, and capability services. Boundary: MCP itself does not provide project planning, reliable task delivery, or acceptance of business outcomes.

<a id="s06"></a>
**[6] Agent Client Protocol — [Protocol overview](https://agentclientprotocol.com/protocol/overview).**

吸收：客户端与编码 Agent 可以通过既有协议交互，而非重新创造每个平台的通信方式。取舍：会话恢复等能力依实现与协商结果而定；协议不等于一个跨平台项目管理系统。

Adopted: clients and coding agents can use an existing communication protocol. Boundary: capabilities such as session loading depend on implementation and negotiation. A protocol is not a cross-platform project-management system.

## Collaboration and its limits

<a id="s07"></a>
**[7] Anthropic — [How we built our multi-agent research system](https://www.anthropic.com/research/multi-agent-research-system).**

吸收：按问题派发、隔离探索上下文、给执行者清晰任务、持久恢复和原始错误可见性。取舍：广度研究中获得的收益与成本不能直接外推到紧密耦合的工程任务。

Adopted: task-directed delegation, isolated exploration contexts, clear assignments, durable recovery, and visible original failures. Boundary: gains and costs in breadth-oriented research cannot be directly generalized to tightly coupled engineering work.

<a id="s08"></a>
**[8] OpenAI — [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents).**

吸收：主会话收集有边界的并行任务结果；探索输出可以留在子上下文。取舍：可用性、触发方式、权限和当前并行额度以实际客户端为准。本文不承诺无限成员或持久自治。

Adopted: collect results from bounded parallel tasks while leaving exploration output in separate contexts. Boundary: availability, triggering, permissions, and concurrency depend on the actual client. No unlimited team or persistent autonomy is promised.

<a id="s09"></a>
**[9] Cemri et al. — [Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657), read v3.**

吸收：从系统设计、成员对齐与验证等结构因素调查失败。取舍：研究所分析的模型、框架和任务有范围；不能据此断言一个本地故障必然属于其中某类，也不能认为模型能力无关。

Adopted: investigate structural failures in system design, agent alignment, and verification. Boundary: the analyzed models, frameworks, and tasks have a scope. The taxonomy neither diagnoses every local failure nor makes model capability irrelevant.

<a id="s10"></a>
**[10] Kim et al. — [Towards a Science of Scaling Agent Systems](https://arxiv.org/abs/2512.08296), read v3.**

吸收：按任务结构和协调成本判断多 Agent 的价值。取舍：受控基准中的架构偏好不等于我们项目的最优成员数或效率预测。论文版本有扩展，本文依据 v3，不把早期博客的样本规模混用为当前论文结论。

Adopted: evaluate collaboration against task structure and coordination cost. Boundary: architecture preferences in controlled benchmarks do not determine our optimal team size or productivity. We read v3 and do not mix earlier blog sample sizes with the revised paper.

## State, orchestration, and actual implementation

<a id="s11"></a>
**[11] Google ADK — [State](https://github.com/google/adk-docs/blob/main/docs/sessions/state.md).**

吸收：会话状态的范围、更新方式和持久化服务需要明确。取舍：内存服务与持久服务行为不同；“有 state”不足以证明重启后能恢复。

Adopted: define state scope, update behavior, and persistence service explicitly. Boundary: in-memory and persistent services behave differently. Having state does not establish restart recovery.

<a id="s12"></a>
**[12] LangGraph — [Persistence](https://docs.langchain.com/oss/python/langgraph/persistence).**

吸收：用明确的持久检查点支撑后续读取与继续执行。取舍：保存状态不自动提供任意外部副作用的 exactly-once 保证；恢复仍需处理实际提交情况。

Adopted: explicit persisted checkpoints support inspection and continuation. Boundary: saving state does not automatically guarantee exactly-once behavior for arbitrary external side effects; recovery still needs to account for actual commits.

<a id="s13"></a>
**[13] OpenAI — [Codex app-server](https://learn.chatgpt.com/docs/app-server).**

吸收：现成的会话、执行轮次和流式事件接口可以用于接入。取舍：接口可调用不等于可靠队列已经建成；本文没有提供调度器实现。

Adopted: existing thread, turn, and streamed-event interfaces can support integrations. Boundary: callable interfaces do not establish an implemented reliable queue. This repository ships no scheduler.

<a id="s14"></a>
**[14] Orchestrator.inc — [Agent Orchestrator](https://github.com/OrchestratorInc/agent-orchestrator).**

吸收：以现成项目评估主 Agent 调度、工作区隔离与反馈路由。取舍：当前仓库文档围绕代码、分支和 PR；大型桌面应用的共享运行资源仍要专门安排。本次写作未安装或实测该项目。

Adopted: evaluate an existing project for lead-agent scheduling, workspace isolation, and feedback routing. Boundary: current documentation centers on code, branches, and PRs. Shared runtime resources in large desktop applications still need specific coordination. We did not install or test it for this article.

<a id="s15"></a>
**[15] Vibe Kanban — [MCP server](https://www.vibekanban.com/docs/integrations/vibe-kanban-mcp-server).**

吸收：已有任务、关系、会话启动与执行查询接口可以减少人工转发。取舍：这些接口仍需被负责人或调度程序使用，不能把看板展示直接等同于自动闭环。本次写作未安装或实测该项目。

Adopted: existing task, relationship, session-start, and execution-inspection interfaces can reduce forwarding. Boundary: a lead agent or scheduler must use them. A visible board does not establish an automatic end-to-end loop. We did not install or test it for this article.

## Revisit scaffolding as conditions change

<a id="s16"></a>
**[16] Anthropic — [Harness design for long-running application development](https://www.anthropic.com/research/harness-design-long-running-apps).**

吸收：逐项检查流程部件的实际贡献，模型增强后减少不再需要的补偿。取舍：其规划者、生成者、评估者和冲刺实验依赖特定模型与任务，不照搬成固定组织架构。

Adopted: inspect the contribution of individual process components and reduce compensation that becomes unnecessary as models improve. Boundary: its planner, generator, evaluator, and sprint experiments depend on particular models and tasks, rather than defining a fixed organization.

<a id="s17"></a>
**[17] Anthropic — [Scaling Managed Agents: Decoupling the brain from the hands](https://www.anthropic.com/research/managed-agents).**

吸收：把会话、harness 与执行环境视为可分别演进的责任。取舍：这是托管基础设施设计，与本文在本地保留可迁移工作材料的层次不同；我们没有声称实现了同样的运行隔离。

Adopted: treat sessions, harnesses, and execution environments as responsibilities that can evolve separately. Boundary: this hosted infrastructure design operates at a different layer from portable local working material. We do not claim equivalent runtime isolation.

<a id="s18"></a>
**[18] Google Antigravity — [Artifacts](https://antigravity.google/docs/artifacts).**

吸收：用可查看的计划、差异和结果支持人参与关键判断。取舍：具体审批行为随配置变化，本文不要求每一步都暂停。

Adopted: inspectable plans, diffs, and results help people make important judgments. Boundary: approval behavior depends on configuration. This workflow does not require pausing after every step.

<a id="s19"></a>
**[19] Anthropic — [Building effective agents](https://www.anthropic.com/research/building-effective-agents).**

吸收：从简单可组合方案开始，根据问题选择工作流和自主决策。取舍：文章已提示部分工具背景发生变化；保留设计原则，具体能力查当前文档。

Adopted: start with simple composable approaches and choose workflow structure and autonomy according to the problem. Boundary: the article itself notes changes in the tooling landscape. We retain design principles and use current documentation for capability claims.

## Figure method

<a id="s20"></a>
**[20] K-Dense — [Scientific Visualization Skill](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-visualization/SKILL.md) and [Scientific Schematics Skill](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-schematics/SKILL.md).**

采用前者的相关指导：忠实表达、冗余编码、清楚字号、矢量导出与实际查看。后者用于比较，当前方案以生成位图为主，本次没有调用它的生成服务、安装 Skill 或使用其脚本。图示由本仓库原创 Matplotlib 代码绘制；不是数据结果图。

We applied relevant visualization guidance: faithful representation, redundant encoding, readable typography, vector export, and inspection. The schematic skill was evaluated as an alternative; its current workflow primarily generates raster drafts. We did not call that service, install skills, or use their scripts. Figures are drawn with original Matplotlib code in this repository and are not empirical result plots.

<a id="s21"></a>
**[21] Kassis, T., Agarwal, V., He, Y., Patel, D., & Brueckner, A. M. (2026). [Scientific Agent Skills: A Library of Procedural Knowledge for Research Agents](https://doi.org/10.48550/arXiv.2609.00065).**

该库的论文说明，查阅时为 v2。用于来源归属；它没有提供本文工作流的任务效果实证。

The library's paper, v2 at consultation, is credited for provenance. It provides no task-level evidence for this workflow's effectiveness.

## What this comparison changed / 本次对照带来的调整

- **把可迁移内容与运行机制分开。** 可以共享资料和方法，同时承认每个平台的恢复与权限差异。 / **Separate portable content from runtime mechanisms.** Shared material can coexist with different recovery and permission behavior.
- **把调度、协作与接力区分。** 成员能对话，不等于任务自动接续；有文件，也不等于结果已集成。 / **Distinguish messaging, orchestration, and handoff.** Communication does not establish automatic continuation, and files do not establish integration.
- **保留执行者的判断空间。** 方法和工具说明其适用范围，并允许从原件纠错。 / **Keep executor judgment available.** Methods and tools state their scope and allow correction from original evidence.
- **让流程可以删减。** 重复出现的问题才值得固化，条件变化后再检验必要性。 / **Allow process to shrink.** Repeated problems may justify structure; changed conditions justify reassessing it.
- **以可运行结果和人的负担观察价值。** 本文没有把厂商研究结果、仓库热度或 Agent 数量当作自身验证。 / **Observe usable outcomes and human effort.** Vendor results, repository popularity, and agent counts are not validation of this workflow.
