import streamlit as st
import requests

API_URL = st.secrets["API_URL"]

st.title("📊 Customer Churn Prediction")

st.write(
    "Enter customer details below to estimate the customer's churn risk."
)


with st.form("churn_prediction_form"):

    st.subheader("Customer Information")

    col1, col2 = st.columns(2)

    with col1:

        senior_citizen = st.selectbox(
            "Senior Citizen",
            ["No", "Yes"]
        )

        partner = st.selectbox(
            "Partner",
            ["No", "Yes"]
        )

        dependents = st.selectbox(
            "Dependents",
            ["No", "Yes"]
        )

        tenure_months = st.number_input(
            "Tenure Months",
            min_value=0,
            step=1
        )

        internet_service = st.selectbox(
            "Internet Service",
            ["Fibre optic", "DSL", "No"]
        )

        online_security = st.selectbox(
            "Online Security",
            ["No", "Yes"]
        )

        online_backup = st.selectbox(
            "Online Backup",
            ["No", "Yes"]
        )

    with col2:

        device_protection = st.selectbox(
            "Device Protection",
            ["No", "Yes"]
        )

        tech_support = st.selectbox(
            "Tech Support",
            ["No", "Yes"]
        )

        contract = st.selectbox(
            "Contract",
            ["Month-to-month", "One year", "Two year"]
        )

        paperless_billing = st.selectbox(
            "Paperless Billing",
            ["No", "Yes"]
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

        monthly_charges = st.number_input(
            "Monthly Charges",
            min_value=18.25,
            max_value=118.75,
            step=0.01
        )

        total_charges = st.number_input(
            "Total Charges",
            min_value=0.0,
            max_value=8684.80,
            step=0.01
        )

    submitted = st.form_submit_button(
        "🔮 Predict Churn",
        use_container_width=True
    )


if submitted:

    payload = {
        "Senior Citizen": senior_citizen,
        "Partner": partner,
        "Dependents": dependents,
        "Tenure Months": tenure_months,
        "Internet Service": internet_service,
        "Online Security": online_security,
        "Online Backup": online_backup,
        "Device Protection": device_protection,
        "Tech Support": tech_support,
        "Contract": contract,
        "Paperless Billing": paperless_billing,
        "Payment Method": payment_method,
        "Monthly Charges": monthly_charges,
        "Total Charges": total_charges
    }

    try:

        response = requests.post(
            f"{API_URL}/predict",
            json=payload
        )
        if response.status_code == 200:

            result = response.json()

            probability = result["churn_probability"] * 100

            if result["prediction"] == "Churn":

                st.error(
                    f"⚠️ Churn Risk: {probability:.2f}%"
                )

            else:

                st.success(
                    f"✅ No Churn: {probability:.2f}%"
                )

        else:

            st.error(
                f"Prediction request failed. Status code: {response.status_code}"
            )

    except requests.exceptions.ConnectionError:

        st.error(
            "Unable to connect to the FastAPI backend. "
            "Make sure the FastAPI server is running."
        )