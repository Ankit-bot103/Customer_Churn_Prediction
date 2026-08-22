import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


DATA_PATH = Path("data/customer_churn.csv")
ARTIFACTS_DIR = Path("artifacts")
ARTIFACTS_DIR.mkdir(exist_ok=True)


def build_preprocessor(X):
    numeric_features = X.select_dtypes(include=["number"]).columns.tolist()
    categorical_features = X.select_dtypes(exclude=["number"]).columns.tolist()

    numeric_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )

    categorical_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features),
        ]
    )
    return preprocessor


def evaluate_model(name, model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    metrics = {
        "Model": name,
        "Accuracy": round(accuracy_score(y_test, y_pred), 4),
        "Precision": round(precision_score(y_test, y_pred, zero_division=0), 4),
        "Recall": round(recall_score(y_test, y_pred, zero_division=0), 4),
        "F1": round(f1_score(y_test, y_pred, zero_division=0), 4),
        "ROC_AUC": round(roc_auc_score(y_test, y_proba), 4),
        "ConfusionMatrix": confusion_matrix(y_test, y_pred).tolist(),
        "ClassificationReport": classification_report(y_test, y_pred, zero_division=0),
    }
    return model, metrics


def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found at {DATA_PATH}. Run 'python src/generate_data.py' first."
        )

    df = pd.read_csv(DATA_PATH)
    target = "Churn"

    X = df.drop(columns=[target, "CustomerID"])
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    preprocessor = build_preprocessor(X)

    models = {
        "LogisticRegression": LogisticRegression(max_iter=1000, random_state=42),
        "RandomForest": RandomForestClassifier(n_estimators=300, random_state=42, max_depth=8),
        "GradientBoosting": GradientBoostingClassifier(random_state=42),
    }

    model_results = []
    best_model = None
    best_metrics = None

    for name, model in models.items():
        pipeline = Pipeline(
            steps=[
                ("preprocessor", preprocessor),
                ("model", model),
            ]
        )
        trained_model, metrics = evaluate_model(name, pipeline, X_train, X_test, y_train, y_test)
        model_results.append(metrics)

        if best_metrics is None or metrics["ROC_AUC"] > best_metrics["ROC_AUC"]:
            best_model = trained_model
            best_metrics = metrics

    output_path = ARTIFACTS_DIR / "churn_model.pkl"
    joblib.dump(best_model, output_path)

    metrics_path = ARTIFACTS_DIR / "metrics.json"
    with open(metrics_path, "w") as f:
        json.dump(best_metrics, f, indent=2)

    print("\nModel comparison results:\n")
    for result in model_results:
        print(f"{result['Model']}: Accuracy={result['Accuracy']}, Precision={result['Precision']}, Recall={result['Recall']}, F1={result['F1']}, ROC_AUC={result['ROC_AUC']}")

    print(f"\nBest model selected: {best_metrics['Model']}")
    print(f"Saved best pipeline to: {output_path}")
    print(f"Saved metrics to: {metrics_path}")


if __name__ == "__main__":
    main()
