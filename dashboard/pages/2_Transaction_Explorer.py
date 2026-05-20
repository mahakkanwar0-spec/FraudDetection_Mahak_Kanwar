import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("processed_data.csv")

st.title("🔍 Transaction Explorer")

# Sidebar Filters
risk_filter = st.sidebar.multiselect(
    "Select Risk Tier",
    options=df['RiskTier'].unique(),
    default=df['RiskTier'].unique()
)

filtered_df = df[
    df['RiskTier'].isin(risk_filter)
]

# Show limited rows only
st.subheader("Filtered Transactions")

st.dataframe(
    filtered_df.head(500)
)

st.info(
    "Showing first 500 rows to improve dashboard performance."
)

# Search by TransactionID
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