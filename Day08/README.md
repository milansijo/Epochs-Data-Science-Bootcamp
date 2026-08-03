# Customer Churn Prediction – Model Optimization

**Name:** Milan Sijo  
**MUID:** milansijo@mulearn

## Project Summary

This project focuses on optimizing a Machine Learning model for **Customer Churn Prediction**.

The objective is to predict whether a customer is likely to churn and analyze the factors that are most important in the model's churn predictions.

A **Random Forest Classifier** was used as the baseline model. The model was then optimized using hyperparameter tuning, and the baseline and optimized models were compared using Accuracy, Precision, Recall, and F1-Score.

Feature importance from the optimized Random Forest was also analyzed to identify the customer attributes that contributed most to its predictions.

---

## Dataset

**Dataset:** Customer Churn Dataset  
**Source:** Kaggle

The dataset contains customer demographic, subscription, usage, spending, payment, and interaction information.

The target variable is:

`Churn`

- `0` – Customer did not churn
- `1` – Customer churned

The dataset contains features including:

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

`CustomerID` was excluded from model training because it is an identifier rather than a customer behavior feature.

---

## Baseline Model

A **Random Forest Classifier** was used as the baseline classification model.

The baseline model achieved:

| Metric | Score |
|---|---:|
| Accuracy | 50.35% |
| Precision | 48.82% |
| Recall | 99.86% |
| F1-Score | 65.58% |

The model achieved extremely high Recall, meaning that it identified almost all customers who churned.

However, the relatively low Precision indicates that many non-churning customers were also incorrectly predicted as churners.

---

## Optimization Approach

The Random Forest model was optimized using **RandomizedSearchCV**.

The hyperparameters explored included:

- Number of trees (`n_estimators`)
- Maximum tree depth (`max_depth`)
- Minimum samples required to split a node (`min_samples_split`)
- Minimum samples required at a leaf (`min_samples_leaf`)
- Number of features considered at each split (`max_features`)

The search used **3-fold cross-validation** and F1-Score as the optimization metric.

### Best Hyperparameters

The best parameters identified were:

```text
n_estimators      = 200
max_depth         = None
max_features      = log2
min_samples_split = 2
min_samples_leaf  = 1
```

These parameters were used for the optimized Random Forest model.

---

## Model Performance Comparison

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---:|---:|---:|---:|
| Baseline Random Forest | 50.35% | 48.82% | 99.86% | 65.58% |
| Optimized Random Forest | 50.34% | 48.82% | 99.86% | 65.58% |

### Comparison

Hyperparameter optimization did **not produce a meaningful improvement** in test performance.

The baseline and optimized models achieved almost identical Precision, Recall, and F1-Score. Accuracy decreased very slightly from approximately 50.35% to 50.34%.

The high Recall indicates that both models successfully identify almost all churners. However, the Precision of approximately 48.82% indicates that the models also classify many non-churning customers as churners.

---

## Feature Importance

Feature importance from the optimized Random Forest was analyzed to understand which variables contributed most to the model's predictions.

| Feature | Importance |
|---|---:|
| Support Calls | 30.42% |
| Total Spend | 21.09% |
| Age | 13.89% |
| Contract Length – Monthly | 12.79% |
| Payment Delay | 12.46% |
| Last Interaction | 3.92% |
| Gender – Male | 3.41% |
| Tenure | 0.93% |
| Contract Length – Quarterly | 0.55% |
| Usage Frequency | 0.34% |
| Subscription Type – Premium | 0.10% |
| Subscription Type – Standard | 0.09% |

### Most Important Features

The five most important features were:

1. **Support Calls – 30.42%**
2. **Total Spend – 21.09%**
3. **Age – 13.89%**
4. **Monthly Contract – 12.79%**
5. **Payment Delay – 12.46%**

Together, these features accounted for most of the feature importance in the Random Forest model.

Support Calls was the most influential feature, followed by Total Spend.

Feature importance represents how useful a feature was to the Random Forest for making predictions. It does not by itself establish that the feature causes customer churn.

---

## Important Observations and Findings

- Both Random Forest models achieved approximately **99.86% Recall**.
- The models were therefore able to identify almost all customers who actually churned.
- Precision remained relatively low at approximately **48.82%**, indicating a high number of false-positive predictions.
- Hyperparameter tuning did not significantly improve model performance.
- **Support Calls** was the most important feature in the optimized Random Forest.
- **Total Spend, Age, Monthly Contract, and Payment Delay** also contributed strongly to the model's predictions.
- Subscription Type and Usage Frequency had comparatively low feature importance.
- The model's very high Recall but low Precision suggests that it tends to classify customers as churners aggressively.

---

## Model Improvements

RandomizedSearchCV successfully identified an alternative set of Random Forest hyperparameters, but these parameters did not improve performance on the test dataset.

Further improvements could include:

- **Classification threshold tuning** to find a better balance between Precision and Recall.
- Performing more extensive **hyperparameter tuning** with a larger search space.
- Using **cross-validation** to analyze model stability.
- Performing additional **feature engineering** using customer behavior and interaction information.
- Comparing Random Forest with other classification algorithms such as Gradient Boosting, XGBoost, LightGBM, or CatBoost.
- Evaluating the model using additional metrics such as **ROC-AUC** and **Precision-Recall AUC**.
- Investigating the training and testing distributions to understand the unusually high Recall and false-positive behavior.

---

## Business Recommendations

The model results can be used to guide further customer retention analysis.

- Customers showing patterns in important features such as **Support Calls** and **Payment Delay** can be monitored more closely.
- Support interactions should be analyzed to identify recurring service issues that may be associated with churn risk.
- Payment-related behavior can be monitored to identify customers who may require reminders or additional payment support.
- Contract length and customer spending behavior can be considered when designing retention campaigns.
- Churn predictions can be used as an early risk signal for identifying customers requiring further analysis.
- Because the model produces many false positives, expensive retention offers should not be automatically given to every customer predicted to churn.

---

## Final Conclusion

This project optimized a Random Forest model for Customer Churn Prediction using **RandomizedSearchCV**.

The optimized model achieved approximately **50.34% Accuracy, 48.82% Precision, 99.86% Recall, and 65.58% F1-Score**.

Hyperparameter tuning did not result in a meaningful improvement compared with the baseline Random Forest model. Both models demonstrated extremely high Recall but relatively low Precision.

Feature importance analysis showed that **Support Calls, Total Spend, Age, Monthly Contract, and Payment Delay** were the most influential features in the model's predictions.

Although the model successfully identifies most churners, the large number of false positives indicates that further optimization is required before using its predictions directly for costly customer retention decisions.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Google Colab

### Machine Learning Techniques

- Data Preprocessing
- Categorical Encoding
- Random Forest Classification
- RandomizedSearchCV
- Hyperparameter Tuning
- Cross-Validation
- Model Evaluation
- Feature Importance Analysis

---

## Repository Structure

```text
Day8/
│
├── model_optimization.ipynb
└── README.md
```

---

## Assignment Details

**Epochs '26 – Assignment 8**  
**Model Optimization – Customer Churn Prediction**

**Name:** Milan Sijo  
**MUID:** milansijo@mulearn

**Submission Tag:** `#evn-ds-epochs26-day08`