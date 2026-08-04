# 📉 Customer Churn Prediction

**Name:** Milan Sijo  
**MUID:** milansijo@mulearn

---

## 📖 Project Overview

Customer churn occurs when a customer stops using a company's products or services. Predicting customer churn can help businesses identify customers who are at risk of leaving and take appropriate retention measures.

The objective of this project is to build and compare multiple Machine Learning classification models to predict whether a customer is likely to churn based on customer demographic, subscription, usage, spending, and interaction information.

This can help businesses make better customer retention decisions by identifying potentially high-risk customers before they leave.

Since the target variable represents whether a customer churned or not, this is a **Supervised Machine Learning Classification problem**.

---

## 📂 Dataset Overview

**Dataset:** Customer Churn Dataset  
**Source:** Kaggle

The dataset contains customer information related to demographics, subscription details, usage behavior, customer support interactions, payments, spending, and churn status.

Separate training and testing datasets were provided and used for model development and evaluation.

The dataset contains the following columns:

- `CustomerID`
- `Age`
- `Gender`
- `Tenure`
- `Usage Frequency`
- `Support Calls`
- `Payment Delay`
- `Subscription Type`
- `Contract Length`
- `Total Spend`
- `Last Interaction`
- `Churn`

---

## 🎯 Features & Target Variable

### Target Variable

The target variable is:

`Churn`

It represents whether a customer has churned.

- `0` → Customer did not churn
- `1` → Customer churned

### Numerical Features

The numerical features used for prediction are:

- `Age`
- `Tenure`
- `Usage Frequency`
- `Support Calls`
- `Payment Delay`
- `Total Spend`
- `Last Interaction`

### Categorical Features

The categorical features are:

- `Gender`
- `Subscription Type`
- `Contract Length`

### Removed Feature

`CustomerID` was removed before model training because it is an identifier and does not represent customer behavior or characteristics useful for predicting churn.

---

## 🛠️ Preprocessing Pipeline

The dataset was prepared before training the classification models.

### 1. Missing Value Handling

Missing values were checked in both the training and testing datasets.

Numerical missing values were handled using the median values obtained from the training data.

Categorical missing values were handled using the most frequent category from the training data.

### 2. Removing CustomerID

The `CustomerID` column was removed because it serves only as a unique identifier and does not provide meaningful predictive information about customer churn.

### 3. Categorical Encoding

Categorical variables were converted into numerical format using **One-Hot Encoding**.

The encoded categorical features were:

- `Gender`
- `Subscription Type`
- `Contract Length`

The training and testing datasets were aligned after encoding to ensure that both contained the same feature columns.

### 4. Feature Scaling

Numerical features were standardized using `StandardScaler`.

The scaler was fitted using the training dataset and the same transformation was applied to the testing dataset.

### 5. Training and Testing Data

The dataset already contained separate training and testing files. Therefore, these provided datasets were used directly for model training and testing.

---

## 🤖 Models Implemented

Three classification models were developed and compared.

### 1. Logistic Regression

Logistic Regression was implemented as a baseline classification model.

It estimates the probability of a customer belonging to the churn class based on the input features.

### 2. Decision Tree Classifier

Decision Tree Classifier was implemented to capture nonlinear relationships and interactions between customer characteristics.

The model creates decision rules by recursively splitting the dataset based on feature values.

### 3. Random Forest Classifier

Random Forest Classifier combines predictions from multiple Decision Trees.

Using multiple trees can reduce the variance associated with an individual Decision Tree and allows the model to capture complex relationships between customer characteristics.

---

## 📊 Performance Comparison

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

The obtained results were:

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---:|---:|---:|---:|
| Logistic Regression | **57.11%** | **52.51%** | 99.06% | **68.64%** |
| Decision Tree Classifier | 50.33% | 48.81% | **99.87%** | 65.58% |
| Random Forest Classifier | 50.35% | 48.82% | 99.86% | 65.58% |

### Confusion Matrix — Logistic Regression

```text
[[ 6561 27320]
 [  287 30206]]
```

- True Negatives: 6,561
- False Positives: 27,320
- False Negatives: 287
- True Positives: 30,206

### Confusion Matrix — Decision Tree Classifier

```text
[[ 1948 31933]
 [   40 30453]]
```

- True Negatives: 1,948
- False Positives: 31,933
- False Negatives: 40
- True Positives: 30,453

### Confusion Matrix — Random Forest Classifier

```text
[[ 1960 31921]
 [   43 30450]]
```

- True Negatives: 1,960
- False Positives: 31,921
- False Negatives: 43
- True Positives: 30,450

---

## 🏆 Best Model with Justification

Among the three models evaluated, **Logistic Regression was selected as the best-performing model overall**.

Its performance was:

- **Accuracy:** 57.11%
- **Precision:** 52.51%
- **Recall:** 99.06%
- **F1-Score:** 68.64%

Logistic Regression achieved the **highest Accuracy, Precision, and F1-Score** among the three models while maintaining an extremely high Recall of **99.06%**.

Decision Tree achieved the highest Recall of 99.87%, while Random Forest achieved 99.86%. However, both models had considerably lower Accuracy and Precision and lower F1-Scores than Logistic Regression.

Therefore, Logistic Regression provides the best overall balance among the three models tested.

Its high Recall means that the model successfully identifies most customers who actually churn. Out of 30,493 actual churners in the test data, Logistic Regression correctly identified 30,206 and missed only 287.

However, the model also produced 27,320 false positives. Therefore, although it performed best among the three tested models, there is significant scope for improving its ability to distinguish churners from non-churners.

---

## 🔍 Key Observations

1. **All three models achieved extremely high Recall**, meaning that almost all actual churners were identified.

2. **Logistic Regression achieved the best overall performance**, with the highest Accuracy, Precision, and F1-Score.

3. **Decision Tree achieved the highest Recall** at approximately 99.87%, but this came with low Precision and a large number of false positives.

4. **Random Forest produced results very similar to Decision Tree**, achieving 99.86% Recall but only 48.82% Precision.

5. All three models produced a **large number of false positives**, indicating that many customers who did not churn were classified as churners.

6. The results demonstrate why Accuracy alone is not sufficient for evaluating a churn classifier. Precision, Recall, F1-Score, and the Confusion Matrix provide important additional information about model behavior.

7. Logistic Regression provided the best balance among the models evaluated, but its relatively low Precision shows that further optimization would be necessary before relying on the model for real-world retention decisions.

---

## 💼 Business Recommendations

### 1. Identify Potential Churners Early

The churn model can be used as an early-warning system to identify customers who may be at risk of leaving.

Customers identified as high risk can be considered for proactive retention strategies.

### 2. Apply Targeted Retention Strategies

Potential churners can be targeted with measures such as:

- Personalized offers
- Loyalty rewards
- Subscription incentives
- Customer support outreach
- Service improvements

### 3. Consider the Cost of False Positives

The Logistic Regression model produced 27,320 false positives.

This means that automatically providing expensive incentives to every predicted churner could result in significant unnecessary spending.

Model predictions should therefore be combined with additional business rules or risk scoring before costly retention actions are taken.

### 4. Monitor Customer Behavior

Factors such as:

- Usage frequency
- Support calls
- Payment delays
- Customer tenure
- Total spending
- Last interaction

can be monitored to identify changes in customer behavior that may indicate an increased risk of churn.

### 5. Prioritize Retention Resources

Rather than treating every predicted churner equally, businesses can prioritize customers based on churn probability, customer value, and the cost of retention.

---

## 🔮 Future Improvements

### 1. Classification Threshold Tuning

The default classification threshold can be adjusted to achieve a better balance between Precision and Recall.

This may help reduce the large number of false-positive predictions.

### 2. Hyperparameter Tuning

`GridSearchCV` or `RandomizedSearchCV` can be used to optimize parameters for Decision Tree and Random Forest models.

### 3. Cross-Validation

K-Fold Cross-Validation can be used to evaluate the models across multiple data splits and obtain a more reliable estimate of model performance.

### 4. Additional Classification Models

More advanced classification algorithms can be explored, such as:

- Gradient Boosting
- XGBoost
- LightGBM
- CatBoost

### 5. Additional Evaluation Metrics

Future experiments can use:

- ROC-AUC
- Precision-Recall Curve
- PR-AUC
- Specificity

These metrics can provide additional insight into model performance.

### 6. Feature Engineering

Additional features derived from customer behavior, spending patterns, support interactions, and subscription history could potentially improve churn prediction.

---

## 🛠️ Tech Stack

### Libraries

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Google Colab

---

## 📂 Project Structure

```text
Day06/
│
├── customer_churn_prediction.ipynb
└── README.md
```

The notebook contains:

- Data preprocessing
- Model development
- Model evaluation
- Model comparison
- Final model selection

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/milansijo/Epochs-Data-Science-Bootcamp.git
```

Navigate to the project:

```bash
cd Epochs-Data-Science-Bootcamp/Day06
```

Install the required libraries:

```bash
pip install pandas numpy scikit-learn matplotlib
```

---

## ▶️ Run Locally

1. Open `customer_churn_prediction.ipynb` in Google Colab or Jupyter Notebook.

2. Run all notebook cells to reproduce the preprocessing, model training, evaluation, and comparison.

---

## 🎯 Learning Outcomes

This project demonstrates:

- Supervised Machine Learning (Classification)
- Data Preprocessing and Encoding
- Model Training and Evaluation
- Confusion Matrix Analysis
- Business Recommendations from ML Predictions

---

## 👨‍💻 Author

**Milan Sijo**

**MUID:** milansijo@mulearn

---

## 📄 License

This project was developed as part of the **Epochs Data Science Bootcamp – Day 06 Assignment** for educational purposes.