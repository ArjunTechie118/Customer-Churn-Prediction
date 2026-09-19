import streamlit as st

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
    st.session_state.theme_toggle = st.session_state.dark_mode

def toggle_theme():
    st.session_state.dark_mode = st.session_state.theme_toggle

# =========================================================
# PAGES
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

    :root {{
        --bg-color:{bg_color};
        --card-color:{card_color};
        --text-color:{text_color};
        --muted-color:{muted_color};
        --border-color:{border_color};
        --input-color:{card_color};
        --hover-color:{hover_color};
        --nav-text:{nav_text};
        --accent-color:{accent_color};
        --accent-light:{accent_light};
    }}

    html,
    body,
    [data-testid="stAppViewContainer"],
    [data-testid="stHeader"] {{
        background-color:{bg_color}!important;
    }}

    .stApp {{
        background-color:{bg_color}!important;
        color:{text_color}!important;
    }}

    .block-container {{
        padding-top:3.5rem!important;
        padding-left:1rem!important;
        padding-right:1rem!important;
        padding-bottom:3rem!important;
        max-width:100%!important;
    }}

    /* =====================================================
       NAVBAR
       ===================================================== */

    .churniq-navbar {{
        width:100%;
        display:flex;
        align-items:center;
        overflow:visible!important;
    }}

    .brand-name {{
        font-size:27px;
        font-weight:800;
        color:var(--text-color)!important;
        line-height:1.2;
        white-space:nowrap!important;
        overflow:visible!important;
        padding-top:4px;
    }}

    .tagline {{
        color:var(--muted-color)!important;
        font-size:13px;
        margin-top:5px;
        white-space:nowrap!important;
        overflow:visible!important;
    }}

    /* Streamlit navigation buttons */

    div[data-testid="stButton"] {{
        width:100%!important;
        overflow:visible!important;
    }}

    div[data-testid="stButton"] > button {{
        width:100%!important;
        min-width:max-content!important;
        min-height:44px!important;
        padding:10px 14px!important;
        border-radius:10px!important;
        border:1px solid var(--border-color)!important;
        background-color:var(--card-color)!important;
        color:var(--nav-text)!important;
        font-size:15px!important;
        font-weight:600!important;
        white-space:nowrap!important;
        overflow:visible!important;
        box-shadow:none!important;
    }}

    div[data-testid="stButton"] > button:hover {{
        background-color:var(--hover-color)!important;
        color:var(--accent-color)!important;
        border-color:var(--accent-color)!important;
        box-shadow:none!important;
    }}

    /* Active navigation item */

    .active-nav {{
        width:100%;
        min-width:max-content;
        min-height:44px;
        display:flex;
        justify-content:center;
        align-items:center;
        padding:10px 14px;
        border-radius:10px;
        background-color:var(--hover-color);
        border:1px solid var(--accent-color);
        color:var(--accent-color)!important;
        font-size:15px;
        font-weight:700;
        white-space:nowrap!important;
        overflow:visible!important;
        box-sizing:border-box;
    }}

    /* Theme toggle */

    div[data-testid="stToggle"] {{
        display:flex!important;
        justify-content:center!important;
        align-items:center!important;
    }}

    div[data-testid="stToggle"] label {{
        display:none!important;
    }}

    /* Navbar divider */

    .nav-divider {{
        width:1px;
        height:30px;
        background-color:var(--border-color);
        margin:auto;
    }}

    /* =====================================================
       MOBILE
       ===================================================== */

    @media(max-width:900px) {{

        .block-container {{
            padding-left:0.8rem!important;
            padding-right:0.8rem!important;
        }}

        .brand-name {{
            font-size:23px;
        }}

        .tagline {{
            font-size:11px;
        }}

        div[data-testid="stButton"] > button,
        .active-nav {{
            font-size:13px!important;
            padding:8px 8px!important;
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
    [3.4, 1.05, 1.65, 1.05, 0.2, 0.65],
    vertical_alignment="center"
)

with brand_col:
    st.markdown(
        """
        <div class="churniq-navbar">
            <div>
                <div class="brand-name">ChurnIQ</div>
                <div class="tagline">AI-Powered Churn Intelligence</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

current_page = pg.url_path if hasattr(pg, "url_path") else ""

with home_col:
    if current_page.endswith("home") or current_page == "":
        st.markdown(
            '<div class="active-nav">Home</div>',
            unsafe_allow_html=True
        )
    else:
        if st.button("Home", key="nav_home"):
            st.switch_page("pages/home.py")

with predict_col:
    if current_page.endswith("predict"):
        st.markdown(
            '<div class="active-nav">Predict Churn</div>',
            unsafe_allow_html=True
        )
    else:
        if st.button("Predict Churn", key="nav_predict"):
            st.switch_page("pages/predict.py")

with about_col:
    if current_page.endswith("about"):
        st.markdown(
            '<div class="active-nav">About</div>',
            unsafe_allow_html=True
        )
    else:
        if st.button("About", key="nav_about"):
            st.switch_page("pages/about.py")

with divider_col:
    st.markdown(
        '<div class="nav-divider"></div>',
        unsafe_allow_html=True
    )

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