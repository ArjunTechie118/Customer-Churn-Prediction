import streamlit as st

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="ChurnIQ",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# THEME STATE
# =========================================================

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

if "theme_toggle" not in st.session_state:
    st.session_state.theme_toggle = False

def toggle_theme():
    st.session_state.dark_mode = st.session_state.theme_toggle

# =========================================================
# NAVIGATION
# =========================================================

home_page = st.Page(
    "pages/home.py",
    title="Home",
    icon="🏠"
)

predict_page = st.Page(
    "pages/predict.py",
    title="Predict Churn",
    icon="🎯"
)

about_page = st.Page(
    "pages/about.py",
    title="About",
    icon="ℹ️"
)

pg = st.navigation(
    [home_page, predict_page, about_page],
    position="hidden"
)

# =========================================================
# THEME COLORS
# =========================================================

if st.session_state.dark_mode:
    bg_color = "#0B0F19"
    card_color = "#1E293B"
    text_color = "#F8FAFC"
    muted_color = "#CBD5E1"
    border_color = "#334155"
    hover_color = "#263449"
    nav_text = "#E2E8F0"
    toggle_off = "#475569"
    brand_color = "#FFFFFF"
else:
    bg_color = "#F8FAFC"
    card_color = "#FFFFFF"
    text_color = "#0F172A"
    muted_color = "#475569"
    border_color = "#CBD5E1"
    hover_color = "#EFF6FF"
    nav_text = "#334155"
    toggle_off = "#94A3B8"
    brand_color = "#2563EB"

accent_color = "#2563EB"
accent_light = "#60A5FA"

# =========================================================
# GLOBAL CSS
# =========================================================

st.markdown(
    f"""
    <style>

    :root {{
        --accent-color:{accent_color};
        --accent-light:{accent_light};
        --bg-color:{bg_color};
        --card-color:{card_color};
        --text-color:{text_color};
        --muted-color:{muted_color};
        --border-color:{border_color};
        --hover-color:{hover_color};
        --nav-text:{nav_text};
        --toggle-off:{toggle_off};
        --brand-color:{brand_color};
    }}

    .stApp {{
        background-color:{bg_color};
        color:{text_color};
    }}

    .block-container {{
        padding-top:3.5rem;
        padding-left:4rem;
        padding-right:4rem;
        padding-bottom:3rem;
        max-width:100%;
    }}

    /* =====================================================
       NAVBAR BRAND
       ===================================================== */

    .brand-name {{
        font-size:27px;
        font-weight:800;
        line-height:1.2;
        white-space:nowrap;
        overflow:visible;
        color:var(--brand-color) !important;
    }}

    .brand-name .iq {{
        color:#60A5FA !important;
    }}

    .tagline {{
        color:var(--muted-color) !important;
        font-size:13px;
        margin-top:6px;
        white-space:nowrap;
        overflow:visible;
    }}

    /* =====================================================
       NAVIGATION BUTTONS
       ===================================================== */

    div[data-testid="stButton"] {{
        display:flex !important;
        justify-content:center !important;
        align-items:center !important;
        width:100% !important;
    }}

    div[data-testid="stButton"] > button {{
        width:100% !important;
        height:44px !important;
        min-height:44px !important;

        display:flex !important;
        align-items:center !important;
        justify-content:center !important;

        box-sizing:border-box !important;

        margin:0 !important;
        padding:0 12px !important;

        border:1px solid transparent !important;
        border-radius:10px !important;

        background:transparent !important;
        color:var(--nav-text) !important;

        font-family:inherit !important;
        font-size:15px !important;
        font-weight:600 !important;

        line-height:1 !important;
        white-space:nowrap !important;

        transform:none !important;
        position:static !important;

        box-shadow:none !important;

        outline:none !important;

        transition:
            background-color .15s ease,
            color .15s ease !important;
    }}

    div[data-testid="stButton"] > button:hover {{
        background:var(--hover-color) !important;
        color:var(--accent-color) !important;

        border-color:transparent !important;

        transform:none !important;
        position:static !important;

        box-shadow:none !important;
    }}

    div[data-testid="stButton"] > button:active {{
        background:var(--hover-color) !important;
        color:var(--accent-color) !important;

        border-color:transparent !important;

        transform:none !important;
        position:static !important;

        box-shadow:none !important;
    }}

    div[data-testid="stButton"] > button:focus {{
        background:transparent !important;
        color:var(--nav-text) !important;

        border-color:transparent !important;

        outline:none !important;
        transform:none !important;
        position:static !important;

        box-shadow:none !important;
    }}

    div[data-testid="stButton"] > button:focus-visible {{
        outline:none !important;
        border-color:transparent !important;
        box-shadow:none !important;
    }}

    /* =====================================================
       THEME DIVIDER
       ===================================================== */

    .theme-divider {{
        width:1px;
        height:30px;
        background-color:var(--border-color);
        margin:auto;
    }}

    /* =====================================================
       THEME TOGGLE
       ===================================================== */

    div[data-testid="stToggle"] {{
        display:flex !important;
        justify-content:center !important;
        align-items:center !important;
        visibility:visible !important;
        opacity:1 !important;
    }}

    div[data-testid="stToggle"] > label {{
        visibility:hidden !important;
        width:0 !important;
        margin:0 !important;
        padding:0 !important;
    }}

    div[data-testid="stToggle"] [role="switch"] {{
        width:46px !important;
        min-width:46px !important;
        height:24px !important;
        min-height:24px !important;

        background-color:var(--toggle-off) !important;

        border:1px solid var(--border-color) !important;
        border-radius:999px !important;

        box-shadow:none !important;

        visibility:visible !important;
        opacity:1 !important;
    }}

    div[data-testid="stToggle"] [role="switch"][aria-checked="true"] {{
        background-color:var(--accent-color) !important;
        border-color:var(--accent-color) !important;
    }}

    div[data-testid="stToggle"] [role="switch"]::after {{
        width:18px !important;
        height:18px !important;
        background-color:#FFFFFF !important;

        visibility:visible !important;
        opacity:1 !important;
    }}

    div[data-testid="stToggle"] [role="switch"]:hover {{
        box-shadow:0 0 0 3px rgba(37,99,235,0.12) !important;
    }}

    /* =====================================================
       PRIMARY BUTTONS
       ===================================================== */

    div.stButton > button[kind="primary"] {{
        background-color:var(--accent-color) !important;
        color:#FFFFFF !important;

        border:1px solid var(--accent-color) !important;
        border-radius:10px !important;

        font-weight:700 !important;
        min-height:46px;

        transition:
            background-color .2s ease,
            border-color .2s ease,
            box-shadow .2s ease !important;
    }}

    div.stButton > button[kind="primary"]:hover {{
        background-color:#1D4ED8 !important;
        border-color:#1D4ED8 !important;
        box-shadow:0 6px 18px rgba(37,99,235,0.25);
    }}

    /* =====================================================
       HEADER
       ===================================================== */

    header[data-testid="stHeader"] {{
        background-color:transparent;
    }}

    /* =====================================================
       MOBILE
       ===================================================== */

    @media (max-width:900px) {{

        .block-container {{
            padding-left:1.2rem;
            padding-right:1.2rem;
        }}

        .brand-name {{
            font-size:23px;
        }}

        .tagline {{
            font-size:11px;
        }}

        div[data-testid="stButton"] > button {{
            font-size:13px !important;
            padding:0 6px !important;
        }}

    }}

    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# NAVBAR
# =========================================================

brand_col, home_col, predict_col, about_col, divider_col, theme_col = st.columns(
    [2.8,1.1,1.4,1.1,0.25,0.7],
    vertical_alignment="center"
)

# =========================================================
# BRAND
# =========================================================

with brand_col:
    st.markdown(
        """
        <div class="brand-name">
            Churn<span class="iq">IQ</span>
        </div>
        <div class="tagline">
            AI-Powered Churn Intelligence
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# HOME
# =========================================================

with home_col:
    if st.button(
        "🏠  Home",
        key="nav_home",
        use_container_width=True
    ):
        st.switch_page("pages/home.py")

# =========================================================
# PREDICT CHURN
# =========================================================

with predict_col:
    if st.button(
        "🎯  Predict Churn",
        key="nav_predict",
        use_container_width=True
    ):
        st.switch_page("pages/predict.py")

# =========================================================
# ABOUT
# =========================================================

with about_col:
    if st.button(
        "ℹ️  About",
        key="nav_about",
        use_container_width=True
    ):
        st.switch_page("pages/about.py")

# =========================================================
# DIVIDER
# =========================================================

with divider_col:
    st.markdown(
        '<div class="theme-divider"></div>',
        unsafe_allow_html=True
    )

# =========================================================
# THEME TOGGLE
# =========================================================

with theme_col:
    st.toggle(
        "Theme",
        key="theme_toggle",
        label_visibility="collapsed",
        on_change=toggle_theme
    )

# =========================================================
# RUN CURRENT PAGE
# =========================================================

pg.run()