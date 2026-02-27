# 🏦 Credit Risk Prediction System

## 📌 Overview

The **Credit Risk Prediction System** is a Machine Learning based application designed to evaluate the financial risk associated with loan applicants.
The system analyzes applicant information, credit behaviour, and loan characteristics to estimate the probability of loan default and generate a credit score.

This project demonstrates an **end-to-end Machine Learning pipeline**, including data preprocessing, model training, feature engineering, and deployment using Streamlit.

---

## 🚀 Live Application

🔗 Live Demo: https://your-app-name.streamlit.app

---

## 🎯 Problem Statement

Financial institutions must assess whether a borrower is capable of repaying a loan. Manual evaluation is time-consuming and prone to bias.

This project automates credit evaluation using Machine Learning to support **data-driven lending decisions**.

---

## ⚙️ Features

* Credit Risk Prediction
* Default Probability Estimation
* Credit Score Generation (300–900)
* Risk Rating Classification
* Interactive Streamlit Dashboard
* Financial Parameter Documentation Guide

---

## 🧠 Machine Learning Workflow

1. Data Collection
2. Data Cleaning & Preprocessing
3. Feature Engineering
4. Feature Scaling using MinMaxScaler
5. Model Training (Logistic Regression)
6. Model Fine Tuning using optuna
7. Model Serialization using Joblib
8. Deployment using Streamlit Cloud

---

## 🛠 Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib

---

## 📊 Input Parameters

The model evaluates applicants using:

* Age
* Income
* Loan Amount
* Loan Tenure
* Loan to Income Ratio
* Credit Utilization Ratio
* Average Days Past Due (DPD)
* Delinquency Ratio
* Number of Open Accounts
* Residence Type
* Loan Purpose
* Loan Type

---

## 📈 Model Output

The system provides:

* Default Probability
* Credit Score (300–900)
* Risk Rating (Poor / Average / Good / Excellent)

---

## 📂 Project Structure

```
ml-project-credit-risk-model
│
├── artifacts/
│   └── model_data.joblib
├── main.py
├── prediction_helper.py
├── requirements.txt
├── README.md
└── images/
```

---

## ▶️ How to Run Locally

Clone repository:

```
git clone https://github.com/Pratham037/ml-project-credit-risk-model.git
```

Move into project folder:

```
cd ml-project-credit-risk-model
```

Install dependencies:

```
pip install -r requirements.txt
```

Run application:

```
streamlit run main.py
```

---

## 📷 Application Preview

(Add screenshots here after deployment)

---

## 🌐 Deployment

The application is deployed using **Streamlit Cloud** for real-time access.

---

## 👨‍💻 Author

**Pratham More**

Computer Science Engineering (Data Science)

---

## ⭐ Future Improvements

* Advanced ML Models (XGBoost / Random Forest)
* Explainable AI (SHAP values)
* API integration using FastAPI
* Banking dataset expansion
