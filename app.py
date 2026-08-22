import joblib
import pandas as pd
import streamlit as st

MODEL_PATH = "artifacts/churn_model.pkl"

st.set_page_config(page_title="Customer Churn Predictor", page_icon="📉", layout="wide")

st.title("Customer Churn Prediction Dashboard")

if not MODEL_PATH:
    st.error("Model file not found. Please run the training script first.")
    st.stop()

try:
    model = joblib.load(MODEL_PATH)
except FileNotFoundError:
    st.error("Model file not found. Please run: python src/train_model.py")
    st.stop()

st.subheader("Input customer details")

with st.form("churn_form"):
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior_citizen = st.selectbox("Senior citizen", [0, 1])
    partner = st.selectbox("Partner", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["Yes", "No"])
    tenure_months = st.slider("Tenure (months)", 1, 72, 12)
    phone_service = st.selectbox("Phone service", ["Yes", "No"])
    multiple_lines = st.selectbox("Multiple lines", ["No", "Yes", "No phone service"])
    internet_service = st.selectbox("Internet service", ["DSL", "Fiber optic", "No"])
    online_security = st.selectbox("Online security", ["Yes", "No", "No internet service"])
    online_backup = st.selectbox("Online backup", ["Yes", "No", "No internet service"])
    device_protection = st.selectbox("Device protection", ["Yes", "No", "No internet service"])
    tech_support = st.selectbox("Tech support", ["Yes", "No", "No internet service"])
    streaming_tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
    streaming_movies = st.selectbox("Streaming movies", ["Yes", "No", "No internet service"])
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    paperless_billing = st.selectbox("Paperless billing", ["Yes", "No"])
    payment_method = st.selectbox(
        "Payment method",
        ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"],
    )
    monthly_charges = st.number_input("Monthly charges", min_value=5.0, max_value=200.0, value=65.0)
    total_charges = st.number_input("Total charges", min_value=0.0, max_value=10000.0, value=500.0)

    submitted = st.form_submit_button("Predict churn")

if submitted:
    input_df = pd.DataFrame(
        [{
            "Gender": gender,
            "SeniorCitizen": senior_citizen,
            "Partner": partner,
            "Dependents": dependents,
            "TenureMonths": tenure_months,
            "PhoneService": phone_service,
            "MultipleLines": multiple_lines,
            "InternetService": internet_service,
            "OnlineSecurity": online_security,
            "OnlineBackup": online_backup,
            "DeviceProtection": device_protection,
            "TechSupport": tech_support,
            "StreamingTV": streaming_tv,
            "StreamingMovies": streaming_movies,
            "Contract": contract,
            "PaperlessBilling": paperless_billing,
            "PaymentMethod": payment_method,
            "MonthlyCharges": monthly_charges,
            "TotalCharges": total_charges,
        }]
    )

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0, 1]

    st.subheader("Prediction Result")
    if prediction == 1:
        st.error(f"High risk of churn: {probability * 100:.1f}% likely to churn")
    else:
        st.success(f"Low risk of churn: {probability * 100:.1f}% likely to churn")

    st.write("Model probability of churn:", round(probability, 3))
