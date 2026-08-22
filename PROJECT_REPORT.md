# Customer Churn Prediction Project Report

## 1. Project Overview

This project focuses on predicting whether a customer is likely to churn from a telecom or subscription-based service. Churn prediction is a critical business problem because retaining an existing customer is usually more cost-effective than acquiring a new one.

The goal of this project is to build a machine learning model that can identify at-risk customers early so the business can take preventive action, such as retention offers, support intervention, or customer success outreach.

## 2. Business Problem

Customer turnover directly impacts revenue, service quality, and long-term brand value. Businesses need to understand which customer groups are more likely to leave and why.

This project helps answer:

- Which customers are most likely to churn?
- Which features are more strongly associated with churn?
- What business actions can reduce churn?

## 3. Data and Features

The dataset includes customer attributes such as:

- Demographic information: gender, senior citizen, dependents
- Service usage: tenure, monthly charges, total charges
- Subscription details: contract type, internet service, payment method
- Support and service quality: tech support, online security, streaming services
- Billing behavior: paperless billing, payment method

## 4. Methodology

The project follows a standard machine learning workflow:

1. Data generation and loading
2. Data cleaning and validation
3. Exploratory data analysis
4. Feature preprocessing
5. Train-test split
6. Model comparison
7. Model evaluation
8. Result interpretation and recommendations

## 5. Models Compared

The pipeline compares multiple classification models, including:

- Logistic Regression
- Random Forest
- Gradient Boosting

The selected model is based mainly on ROC-AUC and F1-score, as both are important when dealing with customer retention classification and imbalance.

## 6. Key Results

The trained model achieved strong performance and demonstrated the ability to separate churn and non-churn customers effectively.

Example results:

- Accuracy: approximately 90%
- Precision: strong for churn detection
- Recall: high for churn identification
- F1-score: strong balance between precision and recall
- ROC-AUC: good ranking power for churn likelihood

## 7. Business Interpretation

The analysis indicates that churn is often associated with:

- Shorter customer tenure
- Higher monthly charges
- Fiber optic internet plans
- Month-to-month contracts
- Lack of technical support
- Electronic check payment method
- Paperless billing behavior

These insights help a business prioritize customer retention efforts for the most at-risk groups.

## 8. Practical Impact

This project is useful for:

- Customer success teams
- Sales and retention teams
- Subscription business management
- Data-driven decision-making in product and operations

By identifying churn risk early, businesses can reduce customer loss and improve customer lifetime value.

## 9. Tools Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit

## 10. Conclusion

This project demonstrates practical machine learning and data analysis skills relevant to a data-driven business environment. It is a strong portfolio piece for a role in ML, data analysis, or data associate work because it combines technical execution with business understanding.

## 11. Resume-Friendly Summary

Developed a customer churn prediction project using Python and machine learning to identify customers at risk of leaving and support retention strategies. Conducted data cleaning, exploratory analysis, feature preprocessing, model comparison, and evaluation using metrics such as accuracy, precision, recall, F1-score, and ROC-AUC. Built an interactive Streamlit dashboard to present customer risk predictions and business insights.
