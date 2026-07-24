# 🚗 Used Car Price Prediction - EDA, Data Cleaning & Feature Engineering

## 📖 Overview

This project was completed as part of the **Epochs: Data Science Bootcamp '26 - Day 03 Assignment**.

The objective of this project is to perform Exploratory Data Analysis (EDA), clean the dataset, engineer meaningful features, and prepare the data for future Machine Learning models.

---

# 📂 Dataset

**Dataset:** Used Car Price Prediction Dataset

**Source:** https://www.kaggle.com/datasets/taeefnajib/used-car-price-prediction-dataset

---

# 🔍 Exploratory Data Analysis (EDA)

The following analyses were performed:

- Explored the dataset structure and dimensions.
- Identified numerical and categorical features.
- Generated descriptive statistics.
- Checked for missing values.
- Checked for duplicate records.
- Examined unique values in categorical columns.
- Identified potential outliers using box plots.

---

# 🧹 Data Cleaning

The following preprocessing steps were applied:

- Missing values in categorical columns (`fuel_type`, `accident`, and `clean_title`) were handled using mode imputation.
- Duplicate records were identified and removed where applicable.
- Incorrect data types were corrected for numerical columns such as `price` and `milage`.
- Outliers were analyzed and handled where necessary to improve data quality.

---

# ⚙️ Feature Engineering

Three new features were created to improve the usefulness of the dataset for future Machine Learning models.

### 1. Car Age

Calculates the age of the vehicle from its manufacturing year.

```
Car Age = Current Year − Model Year
```

### 2. Price per KM

Measures the selling price relative to the distance driven.

```
Price per KM = Price / Mileage
```

### 3. Mileage per Year

Calculates the average distance driven per year.

```
Mileage per Year = Mileage / Car Age
```

---

# 💡 Business Insights

1. Older vehicles generally have lower resale prices, making **Car Age** an important indicator of vehicle value.

2. Vehicles with a lower **Price per KM** often represent better value for buyers and may indicate competitive pricing.

3. Cars with high **Mileage per Year** are likely to have experienced heavier annual usage, which may negatively impact resale value.

4. Most missing values were concentrated in a few categorical columns, while the remaining dataset was largely complete, reducing the amount of required preprocessing.

5. Feature engineering created more informative variables that capture vehicle usage patterns better than the original features alone, making them valuable for future predictive models.

---

# 🛠 Technologies Used

- Python 3
- Pandas
- NumPy
- Matplotlib
- Google Colab

---

# 📁 Repository Structure

```
├── task-3.ipynb
├── cleaned_used_cars.csv
└── README.md
```

---

# 🚀 How to Run

1. Clone the repository.

```bash
git clone <repository-url>
cd <repository-name>
```

2. Install the required libraries.

```bash
pip install pandas numpy matplotlib kagglehub
```

3. Download the dataset using KaggleHub or place the dataset in the project directory.

4. Open `task-3.ipynb` in Google Colab or Jupyter Notebook.

5. Run all cells to reproduce the EDA, data cleaning, feature engineering, and generate the cleaned dataset.

---

# 📌 Assignment

**Epochs: Data Science Bootcamp '26' – Day 03**

**Tag:**

```
#evn-ds-epochs26-day03
```