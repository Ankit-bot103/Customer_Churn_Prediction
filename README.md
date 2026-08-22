# Customer Churn Prediction: Executive-Level ML Portfolio Project

## Executive Summary

This project is designed to solve a high-value business problem: predicting which customers are likely to churn so that a company can take proactive retention actions before revenue is lost. By combining data analysis, machine learning, and business interpretation, this project demonstrates how predictive analytics can support customer retention strategy and strategic decision-making.

The solution includes data preparation, exploratory analysis, model development, evaluation, explainability, and an interactive prediction interface. The project is structured to look like a real-world business analytics initiative rather than a simple academic exercise.

## Business Problem

Customer churn is one of the biggest challenges for subscription-based and service-based businesses. When customers leave, companies lose revenue, face reduced customer lifetime value, and often incur higher acquisition costs to replace them.

The business objective is to:

- identify customers with high churn risk
- understand which features drive churn
- prioritize retention campaigns for the most vulnerable users
- reduce revenue leakage through early intervention

## Business Value

This project creates real business value by allowing teams to:

- monitor churn risk in customer segments
- focus support and retention resources on high-risk accounts
- reduce unnecessary customer loss
- improve retention planning and strategic forecasting

## Project Scope

The project covers the full data science lifecycle:

- data collection and synthetic data generation
- cleaning and preprocessing
- exploratory data analysis
- model comparison and evaluation
- feature importance analysis using SHAP
- deployment through an interactive dashboard
- presentation-ready documentation and reporting

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- SHAP
- Streamlit
- Joblib
- python-pptx

## Project Structure

```text
ML Data associate project 2/
├── README.md
├── PROJECT_REPORT.md
├── requirements.txt
├── .gitignore
├── app.py
├── data/
│   └── customer_churn.csv
├── src/
│   ├── generate_data.py
│   ├── train_model.py
│   ├── feature_importance.py
│   └── create_project_slides.py
├── artifacts/
│   ├── churn_model.pkl
│   ├── metrics.json
│   └── shap_feature_importance.png
├── docs/
│   └── customer_churn_presentation.pptx
├── notebooks/
│   └── customer_churn_eda_and_portfolio_upgrade.ipynb
└── .venv/
```

## Methodology

1. Data generation and validation
2. Exploratory data analysis and trend discovery
3. Feature preprocessing and train-test split
4. Model selection across multiple algorithms
5. Performance comparison using business-focused metrics
6. Explainability with SHAP feature importance
7. Deployment as a live churn prediction dashboard
8. Reporting for stakeholder communication

## Model Performance

The current model performance is strong for a churn prediction use case and is suitable for portfolio demonstration.

Key metrics include:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

This model is selected based on a balance of business usefulness and statistical performance.

## Key Business Features

The project uses customer characteristics such as:

- tenure
- contract type
- monthly charges
- internet service
- payment method
- support coverage
- billing behavior
- service quality indicators

These features help explain why some customers are at a higher risk of leaving.

## How to Run the Project

### 1. Activate environment

```powershell
cd "C:\Users\mitta\OneDrive\Documents\Desktop\ML Data associate project 2"
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### 3. Generate data

```powershell
python src/generate_data.py
```

### 4. Train the model

```powershell
python src/train_model.py
```

### 5. Generate SHAP explainability chart

```powershell
python src/feature_importance.py
```

### 6. Generate the presentation deck

```powershell
python src/create_project_slides.py
```

### 7. Launch the application

```powershell
streamlit run app.py
```

## Project Outputs

This project produces:

- a trained churn prediction model
- model performance metrics
- SHAP interpretability chart
- PowerPoint presentation
- interactive dashboard for prediction
- professional project documentation

## Resume-Ready Summary

Developed an executive-level customer churn prediction project using Python, machine learning, and business analytics to identify customers at risk of leaving and support retention strategy. Performed data cleaning, exploratory analysis, feature preprocessing, model comparison, and evaluation using precision, recall, F1-score, and ROC-AUC. Added SHAP-based explainability and built an interactive Streamlit dashboard to present predictions and key risk drivers to business stakeholders.

## Why This Project Is Strong for Recruiters

This project demonstrates:

- end-to-end ML workflow experience
- ability to solve a real business problem
- knowledge of data preparation and model evaluation
- communication of technical findings to non-technical stakeholders
- deployment and presentation readiness

## Future Enhancements

- publish the dashboard on Streamlit Cloud
- add a Power BI dashboard version
- add customer cohort analysis and retention ROI modeling
- integrate with a real telecom dataset for enterprise-style validation

## License

This project is intended for learning, portfolio development, and professional resume enhancement.
