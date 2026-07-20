# Search depth and coverage gates

Read this file before Step 2. Apply the same search requirements in parallel and
sequential execution.

## Deepening loop

For every discovery lane:

1. **Seed:** run at least three materially different queries: user wording,
   canonical field terminology, and benchmark/method terminology.
2. **Harvest:** extract method, architecture, benchmark, dataset, task, author,
   venue, and arXiv-category vocabulary from fetched results.
3. **Refine:** run at least three new queries using harvested vocabulary.
4. **Snowball:** for the strongest 3–5 candidates, inspect citations and
   references to find newer work and possible classic ancestors.
5. **Saturate:** stop only after two consecutive rounds add no candidate or an
   explicit lane budget is reached. Record the budget and saturation reason.

Search snippets select pages to open; they never support final claims.

## Effort floors

| Scope | Searches | Fetches | Rounds |
|---|---:|---:|---:|
| Each discovery lane | 6 | 5 | 2 plus snowballing |
| Whole task, `num_papers <= 10` | 10 | 15 | — |
| Whole task, default `num_papers ~= 30` | 20 | 40 | — |
| Whole task, `num_papers >= 50` | 30 | 70 | — |

These are floors, not targets. Set a maximum query/fetch/time budget per lane in
the discovery manifest so a broad request cannot run without a bound. If the
user requests an impractically large list, state a safe batch size and complete
that batch rather than silently weakening validation.

## Discovery floor

After deduplication in Step 4, require:

```text
merged >= 3 * num_papers
merged >= 4 * num_papers when institutions == reputable
```

`merged` counts unique candidates, not repeated lane hits. If below the floor,
return to discovery. Proceed below it only after all three conditions hold:

1. two additional rounds ran after missing the floor;
2. those rounds used at least two new phrasings and two previously untried
   sources;
3. they produced no candidate.

Record this escape under Coverage & limitations. Missing the floor without the
escape is under-searching, not demonstrated scarcity.

## Query craft

- Search method, comparison, benchmark, venue, and current-year phrasings.
- Include site-scoped arXiv/venue/project queries alongside open-web queries.
- Search both old and new names for a renamed subfield.
- Treat a thin source response as a query/source problem until at least two
  sources and two phrasings agree.
