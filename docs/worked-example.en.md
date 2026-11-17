# An example: add search to a local document browser

[Main article](../README.en.md) · [中文](worked-example.zh-CN.md)

Here is a hypothetical example of how the workflow could be used. The application and results are illustrative; this repository does not implement it.

## Start with the request

Suppose I already have a document browser that opens local folders. The collection has grown, so I ask an agent: “Add search. Maybe use a vector database, and get a few agents working on it.”

I want documents to be easier to find. After looking at the collection, the agent finds mostly text and Markdown. I usually search by terms, filenames, and exact phrases. There are also attachments the application cannot read yet. The documents need to stay local.

We could reuse the existing reader, add full-text search, and make results open the original text. Queries that keywords handle poorly can inform a later comparison with semantic search. Attachments, automatic updates, and duplicates stay on the list while we connect the first complete search path.

## Check what we already have

The agent can look in the tool registry for readers, search interfaces, and ways to interact with the page. The knowledge library may explain encoding and format issues. Read relevant skills when needed. The project record provides the current version, entry point, and previous decisions.

If the registry has no match, continue into the code or public libraries. Try candidate components on a few documents and check whether their results fit the current page. Keep unreadable inputs and original errors available for investigation.

## Agree on how the pieces will connect

Assume indexing and the results panel can be developed separately. One agent handles reading, indexing, and queries; another works on the page.

They first need to agree on what a result contains: file identity, match location, an excerpt, and which documents the query covered. The exact fields depend on the application. Workers can discuss location formats directly and record the decision with the project.

They can edit different files and use separate development indexes. The agent bringing the pieces together updates the main application, avoiding concurrent writes to one index. A small job could stay with one agent instead.

The indexing assignment might read:

> Add full-text search to the current document browser. Start with text and Markdown in the user-selected directory, keep originals read-only, and reuse the existing reader and search capabilities. Return snippets and original locations so the page can open a match. You own the search module and relevant tests; discuss shared interface changes with the page worker. Deliver the changes, run instructions, and results from a few representative documents. Explain which inputs could not be read. Replace a candidate component if it doesn't fit, and leave the reason.

That should be enough to start. The assignment doesn't need the entire search history.

## Connect it to the page

Once indexing returns results, connect it to the panel. Search for a term and open a match. Does it show the right file at the right location? This checks whether both sides interpret a position the same way.

Then change a sample document, refresh, and search again. Is the new content searchable? Have old positions updated? If navigation lands on the wrong line, follow file reading, index positions, transport, and page navigation to find the first error.

If attachments remain unreadable, explain which documents the query covered. Missing results can still be investigated; they do not prove that the content is absent from the whole collection.

## Leave enough to resume

A short note could say:

> Goal: search locally and return to the original text. Keyword results are connected to the page; this delivery links the changes and run instructions. Start with full-text search and compare semantic retrieval if real queries need it. Attachments and automatic updates remain. Next, check reindexing after a file change through the existing refresh entry point. Development copies have separate indexes; the integrator updates the main index. Checks and input versions are in the record.

In a real project, use actual files and links. The next conversation checks what is there and continues with unfinished work, avoiding duplicate writes and reruns.

## Put useful results back where they belong

Implementation and tests stay in the project. If a reusable search component emerges, add its entry to the tool registry. Confirmed discoveries about encoding or formats go in the knowledge library. A method that repeatedly helps may become a skill. The project record keeps the current conclusion and next step. One-off indexes and intermediate output can be cleaned up within the task's scope.

Afterward, see what still takes too much effort. A need for ongoing dispatch or another programmatic client can inform whether to add orchestration or MCP support.
