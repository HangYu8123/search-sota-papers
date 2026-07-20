# Multi-agent orchestration contracts

Read this file before creating discovery or validation workers. The main agent
owns constraints, coverage, deduplication, conflict resolution, ranking, and the
only final report.

## Preference and recovery

- `no`: create no workers; run every lane sequentially.
- `auto`: use workers only when the host provides them and at least two
  independent lanes are useful.
- `yes`: attempt bounded parallel work; if unavailable, state the fallback once
  and run the same lanes sequentially.

Use normally 2–4 independent lanes. Wait at discovery and validation barriers.
If a worker is missing, shallow, or failed, rerun only its assignment
sequentially. Inline roleplay is not parallel work.

## Discovery worker contract

Give every worker normalized constraints, one distinct objective, source
priorities, target count, explicit query/fetch/time budget, saturation rule, and
the search requirements from `references/search-depth.md`. Require live search
and fetch; a worker without them returns an empty ledger and the reason.

Workers return compact rows, not prose:

```text
lane_id | queries_and_sources_checked | candidate_id | title | authors | venue |
date | canonical_url | citation_count | citation_source |
citation_evidence_url | sota_evidence_urls | content_evidence_urls | intuition |
contribution | setup | results_vs_baselines | relevance_note |
unresolved_conflicts
```

Use a versionless arXiv ID, lowercase DOI, or normalized-title fallback as
`candidate_id`. A factual field without a fetched evidence URL is `unknown`.
Workers do not rank globally or write user-facing lists.

## Validation worker contract

The main agent assigns every provisionally retained candidate:

1. canonical identity plus title/author match;
2. bibliographic metadata and a citation count from a citation-bearing source;
3. SOTA, benchmark, setup, baseline, and result claims from the paper or an
   official project/venue/benchmark page;
4. affiliation retrieval only when `institutions == reputable`.

Each verdict must name the fetched URL for every completed check. Return:

```text
assignment_id | candidate_id | checks_completed | canonical_evidence_url |
citation_count_and_source | citation_evidence_url | sota_evidence_urls |
content_evidence_urls | affiliations_found | affiliation_evidence_url |
verdict(LIVE|DROP|CONFLICT) | reason
```

Source failures produce `CONFLICT`, never a familiarity-based verdict. Re-fetch
when sources disagree; otherwise retain `unknown` and drop a paper only when a
required identity, hard threshold, or SOTA claim cannot be established.

Before ranking, compare returned IDs and evidence fields against the coverage
manifest and finish missing checks sequentially. A wholly incomplete lane makes
the search blocked/incomplete; one candidate with failed mandatory validation is
`DROP` with a concrete reason.
