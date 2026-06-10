#!/usr/bin/env python3
"""Build the 1000+ paper literature matrix for Paper 03.

The script uses OpenAlex because it exposes broad public scholarly metadata
without an API key. The extraction fields are conservative heuristic summaries
from titles, abstracts, and concept tags; later documents use these as a map,
not as a substitute for close reading.
"""

from __future__ import annotations

import csv
import json
import math
import re
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CACHE = ROOT / "results" / "openalex_cache.jsonl"
OUT = DOCS / "related_work_matrix.csv"

TARGET_MIN = 1050
PER_QUERY = 120
PAGE_SIZE = 40

QUERIES = [
    "robot world model",
    "robotics world models planning control",
    "embodied world model robot manipulation",
    "action conditioned video prediction robotics",
    "visual foresight robot manipulation",
    "learned dynamics model robot control",
    "latent dynamics robot manipulation",
    "object centric world models robotics",
    "model predictive control learned dynamics robot",
    "model based reinforcement learning robotics dynamics model",
    "robot dynamics model adaptation online",
    "online system identification robot control",
    "residual dynamics learning robotics",
    "sim to real robot dynamics adaptation",
    "model error robot planning",
    "model error detection robot control",
    "model repair planning robotics",
    "predictive coding robot control world model",
    "tactile world model robot manipulation",
    "3D scene dynamics robot manipulation world model",
    "physical reasoning robot learning dynamics",
    "robot foundation model world model planning",
    "large world models embodied agents robotics",
    "causal world model robot manipulation",
    "affordance dynamics model robot manipulation",
    "contact dynamics learning robot manipulation",
    "deformable object dynamics robot learning",
    "legged robot learned dynamics adaptation",
    "robot skill adaptation model error",
    "test time adaptation robot dynamics model",
    "continual learning robot dynamics model",
    "active perception robot world model planning",
    "differentiable physics robot model learning",
    "hybrid analytical learned dynamics robotics",
]

ROBOTICS_HINTS = {
    "robot",
    "robotic",
    "robotics",
    "manipulation",
    "grasp",
    "grasping",
    "locomotion",
    "control",
    "planning",
    "sim-to-real",
    "sim to real",
    "dynamics",
    "tactile",
    "embodied",
    "world model",
    "affordance",
    "contact",
    "mpc",
}

MECHANISM_PATTERNS = [
    (r"\b(video prediction|visual foresight|frame prediction)\b", "action-conditioned visual prediction / visual foresight"),
    (r"\b(model predictive control|mpc)\b", "planning by rolling out a learned or hybrid dynamics model"),
    (r"\b(system identification|parameter identification)\b", "online or offline identification of dynamics parameters"),
    (r"\b(residual|error model)\b", "residual correction on top of a nominal model"),
    (r"\b(latent dynamics|latent space|representation learning)\b", "latent-state dynamics learning"),
    (r"\b(object[- ]centric|object centric)\b", "object-centric state factorization"),
    (r"\b(diffusion|transformer|foundation|large language|large model)\b", "large generative/foundation model conditioning"),
    (r"\b(contact|tactile|force)\b", "contact/tactile dynamics modeling"),
    (r"\b(sim[- ]to[- ]real|domain randomization|transfer)\b", "simulation-to-real transfer or domain randomization"),
    (r"\b(reinforcement learning|policy gradient|q-learning)\b", "reinforcement-learning objective around a learned model"),
    (r"\b(bayesian|uncertainty|ensemble)\b", "uncertainty-aware model estimation"),
    (r"\b(causal|counterfactual)\b", "causal or counterfactual structure learning"),
]

ASSUMPTION_PATTERNS = [
    (r"\b(video prediction|frame prediction|reconstruction)\b", "better prediction loss implies better embodied decisions"),
    (r"\b(mpc|planning|rollout)\b", "model errors remain tolerable over the planner horizon"),
    (r"\b(system identification|parameter identification)\b", "the right repair is expressible as global parameter adaptation"),
    (r"\b(residual)\b", "a smooth additive residual can absorb the important physical mismatch"),
    (r"\b(latent)\b", "the learned latent variables preserve the repair-relevant causal factors"),
    (r"\b(object[- ]centric|scene graph)\b", "objects and relations are separable and persist through contact"),
    (r"\b(uncertainty|bayesian|ensemble)\b", "epistemic uncertainty is calibrated enough to guide action"),
    (r"\b(sim[- ]to[- ]real|domain randomization)\b", "training variation covers deployment mismatches"),
    (r"\b(reinforcement learning)\b", "reward feedback is the main signal for correcting model use"),
    (r"\b(large|foundation|transformer|diffusion)\b", "scale transfers to local physical counterfactual repair"),
]

FAILURE_PATTERNS = [
    (r"\b(contact|tactile|force|deformable|friction|slip)\b", "localized contact/friction failures under action"),
    (r"\b(occlusion|partial observability|latent)\b", "unobserved variables changing repair validity"),
    (r"\b(long horizon|rollout|planning)\b", "planner exploitation of small model errors"),
    (r"\b(sim[- ]to[- ]real|domain)\b", "out-of-distribution deployment mismatch"),
    (r"\b(human|language|foundation)\b", "semantic priors overriding physical evidence"),
    (r"\b(uncertainty|ensemble)\b", "miscalibrated confidence around rare failures"),
]


def openalex_get(url: str, retries: int = 4) -> dict[str, Any]:
    for attempt in range(retries):
        try:
            req = urllib.request.Request(
                url,
                headers={
                    "User-Agent": "paper03-literature-bot/1.0 (mailto:anonymous@example.com)",
                    "Accept": "application/json",
                },
            )
            with urllib.request.urlopen(req, timeout=45) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except Exception as exc:  # noqa: BLE001
            if attempt == retries - 1:
                return {"error": repr(exc), "results": []}
            time.sleep(2.0 + attempt)
    return {"results": []}


def abstract_from_inverted(index: dict[str, list[int]] | None) -> str:
    if not index:
        return ""
    positions: list[tuple[int, str]] = []
    for word, locs in index.items():
        for loc in locs:
            positions.append((loc, word))
    positions.sort()
    return " ".join(word for _, word in positions)


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "").replace("\x00", " ")).strip()


def first_sentence(text: str, fallback: str) -> str:
    text = clean(text)
    if not text:
        return fallback
    bits = re.split(r"(?<=[.!?])\s+", text)
    return clean(bits[0])[:360] or fallback


def concepts(work: dict[str, Any]) -> str:
    names = []
    for c in work.get("concepts") or []:
        name = c.get("display_name")
        score = c.get("score")
        if name and score is not None and score >= 0.25:
            names.append(name)
    for c in work.get("topics") or []:
        name = c.get("display_name")
        if name:
            names.append(name)
    seen = []
    for name in names:
        if name not in seen:
            seen.append(name)
    return "; ".join(seen[:12])


def authors(work: dict[str, Any]) -> str:
    out = []
    for a in work.get("authorships") or []:
        name = ((a.get("author") or {}).get("display_name") or "").strip()
        if name:
            out.append(name)
    return "; ".join(out[:8])


def venue(work: dict[str, Any]) -> str:
    loc = work.get("primary_location") or {}
    source = loc.get("source") or {}
    return source.get("display_name") or ""


def doi(work: dict[str, Any]) -> str:
    raw = work.get("doi") or ""
    return raw.replace("https://doi.org/", "")


def url(work: dict[str, Any]) -> str:
    loc = work.get("primary_location") or {}
    landing = loc.get("landing_page_url") or ""
    return landing or work.get("id") or ""


def text_blob(row: dict[str, str]) -> str:
    return " ".join([row.get("title", ""), row.get("abstract", ""), row.get("concepts", "")]).lower()


def choose(patterns: list[tuple[str, str]], blob: str, default: str) -> str:
    hits = []
    for pattern, label in patterns:
        if re.search(pattern, blob, flags=re.I):
            hits.append(label)
    if not hits:
        return default
    seen = []
    for hit in hits:
        if hit not in seen:
            seen.append(hit)
    return "; ".join(seen[:3])


def infer_problem(row: dict[str, str]) -> str:
    blob = text_blob(row)
    title = row["title"]
    if re.search(r"manipulat|grasp|contact|tactile|deform", blob):
        return "Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions."
    if re.search(r"locomot|legged|walking|quad", blob):
        return "Model robot-body/environment dynamics well enough for adaptive locomotion control."
    if re.search(r"sim[- ]to[- ]real|domain", blob):
        return "Transfer a learned or simulated dynamics/action model from source conditions to deployment."
    if re.search(r"planning|mpc|control", blob):
        return "Use a learned or hybrid world/action model to improve planning or control."
    if re.search(r"video|visual|image|frame", blob):
        return "Predict visual consequences of robot actions as a proxy for embodied world modeling."
    return f"Advance embodied world/dynamics modeling around: {title[:140]}."


def infer_mechanism(row: dict[str, str]) -> str:
    return choose(
        MECHANISM_PATTERNS,
        text_blob(row),
        "task-specific learned dynamics, representation, or planning model",
    )


def infer_assumptions(row: dict[str, str]) -> str:
    return choose(
        ASSUMPTION_PATTERNS,
        text_blob(row),
        "the selected training objective exposes the deployment-critical model errors",
    )


def infer_fixed(row: dict[str, str]) -> str:
    blob = text_blob(row)
    fixed = []
    if "friction" not in blob and re.search(r"manipulat|contact|grasp", blob):
        fixed.append("contact/friction regime")
    if not re.search(r"online|adapt|continual|test time|repair", blob):
        fixed.append("model structure during deployment")
    if not re.search(r"planner|planning|control|mpc", blob):
        fixed.append("downstream planner/controller response to model errors")
    if not re.search(r"partial|occlusion|latent|belief", blob):
        fixed.append("observability of repair-relevant state")
    if not fixed:
        fixed.append("which variables are repairable versus merely predicted")
    return "; ".join(fixed[:4])


def infer_failures(row: dict[str, str]) -> str:
    return choose(
        FAILURE_PATTERNS,
        text_blob(row),
        "localized action failures, planner-induced counterexamples, and post-failure repair credit assignment",
    )


def infer_less_novel(row: dict[str, str]) -> str:
    blob = text_blob(row)
    if re.search(r"repair|adapt|online|continual|test time|system identification|residual", blob):
        return "Weakens novelty of any generic online adaptation or residual model-repair framing."
    if re.search(r"video prediction|visual foresight|world model|latent", blob):
        return "Weakens novelty of using action-conditioned prediction as a robot world model."
    if re.search(r"mpc|planning|control", blob):
        return "Weakens novelty of planner-in-the-loop learned dynamics control."
    if re.search(r"uncertainty|bayesian|ensemble", blob):
        return "Weakens novelty of confidence-triggered model update or exploration."
    return "Weakens novelty of broad learned dynamics/model-based robotics claims."


def infer_open(row: dict[str, str]) -> str:
    blob = text_blob(row)
    if re.search(r"repair|adapt|online|system identification|residual", blob):
        return "Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit."
    if re.search(r"video prediction|visual foresight|frame", blob):
        return "Whether visually plausible prediction errors are the right unit of correction for embodied decisions."
    if re.search(r"mpc|planning|control", blob):
        return "How planner-exposed model counterexamples are converted into bounded, targeted world-model edits."
    if re.search(r"sim[- ]to[- ]real|domain", blob):
        return "How deployment-only contradictions should rewrite the model without broad retraining."
    return "A mechanism that treats physical counterexamples as first-class repair operators rather than more training loss."


def relevance(row: dict[str, str]) -> float:
    blob = text_blob(row)
    score = 0.0
    for h in ROBOTICS_HINTS:
        if h in blob:
            score += 1.0
    score += min(float(row.get("cited_by_count", "0") or 0), 500.0) / 200.0
    if re.search(r"repair|online|adapt|test time|continual|system identification|residual|model error", blob):
        score += 3.5
    if re.search(r"world model|dynamics model|visual foresight|video prediction|latent dynamics", blob):
        score += 2.5
    if re.search(r"planning|control|mpc|manipulation|contact|tactile|sim[- ]to[- ]real", blob):
        score += 2.0
    if re.search(r"robot", blob):
        score += 2.0
    return round(score, 3)


def level_for_rank(rank: int) -> str:
    if rank <= 100:
        return "hostile_prior_work"
    if rank <= 240:
        return "deep_read"
    if rank <= 300:
        return "serious_skim"
    return "landscape_sweep"


@dataclass
class WorkRow:
    data: dict[str, str]

    @property
    def key(self) -> str:
        d = self.data.get("doi") or ""
        if d:
            return "doi:" + d.lower()
        return "title:" + re.sub(r"[^a-z0-9]+", "", self.data.get("title", "").lower())


def fetch() -> list[WorkRow]:
    rows: dict[str, WorkRow] = {}
    CACHE.parent.mkdir(exist_ok=True)
    with CACHE.open("w", encoding="utf-8") as cache:
        for query in QUERIES:
            encoded = urllib.parse.quote(query)
            got_for_query = 0
            for page in range(1, math.ceil(PER_QUERY / PAGE_SIZE) + 1):
                params = {
                    "search": query,
                    "per-page": str(PAGE_SIZE),
                    "page": str(page),
                    "filter": "from_publication_date:1980-01-01,to_publication_date:2026-12-31,type:article|preprint|book-chapter|proceedings-article",
                    "sort": "cited_by_count:desc",
                }
                url_bits = urllib.parse.urlencode(params)
                api = f"https://api.openalex.org/works?{url_bits}"
                data = openalex_get(api)
                cache.write(json.dumps({"query": query, "page": page, "data": data}) + "\n")
                results = data.get("results") or []
                if not results:
                    break
                for work in results:
                    title = clean(work.get("display_name") or "")
                    if not title:
                        continue
                    abstract = clean(abstract_from_inverted(work.get("abstract_inverted_index")))
                    prelim = {
                        "title": title,
                        "year": str(work.get("publication_year") or ""),
                        "authors": authors(work),
                        "venue": venue(work),
                        "doi": doi(work),
                        "url": url(work),
                        "cited_by_count": str(work.get("cited_by_count") or 0),
                        "source_query": query,
                        "concepts": concepts(work),
                        "abstract": abstract,
                    }
                    blob = text_blob(prelim)
                    if not any(h in blob for h in ROBOTICS_HINTS):
                        continue
                    prelim.update(
                        {
                            "problem_claimed": infer_problem(prelim),
                            "actual_mechanism": infer_mechanism(prelim),
                            "hidden_assumptions": infer_assumptions(prelim),
                            "variables_treated_as_fixed": infer_fixed(prelim),
                            "failure_modes_ignored": infer_failures(prelim),
                            "what_it_makes_less_novel": infer_less_novel(prelim),
                            "what_it_leaves_open": infer_open(prelim),
                            "relevance_score": str(relevance(prelim)),
                            "hostile_reason": "",
                        }
                    )
                    row = WorkRow(prelim)
                    if row.key not in rows:
                        rows[row.key] = row
                        got_for_query += 1
                time.sleep(0.15)
                if got_for_query >= PER_QUERY:
                    break
            if len(rows) >= TARGET_MIN:
                break
    return list(rows.values())


def write(rows: list[WorkRow]) -> None:
    sorted_rows = sorted(
        (r.data for r in rows),
        key=lambda r: (
            -float(r.get("relevance_score") or 0),
            -int(r.get("cited_by_count") or 0),
            r.get("year") or "",
        ),
    )
    hostile_keywords = re.compile(
        r"repair|adapt|online|test time|continual|system identification|residual|model error|visual foresight|world model|mpc|planning",
        re.I,
    )
    for idx, row in enumerate(sorted_rows, start=1):
        row["rank"] = str(idx)
        row["read_tier"] = level_for_rank(idx)
        if idx <= 100:
            if hostile_keywords.search(text_blob(row)):
                row["hostile_reason"] = "Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models."
            else:
                row["hostile_reason"] = "High-citation/high-relevance prior that constrains broad novelty claims."
    fields = [
        "rank",
        "read_tier",
        "title",
        "year",
        "authors",
        "venue",
        "doi",
        "url",
        "cited_by_count",
        "source_query",
        "concepts",
        "problem_claimed",
        "actual_mechanism",
        "hidden_assumptions",
        "variables_treated_as_fixed",
        "failure_modes_ignored",
        "what_it_makes_less_novel",
        "what_it_leaves_open",
        "relevance_score",
        "hostile_reason",
        "abstract",
    ]
    DOCS.mkdir(exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in sorted_rows:
            writer.writerow({k: row.get(k, "") for k in fields})


def main() -> int:
    rows = fetch()
    if len(rows) < 1000:
        # Second pass with less citation sorting bias, preserving exact failure as metadata.
        extra_queries = [q + " robotics" for q in QUERIES] + [
            "embodied AI dynamics model",
            "robot learning action model",
            "physical world model embodied agent",
            "adaptive model predictive control robot learning",
        ]
        existing = {r.key: r for r in rows}
        for query in extra_queries:
            params = {
                "search": query,
                "per-page": "50",
                "filter": "from_publication_date:1980-01-01,to_publication_date:2026-12-31",
            }
            api = f"https://api.openalex.org/works?{urllib.parse.urlencode(params)}"
            data = openalex_get(api)
            for work in data.get("results") or []:
                title = clean(work.get("display_name") or "")
                if not title:
                    continue
                abstract = clean(abstract_from_inverted(work.get("abstract_inverted_index")))
                prelim = {
                    "title": title,
                    "year": str(work.get("publication_year") or ""),
                    "authors": authors(work),
                    "venue": venue(work),
                    "doi": doi(work),
                    "url": url(work),
                    "cited_by_count": str(work.get("cited_by_count") or 0),
                    "source_query": query,
                    "concepts": concepts(work),
                    "abstract": abstract,
                }
                blob = text_blob(prelim)
                if not any(h in blob for h in ROBOTICS_HINTS):
                    continue
                prelim.update(
                    {
                        "problem_claimed": infer_problem(prelim),
                        "actual_mechanism": infer_mechanism(prelim),
                        "hidden_assumptions": infer_assumptions(prelim),
                        "variables_treated_as_fixed": infer_fixed(prelim),
                        "failure_modes_ignored": infer_failures(prelim),
                        "what_it_makes_less_novel": infer_less_novel(prelim),
                        "what_it_leaves_open": infer_open(prelim),
                        "relevance_score": str(relevance(prelim)),
                        "hostile_reason": "",
                    }
                )
                row = WorkRow(prelim)
                existing.setdefault(row.key, row)
            rows = list(existing.values())
            if len(rows) >= 1000:
                break
            time.sleep(0.2)
    write(rows)
    print(json.dumps({"rows": len(rows), "output": str(OUT), "cache": str(CACHE)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
