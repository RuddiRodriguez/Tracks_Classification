# Data and code provenance

- `data/simulated/myData.csv`: unchanged public repository table, 1,718 feature rows. Labels D and DM mean diffusion and directed motion, confirmed by the author.
- `data/simulated/myData1.csv`: recovered historical training table, 985 feature rows (389 D; 596 DM). Every cell in the complete Dropbox preview matches the first nine columns and first 985 rows of the public table; reconstructed from those existing public values. Preview checksum FNV-1a: 1625159035 including header. Source folder: `Machine_Learning/Tracks_Classification/Data`.
- `data/simulated/movienonoise4_Tracks_DM.xml`: unchanged example TrackMate export from the public repository.
- `data/real/*.csv`: unchanged public experimental feature exports. Entirely empty feature rows are ignored when loading. D_DM is a placeholder.
- `matlab/trackFeaturesTest.m`: recovered from the original Dropbox preview, with layout condensed and unused intermediate variables removed. Formulas retained. Original feature-method credit belongs to Jo Helmuth, ETHZ, May 23, 2007. No new blanket licence or claim of authorship over this method is added.
- `matlab/prepare_real_features.m`: simplified version of Ruddi Rodriguez Garcia's Dropbox `main_script.m`. Removes commented experiments and unused variables; exports only filled rows. Same coordinate extraction, track selection, feature call, and real-label placeholder.
- `notebooks/original/Full_pipeline.ipynb`: historical public notebook retained byte-for-byte. Saved outputs belong to its historical run, not this refactor.

Dropbox also contains `Data_real/Stream-4candledeno.avi`, `Data_real/origig80candledeno.avi`, TrackMate exports, MATLAB track folders, plots, and additional classification notebooks. These were located but have not been copied into this branch. The complete real-classification notebook and simulation generator remain unrecovered. Experimental calibration, biological identity, and simulation settings should not be inferred from filenames alone.

## Recovered image examples

Original synthetic and real JPEG previews are now in `media/frames/`, with source details in `media/README.md`. The synthetic sequences were located in the separate original `Simulation_MT_images` archive. Original multi-frame TIFF/AVI downloads remain incomplete; no preview is presented as a full movie. The experimenter identifies the real recordings as C. elegans during the first division.

Full published Movies S1, S8, and S9 were subsequently recovered from Europe PMC. See `media/README.md` for filenames, licence, acquisition/playback details, and extracted PNG frames. Supplemental Text 2.5 documents simulation; it does not by itself verify which generated movies supplied each training-table row.
