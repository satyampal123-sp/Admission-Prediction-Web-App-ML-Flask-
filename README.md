# Admission-Prediction-Web-App-ML-Flask-
This project is a machine learning-powered web application built with Flask to predict the chances of admission for a student into a university based on academic and profile parameters such as GRE, TOEFL, CGPA, SOP, and research experience.
# 🎓 Admission Prediction Web App

A machine learning-based web application built using **Flask** that predicts a student's **chance of admission** to a university based on academic profile and research experience.

---

## 🔍 About the Project

This project uses a trained machine learning model to predict the **probability of graduate school admission** based on key factors such as GRE score, TOEFL score, CGPA, university rating, SOP & LOR strengths, and research experience. The prediction is presented as a **percentage chance of admission**.

---

## 🧠 Machine Learning Details

- **Dataset:** [Graduate Admission Dataset from Kaggle](https://www.kaggle.com/mohansacharya/graduate-admissions)
- **Target Variable:** `Chance of Admit`
- **Algorithm Used:** `GradientBoostingClassifier` (converted `Chance of Admit` to binary for classification: ≥ 0.8 = Admit)
- **Scaler Used:** `StandardScaler` from `sklearn`
- **Model Evaluation:** Accuracy scores compared across multiple algorithms (Logistic Regression, SVM, KNN, Random Forest, Gradient Boosting)

---

## 🧾 Features

- Takes 7 input features from the user:
  - GRE Score
  - TOEFL Score
  - University Rating
  - SOP Strength
  - LOR Strength
  - CGPA
  - Research Experience (Yes/No)
- Predicts the **chance of admission** (e.g., `66.0%`)
- User-friendly web interface built with **Flask + HTML**

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS (Basic)
- **Backend:** Flask (Python)
- **ML Tools:** Pandas, NumPy, Scikit-learn, Joblib
- **Deployment Ready:** Localhost (can be deployed to Heroku, Render, etc.)

---
📈 Sample Prediction
Input:

GRE Score: 333

TOEFL Score: 120

University Rating: 4

SOP: 3.5

LOR: 4.5

CGPA: 8.9

Research: Yes

Output:
Chance of admission: 66.0%

📸 Screenshots
![image](https://github.com/user-attachments/assets/e1a4f510-9930-4aae-9e7f-44270f4a3df6)
![image](https://github.com/user-attachments/assets/a0cd91f8-4e5a-4870-8962-e86d7640f2de)
![image](https://github.com/user-attachments/assets/f26d363d-1d91-4fd9-a663-45c3a63be100)
![image](https://github.com/user-attachments/assets/fb38ca93-7ee6-4a6e-b549-a99f0e700d17)






