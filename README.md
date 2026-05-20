# 💳 Fraud Detection & Risk Segmentation System


## 🌐 Streamlit Deployment

Live Dashboard URL:

https://frauddetectionmahakkanwar-puenpugvfjdt4dumuwtckw.streamlit.app/

---

## 📌 Project Overview

This project is an AI-powered Fraud Detection System built using Machine Learning techniques to identify fraudulent financial transactions and classify them into different risk categories.

The system uses transaction behavior, amount patterns, and engineered fraud indicators to predict fraud probability and provide explainable risk analysis through an interactive Streamlit dashboard.

---

## 🚀 Features

- Fraud prediction using XGBoost
- Risk tier segmentation
- SHAP-based explainability
- Interactive Streamlit dashboard
- Transaction Explorer
- Fraud Probability Analysis
- Plotly interactive visualizations
- Hour-of-day fraud pattern analysis

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- LightGBM
- SHAP
- Plotly
- Streamlit
- Matplotlib
- Seaborn

---

## 📊 Machine Learning Models

The following models were trained and evaluated:

- LightGBM
- XGBoost
- Isolation Forest

XGBoost achieved the best overall performance.

---

## 📈 Key Visualizations

- SHAP Summary Plot
- Risk Tier Donut Chart
- Fraud Rate by Hour of Day
- Precision-Recall Curve
- Interactive Plotly Scatter Plot
- Fraud Probability Distribution

---

## 🔍 Dashboard Pages

### 📊 Overview
Displays:
- Fraud metrics
- Risk distribution
- Fraud probability analysis
- Hour-based fraud trends

### 🔍 Transaction Explorer
Allows users to:
- Filter transactions by risk tier
- Search by TransactionID
- Explore transaction details

Shows first 500 rows for better dashboard performance.

### 🧠 SHAP Explainer
Provides:
- Fraud probability prediction
- Risk classification
- Plain-English fraud explanation
- SHAP global summary visualization

---

## 📌 Business Insights

- High transaction amounts strongly increase fraud probability.
- Night-time transactions show elevated fraud risk.
- Behavioral anomalies are major fraud indicators.
- PR-AUC is more effective than accuracy for imbalanced fraud datasets.

---

## 🛡 Business Recommendations

- Real-time review for high-risk transactions
- Adaptive authentication for suspicious activity
- Continuous model retraining and monitoring

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run dashboard/app.py
```

---

## 📁 Project Structure

```text
FraudDetection_Mahak_Kanwar/
│
├── dashboard/
│   ├── app.py
│   ├── model.pkl
│   ├── processed_data.csv
│   └── pages/
│
├── charts/
├── analysis.ipynb
├── requirements.txt
├── README.md
└── Summary.docx
```

---

## Important Note

To ensure smooth GitHub hosting and Streamlit deployment, the dashboard uses a reduced processed dataset containing only 1000 rows instead of the full original dataset.

---

## 👩‍💻 Author

Mahak Kanwar