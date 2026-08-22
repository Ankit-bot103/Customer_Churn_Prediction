from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import shap

DATA_PATH = Path("data/customer_churn.csv")
MODEL_PATH = Path("artifacts/churn_model.pkl")
OUTPUT_DIR = Path("artifacts")
OUTPUT_DIR.mkdir(exist_ok=True)


def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError("Dataset not found. Run: python src/generate_data.py")
    if not MODEL_PATH.exists():
        raise FileNotFoundError("Model not found. Run: python src/train_model.py")

    df = pd.read_csv(DATA_PATH)
    model = joblib.load(MODEL_PATH)

    X = df.drop(columns=["Churn", "CustomerID"])
    transformed_X = model.named_steps["preprocessor"].transform(X)

    if hasattr(transformed_X, "toarray"):
        transformed_X = transformed_X.toarray()

    transformed_X = np.asarray(transformed_X)
    model_to_explain = model.named_steps["model"]

    explainer = shap.Explainer(model_to_explain, transformed_X)
    shap_values = explainer(transformed_X)

    plt.figure(figsize=(10, 7))
    shap.plots.beeswarm(shap_values, max_display=15)
    plt.tight_layout()
    output_file = OUTPUT_DIR / "shap_feature_importance.png"
    plt.savefig(output_file, dpi=200)
    plt.close()

    print(f"SHAP plot saved to: {output_file}")
    print("Top features influencing churn risk are shown in the visualization.")


if __name__ == "__main__":
    main()
