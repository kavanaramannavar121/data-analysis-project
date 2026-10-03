import streamlit as st
import pandas as pd
import joblib

model = joblib.load("churn_model.pkl")
preprocessor = joblib.load("preprocessor.pkl")

st.title("📊 Customer Churn Prediction")
st.write("Enter customer details to predict whether the customer is likely to churn.")
customer_id = st.text_input("Customer ID")

age = st.number_input("Age", min_value=18, max_value=100, value=30)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

tenure = st.number_input(
    "Tenure (months)",
    min_value=0,
    max_value=100,
    value=12
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=50.0
)

contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

payment_method = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

total_charges = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=500.0
)
st.subheader("Prediction")

if st.button("Predict Churn"):

    input_data = pd.DataFrame([{
        "CustomerID": customer_id,
        "Age": age,
        "Gender": gender,
        "Tenure": tenure,
        "MonthlyCharges": monthly_charges,
        "Contract": contract,
        "PaymentMethod": payment_method,
        "TotalCharges": total_charges
    }])

    processed_data = preprocessor.transform(input_data)

    prediction = model.predict(processed_data)[0]

    if prediction == "Yes":
        st.error("⚠️ Customer is likely to churn.")
    else:
        st.success("✅ Customer is likely to stay.")