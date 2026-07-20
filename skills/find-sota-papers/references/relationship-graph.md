# Relationship graph

Read this file in Step 11 only when `relationship_graph` is enabled.

Map relationships among selected papers plus any included classic work. Add no
new paper during this step.

## Retrieve edges

Prefer already-fetched reference data. When POST is available, one Semantic
Scholar batch may retrieve up to 500 selected IDs:

```text
POST https://api.semanticscholar.org/graph/v1/paper/batch?fields=title,externalIds,references.paperId,citations.paperId
     body: {"ids":["ARXIV:2503.01234", ...]}
```

Without POST, use per-paper GET endpoints for the most relevant papers and mark
unverified portions `unknown`. Never imply complete graph coverage after a
partial fallback.

## Allowed relationships

- `A --cites--> B`: fetched citation/reference data shows A cites B.
- `A --builds-on--> B ("supporting phrase")`: A's fetched text explicitly says
  it extends, builds on, or is based on B. A citation alone is insufficient.
- **Separate tracks:** connected components with no edge between them; this is a
  graph observation, not a new paper-level claim.

## Output

1. Name the connected components and map `P1...Pn` to selected-paper titles;
   use `C1`/`C2` for classic works.
2. Emit a plain-text edge list, one edge per line.
3. Optionally add Mermaid, but never as the only representation.

Paper IDs follow their order under `## Papers`. Do not use the
`**[Title](url)**` shape on edge lines because the evaluation fallback interprets
that shape as another paper. State plainly when the graph is sparse, incomplete,
or empty.
