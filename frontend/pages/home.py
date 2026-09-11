import streamlit as st
import textwrap


# =========================================================
# HOME PAGE CSS
# =========================================================

st.markdown(
    textwrap.dedent(
        """
        <style>

        /* =================================================
           HERO SECTION
           ================================================= */

        .hero {
            text-align: center;
            padding: 75px 20px 40px 20px;
        }

        .hero h1 {
            font-size: 56px;
            font-weight: 800;
            color: var(--text-color) !important;
            line-height: 1.15;
            margin: 0 0 20px 0;
        }

        .hero h1 span {
            color: #2563EB !important;
        }


        /* =================================================
           HERO DESCRIPTION
           ================================================= */

        .hero-description {
            text-align: center;

            font-size: 20px;

            color: var(--muted-color) !important;

            max-width: 760px;

            margin: 0 auto 30px auto;

            line-height: 1.6;
        }


        /* =================================================
           SECTION TITLES
           ================================================= */

        .section-title {
            text-align: center;

            color: var(--text-color) !important;

            font-size: 30px;

            font-weight: 700;

            margin-top: 50px;

            margin-bottom: 28px;
        }


        /* =================================================
           FEATURE CARDS
           ================================================= */

        .feature-card {
            background-color: var(--card-color) !important;

            border: 1px solid var(--border-color);

            border-radius: 16px;

            padding: 26px 20px;

            text-align: center;

            min-height: 180px;

            display: flex;

            flex-direction: column;

            justify-content: center;

            box-sizing: border-box;

            box-shadow:
                0 5px 16px rgba(0, 0, 0, 0.10);

            transition:
                transform 0.2s ease,
                box-shadow 0.2s ease,
                border-color 0.2s ease;
        }


        .feature-card:hover {
            transform: translateY(-3px);

            border-color: var(--accent-color);

            box-shadow:
                0 10px 25px rgba(0, 0, 0, 0.14);
        }


        .feature-card h3 {
            color: #60A5FA !important;

            font-size: 20px;

            font-weight: 700;

            margin: 0 0 14px 0;
        }


        .feature-card p {
            color: var(--muted-color) !important;

            font-size: 15px;

            line-height: 1.6;

            margin: 0;
        }


        /* =================================================
           HOW IT WORKS
           ================================================= */

        .step-card {
            background-color: var(--card-color) !important;

            border: 1px solid var(--border-color);

            border-radius: 14px;

            padding: 24px 15px;

            text-align: center;

            min-height: 135px;

            display: flex;

            flex-direction: column;

            justify-content: center;

            box-sizing: border-box;

            box-shadow:
                0 4px 14px rgba(0, 0, 0, 0.08);

            transition:
                transform 0.2s ease,
                border-color 0.2s ease;
        }


        .step-card:hover {
            transform: translateY(-3px);

            border-color: var(--accent-color);
        }


        .step-number {
            color: #60A5FA !important;

            font-size: 24px;

            font-weight: 800;

            line-height: 1.2;
        }


        .step-text {
            color: var(--muted-color) !important;

            font-size: 15px;

            line-height: 1.5;

            margin-top: 10px;
        }


        /* =================================================
           FOOTER
           ================================================= */

        .footer {
            text-align: center;

            color: var(--muted-color) !important;

            font-size: 14px;

            margin-top: 65px;

            padding: 25px 10px;

            border-top: 1px solid var(--border-color);
        }


        /* =================================================
           MOBILE
           ================================================= */

        @media (max-width: 900px) {

            .hero {
                padding-top: 45px;
            }

            .hero h1 {
                font-size: 40px;
            }

            .hero-description {
                font-size: 17px;
            }

            .section-title {
                font-size: 26px;
            }

        }

        </style>
        """
    ),
    unsafe_allow_html=True
)


# =========================================================
# HERO
# =========================================================

st.markdown(
    """
    <div class="hero">
        <h1>
            Predict Customer Churn<br>
            <span>Before It Happens</span>
        </h1>
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# DESCRIPTION
# =========================================================

st.markdown(
    """
    <div class="hero-description">
        An end-to-end machine learning application that estimates
        customer churn risk using customer, service, contract,
        and billing information.
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# PREDICT BUTTON
# =========================================================

col1, col2, col3 = st.columns(
    [1, 1.2, 1]
)

with col2:

    if st.button(
        "🔮 Predict Customer Churn",
        use_container_width=True,
        type="primary"
    ):

        st.switch_page("pages/predict.py")


# =========================================================
# BUILT WITH
# =========================================================

st.markdown(
    '<div class="section-title">Built With</div>',
    unsafe_allow_html=True
)


col1, col2, col3, col4 = st.columns(4)


# ---------- Card 1 ----------

with col1:

    st.markdown(
        """
        <div class="feature-card">
            <h3>🤖 Machine Learning</h3>
            <p>
                Customer churn prediction powered by
                a trained LightGBM model.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------- Card 2 ----------

with col2:

    st.markdown(
        """
        <div class="feature-card">
            <h3>⚡ FastAPI</h3>
            <p>
                A fast REST API serving real-time
                churn predictions.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------- Card 3 ----------

with col3:

    st.markdown(
        """
        <div class="feature-card">
            <h3>🎨 Streamlit</h3>
            <p>
                An interactive and user-friendly
                interface for making predictions.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------- Card 4 ----------

with col4:

    st.markdown(
        """
        <div class="feature-card">
            <h3>💡 LightGBM</h3>
            <p>
                A powerful gradient boosting model used
                for accurate customer churn prediction.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# HOW IT WORKS
# =========================================================

st.markdown(
    '<div class="section-title">How It Works</div>',
    unsafe_allow_html=True
)


col1, col2, col3, col4 = st.columns(4)


steps = [
    ("01", "Enter customer information"),
    ("02", "FastAPI validates the input"),
    ("03", "LightGBM analyzes the customer"),
    ("04", "Get the churn risk prediction")
]


for col, (number, text) in zip(
    [col1, col2, col3, col4],
    steps
):

    with col:

        st.markdown(
            f"""
            <div class="step-card">
                <div class="step-number">
                    {number}
                </div>
                <div class="step-text">
                    {text}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        Customer Churn Prediction
        •
        Machine Learning Project
    </div>
    """,
    unsafe_allow_html=True
)