import streamlit as st

# =========================================================
# THEME
# =========================================================

dark_mode = st.session_state.get("dark_mode", False)

if dark_mode:
    bg_color = "#0B0F19"
    card_color = "#1E293B"
    text_color = "#F8FAFC"
    muted_color = "#CBD5E1"
    border_color = "#334155"
    hover_color = "#263449"
else:
    bg_color = "#F8FAFC"
    card_color = "#FFFFFF"
    text_color = "#0F172A"
    muted_color = "#475569"
    border_color = "#CBD5E1"
    hover_color = "#EFF6FF"

# =========================================================
# CSS
# =========================================================

st.markdown(
    f"""
    <style>

    :root {{
        --bg-color: #F8FAFC;
        --card-color: #FFFFFF;
        --text-color: #0F172A;
        --muted-color: #475569;
        --border-color: #CBD5E1;
        --input-color: #FFFFFF;
        --hover-color: #EFF6FF;
        --accent-color: #2563EB;
        --accent-light: #60A5FA;
    }}

    .stApp {{
        background-color:var(--bg-color);
        color:var(--text-color);
    }}

    .block-container {{
        padding-top:2rem;
        padding-left:4rem;
        padding-right:4rem;
        padding-bottom:5rem;
    }}
    .connect-links{{
        display:flex;
        justify-content:center;
        align-items:center;
        gap:12px;
        margin-top:22px;
        flex-wrap:wrap;
        }}
    .connect-links a{{
        color:var(--text-color)!important;
        text-decoration:none!important;
        font-size:14px;
        font-weight:600;
        padding:9px 16px;
        border:1px solid var(--border-color);
        border-radius:9px;
        background:var(--card-color);
        transition:all .2s ease;
    }}
    .connect-links a:hover{{
        color:#60A5FA!important;
        border-color:#60A5FA;
        transform:translateY(-2px);
        box-shadow:0 6px 18px rgba(37,99,235,.15);
    }}
    /* =================================================
       HERO
       ================================================= */

    .about-hero {{
        position:relative;
        overflow:hidden;
        background:linear-gradient(
            135deg,
            var(--card-color),
            rgba(37,99,235,.08)
        );
        border:1px solid var(--border-color);
        border-radius:24px;
        padding:55px;
        margin-top:15px;
        margin-bottom:45px;
    }}

    .about-hero::before {{
        content:"";
        position:absolute;
        width:280px;
        height:280px;
        border-radius:50%;
        background:rgba(37,99,235,.10);
        right:-80px;
        top:-100px;
        filter:blur(5px);
    }}

    .about-badge {{
        display:inline-block;
        padding:7px 15px;
        border-radius:999px;
        background:rgba(37,99,235,.12);
        border:1px solid rgba(96,165,250,.20);
        color:#60A5FA;
        font-size:13px;
        font-weight:800;
        letter-spacing:.3px;
        margin-bottom:18px;
    }}

    .about-title {{
        font-size:46px;
        line-height:1.1;
        font-weight:850;
        color:var(--text-color);
        margin:0;
    }}

    .about-title span {{
        color:#60A5FA;
    }}

    .about-subtitle {{
        font-size:19px;
        color:#60A5FA;
        font-weight:700;
        margin-top:12px;
    }}

    .about-description {{
        max-width:780px;
        font-size:16px;
        line-height:1.8;
        color:var(--muted-color);
        margin-top:18px;
        margin-bottom:25px;
    }}

    .github-button {{
        display:inline-block;
        padding:11px 20px;
        border-radius:10px;
        background:#2563EB;
        color:white!important;
        text-decoration:none!important;
        font-size:14px;
        font-weight:750;
        transition:all .2s ease;
    }}

    .github-button:hover {{
        background:#1D4ED8;
        transform:translateY(-2px);
        box-shadow:0 8px 22px rgba(37,99,235,.25);
    }}
    .github-links{{
    display:flex;
    align-items:center;
    gap:20px;
    flex-wrap:wrap;
    }}

    .github-links .github-button{{
        margin:0;
    }}

    /* =================================================
       SECTION HEADINGS
       ================================================= */

    .section-header {{
        margin-top:42px;
        margin-bottom:22px;
    }}

    .section-label {{
        color:#60A5FA;
        font-size:13px;
        font-weight:800;
        text-transform:uppercase;
        letter-spacing:1.4px;
        margin-bottom:7px;
    }}

    .section-title {{
        color:var(--text-color);
        font-size:30px;
        font-weight:800;
        margin:0;
    }}

    .section-description {{
        color:var(--muted-color);
        font-size:15px;
        line-height:1.7;
        max-width:750px;
        margin-top:8px;
    }}

    /* =================================================
       CARDS
       ================================================= */

    .info-card {{
        background:var(--card-color);
        border:1px solid var(--border-color);
        border-radius:18px;
        padding:28px;
        height:100%;
        transition:
            transform .2s ease,
            box-shadow .2s ease,
            border-color .2s ease,
            background-color .2s ease;
    }}

    .info-card:hover {{
        transform:translateY(-5px);
        border-color:#60A5FA!important;
        box-shadow:0 12px 30px rgba(37,99,235,.18)!important;
    }}

    .card-icon {{
        width:44px;
        height:44px;
        display:flex;
        align-items:center;
        justify-content:center;
        border-radius:12px;
        background:rgba(37,99,235,.12);
        color:#60A5FA;
        font-size:20px;
        margin-bottom:18px;
    }}

    .info-card-title {{
        color:var(--text-color);
        font-size:19px;
        font-weight:800;
        margin-bottom:9px;
    }}

    .info-card-text {{
        color:var(--muted-color);
        font-size:14px;
        line-height:1.7;
    }}

    /* =================================================
       FLOW
       ================================================= */

    .flow-container {{
        display:flex;
        align-items:center;
        justify-content:center;
        gap:10px;
        flex-wrap:wrap;
        margin-top:25px;
    }}

    .flow-item {{
        background:var(--card-color);
        border:1px solid var(--border-color);
        border-radius:14px;
        padding:18px 22px;
        min-width:145px;
        text-align:center;
        transition:all .2s ease;
    }}

    .flow-item:hover {{
        transform:translateY(-4px);
        border-color:#60A5FA;
        box-shadow:0 10px 24px rgba(37,99,235,.15);
    }}

    .flow-number {{
        font-size:11px;
        color:#60A5FA;
        font-weight:800;
        letter-spacing:1px;
        margin-bottom:6px;
    }}

    .flow-title {{
        color:var(--text-color);
        font-size:14px;
        font-weight:750;
    }}

    .flow-arrow {{
        color:#60A5FA;
        font-size:22px;
        font-weight:800;
    }}

    /* =================================================
       TECH STACK
       ================================================= */

    .tech-card {{
        background:var(--card-color);
        border:1px solid var(--border-color);
        border-radius:16px;
        padding:22px;
        height:100%;
        transition:all .2s ease;
    }}

    .tech-card:hover {{
        transform:translateY(-5px);
        border-color:#60A5FA;
        box-shadow:0 12px 28px rgba(37,99,235,.16);
    }}

    .tech-name {{
        color:var(--text-color);
        font-size:17px;
        font-weight:800;
        margin-bottom:6px;
    }}

    .tech-role {{
        color:var(--muted-color);
        font-size:13px;
        line-height:1.5;
    }}

    /* =================================================
       ARCHITECTURE
       ================================================= */

    .architecture {{
        background:var(--card-color);
        border:1px solid var(--border-color);
        border-radius:20px;
        padding:32px;
        text-align:center;
    }}

    .architecture-row {{
        display:flex;
        align-items:center;
        justify-content:center;
        gap:10px;
        flex-wrap:wrap;
    }}

    .architecture-box {{
        display:inline-block;
        min-width:190px;
        padding:20px 24px;
        border-radius:14px;
        background:var(--input-color);
        border:1px solid var(--border-color);
        transition:all .2s ease;
    }}

    .architecture-box:hover {{
        border-color:#60A5FA;
        transform:translateY(-4px);
        box-shadow:0 10px 25px rgba(37,99,235,.15);
    }}

    .architecture-title {{
        color:var(--text-color);
        font-size:15px;
        font-weight:800;
    }}

    .architecture-subtitle {{
        color:var(--muted-color);
        font-size:12px;
        margin-top:5px;
    }}

    .architecture-arrow {{
        color:#60A5FA;
        font-size:25px;
        font-weight:800;
    }}

    .architecture-down {{
        margin:14px 0;
        text-align:center;
    }}

    /* =================================================
       ROADMAP
       ================================================= */

    .roadmap {{
        background:var(--card-color);
        border:1px solid var(--border-color);
        border-radius:20px;
        padding:28px;
    }}

    .roadmap-item {{
        display:flex;
        align-items:center;
        gap:16px;
        padding:16px 18px;
        border:1px solid var(--border-color);
        border-radius:13px;
        margin-bottom:12px;
        transition:
            transform .2s ease,
            box-shadow .2s ease,
            border-color .2s ease,
            background-color .2s ease;
    }}

    .roadmap-item:last-child {{
        margin-bottom:0;
    }}

    .roadmap-item:hover {{
        border-color:#60A5FA;
        transform:translateX(4px);
        box-shadow:0 10px 24px rgba(37,99,235,.12);
    }}

    .roadmap-status {{
        width:32px;
        height:32px;
        min-width:32px;
        display:flex;
        align-items:center;
        justify-content:center;
        border-radius:50%;
        background:rgba(34,197,94,.12);
        color:#22C55E;
        font-weight:800;
    }}

    .roadmap-future {{
        background:rgba(37,99,235,.12);
        color:#60A5FA;
    }}

    .roadmap-title {{
        color:var(--text-color);
        font-size:14px;
        font-weight:750;
    }}

    .roadmap-description {{
        color:var(--muted-color);
        font-size:12px;
        margin-top:3px;
    }}

    /* =================================================
       CTA
       ================================================= */

    .cta {{
        background:linear-gradient(
            135deg,
            rgba(37,99,235,.16),
            var(--card-color)
        );
        border:1px solid rgba(96,165,250,.28);
        border-radius:22px;
        padding:38px;
        text-align:center;
        margin-top:45px;
    }}

    .cta-title {{
        color:var(--text-color);
        font-size:27px;
        font-weight:800;
    }}

    .cta-text {{
        color:var(--muted-color);
        font-size:14px;
        margin:9px auto 22px auto;
        max-width:600px;
        line-height:1.6;
    }}

    /* =================================================
       RESPONSIVE
       ================================================= */

    @media(max-width:900px) {{

        .block-container {{
            padding-left:1.2rem;
            padding-right:1.2rem;
        }}

        .about-hero {{
            padding:35px 25px;
        }}

        .about-title {{
            font-size:36px;
        }}

        .flow-arrow {{
            display:none;
        }}

        .architecture-row {{
            flex-direction:column;
        }}

        .architecture-arrow {{
            transform:rotate(90deg);
        }}

    }}

    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# HERO / INTRODUCTION
# =========================================================

st.html(
    """
    <div class="about-hero">
        <div class="about-badge">ABOUT THE DEVELOPER & CHURNIQ</div>

        <h1 class="about-title">
            Hi, I'm <span>Arjun.</span>
        </h1>

        <div class="about-subtitle">
            Machine Learning & AI Enthusiast
        </div>

        <p class="about-description">
            I’m an aspiring AI/ML Engineer passionate about building practical, end-to-end machine learning products that go beyond just model training.

            I enjoy turning ML models into real, usable applications that solve practical business problems. I built ChurnIQ with this approach to explore how machine learning can be applied to customer churn and transformed into a complete deployed solution by combining machine learning, API development, frontend development, and deployment. In the future, I plan to extend ChurnIQ with LLM and RAG capabilities to generate personalized, context-aware customer retention recommendations based on relevant business policies and guidelines.
        </p>

                <div class="github-links">
            <a
                class="github-button"
                href="https://github.com/ArjunTechie118"
                target="_blank"
            >
                My GitHub ↗
            </a>
            <a
                class="github-button secondary-link"
                href="https://mail.google.com/mail/?view=cm&fs=1&to=arjun.dadhich004@gmail.com"
                target="_blank"
            >
                Email ↗
            </a>
            <a
                class="github-button secondary-link"
                href="https://www.linkedin.com/in/arjun-dadhich"
                target="_blank"
            >
                LinkedIn ↗
            </a>
        </div>
    </div>
    """
)
# =========================================================
# WHY CHURNIQ
# =========================================================

st.html(
    """
    <div class="section-header">
        <div class="section-label">THE PROJECT</div>

        <h2 class="section-title">
            Why I Built ChurnIQ
        </h2>

        <p class="section-description">
            The goal was not just to train a machine learning model,
            but to understand how an ML model can become a complete,
            usable application.
        </p>
    </div>
    """
)

col1,col2=st.columns(2)

with col1:
    st.html(
        """
        <div class="info-card">
            <div class="card-icon">01</div>

            <div class="info-card-title">
                From Model to Product
            </div>

            <div class="info-card-text">
                ChurnIQ was built to move beyond a notebook-based
                machine learning workflow. The project connects the
                trained model with an API and an interactive frontend,
                creating a complete prediction experience.
            </div>
        </div>
        """
    )

with col2:
    st.html(
        """
        <div class="info-card">
            <div class="card-icon">02</div>

            <div class="info-card-title">
                Practical ML Application
            </div>

            <div class="info-card-text">
                The application accepts customer information and uses
                a trained LightGBM classification model to estimate
                churn probability and provide an interpretable
                risk level.
            </div>
        </div>
        """
    )

# =========================================================
# HOW IT WORKS
# =========================================================

st.html(
    """
    <div class="section-header">
        <div class="section-label">WORKFLOW</div>

        <h2 class="section-title">
            How ChurnIQ Works
        </h2>

        <p class="section-description">
            The application connects customer information with a
            machine learning prediction pipeline.
        </p>
    </div>
    """
)

st.html(
    """
    <div class="flow-container">

        <div class="flow-item">
            <div class="flow-number">01</div>
            <div class="flow-title">Customer Data</div>
        </div>

        <div class="flow-arrow">→</div>

        <div class="flow-item">
            <div class="flow-number">02</div>
            <div class="flow-title">Data Processing</div>
        </div>

        <div class="flow-arrow">→</div>

        <div class="flow-item">
            <div class="flow-number">03</div>
            <div class="flow-title">LightGBM Model</div>
        </div>

        <div class="flow-arrow">→</div>

        <div class="flow-item">
            <div class="flow-number">04</div>
            <div class="flow-title">Churn Probability</div>
        </div>

        <div class="flow-arrow">→</div>

        <div class="flow-item">
            <div class="flow-number">05</div>
            <div class="flow-title">Risk Level</div>
        </div>

    </div>
    """
)

# =========================================================
# MACHINE LEARNING
# =========================================================

st.html(
    """
    <div class="section-header">
        <div class="section-label">MACHINE LEARNING</div>

        <h2 class="section-title">
            The Prediction Engine
        </h2>

        <p class="section-description">
            ChurnIQ currently uses a LightGBM classification model
            to estimate the probability of customer churn.
        </p>
    </div>
    """
)

col1,col2,col3=st.columns(3)

with col1:
    st.html(
        """
        <div class="info-card">
            <div class="card-icon">ML</div>

            <div class="info-card-title">
                LightGBM
            </div>

            <div class="info-card-text">
                A gradient boosting framework used as the core
                classification model for predicting customer churn.
            </div>
        </div>
        """
    )

with col2:
    st.html(
        """
        <div class="info-card">
            <div class="card-icon">01</div>

            <div class="info-card-title">
                Binary Classification
            </div>

            <div class="info-card-text">
                The model predicts whether a customer is likely to
                churn or is likely to remain with the service.
            </div>
        </div>
        """
    )

with col3:
    st.html(
        """
        <div class="info-card">
            <div class="card-icon">%</div>

            <div class="info-card-title">
                Probability
            </div>

            <div class="info-card-text">
                The application displays the model's estimated
                churn probability and converts it into a risk level.
            </div>
        </div>
        """
    )

# =========================================================
# TECHNOLOGY STACK
# =========================================================

st.html(
    """
    <div class="section-header">
        <div class="section-label">TECHNOLOGY</div>

        <h2 class="section-title">
            Technology Stack
        </h2>

        <p class="section-description">
            Technologies used to build the machine learning pipeline,
            backend API and interactive application.
        </p>
    </div>
    """
)

col1,col2,col3=st.columns(3)

tech_data=[
    ("Python","Core programming language"),
    ("Pandas","Data processing and manipulation"),
    ("Scikit-learn","Preprocessing and ML pipeline"),
    ("LightGBM","Churn classification model"),
    ("FastAPI","Prediction API backend"),
    ("Streamlit","Interactive web application")
]

for index,(name,role) in enumerate(tech_data):
    with [col1,col2,col3][index%3]:
        st.html(
            f"""
            <div class="tech-card">
                <div class="tech-name">{name}</div>
                <div class="tech-role">{role}</div>
            </div>
            """
        )

# =========================================================
# DEPLOYMENT ARCHITECTURE
# =========================================================

st.html(
    """
    <div class="section-header">
        <div class="section-label">ARCHITECTURE</div>

        <h2 class="section-title">
            Deployment Architecture
        </h2>

        <p class="section-description">
            ChurnIQ separates the user interface from the prediction
            service, allowing the trained model to be accessed through
            a FastAPI endpoint.
        </p>
    </div>
    """
)

st.html(
    """
    <div class="architecture">

        <div class="architecture-row">

            <div class="architecture-box">
                <div class="architecture-title">
                    Streamlit Frontend
                </div>

                <div class="architecture-subtitle">
                    User interface
                </div>
            </div>

            <span class="architecture-arrow">
                →
            </span>

            <div class="architecture-box">
                <div class="architecture-title">
                    FastAPI Backend
                </div>

                <div class="architecture-subtitle">
                    /predict API
                </div>
            </div>

            <span class="architecture-arrow">
                →
            </span>

            <div class="architecture-box">
                <div class="architecture-title">
                    LightGBM Model
                </div>

                <div class="architecture-subtitle">
                    Churn prediction
                </div>
            </div>

        </div>

        <div class="architecture-down">
            <span class="architecture-arrow">
                ↓
            </span>
        </div>

        <div class="architecture-box">
            <div class="architecture-title">
                API Response
            </div>

            <div class="architecture-subtitle">
                Prediction + Probability
            </div>
        </div>

    </div>
    """
)

# =========================================================
# ROADMAP
# =========================================================

st.html(
    """
    <div class="section-header">
        <div class="section-label">ROADMAP</div>

        <h2 class="section-title">
            What's Next for ChurnIQ?
        </h2>

        <p class="section-description">
            The current application focuses on prediction and deployment.
            Additional intelligence is planned for future iterations.
        </p>
    </div>
    """
)

st.html(
    """
    <div class="roadmap">

        <div class="roadmap-item">

            <div class="roadmap-status">
                ✓
            </div>

            <div>
                <div class="roadmap-title">
                    Customer Churn Prediction
                </div>

                <div class="roadmap-description">
                    Predict churn probability using the trained LightGBM model.
                </div>
            </div>

        </div>

        <div class="roadmap-item">

            <div class="roadmap-status">
                ✓
            </div>

            <div>
                <div class="roadmap-title">
                    FastAPI & Streamlit Deployment
                </div>

                <div class="roadmap-description">
                    Connect the machine learning model to a deployed web application.
                </div>
            </div>

        </div>

        <div class="roadmap-item">

            <div class="roadmap-status roadmap-future">
                →
            </div>

            <div>
                <div class="roadmap-title">
                    SHAP Explainability
                </div>

                <div class="roadmap-description">
                    Add model explainability to understand which customer
                    features contribute to predictions.
                </div>
            </div>

        </div>

        <div class="roadmap-item">

            <div class="roadmap-status roadmap-future">
                →
            </div>

            <div>
                <div class="roadmap-title">
                    LLM + RAG Retention Recommendations
                </div>

                <div class="roadmap-description">
                    Use company policies and guidelines to generate
                    grounded retention recommendations.
                </div>
            </div>

        </div>

    </div>
    """
)

# =========================================================
# CTA
# =========================================================

st.html(
    """
    <div class="cta">

        <div class="cta-title">
            Explore the ChurnIQ Project
        </div>

        <div class="cta-text">
            View the source code, project structure and implementation
            details on GitHub.
        </div>

        <a
            class="github-button"
            href="https://github.com/ArjunTechie118/Customer-Churn-Prediction"
            target="_blank"
        >
            View GitHub Repository ↗
        </a>

    </div>
    """
)