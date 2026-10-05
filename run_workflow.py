"""Train on simulated features, evaluate a holdout, then classify real tracks."""
import argparse
from pathlib import Path

import pandas as pd

from track_classification.data import ROOT, load_features, split_simulated_tracks, training_values
from track_classification.evaluation import evaluate_simulated, predict_real_tracks
from track_classification.models import build_model_search


def run_workflow(training_path, real_paths, output_dir, n_jobs=-1):
    simulated = load_features(training_path)
    training, holdout = split_simulated_tracks(simulated)
    x_train, y_train = training_values(training)
    search = build_model_search(n_jobs)
    search.fit(x_train, y_train)

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(search.cv_results_).to_csv(output_dir / 'model_comparison.csv', index=False)
    scores = evaluate_simulated(search.best_estimator_, holdout)
    scores['report'].to_csv(output_dir / 'simulated_holdout_report.csv')
    scores['confusion_matrix'].to_csv(output_dir / 'simulated_confusion_matrix.csv')
    print('Selected settings:', search.best_params_)
    print('Simulated holdout accuracy:', scores['accuracy'])
    print(scores['report'])

    for path in real_paths:
        real = load_features(path)
        predictions = predict_real_tracks(search.best_estimator_, real)
        destination = output_dir / f'{Path(path).stem}_predictions.csv'
        predictions.to_csv(destination, index=False)
        print(f'Real tracks: {len(predictions)} predictions saved to {destination}')
    return search, scores


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--training', type=Path, default=ROOT / 'data/simulated/myData1.csv')
    parser.add_argument('--real', type=Path, nargs='*', default=sorted((ROOT / 'data/real').glob('*.csv')))
    parser.add_argument('--output', type=Path, default=ROOT / 'results')
    parser.add_argument('--jobs', type=int, default=-1)
    args = parser.parse_args()
    run_workflow(args.training, args.real, args.output, args.jobs)
