# Project Questions and Answers

## 1. What is this project about?
This project is a customer churn prediction system built to identify customers who are likely to leave a service or subscription. The goal is to help businesses reduce churn by taking early retention actions.

## 2. Why is this project important?
Customer churn directly affects revenue, customer lifetime value, and business growth. By predicting which customers are likely to leave, companies can focus retention efforts on the right customers and reduce losses.

## 3. What is the business problem being solved?
The business problem is to detect high-risk customers before they churn and take preventive actions such as retention offers, support outreach, or tailored communication.

## 4. What technologies were used?
The project uses Python, Pandas, NumPy, Scikit-learn, Seaborn, Matplotlib, SHAP, and Streamlit. These tools were used for data processing, model building, analysis, visualization, and deployment.

## 5. What type of data is used?
The project uses customer-level data with features such as tenure, contract type, internet service, monthly charges, billing method, payment method, and support-related attributes.

## 6. What is the target variable?
The target variable is Churn, which indicates whether a customer is likely to leave or stay.

## 7. What models were used?
The project compares multiple models, including Logistic Regression, Random Forest, and Gradient Boosting, and selects the best-performing model based on evaluation metrics.

## 8. Which model performed best?
The Logistic Regression model performed best in this project based on the selected evaluation metrics such as accuracy, precision, recall, F1-score, and ROC-AUC.

## 9. What metrics were used to evaluate the model?
The model was evaluated using accuracy, precision, recall, F1-score, and ROC-AUC. These metrics help measure both predictive power and business usefulness.

## 10. What is the key insight from the project?
The project shows that customer churn is influenced by factors such as shorter tenure, month-to-month contracts, higher monthly charges, limited support, and certain payment methods.

## 11. What is SHAP and why is it useful?
SHAP stands for SHapley Additive exPlanations. It is used to explain the contribution of each feature to a model's prediction, helping business stakeholders understand why a customer is predicted to churn.

## 12. How did you handle data cleaning and preprocessing?
I cleaned the dataset by validating the structure, handling missing values, converting categorical information to a consistent format, and preparing the features for model input. I also separated numerical and categorical variables so the pipeline could process them correctly.

## 13. What is exploratory data analysis and why is it important?
Exploratory Data Analysis (EDA) is the process of understanding the dataset through summaries, distributions, and visualizations. It helps identify patterns, anomalies, and relationships between customer features and churn behavior before building the model.

## 14. What is feature engineering in this project?
Feature engineering involved selecting the most relevant customer attributes and preparing them in a format suitable for machine learning. This included handling categorical variables, scaling numerical features, and ensuring the model could learn from meaningful signals like tenure, contract type, and monthly charges.

## 15. How did you decide which machine learning model to use?
I compared multiple models, including Logistic Regression, Random Forest, and Gradient Boosting, and selected the model based on how well it performed on relevant metrics and how useful it was for business decision-making.

## 16. Which evaluation metrics did you use and why?
I used accuracy, precision, recall, F1-score, and ROC-AUC because they provide a balanced view of model performance. These metrics are especially useful when working with customer churn, where identifying high-risk customers correctly is critical.

## 17. How did you generate business-oriented insights from the model?
I analyzed the model output and feature importance to identify which customer attributes were most associated with churn. This allowed me to translate the technical model into actionable business insights like prioritizing retention for at-risk segments.

## 18. What does model explainability mean in this project?
Model explainability means understanding and communicating why the model made a prediction. In this project, SHAP helped show which features contributed most to churn predictions, making the results easier to explain to non-technical stakeholders.

## 19. How did you deploy the solution?
I deployed the trained model through a Streamlit dashboard, where users can enter customer details and get a churn risk prediction in real time. This makes the project more practical and presentation-friendly.

## 20. Why is this project useful for a resume?
This project demonstrates skills in machine learning, data analytics, model evaluation, feature importance analysis, and dashboard deployment, which are highly relevant for ML Data Associate and data-focused roles.

## 21. What is the deployment part of the project?
A Streamlit application was created so users can input customer information and get a churn prediction in real time.

## 22. What is the business impact of the project?
The project can help companies reduce revenue loss, improve retention strategy, increase customer lifetime value, and make more informed decisions about customer engagement.

## 23. How does this project relate to real-world business problems?
This project reflects a real business challenge in telecom and subscription-based industries, where forecasting customer churn is crucial for maintaining revenue and customer satisfaction.

## 24. What is the GitHub URL for this project?
https://github.com/Ankit-bot103/Customer_Churn_Prediction

## 25. How can I explain this project in an interview?
I can explain it as: "I built a customer churn prediction model to identify at-risk customers and support retention strategies. I cleaned and analyzed customer data, evaluated multiple models, used SHAP to explain feature importance, and deployed the solution as an interactive dashboard."

## 26. What makes this project stand out?
It combines technical execution with business value. The project does not only train a model; it also explains the results, demonstrates practical impact, and includes deployment and presentation-ready materials.

## 27. Can this project be improved further?
Yes, future improvements could include real-world industry datasets, dashboards in Power BI, deployment on Streamlit Cloud, and integration with customer segmentation or retention ROI analysis.

## 28. What is the overall conclusion?
This project is a strong portfolio example because it shows data analysis, machine learning, business problem solving, communication of insights, and a practical deployment layer in a real-world context.
