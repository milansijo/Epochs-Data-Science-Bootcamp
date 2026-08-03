import streamlit as st
import joblib
import pandas as pd

# -----------------------
# Load Model
# -----------------------
model = joblib.load("models/model.pkl")

# -----------------------
# Page Config
# -----------------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📞",
    layout="wide"
)

st.title("📞 Customer Churn Prediction")

st.write(
    """
Predict whether a customer is likely to churn based on
customer information.
"""
)

st.sidebar.header("Customer Details")

# -----------------------
# Inputs
# -----------------------

age = st.sidebar.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=30
)

gender = st.sidebar.selectbox(
    "Gender",
    ["Male", "Female"]
)

tenure = st.sidebar.number_input(
    "Tenure",
    min_value=0,
    max_value=100,
    value=10
)

usage_frequency = st.sidebar.number_input(
    "Usage Frequency",
    min_value=0,
    max_value=100,
    value=20
)

support_calls = st.sidebar.number_input(
    "Support Calls",
    min_value=0,
    max_value=20,
    value=2
)

payment_delay = st.sidebar.number_input(
    "Payment Delay",
    min_value=0,
    max_value=100,
    value=5
)

subscription_type = st.sidebar.selectbox(
    "Subscription Type",
    ["Basic", "Standard", "Premium"]
)

contract_length = st.sidebar.selectbox(
    "Contract Length",
    ["Monthly", "Quarterly", "Annual"]
)

total_spend = st.sidebar.number_input(
    "Total Spend",
    min_value=0.0,
    value=500.0
)

last_interaction = st.sidebar.number_input(
    "Last Interaction (days)",
    min_value=0,
    max_value=365,
    value=10
)

# -----------------------
# Prediction
# -----------------------

if st.button("Predict Churn"):

    input_data = pd.DataFrame({

        "Age":[age],
        "Gender":[gender],
        "Tenure":[tenure],
        "Usage Frequency":[usage_frequency],
        "Support Calls":[support_calls],
        "Payment Delay":[payment_delay],
        "Subscription Type":[subscription_type],
        "Contract Length":[contract_length],
        "Total Spend":[total_spend],
        "Last Interaction":[last_interaction]

    })

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0]

    st.subheader("Prediction")

    if prediction == 1:

        st.error("⚠️ Customer is likely to Churn")

    else:

        st.success("✅ Customer is likely to Stay")

    st.subheader("Prediction Probability")

    st.write(f"Stay : {probability[0]*100:.2f}%")

    st.write(f"Churn : {probability[1]*100:.2f}%")

st.markdown("---")

st.caption("Developed by Milan Sijo")