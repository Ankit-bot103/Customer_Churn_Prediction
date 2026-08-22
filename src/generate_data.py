import numpy as np
import pandas as pd
from pathlib import Path


def generate_churn_dataset(output_path: str = "data/customer_churn.csv", n_rows: int = 2500) -> pd.DataFrame:
    rng = np.random.default_rng(42)

    df = pd.DataFrame({
        "CustomerID": [f"CUST_{i:05d}" for i in range(1, n_rows + 1)],
        "Gender": rng.choice(["Male", "Female"], size=n_rows),
        "SeniorCitizen": rng.choice([0, 1], p=[0.82, 0.18], size=n_rows),
        "Partner": rng.choice(["Yes", "No"], p=[0.52, 0.48], size=n_rows),
        "Dependents": rng.choice(["Yes", "No"], p=[0.32, 0.68], size=n_rows),
        "TenureMonths": rng.integers(1, 72, size=n_rows),
        "PhoneService": rng.choice(["Yes", "No"], p=[0.94, 0.06], size=n_rows),
        "MultipleLines": rng.choice(["No", "Yes", "No phone service"], p=[0.45, 0.35, 0.20], size=n_rows),
        "InternetService": rng.choice(["DSL", "Fiber optic", "No"], p=[0.38, 0.42, 0.20], size=n_rows),
        "OnlineSecurity": rng.choice(["Yes", "No", "No internet service"], p=[0.30, 0.45, 0.25], size=n_rows),
        "OnlineBackup": rng.choice(["Yes", "No", "No internet service"], p=[0.32, 0.43, 0.25], size=n_rows),
        "DeviceProtection": rng.choice(["Yes", "No", "No internet service"], p=[0.30, 0.45, 0.25], size=n_rows),
        "TechSupport": rng.choice(["Yes", "No", "No internet service"], p=[0.28, 0.47, 0.25], size=n_rows),
        "StreamingTV": rng.choice(["Yes", "No", "No internet service"], p=[0.48, 0.27, 0.25], size=n_rows),
        "StreamingMovies": rng.choice(["Yes", "No", "No internet service"], p=[0.49, 0.26, 0.25], size=n_rows),
        "Contract": rng.choice(["Month-to-month", "One year", "Two year"], p=[0.56, 0.25, 0.19], size=n_rows),
        "PaperlessBilling": rng.choice(["Yes", "No"], p=[0.61, 0.39], size=n_rows),
        "PaymentMethod": rng.choice([
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ], p=[0.42, 0.18, 0.20, 0.20], size=n_rows),
        "MonthlyCharges": rng.uniform(20, 120, size=n_rows).round(2),
        "TotalCharges": np.nan,
    })

    # Create realistic total charges based on tenure and monthly charges
    df["TotalCharges"] = df["MonthlyCharges"] * df["TenureMonths"] + rng.normal(0, 35, size=n_rows)
    df["TotalCharges"] = np.clip(df["TotalCharges"], 0, None).round(2)

    # Build churn probability through realistic risk factors
    tenure_term = -0.035 * df["TenureMonths"]
    month_risk = 0.025 * df["MonthlyCharges"]
    fiber_risk = np.where(df["InternetService"] == "Fiber optic", 1.2, 0)
    contract_risk = np.where(df["Contract"] == "Month-to-month", 1.0, np.where(df["Contract"] == "One year", 0.2, -0.5))
    payment_risk = np.where(df["PaymentMethod"] == "Electronic check", 0.9, 0)
    support_risk = np.where(df["TechSupport"] == "No", 0.8, 0)
    online_security_risk = np.where(df["OnlineSecurity"] == "No", 0.6, 0)
    senior_risk = 0.5 * df["SeniorCitizen"]
    paperless_risk = 0.35 * (df["PaperlessBilling"] == "Yes")

    linear_score = (
        tenure_term
        + month_risk
        + fiber_risk
        + contract_risk
        + payment_risk
        + support_risk
        + online_security_risk
        + senior_risk
        + paperless_risk
    )

    prob = 1 / (1 + np.exp(-linear_score))
    churn = rng.binomial(1, prob)
    df["Churn"] = churn

    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_file, index=False)
    print(f"Dataset saved to: {output_file} | Rows: {len(df)} | Churn rate: {df['Churn'].mean():.2f}")
    return df


if __name__ == "__main__":
    generate_churn_dataset()
