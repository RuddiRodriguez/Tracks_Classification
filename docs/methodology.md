# Methodology and preservation notes

## Scientific question

Distinguish diffusion (D) from directed motion (DM) using measurements of tracked trajectories. Ruddi Rodriguez Garcia confirms the original study trained on simulated tracks and applied the classifier to real experimental tracks. Tracking and classification are separate stages: this Python workflow starts with existing feature tables, not raw movies.

## Original sequence

1. Obtain simulated movies/tracks with known D or DM labels.
2. Calculate seven features: net displacement, efficiency, straightness, asymmetry, bending, absolute projected skewness, and projected kurtosis.
3. Split simulated feature rows randomly: 80% training, 20% holdout, seed 42. No added stratification or grouping.
4. Fit missing-value replacement and MinMax scaling inside each training fold.
5. Compare logistic regression and random forest using the original grid: 267 settings, five folds, 1,335 fits.
6. Score macro precision, recall, F1, and balanced accuracy. Select by macro recall.
7. Evaluate the chosen training-fitted model on the simulated holdout.
8. Apply that same model and preparation to real feature tables. Do not retrain on real tracks or use their placeholder labels as known outcomes.

## Preserved choices

All seven features, imputation choices, scaling, model families, search ranges, validation folds, selection score, and 80/20 split come from `notebooks/original/Full_pipeline.ipynb`. Real prediction is now an explicit function using the same fitted estimator; it makes the intended research sequence visible.

## Changes for clarity or current Python compatibility

- Explicit column selection replaces the custom selector class and position-based column slicing.
- D and DM remain readable labels instead of separately creating integer category mappings for training and testing.
- Logistic regression uses `liblinear` so both original l1 and l2 options work with current scikit-learn. The notebook left its solver unspecified; exact historical solver equivalence is not established.
- Random forest and logistic regression now have seed 42 for repeatability. The original estimators did not set seeds.
- Entirely empty feature rows from preallocated MATLAB exports are removed. Partially missing rows remain and follow the original training-fitted imputation.
- The MATLAB feature function is preserved with condensed layout and its original credit. Experimental preparation removes unused code and empty preallocated export rows; formulas and track selection stay unchanged.
- The original notebook is kept unchanged as a historical reference, including its saved output and old machine-specific path.

## Feature preparation recovered from Dropbox

`main_script.m` reads MATLAB tracked-feature structures, selects available x/y positions, keeps tracks longer than four positions, calls `trackFeaturesTest(x,y,length(x)-1)`, and writes a real feature table with the placeholder `D_DM`. The feature function credits Jo Helmuth, Computational Biophysics Laboratory, ETHZ, last changed May 23, 2007. Feature-method credit must remain separate from my classification workflow.

The original angle code leaves horizontal steps (dy = 0) at its initial angle of zero, including negative horizontal steps. Do not silently replace this with atan2 when translating: that changes straightness and bending for some tracks. Efficiency is squared net displacement divided by the number of steps and sum of squared step lengths. Kurtosis is the ordinary Pearson form, not excess kurtosis.

## What the reported results mean

The historical notebook reports 96.95% accuracy on 197 held-out rows from a 985-row input. It loads `Data/myData1.csv` from an old Dropbox path. The public `myData.csv` contains 1,718 rows. The historical `myData1.csv` has been recovered: its 985 rows and nine columns match the first 985 rows and first nine columns of the public table. A checksum of every displayed cell matches the complete Dropbox preview (FNV-1a 1625159035, including header). The recovered table is the runnable default. Fresh results remain separate from saved historical output.

Real tables use `D_DM`, with no verified individual D/DM truth labels. Predictions on these tables are application results, not measured real-data accuracy. The random split may place tracks from the same movie in both subsets; a future unseen-movie validation would be a separate methodological experiment, not a hidden change to this reproduction.

## Missing material

Dropbox contains additional notebooks, TrackMate XML exports, and experimental AVI movies. `myData1.csv` is now recovered locally. Notebook download could not be completed in the browser session. Simulation generator, exact simulation settings, calibration, and the full original real-prediction notebook remain unrecovered. No substitute simulation generator or invented experimental result is added.

## Reading the seven measurements

| Measurement | What it describes |
| --- | --- |
| `netDisp` | Distance between the first and last position in the selected window. |
| `efficiency` | Squared end-to-end distance divided by step count and the sum of squared step distances. |
| `straightness` | Average cosine of direction changes between consecutive steps. |
| `Asym` | Elongation of the position cloud, from the two eigenvalues of its gyration tensor. |
| `bending` | Absolute average sine of direction changes. A trajectory descriptor, not membrane bending rigidity. |
| `pointSkew` | Absolute skewness of positions projected onto the main direction of the position cloud. |
| `pointKurt` | Pearson kurtosis of those projected positions. |

These quantities describe a tracked path. They do not identify a protein, establish a biological mechanism, or replace experimental controls.
