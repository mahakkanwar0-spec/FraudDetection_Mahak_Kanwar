import streamlit as st

st.set_page_config(
    page_title="Fraud Detection Dashboard",
    page_icon="💳",
    layout="wide"
)

st.title("💳 Real-Time Fraud Detection Dashboard")

st.markdown("""
### Welcome to the AI-Powered Fraud Detection System

This dashboard provides:

- 📊 Fraud analytics and visualizations
- 🔍 Transaction-level fraud investigation
- 🧠 SHAP-based model explainability
- ⚠️ Risk tier analysis and fraud insights

Use the sidebar to navigate between dashboard modules.
""")

st.divider()

st.info(
    "Built using XGBoost, SHAP, Streamlit, and Plotly."
)