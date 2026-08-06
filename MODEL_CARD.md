
# Model Card: LightMamba Frozen Checkpoint

## Model Purpose

LightMamba fuses paired infrared and visible images for pedestrian-oriented nighttime fusion research.

## Intended Use

Research reproduction, method comparison under the documented protocol, and diagnostic analysis of TSAG gating.

## Out-of-Scope Use

Autonomous deployment, safety-critical perception, cross-domain performance guarantees, or method selection on official test data.

## Final Architecture

The frozen model uses normalized thermal evidence, TSAG, S6/SS2D blocks, identity modulation, and semantic-prior-free inference.

## Training Data

LLVIP revision train split, 10521 stems. The dataset is not redistributed.

## Evaluation Data

LLVIP revision validation, LLVIP official test, and M3FD zero-shot pairs. Dataset files are not redistributed.

## Official-Test Results

Final LightMamba achieved mAP@0.5 `0.9130` and mAP@0.5:0.95 `0.6058` under the frozen clean RT-DETR-L evaluator. These are single-checkpoint point estimates.

## Baseline Scope

Seven fixed Gray LLVIP baselines were evaluated under Step 7E. The package standardizes evaluation documentation, not baseline training budgets.

## M3FD Zero-Shot Scope

M3FD validation was zero-shot, fusion-metric only, and accepted as `CONDITIONAL_PASS_LIMITED_BASELINES`.

## Three-Seed Ablation

The TSAG reference exceeded the old gate on mAP@0.5:0.95 in 3/3 paired seeds. The No-SAM package was higher on average for mAP@0.5:0.95 in 2/3 seeds.

## Limitations and Domain Bias

The official-test detector is biased toward infrared-only inputs. Results are LLVIP-centered, single official-test checkpoint, and do not imply statistical significance.

## Ethical Considerations

The data involve pedestrian imagery. Use should respect dataset terms, privacy requirements, and local regulations.

## Checkpoint

Checkpoint SHA256: `68abaeefc322edec12592017ef57f806f89614dbc7438bf766da45e4a0fc27f9`.

The checkpoint is not included. Authors must provide authorized access instructions before public release.
