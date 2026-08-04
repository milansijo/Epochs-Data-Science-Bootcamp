# 🌐 Customer Churn Prediction Web Application

**Name:** Milan Sijo  
**MUID:** milansijo@mulearn

---

## 📖 Project Overview

This project deploys a **Machine Learning Customer Churn Prediction Model** as an interactive web application using **Streamlit**.

The application allows users to enter customer information such as age, tenure, subscription details, support calls, payment delay, and spending history. Based on these inputs, the trained machine learning model predicts whether the customer is likely to **churn** or **remain with the company**.

The project demonstrates the complete deployment workflow from model training to a publicly accessible web application.

---

## 🎯 Problem Statement

Customer churn is one of the biggest challenges faced by subscription-based businesses. Predicting potential churners allows companies to take preventive actions through personalized offers, improved customer support, and targeted retention strategies.

The objective of this project is to deploy a trained customer churn prediction model that enables users to obtain real-time predictions through a web interface.

---

## 📂 Dataset

**Dataset:** Customer Churn Dataset

**Source:** Kaggle

The dataset contains customer-related information including:

- Age
- Gender
- Tenure
- Usage Frequency
- Support Calls
- Payment Delay
- Subscription Type
- Contract Length
- Total Spend
- Last Interaction
- Churn (Target Variable)

---

## 🤖 Machine Learning Model

The deployed application uses a **Logistic Regression** model trained using Scikit-learn.

A preprocessing pipeline was created to ensure that:

- Missing values are handled automatically.
- Numerical features are standardized using StandardScaler.
- Categorical features are encoded using OneHotEncoder.
- The complete preprocessing and prediction workflow is stored as a single pipeline.

The trained pipeline is saved as:

```text
models/model.pkl
```

---

## 🛠️ Tech Stack

### Frontend

- Streamlit

### Backend

- Python

### Libraries

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- KaggleHub

---

## 🚀 Deployment Approach

The deployment process involved the following steps:

1. Downloaded the dataset from Kaggle.
2. Preprocessed the dataset.
3. Trained the Logistic Regression model.
4. Saved the complete preprocessing pipeline using Joblib.
5. Built an interactive Streamlit web application.
6. Uploaded the project to GitHub.
7. Deployed the application on Render.

---

## ✨ Application Features

The web application allows users to:

- Enter customer details through an interactive interface.
- Predict customer churn.
- Display whether the customer is likely to churn or stay.
- Display prediction probabilities for both classes.

---

## 📋 Input Features

The application accepts the following customer details:

- Age
- Gender
- Tenure
- Usage Frequency
- Support Calls
- Payment Delay
- Subscription Type
- Contract Length
- Total Spend
- Last Interaction

---

## 📤 Output

The application predicts:

- Customer is likely to Stay
- Customer is likely to Churn

It also displays the prediction probability for each class.

---

## ⚠️ Challenges Faced

During deployment, several challenges were encountered:

- Python environment conflicts caused by multiple Python installations.
- Dependency management for deployment.
- Large model size during initial deployment attempts.
- Model serialization and loading issues.
- Configuring the deployment environment.

These issues were resolved by using a deployment-friendly preprocessing pipeline and a lightweight Logistic Regression model.

---

## 🔍 Observations

- The deployed model provides predictions instantly through a simple web interface.
- Integrating preprocessing into the model pipeline simplifies deployment.
- Streamlit provides an efficient framework for deploying machine learning applications.
- Logistic Regression offers fast inference with a compact model size suitable for deployment.

---

## 🔮 Future Improvements

The application can be further improved by:

- Training more advanced models such as XGBoost or LightGBM.
- Adding visualizations for prediction probabilities.
- Including feature importance explanations.
- Supporting batch predictions using CSV uploads.
- Adding user authentication and prediction history.
- Improving the interface with custom themes and charts.

---

## 📂 Project Structure

```text
Day09/
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
└── models/
    └── model.pkl
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/milansijo/Epochs-Data-Science-Bootcamp.git
```

Navigate to the project:

```bash
cd Epochs-Data-Science-Bootcamp/Day09
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Locally

```bash
streamlit run app.py
```

---

## 🚀 Deployment

**Platform:** Render

**Live Application:**

```text
https://your-render-url.onrender.com
```

Replace the above link with your deployed Render URL after deployment.

---

## 📌 Conclusion

This project successfully demonstrates the end-to-end deployment of a Machine Learning model for customer churn prediction.

By combining a trained Logistic Regression model with Streamlit, the application provides an easy-to-use interface for generating real-time churn predictions. The project highlights the practical workflow of preprocessing, model training, deployment, and user interaction, making it a complete machine learning deployment solution.

---

## 🎯 Learning Outcomes

This project demonstrates:

- Machine Learning Model Deployment
- Streamlit Web Application Development
- End-to-End ML Pipeline
- Model Serialization with Joblib
- Cloud Deployment using Render

---

## 👨‍💻 Author

**Milan Sijo**

**MUID:** milansijo@mulearn

---

## 📄 License

This project was developed as part of the **Epochs Data Science Bootcamp – Day 09 Assignment** for educational purposes.