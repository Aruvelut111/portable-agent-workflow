# Keep the Work, Change the Harness

**An evolving local agent workflow: from unclear requests and capability reuse to multi-agent collaboration and usable results.**

[中文完整文章](README.md) · [Start with a worked example](docs/worked-example.en.md) · [Sources and design choices](docs/references.md) · [Figures and reproduction](figures/README.md)

We want to make sustained progress on complex work with AI while reducing the human effort spent repeating context, finding tools, forwarding prompts, and reconciling progress. As projects, capabilities, and conversations accumulated, we began turning information that lived only in chat into working material that could be found, used, corrected, and resumed.

These practices grew through ongoing practical use and continue to evolve. They address needs shared by different kinds of work: understanding goals, finding available capabilities, continuing context, coordinating contributions, and delivering results. Research, development, creative work, learning, and information management can draw on the methods as needed. The subject and form of delivery can change, and the collaboration should adapt with them.

This repository shares methods and structure distilled from that experience. Examples are deliberately abstracted, and figures show conceptual relationships. We have not conducted a controlled cross-platform study and report no productivity improvement percentages.

We distinguish **practices already adopted, public research used for comparison, and automation that still needs implementation**. Project records and reusable procedures already help with handoffs. Reliable automatic dispatch, failure recovery, and execution across platforms still depend on the particular implementation.

## 1. Start with repeated human work

A complex project may have several AI conversations open at once: some researching, some implementing, others maintaining tools. Everyone can appear busy while the human still has to:

- Explain the background again, including why an earlier approach was abandoned.
- Forward one worker's output to another and remind the recipient to use the latest files.
- Distinguish a completion claim from a generated file and from something the user can actually use.
- Rediscover an existing capability, or notice that a new tool duplicates it.

These symptoms direct our attention to how work connects, how results enter the product, and how useful experience survives. Work that fits one conversation can stay there. Additional coordination becomes useful when dependencies, scale, or context pressure justify it.

## 2. A request is a starting point; the agent must develop an implementation approach

People often express their needs through examples, and may describe one implementation they know as though it were the problem itself. The agent needs to examine the intended outcome: what will the person use, what inputs exist, and what is missing? The gap might be data, an algorithm, interaction, an execution environment, or an interface connecting these pieces.

For example, “make these documents searchable” might call for folder browsing, full-text search, structured filters, or semantic retrieval. The right choice depends on the documents and the use case. Installing a database mentioned in passing does not settle that question.

We clarify the outcome and actual conditions, investigate useful existing approaches, and develop an actionable explanation: **what changes the input must undergo, who consumes the result, where it becomes observable, and which unknown could overturn the approach.** A few sentences may suffice for a small task. Complex work may need a saved architectural explanation and its main dependencies.

Gaps involving the goal, authorization, or a substantial commitment require coordination. The agent can make reversible implementation choices within scope and explain its reasoning. This supports needs the user did not anticipate while preserving the user's authority over the goal.

## 3. Research and reuse should inform a current choice

Before implementation, look for capabilities in local records, native features of the target environment, public implementations, and relevant research. The investigation is useful when it changes the approach: what can be used directly, what needs adaptation, and which assumptions do not hold.

We check the details most likely to affect the decision: actual inputs and outputs, version compatibility, whether the current consumer can use the result, and maintenance costs after integration. Implementation starts when there is enough evidence to choose a route. New evidence can change it later.

A useful repository or author can lead to upstream projects, dependencies, issues, other repositories, and paper citations. Follows and stars provide leads. Suitability depends on what works with the actual local input.

Reuse has several depths: call an established library, extract a stable core, reuse a representation, or borrow an idea. An existing implementation is a candidate foundation. It can be replaced, or a necessary part built independently, when its limitations conflict with the goal.

## 4. Separate working material by responsibility, and connect it around the task

Our library gradually developed several responsibilities. These are logical relationships that can be implemented with existing directories, repositories, or databases.

| Material | What belongs there | When to read or maintain it |
|---|---|---|
| Short working rules | Cross-task essentials such as authorization, data protection, and honest reporting | Keep concise; store tool versions and project progress elsewhere |
| Knowledge library | Facts, sources, conditions of applicability, parameter meanings, and confirmed experience | Read when domain evidence is needed; revise when new facts change a conclusion |
| Skills / reusable procedures | Repeatedly useful methods, triggers, necessary interfaces, and exceptions | Load for relevant tasks; reconsider when mechanisms or model capabilities change |
| Capability and tool registry | Problems solved, real entry points, inputs, outputs, dependencies, coverage, and failure behavior | Search when finding capabilities; update when an entry point changes |
| Project ledger | Goals, current decisions, artifact locations, remaining work, next actions, and ownership | Update at handoffs, changes of approach, important deliveries, or cross-session continuation |
| Project workspace and scratch area | Active implementation, necessary experiments, and intermediate results | Support the current task; retain useful material at completion |

![Working material is separate from execution: rules, knowledge, procedures, capability records, and project state feed task-relevant entry points for different harnesses. Execution still depends on each platform's tools, permissions, and environment.](figures/01-portability.svg)

*Figure 1. Working semantics and locatable material can be portable. Adapters connect them to an actual platform; runtime capabilities still require confirmation. These are responsibilities, not a requirement to build separate services.*

The registry helps an agent find an existing capability; a skill preserves a useful procedure; the ledger tells a successor what to do now; the knowledge library explains why a fact holds.

A discovery can affect several of these, but its main content should have an appropriate home. If a tool update changes invocation, update the capability entry. If the domain fact remains unchanged, there is no need to copy it into another note. A one-off debugging session does not automatically become a skill.

Small tasks may need no dedicated ledger. A record is worth keeping when the next executor needs it and cannot readily reconstruct it from the current files.

## 5. Keep entry points short, evidence reachable, and context expandable

Loading every rule, tool, and historical exchange into each conversation consumes space needed for the current problem. We prefer a navigable map: the current goal, relevant entry points, recent decisions, actual artifacts, and next action.

A summary helps locate evidence; original material supports the conclusion. The executor should be able to open the real file, inspect its caller, or read the original error. When retrieval finds nothing, changing terms, browsing directly, or choosing another tool should remain available.

Records should also distinguish facts, hypotheses, and decisions. An earlier approach may have been valid under its original conditions. When input or version changes, record its applicability and replacement relationship. Preserve useful experience and the reasons for an explicit rejection so that the next handoff does not revive an abandoned approach.

OpenAI's harness engineering account emphasizes short entry points and navigable repository knowledge. Anthropic's context engineering discusses retrieval on demand, compaction, external notes, and subagents. These ideas resonate with our experience, while their particular runtime mechanisms require separate evaluation.[1–3](docs/references.md#s01)

## 6. Decoupling from the harness has two layers

Here, a harness is software that organizes a model, context, tool calls, permissions, and an execution loop. Codex, Claude Code, Antigravity, and other environments can serve as entry points. Their capabilities and loading mechanisms must be checked individually.

**The content layer is comparatively portable:** goals, facts, procedures, capability descriptions, decisions, and artifact pointers. Clear text, files, and necessary structured fields reduce the cost of explaining the project again when changing environments.

**The execution layer needs adaptation:** loading instructions, starting workers, sending messages, providing tools, waiting for results, continuing tasks, and accessing local applications. Shared content formats can still encounter differences in permissions, context selection, and tool-result semantics.

Consequently, synchronization establishes that a copy is in place. Actual loading and availability require runtime evidence. The presence of a messaging tool also does not establish reliable ongoing scheduling.

Existing specifications such as Agent Skills, MCP, and ACP can cover parts of the interface: packaging procedures, connecting to external capabilities, and communication between a client and a coding agent. Project decisions, shared-write ownership, and outcome review still need a workflow.[4–6](docs/references.md#s04)

We aim to keep the meaning of the work stable—what to do, why, and how far it has progressed—while using narrow adaptations for platform differences. Universal automatic team scheduling across platforms remains an implementation and validation problem.

## 7. Give integration an owner, and divide work by dependency

A complex project can have one main point of contact responsible for understanding the goal, assigning work, coordinating shared interfaces, collecting results, and integrating them into the product. The user can still question a worker directly, and workers can communicate about specific dependencies.

A task description should make work possible: explain the goal, inputs, permitted changes, expected output, and how completion will be judged. Add constraints for shared interfaces, sensitive data, or rejected approaches when relevant. Suggested methods, search terms, and samples are corrigible leads. The executor should be able to revise the approach using new evidence.

![Collaboration: the user mainly talks to the integration owner, who coordinates bounded tasks. Workers continue through shared artifacts and state, communicate directly about relevant dependencies, and sequence work on shared resources.](figures/02-collaboration.svg)

*Figure 2. Responsibility converges on a runnable result while exploration and implementation can be distributed. Blue bidirectional connections show task assignment and result feedback; dashed lines show targeted direct collaboration. Shared state does not mean every worker receives every conversation.*

First ask whether the work can progress independently. Research, investigation of competing hypotheses, and edits to non-overlapping code often benefit from parallelism. Repeated edits to the same file, dependence on one application's state, or a sequence in which every step waits for the previous one can make coordination more expensive than the benefit.

Isolation also has layers. Separate worktrees isolate file changes, but do not automatically isolate databases, browser authentication, editors, GPUs, or shared output directories. Large desktop projects add asset saving, compilation, and runtime resources. The actual task determines the arrangement.

Subagents suit bounded exploration and implementation. Long-lived modules may benefit from dedicated conversations and stable entry points. Team size and roles can change with the problem. The integration owner retains important relationships and decisions; detail stays with the relevant executor and artifacts.

Anthropic's research system and Codex subagents provide useful coordination examples. MAST and agent-scaling research also identify coordination, fragmented context, and verification as possible failure sources. They inform design but cannot replace testing on one's own workload.[7–10](docs/references.md#s07)

## 8. Tools should accelerate operations and remain open to inspection and correction

We want tools to handle indexing, parsing, conversion, batch processing, and application control reliably, giving the model more room for judgment. A tool earns its maintenance cost when it removes real repetition, isolates a changing interface, or prevents consequential errors.

Tool results need room for interpretation. An empty array may mean no match within the current scope. It may also mean unsupported parsing, unloaded dependencies, or an incorrect input root. An agent should be able to inspect scope, relevant arguments, versions, and original errors before changing the entry point or fixing the tool.

A useful result explanation can be simple:

> The readable portion of the selected input was processed. Some formats remain unsupported. Matches cover only the processed portion. Original errors and input locations are available for inspection.

A successful tool response may only mean a request was accepted or output was written. Whether a downstream consumer loaded it and whether it took effect need corresponding evidence. Important negative conclusions need bounded coverage. The model should retain the ability to inspect originals and overturn a tool's interpretation.

People and agents should ideally use the same meaningful parameters and entry points. Add structured invocation when a real machine-interface need appears. A second interface with the same purpose but different semantics creates maintenance work.

## 9. Follow real input through to its actual consumer

A common illusion in a large project is that every module is “complete,” yet the user's whole use case does not work. We prefer to select a path through the critical new dependencies early: real input, processing, handoffs, and the application or person that ultimately uses it.

The consumer might be a runtime, editor, downstream script, or final interface. A conversion tool can generate a file while the consumer misinterprets identity, units, coordinates, timing, or other important semantics. Opening a file and using it correctly need different evidence.

![Delivery and diagnosis: real input passes through processing, handoff, and an actual consumer to create a usable result. A discrepancy prompts investigation of the earliest divergence and revision of affected assumptions or interfaces. Interrupted work resumes from committed artifacts and current records.](figures/03-delivery.svg)

*Figure 3. Diagnose along the actual use path. Investigation may return to any relevant stage. A handoff continues from confirmed results without requiring a replay of the entire chain.*

The first path exposes risk while the overall goal and important uncovered capabilities remain in scope. Next, choose a meaningful variation—replace the input, reopen the application, cancel an operation, or change the environment—to test the explanation and reuse boundary.

If a second object can be integrated through data changes alone, that is evidence for a shared part. If it reveals a new mechanism, evolve the adapter or core. Generality comes from actual differences and permits necessary specialized extensions. Zero core changes and fully data-driven behavior are possible means, not universal goals.

## 10. Handoffs need current facts; automation needs runtime mechanisms

Useful recovery material is usually compact: the current goal and constraints, confirmed artifacts and versions, important decisions and reasons, unresolved questions, and the next executable action. Include workspace and background-job entry points when necessary.

A successor reads these first, then examines files and the current runtime. If evidence conflicts, revisit the premises that could change the next action. Full history can remain available without being reread at every handoff.

Ongoing scheduling also needs program-level support. A task being sent, started, producing an artifact, and being integrated are different states. After interruption, confirm whether a previous write committed before retrying. This is particularly important for publishing, imports, and other actions with side effects.

Written conventions help guide agents, but dependable retries, deduplication, event subscriptions, and persistent queues require runtime mechanisms. Google ADK state services, LangGraph persistence, Codex app-server, and existing orchestrators provide parts of this machinery. Adopt them according to the actual gap.[11–15](docs/references.md#s11)

## 11. Every layer of process needs a continuing reason to exist

Processes tend to grow after each failure. A local incident can become a permanent rule, and compensation for an older model can remain long after conditions change. Both can make later work heavier.

We ask: what real error did this prevent? Does it still help? Is there a more direct implementation? Which outcome would deteriorate if it were removed? Consolidate duplicate entry points, correct obsolete instructions in the main text, and retain facts that remain valid.

Validation also follows risk. One machine check that answers the current question is more useful than repeatedly proving that a file exists. Independent review is useful for important designs, public releases, and consequential claims. Visual and interaction judgments need a person to see the actual result. Different tasks warrant different intensity.

Anthropic's later harness experiments discuss removing some scaffolding as model capability improves. This supports testing the continuing value of process; it does not imply removing every structure at once.[16](docs/references.md#s16)

## 12. Where to start

Choose a real project that already requires repeated explanations or forwarding. Establish the current artifact entry point and make the next action executable by a successor. Then document one frequently reused capability or extract one procedure that has repeatedly helped.

Bring in workers when independent work exists. Add orchestration when sustained dispatch and recovery become necessary. Projects such as AO and Vibe Kanban deserve evaluation against actual needs: documented capability, the installed version's capability, and success on a local task are three different kinds of evidence.[14–15](docs/references.md#s14)

To judge whether a change helps, observe whether people still forward tasks, whether a successor can find current artifacts and decisions, whether investigation can continue after tool failure, whether module outputs enter the product, and whether new work avoids duplicate implementation. We prescribe no universal score for these observations.

This workflow still has unresolved problems: semantic misunderstandings, stale records, correlated errors, duplicate work, and reliable isolation of shared application state. We continue adjusting it through actual projects, aiming to preserve methods that others can use and correct.

## Reading and reuse

- [Worked example and optional task and handoff text](docs/worked-example.en.md)
- [Sources, adopted ideas, and limitations](docs/references.md)
- [Original figures, descriptions, and generation instructions](figures/README.md)

The article, original figures, and original examples in this repository use [CC BY 4.0](LICENSE). Third-party sources are cited and linked; their rights remain with their respective owners. This license does not cover unpublished local material. This is a practice report and does not represent the official position of any platform mentioned.
