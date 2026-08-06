#!/usr/bin/env bash
set -euo pipefail

show_help() {
  cat <<'HELP'
Usage: run_baseline_evaluation.sh --data-root DATA_ROOT --baseline-root BASELINE_ROOT --checkpoint-root CHECKPOINT_ROOT --output-root OUTPUT_ROOT [--dry-run]

Evaluates fixed baseline outputs only. No RGB fallback or output selection.
HELP
}

DRY_RUN=0
ACK=0
ARGS=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    --help|-h) show_help; exit 0 ;;
    --dry-run) DRY_RUN=1; shift ;;
    --acknowledge-frozen-official-test) ACK=1; ARGS+=("$1"); shift ;;
    *) ARGS+=("$1"); shift ;;
  esac
done

case "run_baseline_evaluation" in
  run_final_inference|run_detection_evaluation)
    for arg in "${ARGS[@]}"; do
      if [[ "$arg" == "--official-test" && "$ACK" -ne 1 ]]; then
        echo "ERROR: official-test mode requires --acknowledge-frozen-official-test" >&2
        exit 3
      fi
    done
    ;;
esac

if [[ "$DRY_RUN" -eq 1 ]]; then
  echo "DRY RUN: run_baseline_evaluation would execute with: ${ARGS[*]:-<no args>}"
  exit 0
fi

echo "ERROR: This release wrapper is a parameterized template. Run from the full source repository and provide DATA_ROOT, CHECKPOINT_ROOT, and OUTPUT_ROOT. It does not download restricted data, train detectors, run SAM inference, or overwrite outputs." >&2
exit 2
