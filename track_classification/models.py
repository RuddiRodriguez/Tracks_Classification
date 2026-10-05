"""Original preparation and model-search choices, separated from the notebook."""
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler


def build_model_search(n_jobs=-1):
    pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', MinMaxScaler()),
        ('model', LogisticRegression(solver='liblinear', random_state=42)),
    ])
    parameters = [
        {
            'model': [LogisticRegression(solver='liblinear', random_state=42)],
            'model__penalty': ['l1', 'l2'],
            'model__C': [10, 25, 30, 40],
            'model__class_weight': ['balanced'],
            'imputer__strategy': ['mean', 'median', 'most_frequent'],
        },
        {
            'model': [RandomForestClassifier(random_state=42)],
            'model__n_estimators': [10, 100, 1000],
            'model__max_depth': [25, 30, None],
            'model__min_samples_leaf': [10, 15, 100],
            'model__max_leaf_nodes': [2, 5, 10],
            'imputer__strategy': ['mean', 'median', 'most_frequent'],
        },
    ]
    return GridSearchCV(
        pipeline, parameters, cv=5, n_jobs=n_jobs, verbose=1,
        scoring=['precision_macro', 'recall_macro', 'f1_macro', 'balanced_accuracy'],
        refit='recall_macro',
    )
