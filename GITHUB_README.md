# Customer Churn Prediction

## Overview
This project focuses on predicting customer churn for a subscription-based or telecom business. The goal is to help businesses identify customers who are likely to leave and take proactive retention actions before revenue is lost.

Customer churn is a critical business challenge because retaining existing customers is often more cost-effective than acquiring new ones. This project applies data science and machine learning to support smarter business decisions and improve customer retention strategies.

## Business Problem
Businesses often struggle to identify which customers are at risk of leaving. Without early detection, retention teams may not act soon enough, resulting in revenue loss and lower customer lifetime value.

This project addresses the problem by:

- analyzing customer behavior and subscription patterns
- identifying churn risk factors
- predicting likely churners using machine learning
- helping teams prioritize retention actions

## Objectives
- Build a reliable customer churn prediction model
- Understand the strongest churn drivers
- Provide actionable business insights
- Create a simple, interactive dashboard for prediction

## Dataset
The project uses synthetic customer data designed to mimic a telecom or subscription environment. It includes features such as:

- tenure
- monthly charges
- total charges
- contract type
- internet service
- payment method
- billing pattern
- support and service quality indicators

## Methodology

1. Data generation and validation
2. Data cleaning and preprocessing
3. Exploratory data analysis
4. Feature engineering and transformation
5. Train-test split
6. Model comparison using multiple classifiers
7. Evaluation with accuracy, precision, recall, F1-score, and ROC-AUC
8. SHAP-based explainability for feature importance
9. Deployment through a Streamlit app

## Models Evaluated
- Logistic Regression
- Random Forest
- Gradient Boosting

## Best Model
The final selected model is Logistic Regression, based on overall predictive performance and business relevance.

## Key Metrics
- Accuracy: 0.908
- Precision: 0.919
- Recall: 0.984
- F1-score: 0.950
- ROC-AUC: 0.885

## Key Findings
The project revealed that churn risk is strongly associated with:

- shorter customer tenure
- month-to-month contract types
- higher monthly charges
- fiber-optic internet service
- lack of technical support
- electronic check payment behavior

These insights can help retention teams focus on high-risk customer segments and reduce churn.

## Project Structure

```text
ML Data associate project 2/
├── README.md
├── GITHUB_README.md
├── PROJECT_REPORT.md
├── PROJECT_SUMMARY.md
├── RESUME_BULLETS.md
├── requirements.txt
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

## Run the Project

### 1. Activate the virtual environment

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

### 5. Run the app

```powershell
streamlit run app.py
```

## Dashboard
The project includes a Streamlit dashboard that accepts customer inputs and predicts churn likelihood in real time.

## Explainability
The project also includes SHAP feature importance analysis to explain which features contribute most to churn predictions.

## Impact
This project demonstrates how data science can support strategic customer retention decisions and deliver measurable business value.

## Future Improvements
- deploy the app on Streamlit Cloud
- add a Power BI dashboard
- integrate a real-world telecom dataset
- create a customer retention ROI model

## Tools Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- SHAP
- Streamlit
- Joblib

## License
This project is intended for portfolio, learning, and resume-building purposes.
