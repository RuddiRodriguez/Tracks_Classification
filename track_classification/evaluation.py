"""Evaluate held-out simulated tracks; label real predictions separately."""
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from .data import FEATURES


def evaluate_simulated(model, data):
    expected = data['Classification']
    predicted = model.predict(data[FEATURES])
    report = classification_report(expected, predicted, output_dict=True)
    return {
        'accuracy': accuracy_score(expected, predicted),
        'report': pd.DataFrame(report).T,
        'confusion_matrix': pd.DataFrame(
            confusion_matrix(expected, predicted, labels=model.classes_),
            index=pd.Index(model.classes_, name='actual'),
            columns=pd.Index(model.classes_, name='predicted'),
        ),
    }


def predict_real_tracks(model, data):
    # D_DM in the original real tables is a placeholder, not ground truth.
    result = data.copy()
    result['predicted_motion'] = model.predict(data[FEATURES])
    return result
