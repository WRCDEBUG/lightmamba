#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

import numpy as np

VARIANT_ORDER = ["Old gate", "TSAG reference", "No-SAM package"]
METRICS = ["precision", "recall", "map50", "map50_95", "en", "sf", "mi", "ssim", "vif", "qabf"]


def read_csv(path: Path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows):
    path.parent.mkdir(parents=True, exist_ok=False if path.parent.exists() is False else True)
    if path.exists():
        raise SystemExit(f"Refusing to overwrite {path}")
    fields = list(rows[0].keys()) if rows else ["status"]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description="Aggregate Step 9B multiseed ablation CSV files.")
    parser.add_argument("--input-dir", required=True, help="Directory containing multiseed_per_seed_results.csv.")
    parser.add_argument("--output-dir", required=True, help="Directory for aggregate outputs.")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    input_path = Path(args.input_dir) / "multiseed_per_seed_results.csv"
    output_dir = Path(args.output_dir)
    if args.dry_run:
        print(f"Would read {input_path} and write aggregate CSV files under {output_dir}")
        return
    rows = read_csv(input_path)
    out = []
    for variant in VARIANT_ORDER:
        vr = [r for r in rows if r["variant"] == variant]
        if len(vr) != 3:
            raise SystemExit(f"Expected 3 seeds for {variant}, got {len(vr)}")
        for metric in METRICS:
            vals = np.asarray([float(r[metric]) for r in vr], dtype=np.float64)
            if not np.isfinite(vals).all():
                raise SystemExit(f"NaN/Inf in {variant} {metric}")
            out.append({
                "variant": variant,
                "metric": metric,
                "n": len(vals),
                "mean": float(np.mean(vals)),
                "sample_std": float(np.std(vals, ddof=1)),
                "median": float(np.median(vals)),
                "min": float(np.min(vals)),
                "max": float(np.max(vals)),
            })
    write_csv(output_dir / "multiseed_aggregate_results.csv", out)


if __name__ == "__main__":
    main()
