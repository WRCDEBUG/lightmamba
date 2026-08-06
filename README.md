
# LightMamba Reproducibility Package

## 1. Project Overview

This package documents a frozen LightMamba experiment chain for infrared-visible image fusion. It is a reproducibility and audit aid, not a standalone redistribution of third-party datasets or model weights.

## 2. Final Method Identity

The frozen method uses normalized thermal evidence, TSAG thermal saliency-aware gating, an S6/SS2D backbone, identity modulation, and semantic-prior-free inference. SAM-derived priors are not used at inference time.

## 3. Repository Layout

- `configs/`: release-safe configuration summaries with `DATA_ROOT`, `CHECKPOINT_ROOT`, and `OUTPUT_ROOT` placeholders.
- `splits/`: revision train/validation stem manifests.
- `scripts/`: parameterized wrappers with safe defaults.
- `metadata/`: sanitized frozen-result summaries and provenance hashes.
- `checksums/`: package checksums.
- `docs/`: entrypoint, evidence, and statement drafts.

## 4. Installation

Create an environment from `environment.yml` or install the direct dependencies in `requirements-minimal.txt`. The full observed environment is recorded in `environment-full.txt`.

## 5. Dataset Preparation

LLVIP and M3FD are third-party datasets and are not redistributed here. Place local copies under a user-defined `DATA_ROOT` following `DATASETS.md`.

## 6. Checkpoint Preparation

The final checkpoint is not included. Place it under `CHECKPOINT_ROOT` and verify SHA256:

`68abaeefc322edec12592017ef57f806f89614dbc7438bf766da45e4a0fc27f9`

RT-DETR/YOLO/SAM checkpoints are also excluded and must be obtained under their own terms.

## 7. Quick Smoke Test

Run:

```bash
bash scripts/run_smoke_test.sh --dry-run
```

## 8. Final Inference

Use `scripts/run_final_inference.sh` with explicit `--data-root`, `--checkpoint-root`, and `--output-root`. The script is parameterized and refuses to overwrite an existing output directory.

## 9. Fusion Metrics

Use `scripts/run_fusion_metrics.sh` after preparing paired IR/visible/fused outputs. Metrics follow a luminance-domain, source-referenced protocol without fused ground truth.

## 10. Detection Evaluation

Use `scripts/run_detection_evaluation.sh` for revision-validation by default. Frozen official-test evaluation requires `--acknowledge-frozen-official-test`.

## 11. Baseline Evaluation

Use `scripts/run_baseline_evaluation.sh` only with pre-fixed baseline outputs. Do not select Gray/RGB outputs based on detector results.

## 12. External Zero-Shot

Step 9A used M3FD with 1050 exact-stem pairs, no fine-tuning, no detector AP, and limited baselines. Text-IF was excluded because of 58 dimension mismatches.

## 13. Multiseed Ablation Aggregation

Use:

```bash
python scripts/aggregate_multiseed_ablation.py --input-dir metadata --output-dir OUTPUT_ROOT
```

Expected three-seed mAP summaries:

- Old gate: mAP@0.5 `0.895304 ± 0.003193`; mAP@0.5:0.95 `0.534820 ± 0.002634`.
- TSAG reference: mAP@0.5 `0.898622 ± 0.002086`; mAP@0.5:0.95 `0.537080 ± 0.002046`.
- No-SAM package: mAP@0.5 `0.898729 ± 0.001699`; mAP@0.5:0.95 `0.537678 ± 0.002350`.

## 14. Expected Outputs

Frozen LLVIP official-test point estimates include Final LightMamba mAP@0.5 `0.9130` and mAP@0.5:0.95 `0.6058`. Average reference is `0.7928` / `0.4859`; Infrared Only reference is `0.9640` / `0.6643`.

## 15. Expected SHA256

See `metadata/frozen_hashes.json` and `checksums/package_sha256.txt`.

## 16. Known Limitations

The official-test model is one fixed training seed. The core gate ablation repeats three seeds. Bootstrap confidence intervals are deferred. The held-out detector shows infrared-domain bias, and evidence remains LLVIP-centered with limited external zero-shot support.

## 17. Third-Party Licenses

See `THIRD_PARTY_LICENSES.md`. Several licenses require author verification before public release.

## 18. Citation

Use `CITATION.cff.draft` only after author, version, repository, and DOI confirmation.

## 19. Contact

For questions about this repository, contact wrclive@outlook.com.

## 20. Reproducibility Scope

This package supports audit and reproduction of the frozen protocols when users independently obtain datasets and checkpoints. It must not be used to select checkpoints or tune methods on official test data.
