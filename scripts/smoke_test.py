#!/usr/bin/env python3
"""Fast repository smoke test for the repair-loop simulator."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from repair_loop_sim import make_env, prediction_error, run_episode, strategy_factory  # noqa: E402


def main() -> int:
    env = make_env(0)
    checks: dict[str, object] = {}
    for strategy in ["nominal_no_repair", "ccra_exact_guard", "ccra_row_guard"]:
        model = strategy_factory(strategy)
        before = prediction_error(env, model)
        out = run_episode(env, model)
        after = prediction_error(env, model)
        checks[strategy] = {
            "before_prediction_error": before,
            "after_prediction_error": after,
            "episode": out,
        }
    exact = checks["ccra_exact_guard"]["episode"]
    if not exact["success"] or exact["mismatches"] != 1:
        print(json.dumps(checks, indent=2))
        return 1
    print(json.dumps(checks, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
