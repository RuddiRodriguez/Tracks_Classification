"""Read feature tables and TrackMate trajectories."""
from pathlib import Path
import xml.etree.ElementTree as ET

import pandas as pd
from sklearn.model_selection import train_test_split

FEATURES = [
    'netDisp', 'efficiency', 'straightness', 'Asym',
    'bending', 'pointSkew', 'pointKurt',
]
ROOT = Path(__file__).resolve().parents[1]


def load_features(path):
    # Original real-data exports contain empty preallocated rows.
    data = pd.read_csv(path)
    return data.dropna(subset=FEATURES, how='all').copy()


def split_simulated_tracks(data):
    # Keep the original random 80/20 split, without adding stratification.
    return train_test_split(data, test_size=0.2, random_state=42)


def training_values(data):
    # Keep named labels rather than separately encoding each dataset.
    return data[FEATURES], data['Classification']


def read_trackmate(path):
    root = ET.parse(path).getroot()
    return [
        pd.DataFrame([
            {name: float(spot.get(name)) for name in ['t', 'x', 'y', 'z']}
            for spot in track
        ])
        for track in root
    ]
