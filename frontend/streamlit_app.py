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

if "theme_toggle" not in st.session_state:
    st.session_state.theme_toggle = False

# Single source of truth
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
else:
    bg_color = "#F8FAFC"
    card_color = "#FFFFFF"
    text_color = "#0F172A"
    muted_color = "#475569"
    border_color = "#CBD5E1"
    hover_color = "#EFF6FF"
    nav_text = "#334155"
    toggle_off = "#94A3B8"

accent_color = "#2563EB"
accent_light = "#60A5FA"

# =========================================================
# GLOBAL CSS
# =========================================================

st.markdown(
    f"""
    <style>

    :root {{
        --accent-color: {accent_color};
        --accent-light: {accent_light};
        --bg-color: {bg_color};
        --card-color: {card_color};
        --text-color: {text_color};
        --muted-color: {muted_color};
        --border-color: {border_color};
        --hover-color: {hover_color};
        --nav-text: {nav_text};
        --toggle-off: {toggle_off};
    }}

    html,
    body {{
        background-color: {bg_color} !important;
    }}

    .stApp {{
        background-color: {bg_color} !important;
        color: {text_color} !important;
    }}

    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    main {{
        background-color: {bg_color} !important;
        color: {text_color} !important;
    }}

    [data-testid="stHeader"] {{
        background-color: {bg_color} !important;
    }}

    [data-testid="stToolbar"] {{
        background-color: transparent !important;
    }}

    [data-testid="stDecoration"] {{
        display: none !important;
    }}

    .block-container {{
        padding-top: 1.4rem !important;
        padding-left: 2.2rem !important;
        padding-right: 2.2rem !important;
        padding-bottom: 3rem !important;
        max-width: 100% !important;
    }}

    /* =====================================================
       NAVBAR
       ===================================================== */

    .brand-name {{
        font-size: 27px;
        font-weight: 800;
        color: var(--text-color) !important;
        line-height: 1.1;
        white-space: nowrap;
    }}

    .brand-name span {{
        color: var(--accent-color) !important;
    }}

    .tagline {{
        color: var(--muted-color) !important;
        font-size: 13px;
        margin-top: 6px;
        white-space: nowrap;
    }}

    /* =====================================================
       NAVIGATION BUTTONS
       ===================================================== */

    div[data-testid="stButton"] {{
        display: flex;
        justify-content: center;
    }}

    div[data-testid="stButton"] > button {{
        width: 100%;
        min-height: 44px;
        border-radius: 10px !important;
        border: 1px solid transparent !important;
        background-color: transparent !important;
        color: var(--nav-text) !important;
        font-size: 15px;
        font-weight: 600;
        box-shadow: none !important;
        transition:
            background-color 0.2s ease,
            color 0.2s ease,
            box-shadow 0.2s ease;
    }}

    div[data-testid="stButton"] > button:hover {{
        background-color: var(--hover-color) !important;
        border-color: transparent !important;
        color: var(--text-color) !important;
    }}

    div[data-testid="stButton"] > button:focus {{
        color: var(--text-color) !important;
        border-color: transparent !important;
        box-shadow: none !important;
    }}

    /* =====================================================
       ACTIVE NAVIGATION
       ===================================================== */

    .active-nav {{
        width: 100%;
        min-height: 44px;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 10px 16px;
        border-radius: 10px;
        background-color: transparent;
        color: var(--accent-color) !important;
        font-size: 15px;
        font-weight: 700;
    }}

    /* =====================================================
       THEME DIVIDER
       ===================================================== */

    .theme-divider {{
        width: 1px;
        height: 34px;
        background-color: var(--border-color);
        margin: auto;
    }}

    /* =====================================================
       THEME TOGGLE
       ===================================================== */

    div[data-testid="stToggle"] {{
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        visibility: visible !important;
        opacity: 1 !important;
    }}

    div[data-testid="stToggle"] > label {{
        visibility: hidden !important;
        width: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
    }}

    div[data-testid="stToggle"] [role="switch"] {{
        width: 46px !important;
        min-width: 46px !important;
        height: 24px !important;
        min-height: 24px !important;
        background-color: var(--toggle-off) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 999px !important;
        box-shadow: none !important;
        visibility: visible !important;
        opacity: 1 !important;
    }}

    div[data-testid="stToggle"] [role="switch"][aria-checked="true"] {{
        background-color: var(--accent-color) !important;
        border-color: var(--accent-color) !important;
    }}

    div[data-testid="stToggle"] [role="switch"]::after {{
        width: 18px !important;
        height: 18px !important;
        background-color: #FFFFFF !important;
        visibility: visible !important;
        opacity: 1 !important;
    }}

    div[data-testid="stToggle"] [role="switch"]:hover {{
        box-shadow: 0 0 0 3px rgba(37,99,235,0.12) !important;
    }}

    /* =====================================================
       PRIMARY BUTTON
       ===================================================== */

    div.stButton > button[kind="primary"] {{
        background-color: var(--accent-color) !important;
        color: #FFFFFF !important;
        border: 1px solid var(--accent-color) !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
        min-height: 46px;
        transition: all 0.2s ease;
    }}

    div.stButton > button[kind="primary"]:hover {{
        background-color: #1D4ED8 !important;
        border-color: #1D4ED8 !important;
        box-shadow: 0 6px 18px rgba(37,99,235,0.25);
    }}

    /* =====================================================
       MOBILE
       ===================================================== */

    @media (max-width: 900px) {{

        .block-container {{
            padding-left: 1.2rem !important;
            padding-right: 1.2rem !important;
        }}

        .brand-name {{
            font-size: 23px;
        }}

        .tagline {{
            font-size: 11px;
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
    [2.8, 1.1, 1.4, 1.1, 0.25, 0.7],
    vertical_alignment="center"
)

# =========================================================
# BRAND
# =========================================================

with brand_col:
    st.markdown(
        '<div class="brand-name">Churn<span>IQ</span></div>'
        '<div class="tagline">AI-Powered Churn Intelligence</div>',
        unsafe_allow_html=True
    )

# =========================================================
# CURRENT PAGE
# =========================================================

current_page = pg.url_path if hasattr(pg, "url_path") else ""

# =========================================================
# HOME
# =========================================================

with home_col:

    if current_page.endswith("home") or current_page == "":
        st.markdown(
            '<div class="active-nav">🏠&nbsp; Home</div>',
            unsafe_allow_html=True
        )

    else:
        if st.button(
            "🏠  Home",
            key="nav_home"
        ):
            st.switch_page("pages/home.py")

# =========================================================
# PREDICT CHURN
# =========================================================

with predict_col:

    if current_page.endswith("predict"):
        st.markdown(
            '<div class="active-nav">🎯&nbsp; Predict Churn</div>',
            unsafe_allow_html=True
        )

    else:
        if st.button(
            "🎯  Predict Churn",
            key="nav_predict"
        ):
            st.switch_page("pages/predict.py")

# =========================================================
# ABOUT
# =========================================================

with about_col:

    if current_page.endswith("about"):
        st.markdown(
            '<div class="active-nav">ℹ️&nbsp; About</div>',
            unsafe_allow_html=True
        )

    else:
        if st.button(
            "ℹ️  About",
            key="nav_about"
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
        label_visibility="collapsed"
    )

# =========================================================
# IMPORTANT:
# Sync theme AFTER toggle is processed
# =========================================================

st.session_state.dark_mode = st.session_state.theme_toggle

# =========================================================
# RUN CURRENT PAGE
# =========================================================

pg.run()