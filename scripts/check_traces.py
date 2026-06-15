#!/usr/bin/env python3
"""Deterministic traceability + structure validator for the Expectationeering workbook.

Runs the MECHANICAL part of the Quality Assurance audit as a plain script — zero
model tokens. It checks exactly the class of findings the QA loop otherwise spends
~250k tokens on per full-workbook read:

  * every Traces reference points to an ID that actually exists (no dangling refs)
  * every traced item points to an ALLOWED upstream prefix (per the flow DAG)
  * every item that requires an upstream trace has one
  * every RQ_FN_* is covered by an SV feature file (an @ID:RQ_FN_xx gherkin tag)
  * every DC_* gap is addressed by at least one expectation
  * ID sequences per prefix have no duplicates or gaps
  * no fill-in placeholders are left behind

Semantic INCOSE quality (clarity, atomicity, verifiability, SMART-ness) is NOT
checked here — that is the job of the Quality Assurance agent, which should run
only after this script returns clean.

Usage:
    python scripts/check_traces.py <workbook.md> [--json]

Exit code 0 = no errors (warnings allowed), 1 = at least one error.
"""
import re
import sys
import json
from collections import defaultdict

# prefix -> list of allowed upstream prefixes. [] marks a root (no upstream trace).
# Prefixes NOT in this map (IU_, IF_) are valid trace TARGETS but are not
# themselves trace-validated (they are roots of the solution domain).
RULES = {
    "DC_":         [],
    "UE_":         ["DC_"],
    "ME_":         ["DC_"],
    "BE_":         ["DC_"],
    "RE_":         ["DC_"],
    "KA_":         ["UE_", "ME_", "BE_", "RE_"],
    "BR_":         ["KA_"],
    "MD_":         ["IU_"],
    "UR_":         ["IU_", "BR_"],
    "USER_DFMEA_": ["UR_"],
    "UT_":         ["UR_"],
    "UFMEA_":      ["UT_"],
    "USR_":        ["UR_", "UFMEA_"],
    "UC_":         ["UT_", "UR_"],
    "DD_":         ["UC_", "BR_"],
    "RQ_IF_":      ["IF_"],
    "RQ_FN_":      ["UC_", "UR_"],
    "RQ_PR_":      ["RQ_FN_"],
    "RQ_NF_":      ["BR_", "RE_"],
    "RQ_CS_":      ["RE_"],
}
# longest prefix first, so RQ_FN_ wins over a hypothetical RQ_ and
# USER_DFMEA_ is never shadowed by a shorter key.
PREFIXES = sorted(RULES, key=len, reverse=True)

ID_RE = re.compile(r"(?:[A-Z]+_)+\d+")
ROW_ID_RE = re.compile(r"^((?:[A-Z]+_)+\d+)$")

# Comments that are part of the template by design and must NOT be flagged as
# unfilled placeholders.
INTENTIONAL_COMMENT = ("Not filled by this flow", "====", "white-box", "Per-item",
                       "sequence diagrams", "Design FMEA")


def rule_prefix(id_):
    """Return the RULES key this ID belongs to, or None."""
    return next((p for p in PREFIXES if id_.startswith(p)), None)


def any_prefix(id_):
    """Best-effort prefix for grouping IDs that have no rule (IF_, IU_, ...)."""
    p = rule_prefix(id_)
    if p:
        return p
    m = re.match(r"((?:[A-Z]+_)+)", id_)
    return m.group(1) if m else id_


def parse(md):
    ids = set()
    traces = {}                       # id -> set(upstream ids it cites)
    sv_targets = set(re.findall(r"@ID:\s*(RQ_FN_\d+)", md))

    for row in re.findall(r"^\|.*\|$", md, re.M):
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        if not cells:
            continue
        m = ROW_ID_RE.match(cells[0])
        if not m:                     # header / separator / non-ID row
            continue
        id_ = cells[0]
        ids.add(id_)

        # Where the trace IDs live depends on the table:
        #  - KA_ has NO Traces column; the upstream expectation is named in the row.
        #  - UC_ carries Satisfies (UR_) in a middle column plus Traces last.
        #  - everything else: the last column is Traces.
        if id_.startswith("KA_"):
            refs = set(re.findall(r"(?:UE|ME|BE|RE)_\d+", row))
        elif id_.startswith("UC_"):
            refs = set(ID_RE.findall(cells[-1])) | set(re.findall(r"UR_\d+", row))
        else:
            refs = set(ID_RE.findall(cells[-1]))
        refs.discard(id_)
        traces[id_] = refs

    return ids, traces, sv_targets


def validate(md):
    ids, traces, sv = parse(md)
    findings = []

    def add(sev, where, msg):
        findings.append({"severity": sev, "id": where, "msg": msg})

    for id_, refs in traces.items():
        rule = rule_prefix(id_)
        if rule is None:              # IF_/IU_ etc — valid target, not validated
            continue
        allowed = RULES[rule]

        # dangling references
        for r in refs:
            if r not in ids:
                add("error", id_, f"traces to {r} which does not exist in the workbook")

        if not allowed:               # root table (DC_) — no trace required
            continue

        if not refs:
            add("error", id_, f"has no upstream trace (must trace to {'/'.join(allowed)})")
        else:
            for r in refs:
                if not any(r.startswith(a) for a in allowed):
                    add("error", id_,
                        f"traces to {r}, but allowed upstream is {'/'.join(allowed)}")

    # every RQ_FN_* needs an SV feature file
    for id_ in sorted(ids):
        if id_.startswith("RQ_FN_") and id_ not in sv:
            add("error", id_, "no SV feature file (@ID tag) covers this functional requirement")

    # orphan gaps: a DC_ no expectation traces to
    cited = {r for refs in traces.values() for r in refs}
    for id_ in sorted(ids):
        if id_.startswith("DC_") and id_ not in cited:
            add("warning", id_, "gap is not addressed by any expectation")

    # ID sequence: duplicates and gaps per prefix
    seq = defaultdict(list)
    for id_ in ids:
        seq[any_prefix(id_)].append(int(id_.rsplit("_", 1)[1]))
    for p, nums in sorted(seq.items()):
        if len(nums) != len(set(nums)):
            dupes = sorted({n for n in nums if nums.count(n) > 1})
            add("error", p, f"duplicate IDs: {[f'{p}{n:02d}' for n in dupes]}")
        gaps = [n for n in range(1, max(nums) + 1) if n not in nums]
        if gaps:
            add("warning", p, f"ID sequence gaps: {[f'{p}{n:02d}' for n in gaps]}")

    # leftover fill-in placeholders
    for ph in re.findall(r"<!--.*?-->", md, re.S):
        if any(tok in ph for tok in INTENTIONAL_COMMENT):
            continue
        flat = " ".join(ph.split())
        add("warning", "template", f"unfilled placeholder remains: {flat[:60]}")

    return findings


def main():
    args = sys.argv[1:]
    as_json = "--json" in args
    paths = [a for a in args if not a.startswith("--")]
    if not paths:
        print("usage: python scripts/check_traces.py <workbook.md> [--json]", file=sys.stderr)
        return 2

    md = open(paths[0], encoding="utf-8").read()
    findings = validate(md)

    if as_json:
        print(json.dumps(findings, indent=2))
    else:
        for f in findings:
            print(f"[{f['severity'].upper()}] {f['id']}: {f['msg']}")
        errors = sum(1 for f in findings if f["severity"] == "error")
        warnings = len(findings) - errors
        if findings:
            print(f"\n{errors} error(s), {warnings} warning(s).")
        else:
            print("PASS - no structural or traceability findings.")

    return 1 if any(f["severity"] == "error" for f in findings) else 0


if __name__ == "__main__":
    sys.exit(main())
