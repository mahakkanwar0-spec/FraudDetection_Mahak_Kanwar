import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# =========================
# PATH SETUP
# =========================

BASE_DIR = Path(__file__).resolve().parent.parent

# =========================
# LOAD DATA & MODEL
# =========================

df = pd.read_csv(
    BASE_DIR / "processed_data.csv"
)

model = joblib.load(
    BASE_DIR / "model.pkl"
)

# =========================
# TITLE
# =========================

st.title("🧠 SHAP Fraud Explainer")

# =========================
# TRANSACTION INPUT
# =========================

transaction_id = st.number_input(
    "Enter TransactionID",
    min_value=int(df['TransactionID'].min()),
    max_value=int(df['TransactionID'].max()),
    step=1
)

# =========================
# FIND TRANSACTION
# =========================

transaction = df[
    df['TransactionID'] == transaction_id
]

if not transaction.empty:

    st.subheader("Transaction Details")

    st.write(transaction)

    # Store values
    actual_amt = transaction[
        'TransactionAmt'
    ].values[0]

    actual_hour = transaction[
        'HourOfDay'
    ].values[0]

    # Features
    features = transaction.drop(
        columns=[
            'TransactionID',
            'ActualFraud',
            'RiskTier',
            'FraudProbability',
            'HourOfDayOriginal'
        ],
        errors='ignore'
    )

    # Prediction
    fraud_prob = model.predict_proba(
        features
    )[:,1][0]

    st.subheader("Fraud Probability")

    st.write(f"{fraud_prob:.2%}")

    # =========================
    # RISK LEVEL
    # =========================

    if fraud_prob >= 0.75:
        risk = "🔴 Critical Risk"

    elif fraud_prob >= 0.40:
        risk = "🟡 Suspicious"

    else:
        risk = "🟢 Clear"

    st.subheader("Risk Tier")

    st.write(risk)

    # =========================
    # EXPLANATION
    # =========================

    st.subheader("Explanation")

    explanation = []

    if actual_amt > df[
        'TransactionAmt'
    ].mean():

        explanation.append(
            "High transaction amount increased fraud suspicion."
        )

    if actual_hour >= 22 or actual_hour <= 5:

        explanation.append(
            "Transaction occurred during unusual night hours."
        )

    if fraud_prob >= 0.75:

        explanation.append(
            "Model detected strong fraud-related behavioral patterns."
        )

    if fraud_prob < 0.40:

        explanation.append(
            "Transaction behavior appears normal and low risk."
        )

    if len(explanation) == 0:

        explanation.append(
            "Transaction contains moderate risk indicators."
        )

    for exp in explanation:

        st.write("- ", exp)

    # =========================
    # SHAP IMAGE
    # =========================

    st.subheader("SHAP Global Summary")

    st.image(
         "shap_summary.png"
    )

else:
    st.error("TransactionID not found.")