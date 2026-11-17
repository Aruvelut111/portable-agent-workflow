# Worked Example: Adding Search to a Local Document Browser

[English article](../README.en.md) · [中文](worked-example.zh-CN.md)

This hypothetical request illustrates how the library, design choices, assignments, and delivery checks connect. The application, tasks, and results are illustrative. This repository does not implement the application.

## 1. Separate the intended use from proposed solutions

Suppose a local document browser already supports browsing folders and opening files. The user asks: “There are too many documents. Add search. Could we use a vector database and have several agents work on it?”

The established goal is to make documents easier to find. A vector database and multiple agents are candidate solutions that need to be assessed against the existing application.

Inspection establishes that most documents are text or Markdown; common queries use terms, filenames, or exact phrases; an existing reader can be reused; some attachments cannot yet be parsed; and source files should remain read-only, with content kept locally. Given these conditions, an initial implementation can use full-text search and let results navigate to their source locations. Semantic retrieval remains an option to compare when real queries reveal limitations in lexical search.

The reason for this choice should be recorded alongside the decision. If users later make many concept-based queries or document types change, a successor can assess whether the choice still holds.

## 2. Find reusable parts in the library

Project records supply the current version, launch instructions, and prior decisions. The tool registry helps locate readers, search components, and application-control capabilities. The knowledge base supplies confirmed findings about formats, encoding, and source navigation. Relevant skills are loaded only when their methods are needed.

Test candidate components on a few representative documents to check reading, querying, and return formats. Important questions include whether the reader preserves source locations, whether the panel can use search results, and how old locations become invalid after a file changes. If the registry search finds nothing, inspect project code, related capabilities, and public implementations. One search is not a complete inventory.

Reuse may be limited in scope: retain the reader, adopt a mature full-text component, and add the result adaptation needed by the application. Consider broader replacement only if these parts cannot satisfy the goal.

## 3. Clarify the interface before choosing parallel work

If search and the result panel have a clear boundary, they can be assigned separately. If the change is small, one agent may be simpler. Before parallel work, establish a shared understanding of the result:

| Interface concern | Problem it addresses |
|---|---|
| Stable document identity and an openable location | Results still point to the correct document after sorting, refreshing, or rebuilding the index |
| Match location and its representation | The panel interprets positions correctly, without mixing character and byte offsets |
| File version used by the index | Old snippets and locations can be recognized after a file changes |
| Snippet and display information | The panel can present understandable results without reconstructing their meaning |
| Processing scope and failures | No match, unprocessed inputs, and execution failure remain distinguishable |

These are shared meanings to establish. Concrete fields can follow the existing application; generality alone is not a reason to invent another protocol.

Contributors modify their own modules and use independent development indexes. The integration lead updates the main application and index. If the interface needs to change, affected dependencies are coordinated and the decision is recorded in the project.

An actionable assignment might read:

> Add full-text search to the existing document browser. Inputs are text and Markdown in the user-selected folder. Keep source files read-only and data local. Reuse the reader; select the search component based on fit. You own the search module and relevant checks; another contributor owns the panel. Location, version, and coverage information must agree with the panel interface. Deliver the actual changes, run commands, and results on representative inputs, identifying read failures and unsupported inputs. Place outputs in the agreed project directory and coordinate shared interface changes with the integration lead.

An actual assignment supplies concrete locations for inputs, code, and outputs. Candidate components can be included as leads without making them unchangeable implementation requirements.

## 4. Check interface meaning through actual use

Once the index returns results, connect it to the panel and check the path from query to source navigation. Representative checks might include:

- Query a document containing both Chinese and English, click a match, and confirm the document and location.
- Edit the matching passage and refresh. Confirm that the index and location update, or that the old version is identified.
- Include an unreadable attachment and confirm that coverage and failure information remain visible.

Each check targets a risk that could change the result. The first checks position representation, the second checks updates and invalidation, and the third checks the scope of an empty result.

If the panel opens the correct file at the wrong location, compare location values and their interpretation through reading, indexing, the interface, and the panel. Find the first divergence. Rebuilding the index or adjusting the UI without that diagnosis is insufficient.

“No results” also needs a scope. No match in the currently readable text is different from an absence of relevant content in all documents. Users and agents should be able to continue inspecting attachments, originals, and diagnostics.

## 5. Resume from current outputs after interruption

A handoff record might contain:

> Current goal: search documents locally and navigate from results to the source. Full-text search for text and Markdown is connected to the panel; changes, run instructions, and checks are in the current delivery. Full-text search was chosen because current queries mainly use terms and exact phrases. Attachment parsing and automatic updates remain unfinished. Next, use the existing refresh entry point to check reindexing after a file edit. Development indexes are separate; the integration lead maintains the main index.

A real record links actual outputs, input versions used for checks, and the current workspace. The successor checks file state first and continues unfinished work. If an earlier update may already have committed, inspect the result before repeating it.

## 6. Maintain results in the right place

Implementation, tests, and experiments remain in the project. An independently reusable search component receives a tool entry. Newly confirmed facts about formats or location semantics enter the knowledge base. A method becomes a skill when repeated use establishes its value. Project records update the current output, unfinished scope, and next action; intermediate outputs are handled within the authorized scope.

This example first addresses querying and source navigation. Attachments, automatic updates, and semantic queries remain future capabilities. A working initial path does not complete them. MCP or continuing scheduling should be added in response to an actual need for external invocation or task dispatch.
