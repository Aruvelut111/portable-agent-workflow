# 参考资料 / References

[中文正文](../README.md) · [English article](../README.en.md)

以下资料按正文涉及的设计问题分类。每项说明本文采用的观点及其适用范围。查阅日期为 **2026-11-17**；网页内容可能更新，论文注明阅读版本。

Sources are grouped by the design questions discussed in the article. Each entry explains its contribution and scope. Checked on **2026-11-17**. Web content may change; paper entries identify the version read.

本文没有将外部实验结果作为本地工作流的性能证据，也未安装实测下列编排项目。

Results from external experiments are not evidence of this local workflow's performance. The orchestration projects listed below were not installed or tested for this article.

## 上下文与长期任务 / Context and long-running work

<a id="s01"></a>
**[1] OpenAI — [Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/)**

参考仓库知识的组织方式：简短入口提供导航，详细依据留在可检索的工程资料中。其审查、合并与基础设施安排属于对应工程条件。

Informs the organization of repository knowledge: short entry points guide agents to searchable engineering evidence. Its review, merge, and infrastructure arrangements belong to its engineering setting.

<a id="s02"></a>
**[2] Anthropic — [Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)**

参考按需检索、外部记录、压缩与子代理对不同上下文问题的处理。摘要可能遗漏细节，因此本文保留原始资料的引用路径。

Informs the use of retrieval, external notes, compaction, and subagents for different context problems. Summaries can omit detail, so the workflow retains references to original material.

<a id="s03"></a>
**[3] Anthropic — [Effective harnesses for long-running agents](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents)**

参考跨会话的进度记录、当前文件核对，以及局部进展与整体完成的区分。初始化与功能清单等安排需按项目选择。

Informs cross-session progress records, checks against current files, and the distinction between local progress and overall completion. Initializer and feature-list arrangements need to fit the project.

## 内容规范与通信接口 / Content specifications and communication interfaces

<a id="s04"></a>
**[4] Agent Skills — [Specification](https://agentskills.io/specification)**

提供以文件组织可复用方法、按需加载内容的规范。工具接入、依赖、权限与加载行为仍取决于宿主。本文介绍库结构，不公开本地 Skill 正文。

Defines file-based packaging and progressive loading for reusable procedures. Tool integration, dependencies, permissions, and loading behavior still depend on the host. The article describes library structure without publishing local skill contents.

<a id="s05"></a>
**[5] Model Context Protocol — [Architecture](https://modelcontextprotocol.io/docs/learn/architecture)**

用于界定宿主、客户端与外部能力服务的连接关系。项目规划、持续调度与交付判断需要在协议之上实现。

Defines the relationships between hosts, clients, and external capability services. Project planning, continuing scheduling, and delivery assessment need implementations above the protocol.

<a id="s06"></a>
**[6] Agent Client Protocol — [Protocol overview](https://agentclientprotocol.com/protocol/overview)**

提供客户端与编码 Agent 之间的通信接口。具体能力取决于实现与协商结果，不能据此推定完整项目协作已经具备。

Provides communication between clients and coding agents. Specific capabilities depend on implementation and negotiation; the protocol alone does not establish a complete collaboration system.

## 多 Agent 的分工与失效 / Multi-agent decomposition and failure

<a id="s07"></a>
**[7] Anthropic — [How we built our multi-agent research system](https://www.anthropic.com/research/multi-agent-research-system)**

参考任务分派、探索上下文分离、进度保存与原始错误保留。其研究工作负载中的收益与成本不能直接外推到紧密耦合的工程任务。

Informs delegation, separate exploration contexts, progress persistence, and preservation of original errors. Its research-workload gains and costs cannot be directly transferred to tightly coupled engineering tasks.

<a id="s08"></a>
**[8] OpenAI — [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)**

参考将边界明确的工作交给子上下文、由主会话回收结果的方式。触发、权限与并行额度需要核对当前客户端。

Informs bounded delegation into separate contexts, with results collected by the main conversation. Triggering, permissions, and concurrency limits need checking in the current client.

<a id="s09"></a>
**[9] Cemri et al. — [Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657), v3**

MAST 从系统设计、成员对齐与验证等方面归纳失效模式，可用于提出排查假设。分类本身不能确定本地故障原因，结论也受模型、框架与任务范围限制。

MAST categorizes failures in system design, agent alignment, and verification, helping frame diagnostic hypotheses. The categories do not establish a local cause; findings are scoped to the models, frameworks, and tasks studied.

<a id="s10"></a>
**[10] Kim et al. — [Towards a Science of Scaling Agent Systems](https://arxiv.org/abs/2512.08296), v3**

参考任务结构、协调成本与多 Agent 收益之间的关系。本文不据此估算最优成员数或效率；阅读版本为扩展后的 v3。

Informs the relationship between task structure, coordination costs, and multi-agent gains. The article does not use it to estimate an optimal team size or productivity. The version read was the expanded v3.

## 状态、持久化与调度 / State, persistence, and scheduling

<a id="s11"></a>
**[11] Google ADK — [State](https://github.com/google/adk-docs/blob/main/docs/sessions/state.md)**

用于区分状态作用域、更新方式与持久性。内存服务和持久服务的恢复行为不同，需要结合所选实现判断。

Distinguishes state scope, updates, and persistence. In-memory and persistent services have different recovery behavior, which needs to be assessed for the chosen implementation.

<a id="s12"></a>
**[12] LangGraph — [Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)**

参考检查点的状态读取与恢复机制。任意外部副作用是否已提交仍需单独确认，持久化本身不提供通用的 exactly-once 保证。

Informs state inspection and recovery through checkpoints. Whether an external effect committed still needs separate confirmation; persistence alone provides no general exactly-once guarantee.

<a id="s13"></a>
**[13] OpenAI — [Codex app-server](https://learn.chatgpt.com/docs/app-server)**

提供线程、执行轮次和流式事件等集成接口。可靠派发、状态关联与重试仍需相应运行逻辑，本仓库不包含调度器实现。

Provides integration interfaces for threads, turns, and streamed events. Reliable dispatch, state correlation, and retries still need runtime logic. This repository includes no scheduler implementation.

<a id="s14"></a>
**[14] Orchestrator.inc — [Agent Orchestrator](https://github.com/OrchestratorInc/agent-orchestrator)**

其文档介绍主 Agent 调度、工作区隔离与反馈路由，可用于评估现成编排能力。当前主要面向代码、分支和 PR；共用桌面应用时仍需处理运行资源冲突。

Its documentation describes lead-agent scheduling, workspace isolation, and feedback routing, making it a candidate for evaluating existing orchestration. Its current focus is code, branches, and PRs; shared desktop runtimes need additional resource coordination.

<a id="s15"></a>
**[15] Vibe Kanban — [MCP server](https://www.vibekanban.com/docs/integrations/vibe-kanban-mcp-server)**

文档提供任务、关系、会话启动与执行查询接口，可用于减少人工转发。持续跟进取决于负责人或调度程序如何使用这些接口。

The documentation provides interfaces for tasks, relationships, session startup, and execution queries that may reduce manual forwarding. Continuing follow-up depends on how a lead or scheduler uses them.

## 架构演进与结果可见性 / Architectural evolution and inspectable results

<a id="s16"></a>
**[16] Anthropic — [Harness design for long-running application development](https://www.anthropic.com/research/harness-design-long-running-apps)**

参考随模型能力变化重新评估、移除部分流程结构的实验。规划、生成与评估的具体组合属于其当时条件，不作为本文固定流程。

Informs reassessing and removing workflow structures as model capability changes. Its particular combinations of planning, generation, and evaluation belong to those experiments and are not prescribed here.

<a id="s17"></a>
**[17] Anthropic — [Scaling Managed Agents: Decoupling the brain from the hands](https://www.anthropic.com/research/managed-agents)**

从基础设施层面区分会话、harness 与执行环境。与本地工作信息的可迁移性处于不同层次；本文未实现同样的托管运行隔离。

Separates sessions, harnesses, and execution environments at the infrastructure layer. This differs from the portability of local working information. This workflow does not implement equivalent hosted runtime isolation.

<a id="s18"></a>
**[18] Google Antigravity — [Artifacts](https://antigravity.google/docs/artifacts)**

参考将计划、修改和结果作为可查看产物呈现的方式。确认与审批行为取决于配置，本文不要求每步暂停。

Informs presenting plans, changes, and results as inspectable artifacts. Confirmation and approval behavior depend on configuration; the workflow does not require a pause at every step.

<a id="s19"></a>
**[19] Anthropic — [Building effective agents](https://www.anthropic.com/research/building-effective-agents)**

参考按问题采用简单、可组合结构的设计原则。该文较早，且原文已说明工具环境变化，具体能力应以当前文档为准。

Informs choosing simple, composable structures for the problem. It is an older article and notes changes in tooling; current documentation is needed for specific capabilities.

<a id="figure-method"></a>
## 图示方法 / Figure method

<a id="s20"></a>
**[20] K-Dense — [Scientific Visualization Skill](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-visualization/SKILL.md) · [Scientific Schematics Skill](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-schematics/SKILL.md)**

图示采用前者关于清晰表达、字号、线型与颜色配合、矢量导出和成图检查的建议。也比较了后者以生成位图为主的方法。本次使用原创 Matplotlib 代码绘图，未安装这些 Skill、运行其脚本或调用生成服务。

The visualization guidance informs clarity, typography, redundant use of line styles and color, vector export, and inspection. The schematic skill's primarily raster-generation approach was also considered. These figures use original Matplotlib code, without installing the skills, running their scripts, or calling a generation service.

<a id="s21"></a>
**[21] Kassis, T., Agarwal, V., He, Y., Patel, D., & Brueckner, A. M. (2026). [Scientific Agent Skills: A Library of Procedural Knowledge for Research Agents](https://doi.org/10.48550/arXiv.2609.00065), v2**

上述库的论文说明，用于追溯图示方法来源；该研究未评测本文的工作流。

Describes the library above and establishes provenance for the figure-method reference. It does not evaluate this workflow.
