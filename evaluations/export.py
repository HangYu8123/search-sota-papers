#!/usr/bin/env python3
"""Project ``evaluations/*.json`` into the training views described in EVALUATION.md.

    python evaluations/export.py               # write evaluations/exports/*.jsonl
    python evaluations/export.py --stats       # summary only, write nothing

Four views, all derived — never hand-edit them, re-run this instead:

    preference.jsonl    {prompt, chosen, rejected}           TRL / OpenAI DPO
    rubric_reward.jsonl {prompt, completion, reward, ...}    reward-model / RaR
    items.jsonl         per-paper relevance labels           ranking stage
    verifiable.jsonl    binary checks                        RLVR slice

A vetoed record (fabricated citation) may appear as ``rejected`` but never as
``chosen`` and never as a positive reward row. That is the one asymmetry worth
hard-coding: the failure this skill exists to prevent must not become the
behavior a preference pair teaches.
"""

import argparse
import itertools
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RESULTS_DIR = os.path.join(ROOT, "results")
EXPORT_DIR = os.path.join(HERE, "exports")

# Below this reward gap two runs are treated as indistinguishable. Pairs closer
# than this teach noise: the difference is inside rater precision, not skill.
DEFAULT_MARGIN = 0.05


def load_records():
    records = []
    for name in sorted(os.listdir(HERE)):
        if not name.endswith(".json"):
            continue
        path = os.path.join(HERE, name)
        try:
            with open(path, "r", encoding="utf-8") as handle:
                record = json.load(handle)
        except (OSError, ValueError) as exc:
            print("  skipped {}: {}".format(name, exc), file=sys.stderr)
            continue
        if record.get("schema") != "find-sota-papers/eval@1":
            print("  skipped {}: not eval@1".format(name), file=sys.stderr)
            continue
        record["_file"] = name
        records.append(record)
    return records


def report_body(run_id):
    """The result file's markdown minus its frontmatter — the 'completion'."""
    path = os.path.join(RESULTS_DIR, run_id + ".md")
    if not os.path.isfile(path):
        return None
    with open(path, "r", encoding="utf-8") as handle:
        text = handle.read()
    return re.sub(r"^---\r?\n.*?\r?\n---\r?\n", "", text, count=1, flags=re.S).strip()


def prompt_of(record):
    run = record.get("run") or {}
    if run.get("prompt"):
        return run["prompt"].strip()
    constraints = run.get("constraints") or {}
    parts = [
        "Find the SOTA papers.",
        "Field: {}".format(constraints.get("field")),
        "Topics: {}".format(constraints.get("topics")),
        "SOTA requirements: {}".format(constraints.get("sota_requirements")),
    ]
    return "\n".join(p for p in parts if "None" not in p)


def topic_key(record):
    constraints = (record.get("run") or {}).get("constraints") or {}
    raw = "{} {}".format(constraints.get("field") or "", constraints.get("topics") or "")
    return re.sub(r"[^a-z0-9]+", "-", raw.lower()).strip("-")


def reward_of(record):
    return ((record.get("reward") or {}).get("scalar"))


def vetoed(record):
    return bool((record.get("reward") or {}).get("veto"))


def build_preference(records, margin):
    """Explicit rater verdicts first; reward-gap pairs fill in the rest."""
    rows, seen = [], set()

    def emit(winner, loser, source):
        key = tuple(sorted([winner["run_id"], loser["run_id"]]))
        if key in seen or winner["run_id"] == loser["run_id"]:
            return
        if vetoed(winner):
            return
        chosen, rejected = report_body(winner["run_id"]), report_body(loser["run_id"])
        if not chosen or not rejected:
            return
        seen.add(key)
        rows.append({
            "prompt": prompt_of(winner),
            "chosen": chosen,
            "rejected": rejected,
            "meta": {
                "chosen_run": winner["run_id"],
                "rejected_run": loser["run_id"],
                "source": source,
                "chosen_reward": reward_of(winner),
                "rejected_reward": reward_of(loser),
            },
        })

    by_run = {r["run_id"]: r for r in records}
    for record in records:
        preference = record.get("preference") or {}
        other_id, verdict = preference.get("vs_run"), preference.get("verdict")
        other = by_run.get(other_id)
        if not other or verdict not in ("this", "other"):
            continue
        if verdict == "this":
            emit(record, other, "stated")
        else:
            emit(other, record, "stated")

    groups = {}
    for record in records:
        groups.setdefault(topic_key(record), []).append(record)
    for group in groups.values():
        for a, b in itertools.combinations(group, 2):
            ra, rb = reward_of(a), reward_of(b)
            if ra is None or rb is None or abs(ra - rb) < margin:
                continue
            emit(*( (a, b) if ra > rb else (b, a) ), "reward-gap")
    return rows


def build_rubric_reward(records):
    rows = []
    for record in records:
        completion = report_body(record["run_id"])
        if not completion:
            continue
        reward = record.get("reward") or {}
        rows.append({
            "prompt": prompt_of(record),
            "completion": completion,
            "reward": reward.get("scalar"),
            "components": reward.get("components") or [],
            "veto": bool(reward.get("veto")),
            "meta": {
                "run_id": record["run_id"],
                "rater": record.get("rater"),
                "lead_time_s": record.get("lead_time_s"),
                "cost": (record.get("run") or {}).get("cost"),
            },
        })
    return rows


def build_items(records):
    rows = []
    for record in records:
        prompt = prompt_of(record)
        for item in record.get("items") or []:
            if not item.get("label"):
                continue
            rows.append({
                "prompt": prompt,
                "run_id": record["run_id"],
                "candidate_id": item.get("candidate_id"),
                "title": item.get("title"),
                "url": item.get("url"),
                "label": item.get("label"),
                "link_ok": item.get("link_ok"),
                "flags": item.get("flags") or [],
            })
    return rows


def build_verifiable(records):
    rows = []
    for record in records:
        prompt = prompt_of(record)
        for check, value in (record.get("checks") or {}).items():
            if value is None:
                continue
            rows.append({
                "prompt": prompt,
                "run_id": record["run_id"],
                "check": check,
                "pass": bool(value),
            })
    return rows


def write_jsonl(name, rows):
    os.makedirs(EXPORT_DIR, exist_ok=True)
    path = os.path.join(EXPORT_DIR, name)
    with open(path, "w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    print("  {:<22} {:>5} rows -> {}".format(name, len(rows), os.path.relpath(path, ROOT)))


def print_stats(records):
    rewards = [reward_of(r) for r in records if reward_of(r) is not None]
    print("  records        {}".format(len(records)))
    print("  runs           {}".format(len({r["run_id"] for r in records})))
    print("  raters         {}".format(len({r.get("rater") for r in records})))
    print("  vetoed         {}".format(sum(1 for r in records if vetoed(r))))
    if rewards:
        rewards.sort()
        mid = rewards[len(rewards) // 2]
        print("  reward         min {:.3f} · median {:.3f} · max {:.3f}".format(
            rewards[0], mid, rewards[-1]))
    # Cost is reported next to quality, never folded into it — see EVALUATION.md.
    priced = [
        (reward_of(r), (r.get("run") or {}).get("cost", {}).get("tokens_total"))
        for r in records
    ]
    priced = [(a, b) for a, b in priced if a is not None and isinstance(b, int)]
    if priced:
        print("  reward vs tokens:")
        for reward, tokens in sorted(priced, key=lambda p: -p[0]):
            print("    {:.3f}  {:>10,} tokens".format(reward, tokens))


def main():
    parser = argparse.ArgumentParser(description="Export evaluation records to training views.")
    parser.add_argument("--margin", type=float, default=DEFAULT_MARGIN,
                        help="Minimum reward gap for an inferred preference pair "
                             "(default: {}).".format(DEFAULT_MARGIN))
    parser.add_argument("--stats", action="store_true", help="Print a summary and exit.")
    args = parser.parse_args()

    records = load_records()
    if not records:
        sys.exit("No eval@1 records in {} yet.".format(os.path.relpath(HERE, ROOT)))

    print("Loaded {} record(s).\n".format(len(records)))
    print_stats(records)
    if args.stats:
        return

    print("\nExports:")
    write_jsonl("preference.jsonl", build_preference(records, args.margin))
    write_jsonl("rubric_reward.jsonl", build_rubric_reward(records))
    write_jsonl("items.jsonl", build_items(records))
    write_jsonl("verifiable.jsonl", build_verifiable(records))


if __name__ == "__main__":
    main()
