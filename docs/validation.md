# Validation of the organised workflow

Run date: October 5, 2026. Python 3.14; scikit-learn 1.7.2.

## Guided notebook: recovered historical input

`notebooks/01_motion_classification.ipynb` executed from beginning to end, with saved outputs. Input: `myData1.csv`, 985 tracks (596 DM, 389 D). Original split: 788 training tracks and 197 holdout tracks. Full 267-setting, five-fold search executed; selection by macro recall.

Selected model: random forest, 1,000 trees, max depth 25, minimum leaf size 10, maximum 10 leaves, median imputation, seed 42.

Fresh simulated holdout accuracy: 96.45% (190/197). Macro recall: 96.60%.

| Actual / predicted | D | DM |
| --- | ---: | ---: |
| D | 68 | 2 |
| DM | 5 | 122 |

Applied the training-fitted model to 193 cortex feature rows: 88 D predictions and 105 DM predictions. Those counts describe predictions, not experimentally verified classes.

The historical saved notebook reported 96.95%. Exact numerical equivalence is not claimed: estimator seeds and explicit logistic-regression solver were added, and library versions differ. Original saved notebook remains unchanged.

## Full script: larger public training input

The script also ran the full original search on `myData.csv`, the larger 1,718-row public table. All 267 candidates returned finite macro-recall scores; no fit failures. Holdout accuracy on its 344 simulated tracks: 96.51%.

Real prediction stage completed for all included tables:

| Input | Usable tracks | Predicted D | Predicted DM |
| --- | ---: | ---: | ---: |
| myDatareal1.csv | 1,261 | 408 | 853 |
| myDatareal_dyne.csv | 690 | 202 | 488 |
| myDatarealcortex.csv | 193 | 85 | 108 |

These predictions use the larger-table training run, so they differ from the historical-input notebook. Local outputs from this supplementary run are separated into `results/public_table_demo/`.

## Other checks

- Historical notebook preserved byte-for-byte.
- Recovered training-table cell checksum matches the complete Dropbox CSV preview.
- Seven expected feature columns used; track identifiers excluded from fitting.
- TrackMate XML reader exercised on the included export.
- Empty real-export feature rows excluded; partially missing measurements retained for fitted imputation.
- New Python files parsed; notebook validated; Git whitespace checks passed.

MATLAB feature files were inspected against Dropbox source but not executed here. Raw-movie tracking, simulation generation, and biological correctness of real predictions were not validated by these runs.
