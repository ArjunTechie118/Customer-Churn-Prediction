import streamlit as st
import requests

# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="ChurnIQ - Predict Churn",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# API CONFIGURATION
# =========================================================
API_URL="https://customer-churn-prediction-api-gsqc.onrender.com/predict"

# =========================================================
# THEME
# =========================================================
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode=True

if st.session_state.dark_mode:
    bg_color="#0B0F19"
    card_color="#1E293B"
    text_color="#F8FAFC"
    muted_color="#CBD5E1"
    border_color="#334155"
    input_color="#111827"
    hover_color="#263449"
else:
    bg_color="#F8FAFC"
    card_color="#FFFFFF"
    text_color="#0F172A"
    muted_color="#475569"
    border_color="#CBD5E1"
    input_color="#FFFFFF"
    hover_color="#EFF6FF"

accent_color="#2563EB"
accent_light="#60A5FA"

# =========================================================
# CSS
# =========================================================
st.markdown(
    f"""
    <style>
    :root {{
        --bg-color:{bg_color};
        --card-color:{card_color};
        --text-color:{text_color};
        --muted-color:{muted_color};
        --border-color:{border_color};
        --input-color:{input_color};
        --hover-color:{hover_color};
        --accent-color:{accent_color};
        --accent-light:{accent_light};
    }}

    .stApp {{
        background-color:{bg_color};
        color:var(--text-color);
    }}

    .block-container {{
        padding-top:2rem;
        padding-left:4rem;
        padding-right:4rem;
        padding-bottom:4rem;
    }}

    /* PAGE HEADER */
    .page-header {{
        margin-top:15px;
        margin-bottom:35px;
    }}

    .page-badge {{
        display:inline-block;
        padding:7px 14px;
        border-radius:999px;
        background:rgba(37,99,235,.12);
        color:#60A5FA;
        font-size:13px;
        font-weight:700;
        margin-bottom:14px;
    }}

    .page-title {{
        color:var(--text-color)!important;
        font-size:42px;
        font-weight:800;
        line-height:1.15;
        margin:0;
    }}

    .page-title span {{
        color:#60A5FA!important;
    }}

    .page-description {{
        color:var(--muted-color)!important;
        font-size:16px;
        line-height:1.7;
        max-width:720px;
        margin-top:12px;
    }}

    /* FORM CARDS */
    .form-card {{
        background:var(--card-color);
        border:1px solid var(--border-color);
        border-radius:18px;
        padding:26px;
        margin-bottom:22px;
        transition:transform .2s ease,box-shadow .2s ease,border-color .2s ease;
    }}

    .form-card:hover {{
        transform:translateY(-3px);
        border-color:#60A5FA!important;
        box-shadow:0 12px 30px rgba(37,99,235,.14);
    }}

    .card-title {{
        color:var(--text-color)!important;
        font-size:20px;
        font-weight:750;
        margin-bottom:4px;
    }}

    .card-description {{
        color:var(--muted-color)!important;
        font-size:14px;
        margin-bottom:22px;
    }}

    /* STREAMLIT INPUTS */
    div[data-baseweb="select"] > div {{
        background-color:var(--input-color)!important;
        border-color:var(--border-color)!important;
        color:var(--text-color)!important;
    }}

    input {{
        background-color:var(--input-color)!important;
        color:var(--text-color)!important;
    }}

    label {{
        color:var(--text-color)!important;
    }}

    /* PREDICT BUTTON */
    div.stButton > button[kind="primary"] {{
        background-color:#2563EB!important;
        color:#FFFFFF!important;
        border:1px solid #2563EB!important;
        border-radius:10px!important;
        min-height:50px;
        font-size:16px!important;
        font-weight:700!important;
        transition:all .2s ease;
    }}

    div.stButton > button[kind="primary"]:hover {{
        background-color:#1D4ED8!important;
        border-color:#1D4ED8!important;
        box-shadow:0 8px 22px rgba(37,99,235,.25);
        transform:translateY(-2px);
    }}

    /* RESULT */
    .result-card {{
        background:var(--card-color);
        border:1px solid var(--border-color);
        border-radius:20px;
        padding:30px;
        margin-top:30px;
    }}

    .result-label {{
        color:var(--muted-color)!important;
        font-size:13px;
        font-weight:700;
        letter-spacing:.08em;
        text-transform:uppercase;
    }}

    .result-value {{
        color:var(--text-color)!important;
        font-size:32px;
        font-weight:800;
        margin-top:8px;
    }}

    .risk-high {{
        display:inline-block;
        background:rgba(239,68,68,.12);
        color:#F87171;
        border:1px solid rgba(239,68,68,.25);
        padding:8px 16px;
        border-radius:999px;
        font-weight:700;
        margin-top:12px;
    }}

    .risk-medium {{
        display:inline-block;
        background:rgba(245,158,11,.12);
        color:#FBBF24;
        border:1px solid rgba(245,158,11,.25);
        padding:8px 16px;
        border-radius:999px;
        font-weight:700;
        margin-top:12px;
    }}

    .risk-low {{
        display:inline-block;
        background:rgba(34,197,94,.12);
        color:#4ADE80;
        border:1px solid rgba(34,197,94,.25);
        padding:8px 16px;
        border-radius:999px;
        font-weight:700;
        margin-top:12px;
    }}

    .probability {{
        font-size:52px;
        font-weight:850;
        color:#60A5FA!important;
        line-height:1;
        margin:12px 0;
    }}

    .result-note {{
        color:var(--muted-color)!important;
        font-size:14px;
        line-height:1.6;
        margin-top:14px;
    }}

    @media(max-width:900px) {{
        .block-container {{
            padding-left:1.2rem;
            padding-right:1.2rem;
        }}

        .page-title {{
            font-size:34px;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# HEADER
# =========================================================
st.markdown(
    """
    <div class="page-header">
        <div class="page-badge">AI-Powered Churn Intelligence</div>
        <h1 class="page-title">
            Predict Customer <span>Churn</span>
        </h1>
        <p class="page-description">
            Enter customer information below and ChurnIQ will use the
            trained LightGBM model to estimate the customer's churn risk.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# CUSTOMER PROFILE
# =========================================================
st.markdown(
    """
    <div class="form-card">
        <div class="card-title">Customer Profile</div>
        <div class="card-description">
            Basic information about the customer.
        </div>
    """,
    unsafe_allow_html=True
)

col1,col2,col3=st.columns(3)

with col1:
    senior_citizen=st.selectbox(
        "Senior Citizen",
        ["No","Yes"]
    )

with col2:
    partner=st.selectbox(
        "Partner",
        ["No","Yes"]
    )

with col3:
    dependents=st.selectbox(
        "Dependents",
        ["No","Yes"]
    )

st.markdown("</div>",unsafe_allow_html=True)

# =========================================================
# SERVICE INFORMATION
# =========================================================
st.markdown(
    """
    <div class="form-card">
        <div class="card-title">Service Information</div>
        <div class="card-description">
            Services currently used by the customer.
        </div>
    """,
    unsafe_allow_html=True
)

col1,col2,col3=st.columns(3)

with col1:
    internet_service=st.selectbox(
        "Internet Service",
        ["Fibre optic","DSL","No"]
    )

with col2:
    online_security=st.selectbox(
        "Online Security",
        ["No","Yes"]
    )

with col3:
    online_backup=st.selectbox(
        "Online Backup",
        ["No","Yes"]
    )

col1,col2=st.columns(2)

with col1:
    device_protection=st.selectbox(
        "Device Protection",
        ["No","Yes"]
    )

with col2:
    tech_support=st.selectbox(
        "Tech Support",
        ["No","Yes"]
    )

st.markdown("</div>",unsafe_allow_html=True)

# =========================================================
# CONTRACT & BILLING
# =========================================================
st.markdown(
    """
    <div class="form-card">
        <div class="card-title">Contract & Billing</div>
        <div class="card-description">
            Contract, billing and customer tenure information.
        </div>
    """,
    unsafe_allow_html=True
)

col1,col2,col3=st.columns(3)

with col1:
    tenure_months=st.number_input(
        "Tenure Months",
        min_value=0,
        value=12,
        step=1
    )

with col2:
    contract=st.selectbox(
        "Contract",
        ["Month-to-month","One year","Two year"]
    )

with col3:
    paperless_billing=st.selectbox(
        "Paperless Billing",
        ["No","Yes"]
    )

col1,col2=st.columns(2)

with col1:
    payment_method=st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

with col2:
    monthly_charges=st.number_input(
        "Monthly Charges",
        min_value=18.25,
        max_value=118.75,
        value=70.00,
        step=0.25
    )

total_charges=st.number_input(
    "Total Charges",
    min_value=0.0,
    max_value=8684.80,
    value=840.0,
    step=10.0
)

st.markdown("</div>",unsafe_allow_html=True)

# =========================================================
# PREDICT
# =========================================================
st.markdown("<br>",unsafe_allow_html=True)

col1,col2,col3=st.columns([1,1.4,1])

with col2:
    predict_button=st.button(
        "🎯 Predict Churn",
        type="primary",
        use_container_width=True
    )

# =========================================================
# API PREDICTION
# =========================================================
if predict_button:

    payload={
        "Senior Citizen":senior_citizen,
        "Partner":partner,
        "Dependents":dependents,
        "Tenure Months":tenure_months,
        "Internet Service":internet_service,
        "Online Security":online_security,
        "Online Backup":online_backup,
        "Device Protection":device_protection,
        "Tech Support":tech_support,
        "Contract":contract,
        "Paperless Billing":paperless_billing,
        "Payment Method":payment_method,
        "Monthly Charges":monthly_charges,
        "Total Charges":total_charges
    }

    with st.spinner("Analyzing customer risk..."):

        try:
            response=requests.post(
                API_URL,
                json=payload,
                timeout=30
            )

            if response.status_code==200:

                result=response.json()

                prediction=result["prediction"]
                probability=float(result["churn_probability"])

                percentage=probability*100

                if prediction=="Churn":
                    if percentage>=70:
                        risk_level="HIGH RISK"
                        risk_class="risk-high"
                    else:
                        risk_level="MEDIUM RISK"
                        risk_class="risk-medium"
                else:
                    if percentage<30:
                        risk_level="LOW RISK"
                        risk_class="risk-low"
                    else:
                        risk_level="MEDIUM RISK"
                        risk_class="risk-medium"

                # =================================================
                # RESULT
                # =================================================
                st.markdown(
                    f"""
                    <div class="probability">
                        {percentage:.1f}%
                    </div>

                    <div class="result-label">
                        Prediction
                    </div>

                    <div class="result-value">
                        {prediction}
                    </div>

                    <div class="{risk_class}">
                        {risk_level}
                    </div>

                    <div class="result-note">
                        This prediction is generated by the trained
                        LightGBM model through the ChurnIQ FastAPI backend.
                        Explainability will be added through SHAP in the
                        next stage of the project.
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:
                st.error(
                    f"Prediction request failed. API returned status code {response.status_code}."
                )

                try:
                    st.json(response.json())
                except Exception:
                    st.write(response.text)

        except requests.exceptions.Timeout:
            st.error(
                "The prediction service took too long to respond. Please try again."
            )

        except requests.exceptions.ConnectionError:
            st.error(
                "Could not connect to the FastAPI prediction service. "
                "Please check that the API is running and the API URL is correct."
            )

        except Exception as e:
            st.error(f"Something went wrong: {e}")