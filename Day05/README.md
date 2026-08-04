# 🚗 Car Price Prediction Using Regression Models

**Name:** Milan Sijo  
**MUID:** milansijo@mulearn

---

## 📖 Project Overview

This project was completed as part of the **Epochs: Data Science Bootcamp '26 - Day 05 Assignment**.

The objective of this project is to build and compare multiple **Machine Learning regression models** for predicting the selling price of used cars using the **CarDekho Used Car Dataset**.

The project covers the Machine Learning workflow including problem understanding, data preprocessing, feature engineering, categorical encoding, train-test splitting, model development, model evaluation, comparison, and final model selection.

---

## 🎯 Business Objective

The used-car market contains vehicles with different brands, models, ages, mileage, engine specifications, fuel types, transmission types, and usage histories.

The objective of this project is to develop a Machine Learning model that can estimate the **selling price of a used car based on its characteristics**.

Such a prediction system can help:

- Buyers evaluate used-car prices.
- Sellers estimate suitable selling prices.
- Used-car platforms support automated vehicle valuation.
- Businesses make data-driven pricing decisions.

Since the target variable is numerical and continuous, this is a **Supervised Machine Learning Regression problem**.

---

## 📂 Dataset Overview

**Dataset:** CarDekho Used Car Dataset  
**Source:** Kaggle - CarDekho Used Car Data

The dataset contains information about used cars and their selling prices, including vehicle specifications, usage information, and categorical characteristics.

The dataset was explored before model development to understand:

- Dataset structure
- Numerical and categorical features
- Missing values
- Duplicate records
- Data types
- Feature characteristics

The unnecessary `Unnamed: 0` index column was removed because it did not contain meaningful vehicle information.

---

## 🎯 Target Variable

The target variable is:

```text
selling_price
```

It represents the selling price of a used vehicle.

---

## 🔢 Numerical Features

The numerical features include:

- `vehicle_age`
- `km_driven`
- `mileage`
- `engine`
- `max_power`
- `seats`

An additional numerical feature, `km_per_year`, was created during feature engineering.

---

## 🔤 Categorical Features

The categorical features include:

- `car_name`
- `brand`
- `model`
- `seller_type`
- `fuel_type`
- `transmission_type`

Categorical variables were converted into numerical representations before model training.

---

## 🛠️ Data Preparation

Before model development, the dataset was prepared for Machine Learning.

### Missing Values

Missing values were checked and handled appropriately where required.

### Duplicate Records

Duplicate records were identified and removed where applicable to prevent repeated observations from unnecessarily influencing model training.

### Unnecessary Columns

The `Unnamed: 0` column was removed because it represented an index rather than useful information about a vehicle.

### Categorical Encoding

Categorical variables were encoded into numerical representations so they could be processed by the regression algorithms.

### Feature Scaling

Numerical features were scaled where required to make features suitable for model training.

### Train-Test Split

The dataset was divided into training and testing sets using an **80:20 split**:

- **80%** for training
- **20%** for testing

A fixed `random_state` was used to make the split reproducible.

---

## ⚙️ Feature Engineering

Two new features were engineered from the existing dataset.

### 1. Kilometers Driven Per Year — `km_per_year`

A new feature called `km_per_year` was created by dividing the total kilometers driven by the age of the vehicle.

```python
data["km_per_year"] = (
    data["km_driven"] /
    data["vehicle_age"].clip(lower=1)
)
```

The calculation can be represented as:

```text
km_per_year = km_driven / vehicle_age
```

`vehicle_age` was clipped to a minimum value of `1` to prevent division by zero for vehicles with an age of zero.

This feature provides a measure of the vehicle's **average annual usage** rather than considering total kilometers driven alone.

For example, two vehicles may both have travelled the same total distance, but the newer vehicle may have experienced significantly heavier annual usage.

---

### 2. Automatic Transmission Indicator — `is_automatic`

A binary feature called `is_automatic` was created from the existing `transmission_type` column.

```python
data["is_automatic"] = (
    data["transmission_type"]
    .str.lower()
    .eq("automatic")
    .astype(int)
)
```

The feature represents:

```text
Automatic transmission     → 1
Non-automatic transmission → 0
```

This converts the transmission information into a simple numerical indicator that can be used by the Machine Learning models.

---

## 🤖 Regression Models Implemented

Three regression models were developed and evaluated.

### 1. Linear Regression

Linear Regression was used as a baseline model for predicting used-car selling prices.

#### Strengths

- Simple and computationally efficient
- Easy to understand
- Provides a useful baseline

#### Limitations

- Assumes largely linear relationships
- May struggle with complex interactions between vehicle characteristics
- Can be affected by outliers and multicollinearity

---

### 2. Decision Tree Regressor

Decision Tree Regression predicts selling prices by recursively splitting observations based on their feature values.

#### Strengths

- Captures nonlinear relationships
- Handles complex feature interactions
- Does not require linear relationships between features and the target

#### Limitations

- Can overfit training data
- Can have high variance
- Predictions may be sensitive to changes in the training data

---

### 3. Random Forest Regressor

Random Forest combines predictions from multiple Decision Trees to produce a more robust regression model.

#### Strengths

- Handles nonlinear relationships effectively
- Captures complex interactions between features
- Reduces the variance associated with a single Decision Tree
- Performs well on many tabular datasets

#### Limitations

- More computationally expensive
- Less interpretable than simpler models
- Performance can depend on hyperparameter selection

---

## 📊 Model Evaluation

The three models were evaluated using four regression metrics:

### Mean Absolute Error (MAE)

Measures the average absolute difference between the actual and predicted selling prices.

**Lower is better.**

### Mean Squared Error (MSE)

Measures the average squared difference between actual and predicted values. Large prediction errors receive a greater penalty.

**Lower is better.**

### Root Mean Squared Error (RMSE)

The square root of MSE, expressing the prediction error in the same units as the target variable.

**Lower is better.**

### R² Score

Measures how much of the variation in selling prices is explained by the model.

**Higher is better.**

---

## 📈 Performance Comparison

| Model | MAE | MSE | RMSE | R² Score |
|---|---:|---:|---:|---:|
| Linear Regression | 177,496.44 | 1.507472 × 10¹¹ | 388,261.73 | 0.7997 |
| Decision Tree Regressor | 127,260.83 | 9.469422 × 10¹⁰ | 307,724.26 | 0.8742 |
| **Random Forest Regressor** | **95,721.92** | **4.707407 × 10¹⁰** | **216,965.59** | **0.9375** |

---

## 🏆 Best-Performing Model

The **Random Forest Regressor** achieved the best overall performance.

Its evaluation results were:

```text
MAE      : 95,721.92
MSE      : 4.707407 × 10¹⁰
RMSE     : 216,965.59
R² Score : 0.9375
```

Random Forest achieved:

- The **lowest MAE**
- The **lowest MSE**
- The **lowest RMSE**
- The **highest R² Score**

The R² score of approximately **0.9375** indicates that the model explains approximately **93.75% of the variation in selling prices in the test dataset**.

---

### Why Random Forest Performed Better

Used-car prices depend on complex relationships among factors such as:

- Vehicle age
- Kilometers driven
- Annual vehicle usage
- Brand and model
- Engine capacity
- Maximum power
- Mileage
- Fuel type
- Transmission type
- Seller type

Linear Regression achieved an R² score of approximately **0.80**, providing a useful baseline but showing that a simple linear model could not capture all the relationships in the dataset.

Decision Tree Regression improved the R² score to approximately **0.87** because it can model nonlinear patterns.

Random Forest further improved performance by combining multiple Decision Trees, allowing it to capture nonlinear relationships while reducing the variance associated with relying on a single tree.

Therefore, **Random Forest Regressor was selected as the best-performing model**.

---

## 🔍 Key Observations

1. **Random Forest achieved the strongest overall performance**, with an R² score of approximately 0.9375.

2. **Decision Tree outperformed Linear Regression**, suggesting that nonlinear relationships are important in used-car price prediction.

3. **Random Forest improved considerably over a single Decision Tree**, demonstrating the benefit of ensemble learning.

4. The engineered `km_per_year` feature provides information about **annual vehicle usage**, which gives additional context beyond total kilometers driven.

5. The engineered `is_automatic` feature provides a simple numerical representation of whether a vehicle has an automatic transmission.

6. The results indicate that vehicle pricing depends on multiple interacting characteristics rather than a simple linear relationship.

---

## 🔮 Future Improvements

Although the Random Forest model achieved strong performance, several improvements could be explored.

### 1. Hyperparameter Tuning

Random Forest parameters could be optimized using:

- `GridSearchCV`
- `RandomizedSearchCV`

Parameters such as `n_estimators`, `max_depth`, `min_samples_split`, `min_samples_leaf`, and `max_features` could be tuned.

### 2. Cross-Validation

K-Fold Cross-Validation could be used to evaluate model performance across multiple train-validation splits and provide a more reliable estimate of generalization performance.

### 3. Additional Regression Algorithms

Other regression algorithms could be compared, such as:

- Gradient Boosting Regressor
- XGBoost
- LightGBM
- CatBoost

### 4. Additional Feature Engineering

Future experiments could investigate additional features derived from vehicle specifications and usage characteristics.

### 5. Outlier Analysis

Extreme selling prices and unusual vehicle characteristics could be investigated to determine their effect on prediction errors.

---

## 🛠️ Tech Stack

### Libraries

- Python
- Pandas
- NumPy
- Scikit-learn
- Google Colab

### Machine Learning Techniques

- Data preprocessing
- Feature engineering
- Categorical encoding
- Feature scaling
- Train-test splitting
- Linear Regression
- Decision Tree Regression
- Random Forest Regression
- Regression model evaluation

---

## 📂 Project Structure

```text
Day05/
├── car_price_prediction.ipynb
└── README.md
```

The notebook contains the complete workflow from data preparation through model evaluation and final model selection.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/milansijo/Epochs-Data-Science-Bootcamp.git
```

Navigate to the project:

```bash
cd Epochs-Data-Science-Bootcamp/Day05
```

Install the required libraries:

```bash
pip install pandas numpy scikit-learn
```

---

## ▶️ Run Locally

1. Open `car_price_prediction.ipynb` in Google Colab or Jupyter Notebook.

2. Run the notebook cells in order to reproduce the preprocessing, feature engineering, model training, and evaluation.

---

## 🎯 Learning Outcomes

This project demonstrates:

- Supervised Machine Learning (Regression)
- Data Preprocessing and Feature Engineering
- Model Training and Evaluation
- Model Comparison and Selection
- Regression Metrics Analysis

---

## 👨‍💻 Author

**Milan Sijo**

**MUID:** milansijo@mulearn

---

## 📄 License

This project was developed as part of the **Epochs Data Science Bootcamp – Day 05 Assignment** for educational purposes.