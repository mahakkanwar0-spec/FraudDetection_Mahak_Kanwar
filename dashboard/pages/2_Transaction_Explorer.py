import streamlit as st
import pandas as pd
from pathlib import Path

# =========================
# PATH SETUP
# =========================

BASE_DIR = Path(__file__).resolve().parent.parent

# =========================
# LOAD DATA
# =========================

df = pd.read_csv(
    BASE_DIR / "processed_data.csv"
)

# =========================
# TITLE
# =========================

st.title("🔍 Transaction Explorer")

# =========================
# SIDEBAR FILTERS
# =========================

risk_filter = st.sidebar.multiselect(
    "Select Risk Tier",
    options=df['RiskTier'].unique(),
    default=df['RiskTier'].unique()
)

filtered_df = df[
    df['RiskTier'].isin(risk_filter)
]

# =========================
# SHOW DATA
# =========================

st.subheader("Filtered Transactions")

st.dataframe(
    filtered_df.head(500)
)

st.info(
    "Showing first 500 rows to improve dashboard performance."
)

# =========================
# SEARCH TRANSACTION
# =========================

st.subheader("Search Transaction")

transaction_id = st.number_input(
    "Enter TransactionID",
    min_value=int(df['TransactionID'].min()),
    max_value=int(df['TransactionID'].max()),
    step=1
)

search_result = filtered_df[
    filtered_df['TransactionID'] == transaction_id
]

if not search_result.empty:

    st.subheader("Transaction Details")

    st.write(search_result)

    st.subheader("Fraud Probability")

    fraud_prob = search_result[
        'FraudProbability'
    ].values[0]

    st.write(f"{fraud_prob:.2%}")

    st.subheader("Risk Tier")

    st.write(
        search_result['RiskTier'].values[0]
    )

else:
    st.warning("TransactionID not found.")