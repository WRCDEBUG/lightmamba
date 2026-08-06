
# Reproducibility Protocol

## A. Fast Verification

No dataset is required. Run package checks, configuration hash checks, and synthetic tensor smoke tests:

```bash
bash scripts/run_smoke_test.sh --dry-run
```

This verifies wrapper behavior, frozen SHA metadata, and path safety. It does not train, run detector evaluation, or perform SAM inference.

## B. Revision-Validation Reproduction

Requires LLVIP train data under `DATA_ROOT`. Use `splits/llvip_revision_train.txt` and `splits/llvip_revision_val.txt`. This path is safe for development because it never accesses official test.

Expected counts:

- revision train: 10521 stems, SHA256 `0c94e87067626124947c1b28a6c6b43590a82f0241987f2a83cde7d76f2ef6e5`
- revision validation: 1504 stems, SHA256 `1e594f2b95fc48d1ad2c633842b64853f455506e69f27b5ff56f099cb1b7fd66`
- validation groups: 03, 05, 15

## C. Frozen Official-Test Reproduction

Official-test reproduction is evaluation-only and must not be used for model selection. Commands that touch official test require `--acknowledge-frozen-official-test`. Do not train, fine-tune, choose checkpoints, or select baselines using official-test results.

Frozen official-test manifest SHA256: `45bc1e64dd837b33023fa9e65a62e2925fb53e29b1057daee82b9f309b94e64f`.

## D. External Zero-Shot

Step 9A used M3FD with 1050 exact-stem pairs, manifest SHA256 `55a33f7718b183a1666da7e69d21b8cbb37843321bbb11b94e6beb50d819d673`. LightMamba was run zero-shot with the final checkpoint, no fine-tuning, no kappa tuning, and no detection AP. Text-IF was excluded because 58 files had dimension mismatches. The acceptance status was `CONDITIONAL_PASS_LIMITED_BASELINES`.

## E. Three-Seed Core Ablation

Step 9B used three variants and three seeds:

- Old gate
- TSAG reference
- No-SAM package
- seeds: 7, 17, 29
- teacher epochs: 20
- student epochs: 20
- final epoch only
- no early stopping
- no best-epoch selection

The official-test model remains one fixed training seed; the three-seed evidence applies to the core gate/package ablation, not to the final official-test checkpoint.

Expected aggregate table is in `metadata/expected_results_summary.json`. Full training took roughly 30 hours on one NVIDIA A100 80GB PCIe in the recorded environment.
