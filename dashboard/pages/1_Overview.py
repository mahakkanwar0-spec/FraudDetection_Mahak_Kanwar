import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Fraud Detection Overview",
    layout="wide"
)

# =========================
# PATH SETUP
# =========================

BASE_DIR = Path(__file__).resolve().parent.parent

# =========================
# LOAD DATA
# =========================

@st.cache_data
def load_data():
    return pd.read_csv(
        BASE_DIR / "processed_data.csv"
    )

df = load_data()

# =========================
# TITLE
# =========================

st.title("📊 Fraud Detection Overview")

# =========================
# SIDEBAR FILTERS
# =========================

st.sidebar.header("Filter Options")

risk_filter = st.sidebar.multiselect(
    "Select Risk Tier",
    options=df['RiskTier'].unique(),
    default=df['RiskTier'].unique()
)

filtered_df = df[
    df['RiskTier'].isin(risk_filter)
]

# =========================
# METRICS
# =========================

total_transactions = len(filtered_df)

fraud_count = filtered_df[
    'ActualFraud'
].sum()

detection_rate = (
    fraud_count / total_transactions
) * 100

avg_fraud_amt = filtered_df[
    filtered_df['ActualFraud'] == 1
]['TransactionAmt'].mean()

# =========================
# DISPLAY METRICS
# =========================

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Transactions",
    total_transactions
)

col2.metric(
    "Fraud Count",
    int(fraud_count)
)

col3.metric(
    "Detection Rate",
    f"{detection_rate:.2f}%"
)

col4.metric(
    "Average Fraud Amount",
    f"{avg_fraud_amt:.2f}"
)

# =========================
# RISK TIER CHART
# =========================

st.subheader("Risk Tier Distribution")

risk_counts = filtered_df[
    'RiskTier'
].value_counts()

fig1 = px.pie(
    names=risk_counts.index,
    values=risk_counts.values,
    hole=0.5,
    title="Risk Tier Distribution"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# =========================
# FRAUD PROBABILITY
# =========================

st.subheader("Fraud Probability Distribution")

fig2 = px.histogram(
    filtered_df,
    x="FraudProbability",
    nbins=50,
    title="Fraud Probability Distribution"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# =========================
# HOUR ANALYSIS
# =========================

if 'HourOfDayOriginal' in filtered_df.columns:

    st.subheader(
        "Fraud Pattern by Hour"
    )

    fig3 = px.histogram(
        filtered_df,
        x="HourOfDayOriginal",
        color="RiskTier",
        barmode="group",
        title="Fraud Risk by Hour of Day"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

# =========================
# TOP TRANSACTIONS
# =========================

st.subheader(
    "Top High-Risk Transactions"
)

top_risk = filtered_df.sort_values(
    by='FraudProbability',
    ascending=False
).head(20)

st.dataframe(top_risk)