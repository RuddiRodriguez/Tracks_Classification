# Original image previews

Downloaded from the original Dropbox archive on 5 October 2026, with the author's permission to publish examples.

- `frames/real-embryo-preview.jpg`: Dropbox video poster for `Tracks_Classification/Data_real/Stream-4candledeno.avi`. Preview player reports a 47-second movie. Ruddi Rodriguez Garcia identifies the experimental context as C. elegans embryos during their first division. Fluorescent marker, imaging plane, frame index, and calibration are not established by this poster.
- `frames/simulated-no-noise-preview.jpg`: Dropbox image preview of `movienonoise4.tif`, from the original `Simulation_MT_images/Simulacion/.../test0.050000` archive. The repository contains the matching-name TrackMate export `movienonoise4_Tracks_DM.xml`; correspondence to individual training rows has not been audited.
- `frames/simulated-noisy-preview.jpg`: Dropbox image preview of `movienoisediffuback4.tif` from the same directory. This is an archived simulation variant with background/noise; exact parameters and its inclusion in the training table are unverified.

These are downloaded JPEG previews, not recovered original multi-frame TIFFs or the original AVI. Browser download attempts for the original movie did not return a file; the observed video asset was an HLS playlist that the export tool could not save. No complete Dropbox movie is claimed as published; the published-paper movies recovered later are listed below.

Saved JPEG bytes are unchanged. The portfolio displays the faint synthetic previews with CSS brightness multipliers of 12 and 8 respectively, explicitly labelled in their captions. These display adjustments are not part of model preprocessing or quantitative image analysis.

The methodology begins with synthetic images designed to mimic experimental conditions, then tracking and feature extraction. The Python classifier consumes seven trajectory measurements, not raw image pixels. The simulation generator remains outside this organised branch.

Biological background: Rodriguez-Garcia, Chesneau et al. (2018), https://pmc.ncbi.nlm.nih.gov/articles/PMC6340208/. This paper provides context for directed versus diffusive-like dynein motion; the repository's classifier output alone does not establish a force-generating event.

## Published full movies recovered successfully

Source: Rodriguez-Garcia, Chesneau et al. (2018), https://pmc.ncbi.nlm.nih.gov/articles/PMC6340208/. Downloaded from Europe PMC's supplementary-files archive for PMC6340208. These are collaborative research materials, licensed CC BY-NC-SA 3.0 (https://creativecommons.org/licenses/by-nc-sa/3.0/); attribution and licence apply to these media, including extracted frames. Original MP4 bytes are unchanged.

- `movies/paper-S1-real-dynein.mp4`: original `mbc-29-3093-s002.mp4`, Movie S1, real DYCI-1::mCherry in metaphase, lower spindle plane, no processing.
- `movies/paper-S8-simulated-diffusion.mp4`: original `mbc-29-3093-s009.mp4`, Movie S8, simulated diffusion.
- `movies/paper-S9-simulated-directed.mp4`: original `mbc-29-3093-s010.mp4`, Movie S9, simulated directed motion.

All three movies have 5 Hz acquisition/sampling, published playback accelerated 3x, and a 10 micrometre scale bar. S8/S9 specify SNR 5 and exponentially distributed lifetimes with 10 s mean. PNG poster frames were extracted at playback timestamp 00:01 with FFmpeg, without contrast changes. Movie-to-training-row correspondence is not established.

Supplemental Text 2.5 documents diffusion with/without added drift, exponential lifetimes, experimentally matched intensity, Gaussian optical blur, Gaussian pixel noise, and fast-diffusing fluorescent background particles. Table S2 lists 100 frames / 20 s, 0.2 s sampling, 0.3 micrometre Gaussian PSF, 0.002 square-micrometre/s particle diffusion, and 0.4 micrometre/s drift components. Its printed pixel-size unit reads 0.130 nm; this requires checking against the original code before implementation and is not silently corrected here.

The paper used CANDLE, LoG, u-track, and asymmetry-based classification (alpha 0.1). The later machine-learning repository uses TrackMate exports and seven features to compare logistic regression/random forest. These methods and results must not be conflated.
