import streamlit as st


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="ChurnPredict",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# THEME STATE
# =========================================================

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True


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
    title="Predict",
    icon="📊"
)

about_page = st.Page(
    "pages/about.py",
    title="About",
    icon="ℹ️"
)

contact_page = st.Page(
    "pages/contact.py",
    title="Contact",
    icon="📞"
)

pg = st.navigation(
    [home_page, predict_page, about_page, contact_page],
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

else:

    bg_color = "#F8FAFC"
    card_color = "#FFFFFF"
    text_color = "#0F172A"
    muted_color = "#475569"
    border_color = "#CBD5E1"
    hover_color = "#EFF6FF"
    nav_text = "#334155"


accent_color = "#2563EB"
accent_light = "#60A5FA"


# =========================================================
# GLOBAL CSS
# =========================================================

st.markdown(
    f"""
    <style>

    /* =====================================================
       THEME VARIABLES
       ===================================================== */

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
    }}


    /* =====================================================
       MAIN APPLICATION
       ===================================================== */

    .stApp {{
        background-color: {bg_color};
        color: {text_color};

        --bg-color: {bg_color};
        --card-color: {card_color};
        --text-color: {text_color};
        --muted-color: {muted_color};
        --border-color: {border_color};
        --hover-color: {hover_color};
        --nav-text: {nav_text};
    }}


    /* Main content width / spacing */

    .block-container {{
        padding-top: 2.2rem;
        padding-left: 4rem;
        padding-right: 4rem;
        padding-bottom: 3rem;
    }}


    /* =====================================================
       NAVBAR
       ===================================================== */

    .navbar-wrapper {{
        width: 100%;
        margin-bottom: 30px;
    }}


    /* Brand */

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

    .nav-button {{
        width: 100%;
        min-height: 46px;

        border-radius: 999px;

        border: 1px solid {border_color} !important;

        background-color: transparent;

        color: var(--nav-text) !important;

        font-size: 15px;
        font-weight: 600;

        text-align: center;

        cursor: pointer;

        transition:
            background-color 0.2s ease,
            border-color 0.2s ease,
            color 0.2s ease;
    }}

    .nav-button:hover {{
        background-color: var(--hover-color);
        border-color: var(--border-color);
        color: var(--text-color) !important;
    }}


    /* =====================================================
       STREAMLIT BUTTON RESET / NAV BUTTON STYLE
       ===================================================== */

    div[data-testid="stButton"] {{
        display: flex;
        justify-content: center;
    }}

    div[data-testid="stButton"] > button {{
        width: 100%;
        min-height: 46px;

        border-radius: 999px;

        border: 1px solid var(--border-color) !important;

        background-color: transparent;

        color: var(--nav-text) !important;

        font-size: 15px;
        font-weight: 600;

        transition:
            background-color 0.2s ease,
            border-color 0.2s ease,
            color 0.2s ease,
            box-shadow 0.2s ease;
    }}

    div[data-testid="stButton"] > button:hover {{
        background-color: var(--hover-color) !important;
        border-color: var(--border-color) !important;
        color: var(--text-color) !important;
    }}

    div[data-testid="stButton"] > button:focus {{
        color: var(--text-color) !important;
        border-color: var(--accent-color) !important;
        box-shadow: none !important;
    }}


    /* =====================================================
       ACTIVE NAVIGATION
       ===================================================== */

    .active-nav {{
        width: 100%;
        min-height: 46px;

        display: flex;
        justify-content: center;
        align-items: center;

        padding: 10px 16px;

        border-radius: 999px;

        background-color: #2563EB;

        color: #FFFFFF !important;

        font-size: 15px;
        font-weight: 600;

        box-shadow:
            0 5px 18px rgba(37, 99, 235, 0.30);
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
        display: flex;
        justify-content: center;
        align-items: center;
    }}

    div[data-testid="stToggle"] [role="switch"] {{
        background-color: var(--border-color) !important;
        border: 1px solid var(--border-color) !important;
        box-shadow: none !important;
    }}

    div[data-testid="stToggle"] [role="switch"][aria-checked="true"] {{
        background-color: var(--accent-color) !important;
        border-color: var(--accent-color) !important;
    }}

    div[data-testid="stToggle"] [role="switch"]::after {{
        background-color: #FFFFFF !important;
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

        box-shadow:
            0 6px 18px rgba(37, 99, 235, 0.25);
    }}


    /* =====================================================
       REMOVE DEFAULT TOP SPACE
       ===================================================== */

    header[data-testid="stHeader"] {{
        background-color: transparent;
    }}


    /* =====================================================
       MOBILE RESPONSIVENESS
       ===================================================== */

    @media (max-width: 900px) {{

        .block-container {{
            padding-left: 1.2rem;
            padding-right: 1.2rem;
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

brand_col, home_col, predict_col, about_col, contact_col, divider_col, theme_col = st.columns(
    [2.7, 1.1, 1.2, 1.1, 1.2, 0.25, 0.7],
    vertical_alignment="center"
)


# =========================================================
# BRAND
# =========================================================

with brand_col:

    st.markdown(
        '<div class="brand-name">Churn<span>Predict</span></div>'
        '<div class="tagline">AI-Powered Customer Churn Prediction</div>',
        unsafe_allow_html=True
    )


# =========================================================
# CURRENT PAGE
# =========================================================

current_page = pg.url_path if hasattr(pg, "url_path") else ""


# =========================================================
# NAVIGATION
# =========================================================

with home_col:

    if current_page.endswith("home"):
        st.markdown(
            '<div class="active-nav">🏠&nbsp; Home</div>',
            unsafe_allow_html=True
        )
    else:
        if st.button(
            "🏠  Home",
            key="nav_home",
            use_container_width=True
        ):
            st.switch_page("pages/home.py")


with predict_col:

    if current_page.endswith("predict"):
        st.markdown(
            '<div class="active-nav">📊&nbsp; Predict</div>',
            unsafe_allow_html=True
        )
    else:
        if st.button(
            "📊  Predict",
            key="nav_predict",
            use_container_width=True
        ):
            st.switch_page("pages/predict.py")


with about_col:

    if current_page.endswith("about"):
        st.markdown(
            '<div class="active-nav">ℹ️&nbsp; About</div>',
            unsafe_allow_html=True
        )
    else:
        if st.button(
            "ℹ️  About",
            key="nav_about",
            use_container_width=True
        ):
            st.switch_page("pages/about.py")


with contact_col:

    if current_page.endswith("contact"):
        st.markdown(
            '<div class="active-nav">📞&nbsp; Contact</div>',
            unsafe_allow_html=True
        )
    else:
        if st.button(
            "📞  Contact",
            key="nav_contact",
            use_container_width=True
        ):
            st.switch_page("pages/contact.py")


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

    theme_changed = st.toggle(
        "Theme",
        value=st.session_state.dark_mode,
        label_visibility="collapsed"
    )

    if theme_changed != st.session_state.dark_mode:

        st.session_state.dark_mode = theme_changed

        st.rerun()


# =========================================================
# RUN CURRENT PAGE
# =========================================================

pg.run()