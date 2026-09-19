import streamlit as st
import textwrap
st.markdown(textwrap.dedent("""
<style>
.home-wrapper{width:100%;overflow:hidden}
.hero-section{display:flex;align-items:center;justify-content:space-between;gap:55px;padding:48px 42px 50px;margin:0 -20px;background:radial-gradient(circle at 78% 45%,rgba(37,99,235,.15),transparent 35%),linear-gradient(135deg,var(--card-color,#fff),var(--bg-color,#f8fafc));border-radius:0 0 28px 28px;box-sizing:border-box}
.hero-content{flex:1;max-width:650px}
.hero-badge{display:inline-block;padding:8px 16px;margin-bottom:18px;border-radius:999px;background:var(--hover-color,#e0f2fe);color:#2563eb;font-size:13px;font-weight:700}
.hero-title{margin:0 0 18px}
.hero-title-main{font-size:50px;font-weight:800;color:var(--text-color,#0f172a);line-height:1.08}
.hero-title-accent{font-size:50px;font-weight:800;color:#2563eb;line-height:1.08}
.hero-description{font-size:16px;color:var(--muted-color,#475569);max-width:570px;margin:0;line-height:1.65}
.hero-preview{flex:0 0 400px;display:flex;flex-direction:column;align-items:center}
.risk-card{width:400px;max-width:100%;background:var(--card-color,#fff);border:1px solid var(--border-color,#dbeafe);border-radius:16px;padding:18px 20px 18px;box-shadow:0 18px 45px rgba(15,23,42,.16);box-sizing:border-box}
.risk-card-header{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:4px}
.risk-card-header span{font-size:12px;font-weight:800;color:var(--text-color,#0f172a)}
.risk-card-header small{font-size:10px;color:#2563eb;background:var(--hover-color,#eff6ff);padding:6px 9px;border-radius:999px;white-space:nowrap}
.gauge{position:relative;width:230px;height:125px;margin:8px auto 2px;overflow:hidden;background:conic-gradient(from 270deg,#10b981 0deg,#facc15 55deg,#f59e0b 105deg,#ef4444 180deg,transparent 180deg);border-radius:230px 230px 0 0}
.gauge::before{content:"";position:absolute;width:202px;height:202px;left:14px;top:14px;border-radius:50%;background:var(--card-color,#fff);z-index:1}
.gauge::after{content:"";position:absolute;width:3px;height:88px;left:50%;bottom:3px;background:var(--text-color,#0f172a);border-radius:3px;transform-origin:bottom center;transform:translateX(-50%) rotate(58deg);z-index:3}
.gauge-value{position:absolute;left:0;right:0;bottom:19px;text-align:center;font-size:32px;font-weight:800;color:var(--text-color,#0f172a);z-index:4}
.gauge-label{position:absolute;left:0;right:0;bottom:3px;text-align:center;font-size:12px;color:var(--muted-color,#64748b);z-index:4}
.risk-badge{width:max-content;margin:2px auto 0;padding:9px 22px;border-radius:999px;background:#fee2e2;color:#dc2626;font-size:12px;font-weight:800;letter-spacing:.3px}
.sample-note{margin-top:8px;font-size:10px;color:var(--muted-color,#64748b);text-align:center}
.hero-button-wrap{display:flex;justify-content:center;margin-top:0}
.hero-button-wrap div[data-testid="stButton"] > button{
    width:auto !important;
    min-height:44px !important;
    padding:11px 20px !important;
    border-radius:10px !important;
    border:1px solid #2563EB !important;
    background:#2563EB !important;
    color:#FFFFFF !important;
    font-size:14px !important;
    font-weight:700 !important;
    box-shadow:0 6px 18px rgba(37,99,235,.18) !important;
    transition:all .2s ease !important;
}
.hero-button-wrap div[data-testid="stButton"] > button:hover{
    background:#1D4ED8 !important;
    border-color:#1D4ED8 !important;
    color:#FFFFFF !important;
    transform:translateY(-2px);
    box-shadow:0 10px 24px rgba(37,99,235,.25) !important;
}
.section-heading{text-align:center;margin:48px 0 24px}
.section-heading h2{margin:0;color:var(--text-color,#0f172a);font-size:28px;font-weight:800}
.section-heading p{margin:7px 0 0;color:var(--muted-color,#64748b);font-size:14px}
.feature-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin:0 0 10px}
.feature-card{min-height:170px;padding:22px 20px;border:1px solid var(--border-color,#dbeafe);border-radius:12px;background:var(--card-color,#fff);box-sizing:border-box}
.feature-icon{width:48px;height:48px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:25px;margin-bottom:12px}
.icon-blue{background:#e0f2fe}
.icon-green{background:#dcfce7}
.icon-purple{background:#f3e8ff}
.feature-card,.step-card,.tech-item,.roadmap-item{transition:transform .2s ease,box-shadow .2s ease,border-color .2s ease,background-color .2s ease}
.feature-card:hover,.step-card:hover,.tech-item:hover,.roadmap-item:hover{transform:translateY(-5px);border-color:#60A5FA!important;box-shadow:0 12px 30px rgba(37,99,235,.22)!important}
.planned-tag{display:inline-block;margin-top:9px;padding:4px 8px;border-radius:999px;background:#f3e8ff;color:#7c3aed;font-size:10px;font-weight:700}
.steps-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;position:relative}
.step-card{position:relative;min-height:145px;padding:18px 15px;text-align:center;border:1px solid var(--border-color,#dbeafe);border-radius:12px;background:var(--card-color,#fff);box-sizing:border-box}
.step-number{width:40px;height:40px;margin:0 auto 10px;border-radius:50%;display:flex;align-items:center;justify-content:center;background:var(--hover-color,#dbeafe);color:#2563eb;font-size:14px;font-weight:800}
.step-icon{font-size:23px;margin-bottom:6px}
.step-card h3{margin:0 0 7px;color:var(--text-color,#0f172a);font-size:14px;font-weight:750}
.step-card p{margin:0;color:var(--muted-color,#64748b);font-size:12px;line-height:1.5}
.built-grid{display:grid;grid-template-columns:repeat(4,1fr);border-radius:12px;overflow:hidden;background:var(--card-color,#fff);border:1px solid var(--border-color,#dbeafe)}
.tech-item{text-align:center;padding:10px 18px;border-right:1px solid var(--border-color,#dbeafe)}
.tech-item:last-child{border-right:none}
.tech-icon{height:70px;margin-bottom:5px;display:flex;align-items:center;justify-content:center;overflow:hidden}
.tech-icon img{width:58px !important;height:58px !important;max-width:58px !important;max-height:58px !important;object-fit:contain}
.tech-item:nth-child(3) .tech-icon img{width:105px !important;height:58px !important;max-width:105px !important;max-height:58px !important;object-fit:contain}
.tech-item h3,.tech-item p{text-align:center}
.tech-item h3{margin:0 0 4px;color:var(--text-color,#0f172a);font-size:14px}
.tech-item p{margin:0;color:var(--muted-color,#64748b);font-size:11px}
.roadmap{margin-top:42px;padding:24px 28px;border-radius:12px;background:linear-gradient(120deg,#172f54,#10264a);color:#fff;display:grid;grid-template-columns:1.05fr 1fr;gap:35px;box-sizing:border-box}
.roadmap-badge{display:inline-block;padding:5px 11px;border-radius:999px;background:rgba(56,189,248,.18);color:#7dd3fc;font-size:10px;font-weight:700;margin-bottom:10px}
.roadmap h2{margin:0 0 8px;font-size:22px;line-height:1.15;color:#fff}
.roadmap p{margin:0;color:#dbeafe;font-size:12px;line-height:1.55}
.roadmap-current{display:flex;align-items:center;gap:15px;margin-top:18px;font-size:11px}
.current-label{padding:5px 9px;border-radius:999px;background:rgba(34,197,94,.16);color:#86efac}
.future-label{padding:5px 9px;border-radius:999px;background:rgba(168,85,247,.18);color:#d8b4fe}
.roadmap-flow{display:flex;flex-direction:column;gap:7px;justify-content:center}
.roadmap-step{display:flex;align-items:center;gap:10px;padding:8px 12px;border:1px solid rgba(125,211,252,.25);border-radius:8px;background:rgba(255,255,255,.04);font-size:11px;color:#e0f2fe}
.roadmap-step.active{border-color:#a78bfa;background:rgba(139,92,246,.15);box-shadow:0 0 18px rgba(139,92,246,.18)}
.roadmap-step-icon{font-size:15px}
.github-box{margin-top:16px;padding:20px 24px;border-radius:12px;background:linear-gradient(135deg,var(--hover-color,#eff6ff),var(--bg-color,#f8fafc));border:1px solid var(--border-color,#dbeafe);display:flex;align-items:center;justify-content:space-between;gap:20px}
.github-left{display:flex;align-items:center;gap:18px}
.github-icon{font-size:40px}
.github-left h3{margin:0 0 4px;color:var(--text-color,#0f172a);font-size:15px}
.github-left p{margin:0;color:var(--muted-color,#64748b);font-size:11px}
.footer{margin-top:30px;padding:20px 0;text-align:center;border-top:1px solid var(--border-color,#dbeafe);color:var(--muted-color,#64748b);font-size:11px}
@media(max-width:1000px){.hero-section{gap:30px;padding:40px 28px}.hero-preview{flex-basis:350px}.risk-card{width:350px}.hero-title-main,.hero-title-accent{font-size:42px}.feature-grid,.steps-grid{grid-template-columns:repeat(2,1fr)}.roadmap{grid-template-columns:1fr}.built-grid{grid-template-columns:repeat(2,1fr)}.tech-item:nth-child(2){border-right:none}}
@media(max-width:700px){.hero-section{flex-direction:column;align-items:flex-start;padding:35px 24px 40px;margin:0 -10px}.hero-content{max-width:none}.hero-title-main,.hero-title-accent{font-size:36px}.hero-description{font-size:15px}.hero-preview{width:100%;flex-basis:auto}.risk-card{width:100%;max-width:400px}.feature-grid,.steps-grid,.built-grid{grid-template-columns:1fr}.tech-item{border-right:none;border-bottom:1px solid var(--border-color,#dbeafe)}.tech-item:last-child{border-bottom:none}.roadmap{padding:22px 20px}.github-box{flex-direction:column;align-items:flex-start}}
</style>
"""),unsafe_allow_html=True)
st.markdown("""
<div class="home-wrapper">
<div class="hero-section">
<div class="hero-content">
<div class="hero-badge">AI-Powered Churn Intelligence</div>
<div class="hero-title">
<div class="hero-title-main">Predict Customer Churn</div>
<div class="hero-title-accent">Before It Happens</div>
</div>
<p class="hero-description">ChurnIQ helps you identify customers who are likely to churn using machine learning, so you can take action early and improve customer retention.</p>
</div>
<div class="hero-preview">
<div class="risk-card">
<div class="risk-card-header">
<span>CUSTOMER RISK</span>
<small>Sample Prediction (Illustration)</small>
</div>
<div class="gauge">
<div class="gauge-value">78.6%</div>
<div class="gauge-label">Churn Probability</div>
</div>
<div class="risk-badge">HIGH RISK</div>
</div>
<div class="sample-note">* This is a sample result for demonstration purposes only.</div>
</div>
</div>
</div>
""",unsafe_allow_html=True)
st.markdown('<div class="hero-button-wrap">',unsafe_allow_html=True)
if st.button("Predict Customer Churn  →",key="hero_predict"):
    st.switch_page("pages/predict.py")
st.markdown('</div>',unsafe_allow_html=True)
st.markdown("""
<div class="section-heading">
<h2>What ChurnIQ Does</h2>
<p>Turning customer data into actionable insights.</p>
</div>
<div class="feature-grid">
<div class="feature-card">
<div class="feature-icon icon-blue">🎯</div>
<h3>Churn Prediction</h3>
<p>Predict the likelihood of customer churn using a trained machine learning model.</p>
</div>
<div class="feature-card">
<div class="feature-icon icon-green">🛡️</div>
<h3>Risk Assessment</h3>
<p>Convert model probability into clear risk levels for easier decision making.</p>
</div>
<div class="feature-card">
<div class="feature-icon icon-purple">🔍</div>
<h3>ML Explainability</h3>
<p>Understand the key factors behind predictions using feature importance and planned SHAP analysis.</p>
<span class="planned-tag">COMING SOON</span>
</div>
</div>
""",unsafe_allow_html=True)
st.markdown("""
<div class="section-heading">
<h2>How It Works</h2>
<p>A simple, end-to-end machine learning pipeline.</p>
</div>
<div class="steps-grid">
<div class="step-card">
<div class="step-number">01</div>
<div class="step-icon">👤</div>
<h3>Customer Data</h3>
<p>You enter individual customer information through the application.</p>
</div>
<div class="step-card">
<div class="step-number">02</div>
<div class="step-icon">🗄️</div>
<h3>FastAPI</h3>
<p>The data is sent to the FastAPI backend for processing.</p>
</div>
<div class="step-card">
<div class="step-number">03</div>
<div class="step-icon">🧠</div>
<h3>LightGBM</h3>
<p>The trained model predicts the customer's churn probability.</p>
</div>
<div class="step-card">
<div class="step-number">04</div>
<div class="step-icon">📊</div>
<h3>Risk Result</h3>
<p>You get a clear result with probability, risk level and future key factors.</p>
</div>
</div>
""",unsafe_allow_html=True)

import base64
from pathlib import Path


ASSETS_DIR = Path(__file__).resolve().parents[1] / "assets"


def get_svg_data(filename):
    file_path = ASSETS_DIR / filename
    svg_data = file_path.read_bytes()
    encoded = base64.b64encode(svg_data).decode("utf-8")
    return f"data:image/svg+xml;base64,{encoded}"


python_logo = get_svg_data("python.svg")
lightgbm_logo = get_svg_data("LightGBM.svg")
fastapi_logo = get_svg_data("fastapi.svg")
streamlit_logo = get_svg_data("streamlit.svg")


st.markdown(f"""
<div class="section-heading">
<h2>Built With</h2>
<p>Modern, reliable and industry-standard tools.</p>
</div>

<div class="built-grid">

<div class="tech-item">
<div class="tech-icon">
<img src="{python_logo}" alt="Python">
</div>
<h3>Python</h3>
<p>Core programming language</p>
</div>

<div class="tech-item">
<div class="tech-icon">
<img src="{lightgbm_logo}" alt="LightGBM">
</div>
<h3>LightGBM</h3>
<p>Machine learning model</p>
</div>

<div class="tech-item">
<div class="tech-icon">
<img src="{fastapi_logo}" alt="FastAPI">
</div>
<h3>FastAPI</h3>
<p>High-performance API</p>
</div>

<div class="tech-item">
<div class="tech-icon">
<img src="{streamlit_logo}" alt="Streamlit">
</div>
<h3>Streamlit</h3>
<p>Interactive web interface</p>
</div>

</div>
""", unsafe_allow_html=True)
st.markdown("""
<div class="roadmap">
<div>
<span class="roadmap-badge">Future Roadmap</span>
<h2>From Predicting Churn to Helping Prevent Customer Loss</h2>
<p>The next phase of ChurnIQ will integrate SHAP explainability, company policies and an LLM + RAG system to generate grounded customer-retention recommendations.</p>
<div class="roadmap-current">
<span class="current-label">Current</span>
<span>ML-based churn prediction</span>
<span>→</span>
<span class="future-label">Future</span>
<span>AI-powered retention recommendations</span>
</div>
</div>
<div class="roadmap-flow">
<div class="roadmap-step"><span class="roadmap-step-icon">📊</span>Churn Prediction</div>
<div class="roadmap-step"><span class="roadmap-step-icon">🔍</span>SHAP / Key Factors</div>
<div class="roadmap-step"><span class="roadmap-step-icon">📄</span>Company Policies</div>
<div class="roadmap-step active"><span class="roadmap-step-icon">🧠</span>LLM + RAG</div>
<div class="roadmap-step"><span class="roadmap-step-icon">💡</span>Retention Recommendation</div>
</div>
</div>
""",unsafe_allow_html=True)
st.markdown("""
<div class="github-box">
<div class="github-left">
<div class="github-icon">◉</div>
<div>
<h3>Project Source</h3>
<p>Explore the complete project, architecture, implementation and documentation on GitHub.</p>
</div>
</div>
</div>
""",unsafe_allow_html=True)
st.markdown('<div class="footer">ChurnIQ • AI-Powered Churn Intelligence • Machine Learning Project</div>',unsafe_allow_html=True)