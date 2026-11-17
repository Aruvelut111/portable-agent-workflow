# Worked example: add search to a local document browser

[Main article](../README.en.md) · [中文](worked-example.zh-CN.md)

This is a hypothetical example of the workflow. Files, tasks, and conclusions are illustrative. This repository does not implement or test the application described here.

## Derive an implementable direction

The user says: “My documents are growing. I want AI to help me search them. I heard vector databases are good; start a few agents and build it.”

The integration owner first examines the application and the documents. Assume there is already a folder browser, most material is text and Markdown, and the user often searches for terms, filenames, and phrases before opening the original. Some attachments cannot yet be read. Documents should remain on the machine.

The current recommendation is to reuse file-reading logic and an established full-text search capability, then add keyword search, original-text navigation, and coverage information to the browser. Compare semantic search later if actual queries reveal a gap. The user's example informed the investigation without making a particular database the goal.

The first path ends with a person entering a term, seeing a match, and opening the correct original location. Attachment reading, incremental updates, duplicate documents, and semantic queries remain visible needs. The first path does not complete the whole request.

## What to retrieve from the library

The owner looks up material relevant to the current problem:

- The capability registry: actual invocation and limitations of existing readers, search interfaces, and interface checks.
- The knowledge library: confirmed facts about formats, encoding, and indexing coverage.
- Reusable procedures: only the import or delivery methods needed now.
- The project ledger: the application's current version, decisions, runtime entry point, and related work.

If an entry is not found, continue into the project code or public libraries. A failed lookup describes that lookup's result. When a candidate component is found, check that it processes the chosen input and produces something the current interface can consume.

## Arrange collaboration

Assume two pieces can progress independently: one worker investigates and connects indexing; another builds the results panel. The owner establishes shared result semantics, then assigns non-overlapping file scopes.

The consumer needs to understand original-file identity, match location, snippet, and search coverage. The full set of fields depends on the application. Workers can discuss position representation directly and communicate decisions affecting the public interface to the owner.

Each working copy uses an independent index file. The owner updates the main application during integration. This isolates runtime data as well as code and avoids two processes modifying one index. For a small task, the owner can implement the whole change directly.

## An actionable task description

> Connect the existing full-text search capability to the current document browser so that selected text and Markdown documents return snippets and original locations. Use the current project entry point and user-selected directory; keep original documents read-only. Change the search module and its existing tests. Coordinate changes to the public result interface with the integration owner. Deliver a callable implementation, actual changes, and reproduction instructions. Completion means representative inputs can be searched, the results panel can consume locations, and unreadable inputs have explicit coverage information. You may replace a candidate component; record the reason in the current project record.

The description establishes the goal and boundaries while leaving implementation choices to the executor. It does not copy the whole research history into the task.

## Reach the actual consumer

After the indexing worker reports that the interface returns results, the owner connects it to the real panel. Clicking a result and checking its original location is a discriminating check that covers both identity and interface consumption.

Choose a meaningful variation next: change a sample document and refresh. Check that the new text is searchable and that old positions update. If navigation is wrong, trace file reading, index position encoding, interface transport, and panel interpretation to the earliest divergence. Avoid compensating for a source error with a display offset.

If attachments were unreadable, the interface should accurately state search coverage. The owner retains attachment support as remaining work. An empty result cannot be reported as proof that the content is absent from all documents.

## What to save at interruption

A short handoff might read:

> Goal: search documents locally and navigate to originals. The current implementation and runtime entry point are in this delivery; keyword results are connected to the panel. Decision: start with full-text search, then compare extensions if actual queries expose a semantic gap. Confirmed checks and input versions are linked in the corresponding record. Remaining work: attachment coverage and incremental updates. Next: connect one file-change event through the existing refresh entry point and verify that old positions update in the same document. Development copies have independent indexes; the integrator updates the main index.

The actual record must link real artifacts and checks, rather than retain this illustrative text alone. A successor inspects the current implementation. If the earlier write committed, continue from the unfinished action.

## What remains after completion

Implementation and relevant tests stay in the project. A reusable search component warrants a capability-registry update. Confirmed new format facts belong in the knowledge library. Only a repeatedly useful integration method becomes a skill. The ledger retains current conclusions and next work. Clean up one-off indexes and intermediate output within the task's scope.

The example does not require a unified platform, an MCP release, or a fixed template for every record. Each added structure should explain which repetition or error it reduces.
