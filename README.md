# 📊 Customer Churn Prediction

A Machine Learning web application that predicts whether a telecom customer is likely to churn.

## 🎯 Project Objective

The goal of this project is to predict customer churn based on customer information such as age, gender, tenure, monthly charges, contract type, payment method, and total charges.

This can help telecom companies identify customers who may leave and take appropriate retention actions.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learns
- Random Forest Classifier
- Joblib
- Streamlit

## 🤖 Machine Learning

A Random Forest classification model was trained on telecom customer data.

The machine learning workflow is:

Dataset → Data Preprocessing → Model Training → Model Evaluation → Model Saving → Streamlit Web App → Prediction

## 🌐 Web Application

The Streamlit application allows users to enter customer details and receive a churn prediction.

The application provides two possible results:

- ⚠️ Customer is likely to churn
- ✅ Customer is likely to stay

## 📌 Features

- Customer information input
- Data preprocessing
- Churn prediction using Machine Learning
- Simple and interactive Streamlit interface
- Prediction for new/unseen customer data

## 🚀 How to Run

Install the required libraries:

```bash
pip install streamlit pandas scikit-learn joblib