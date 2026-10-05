# Classifying motion: simulated training, real-track prediction

Research demonstration by Ruddi Rodriguez Garcia.

Can trajectory shape distinguish random diffusion from directed movement? This project trains a classifier on simulated tracks with known motion labels, then applies the same fitted preparation and model to real experimental tracks.

- **D:** diffusion.
- **DM:** directed motion.
- **D_DM:** placeholder in real-data exports, not a verified class.

## Follow the flow

```text
Simulated movies → tracking → seven feature measurements
                                      ↓
                             random 80/20 split
                                      ↓
                   missing values → scaling → model search
                                      ↓
                      held-out simulated evaluation
                                      ↓
Real movies → tracking → same seven features → fitted model → predictions
```

Python starts at the feature tables. Original tracking and feature preparation belong to the earlier MATLAB/TrackMate stage. Read [the methodology](docs/methodology.md) for preserved choices, source credit, and limits.

## Repository guide

| Location | Purpose |
| --- | --- |
| `notebooks/01_motion_classification.ipynb` | Guided demonstration, step by step |
| `track_classification/data.py` | Read tables and TrackMate XML; split simulated rows |
| `track_classification/models.py` | Original preparation and 267-setting model search |
| `track_classification/evaluation.py` | Simulated evaluation and real prediction |
| `run_workflow.py` | Run the complete feature-table flow |
| `data/simulated/` | Public D/DM training table and example XML |
| `data/real/` | Existing experimental feature exports |
| `notebooks/original/` | Unchanged historical notebook and XML reader |
| `matlab/` | Original feature formulas and simplified experimental feature export |
| `docs/` | Methodology, provenance, and results explanation |

Root HTML, fonts, and styles are the original project website, preserved separately from the research workflow.

## Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run_workflow.py --jobs 4
```

The full original search performs 1,335 fits; allow time. Reports and real-track prediction tables go to `results/`. To use another feature table:

```bash
python run_workflow.py --training /path/to/myData1.csv --real /path/to/real_features.csv --jobs 4
```

For the guided version, run `jupyter lab notebooks/01_motion_classification.ipynb`. The notebook uses the same small functions as the script.

## Result boundaries

The historical 96.95% accuracy in the original notebook is a simulated holdout result on its old input, not verified accuracy on real experimental tracks. Current real CSVs lack individual truth labels, so this flow outputs predictions without an accuracy claim. The default is the recovered 985-row historical training table. The larger public table is retained separately; newly calculated results are reported separately from saved historical output.

This is a simple research demonstration. No service, deployment, or production framework is included. The simulation generator and complete original experimental notebook have not yet been recovered. The historical training table was recovered by comparing all 986 table rows (including the header) and nine columns against the Dropbox preview.

## Checked demonstration

The guided notebook ran from beginning to end using the recovered historical input. Fresh simulated holdout accuracy: **96.45%**; real cortex output: 193 classified tracks. The full script was also exercised with the larger public input and all three real tables. Read [validation details](docs/validation.md) for dataset distinctions, selected settings, and what was checked.
