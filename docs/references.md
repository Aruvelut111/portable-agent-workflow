# 参考资料 / References

[中文正文](../README.md) · [English article](../README.en.md)

下面是整理文章时对照过的资料，按主题放在一起。每项后面简单记了它和本文的关系，方便继续读。查阅日期为 **2026-11-17**；网页会更新，论文标出了阅读版本。

These are the sources consulted while preparing the article, grouped by topic. Each note explains why it is here and where its relevance ends. Checked on **2026-11-17**. Web pages change; paper notes identify the versions read.

外部研究的成绩只属于相应实验。本文没有测过跨平台效率，也没有安装实测这里列出的编排项目。

Results reported by other researchers belong to their experiments. This article has no cross-platform productivity measurements, and the orchestration projects listed here were not installed or tested for it.

## 上下文与接力 / Context and handoffs

<a id="s01"></a>
**[1] OpenAI — [Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/)**

文中的仓库知识组织很有参考价值：入口保持简短，让 Agent 能继续找到工程里的依据。具体审查循环、合并方式和基础设施，则要看团队自己的条件。

Its approach to repository knowledge is useful: keep entry points short and let agents find the engineering evidence behind them. Review loops, merge practices, and infrastructure depend on the team.

<a id="s02"></a>
**[2] Anthropic — [Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)**

按需检索、外部记录、压缩和子代理，可以分别处理不同的上下文问题。摘要也可能漏掉重要细节，所以还要保留回到原件的入口。

Retrieval, external notes, compaction, and subagents address different context problems. Summaries can lose information, which is why the workflow keeps links to originals.

<a id="s03"></a>
**[3] Anthropic — [Effective harnesses for long-running agents](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents)**

关注后一个会话怎样从已有文件和进度继续，也讨论局部进展与整体完成的区别。初始化 Agent、功能清单等安排可以参考，是否需要取决于项目。

This discusses how later sessions continue from existing files and progress, and how partial progress differs from completing the goal. Arrangements such as an initializer and feature list need to fit the project.

## 格式与接口 / Formats and interfaces

<a id="s04"></a>
**[4] Agent Skills — [Specification](https://agentskills.io/specification)**

提供了用文件组织可复用方法、按需展开内容的格式。宿主对工具、依赖、权限和加载的处理仍可能不同。本文只介绍库的组织方法，没有发布本地 Skill 正文。

The specification provides a file format for reusable procedures and content loaded as needed. Hosts can still differ in tools, dependencies, permissions, and loading. This article describes the library's organization without publishing local skill contents.

<a id="s05"></a>
**[5] Model Context Protocol — [Architecture](https://modelcontextprotocol.io/docs/learn/architecture)**

用于理解宿主、客户端和能力服务怎么连接。项目规划、任务投递后的跟进、最终结果检查，还需要使用方另行安排。

This explains connections between hosts, clients, and capability services. Project planning, following dispatched tasks, and checking the final result still need their own arrangements.

<a id="s06"></a>
**[6] Agent Client Protocol — [Protocol overview](https://agentclientprotocol.com/protocol/overview)**

客户端和编码 Agent 之间已有可复用的通信协议。会话加载等能力需要看实现和协商结果，接了协议以后，项目协作仍有其他事情要处理。

Clients and coding agents can use an existing communication protocol. Capabilities such as session loading depend on implementation and negotiation; project collaboration also needs work beyond connecting the protocol.

## 多 Agent / Multiple agents

<a id="s07"></a>
**[7] Anthropic — [How we built our multi-agent research system](https://www.anthropic.com/research/multi-agent-research-system)**

可以参考它怎样派任务、分开探索上下文、保存进度，以及保留原始错误。这里研究任务的收益和成本，不能直接套到几个人共同修改一个工程的情况。

Useful details include task assignment, separate exploration contexts, saved progress, and original errors. The gains and costs in this research workload cannot be transferred directly to agents editing a tightly coupled project.

<a id="s08"></a>
**[8] OpenAI — [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)**

说明主会话怎样收回相对独立的工作，以及如何把大量探索留在子上下文里。使用时仍要查当前客户端的触发方式、权限和并行额度。

This describes collecting fairly independent work in the main conversation while keeping extensive exploration in separate contexts. Triggering, permissions, and concurrency need to be checked in the current client.

<a id="s09"></a>
**[9] Cemri et al. — [Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657), v3**

论文从系统设计、成员对齐和验证等方面归纳失败原因，可以帮助我们找排查方向。它分析的是特定模型、框架和任务，不能只凭分类给一个本地故障定因，模型能力也仍会影响结果。

The paper groups failures in system design, agent alignment, and verification, offering useful directions for investigation. Its models, frameworks, and tasks have a scope. The categories alone do not diagnose a local failure, and model capability still matters.

<a id="s10"></a>
**[10] Kim et al. — [Towards a Science of Scaling Agent Systems](https://arxiv.org/abs/2512.08296), v3**

参考它对任务结构、协调成本和多 Agent 收益的讨论。本文没有据此推算最优成员数或效率。阅读的是扩展后的 v3，没有沿用早期博客的样本规模。

This informs the discussion of task structure, coordination costs, and multi-agent gains. It is not used to predict an optimal team size or productivity. The version read was v3, without carrying over sample sizes from earlier blog coverage.

## 状态与调度 / State and scheduling

<a id="s11"></a>
**[11] Google ADK — [State](https://github.com/google/adk-docs/blob/main/docs/sessions/state.md)**

状态存在哪、怎么更新、能保留多久，都需要看服务的实现。内存服务和持久服务的行为不同，重启恢复要单独确认。

State scope, updates, and lifetime depend on the service. In-memory and persistent services behave differently, so restart recovery needs a separate check.

<a id="s12"></a>
**[12] LangGraph — [Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)**

持久检查点可以帮助读取状态和继续执行。对发布、写数据库这类外部操作，恢复时还得判断上次有没有实际提交；保存状态本身没有为任意外部操作提供 exactly-once 保证。

Persisted checkpoints support inspection and continuation. Recovery from publishing, database writes, or other external actions still needs to determine whether the earlier action committed. Saving state alone does not guarantee exactly-once behavior for arbitrary external effects.

<a id="s13"></a>
**[13] OpenAI — [Codex app-server](https://learn.chatgpt.com/docs/app-server)**

已有线程、执行轮次和流式事件接口可以接入。要做可靠的派发和重试，还得在接口之上实现相应逻辑。本文没有附带调度器。

Thread, turn, and streamed-event interfaces are available for integrations. Reliable dispatch and retry logic must still be implemented around them. This repository includes no scheduler.

<a id="s14"></a>
**[14] Orchestrator.inc — [Agent Orchestrator](https://github.com/OrchestratorInc/agent-orchestrator)**

文档介绍了主 Agent 调度、工作区隔离和反馈路由，值得按实际需求评估。目前偏代码、分支和 PR 工作；共用大型桌面应用时，运行资源仍需另行协调。

The documentation describes lead-agent scheduling, workspace isolation, and feedback routing. It is worth evaluating for a concrete need. Its current focus is code, branches, and PRs; shared runtime resources in desktop applications need additional coordination.

<a id="s15"></a>
**[15] Vibe Kanban — [MCP server](https://www.vibekanban.com/docs/integrations/vibe-kanban-mcp-server)**

已有任务、任务关系、会话启动和执行查询接口，可以研究怎样省掉一部分人工转发。负责人或调度程序仍需要使用这些接口跟进任务。

Existing interfaces cover tasks, relationships, starting sessions, and inspecting execution. They may help reduce manual forwarding. A lead agent or scheduler still needs to use them to follow the work.

## 方法也要更新 / Revisiting the method

<a id="s16"></a>
**[16] Anthropic — [Harness design for long-running application development](https://www.anthropic.com/research/harness-design-long-running-apps)**

文中实验会随模型变化，移除部分不再需要的安排。这提醒我回头检查旧流程的价值。规划、生成、评估和冲刺的具体组合，仍属于它当时的实验条件。

The experiments remove some practices as models change. That is a useful reason to revisit older workflow choices. The particular planner, generator, evaluator, and sprint arrangements belong to those experiments.

<a id="s17"></a>
**[17] Anthropic — [Scaling Managed Agents: Decoupling the brain from the hands](https://www.anthropic.com/research/managed-agents)**

从基础设施角度，把会话、harness 和执行环境分别处理，便于各自演进。本文讲的是本地资料和方法怎样保留，两者处在不同层次；这里没有实现同样的托管运行隔离。

This treats sessions, harnesses, and execution environments separately so they can evolve independently. It operates at a different layer from keeping local material and procedures. This repository does not implement the same hosted runtime isolation.

<a id="s18"></a>
**[18] Google Antigravity — [Artifacts](https://antigravity.google/docs/artifacts)**

可查看的计划、修改和结果，有助于人参与重要判断。具体审批方式看配置，本文也没有要求每一步暂停等待。

Inspectable plans, changes, and results help people make important judgments. Approval behavior depends on configuration; this workflow does not call for pausing after every step.

<a id="s19"></a>
**[19] Anthropic — [Building effective agents](https://www.anthropic.com/research/building-effective-agents)**

参考它从简单、可组合做法开始，按问题选择流程的思路。这是一篇较早的文章，原文也提示了工具环境的变化，具体能力需要再看当前文档。

This informs the preference for simple, composable approaches chosen for the problem. It is an older article and notes changes in tooling; current capabilities need current documentation.

## Figure method

<a id="s20"></a>
**[20] K-Dense — [Scientific Visualization Skill](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-visualization/SKILL.md) · [Scientific Schematics Skill](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-schematics/SKILL.md)**

图示参考了前者关于清楚表达、字号、线型和颜色配合、矢量导出以及查看成图的建议。也比较过后者，目前主要走生成位图的方式。本次图示由原创 Matplotlib 代码绘制，没有安装这些 Skill、使用其脚本或调用生成服务。

The visualization guidance informed typography, redundant use of line styles and color, vector export, and inspection. The schematic skill was also considered; its current approach primarily generates raster images. These figures use original Matplotlib code, without installing the skills, using their scripts, or calling a generation service.

<a id="s21"></a>
**[21] Kassis, T., Agarwal, V., He, Y., Patel, D., & Brueckner, A. M. (2026). [Scientific Agent Skills: A Library of Procedural Knowledge for Research Agents](https://doi.org/10.48550/arXiv.2609.00065), v2**

这是上述库的论文说明，列在这里方便追溯来源。它没有评测本文的工作流。

The paper describes the library above and is included for provenance. It does not evaluate this workflow.
