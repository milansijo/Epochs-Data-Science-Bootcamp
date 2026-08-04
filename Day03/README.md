# 🚗 Used Car Price Prediction - EDA, Data Cleaning & Feature Engineering

**Name:** Milan Sijo  
**MUID:** milansijo@mulearn

---

## 📖 Project Overview

This project was completed as part of the **Epochs: Data Science Bootcamp '26 - Day 03 Assignment**.

The objective of this project is to explore and prepare a real-world used car dataset through **Exploratory Data Analysis (EDA), Data Cleaning, and Feature Engineering**. The resulting cleaned dataset can later be used to build Machine Learning models for used car price prediction.

---

## 📂 Dataset

**Dataset:** Used Car Price Prediction Dataset

**Source:** Kaggle - Used Car Price Prediction Dataset

The dataset contains information about used vehicles, including:

- Brand
- Model
- Model Year
- Mileage
- Fuel Type
- Engine
- Transmission
- Exterior Colour
- Interior Colour
- Accident History
- Clean Title
- Price

---

## 🔍 Exploratory Data Analysis

Exploratory Data Analysis was performed to understand the structure, quality, and characteristics of the dataset.

The analysis included:

- Examining the dataset shape and structure
- Identifying numerical and categorical features
- Examining data types
- Generating descriptive statistics
- Checking for missing values
- Checking for duplicate records
- Examining unique values in categorical features
- Analysing distributions
- Identifying potential outliers

---

## ⚠️ Data Quality Issues Identified

During exploration, several data quality issues were identified.

- Missing values were present in `fuel_type`, `accident`, and `clean_title`.
- Some numerical information such as `price` and `milage` was initially stored as object/string data.
- Numerical values required cleaning before they could be used for analysis and feature engineering.
- Potential outliers were identified in numerical features.
- Duplicate records were checked to avoid repeated observations.

---

## 🧹 Data Cleaning

The following techniques were applied to prepare the dataset:

- Missing categorical values were handled using appropriate imputation.
- Duplicate records were identified and removed where applicable.
- Numerical columns stored as strings were cleaned and converted to appropriate numerical data types.
- Potential outliers were analysed and handled where necessary.
- The dataset was checked again after cleaning to ensure it was ready for feature engineering.

---

## ⚙️ Feature Engineering

Five new features were created from the existing variables to provide additional information that may be useful for future Machine Learning models.

### 1. Car Age

Represents the approximate age of a vehicle based on its model year.

```text
Car Age = Current Year - Model Year
```

Car age can provide a more directly useful measure of vehicle depreciation than the model year alone.

### 2. Price per KM

Represents the vehicle's listed price relative to its total mileage.

```text
Price per KM = Price / Mileage
```

This feature provides an additional way to compare the value of vehicles with different mileage levels.

### 3. Mileage per Year

Measures the approximate average distance travelled by a vehicle per year.

```text
Mileage per Year = Mileage / Car Age
```

This helps distinguish heavily used vehicles from vehicles of a similar age that have experienced lower annual usage.

### 4. Is Automatic

A binary feature was created from the transmission information to indicate whether a vehicle has an automatic transmission.

```text
Automatic transmission → 1
Other transmission → 0
```

This simplifies transmission information into a feature that can be easily used by future Machine Learning models.

### 5. Price per Year

Represents the vehicle's price relative to its age.

```text
Price per Year = Price / Car Age
```

This provides another measure for comparing the value of vehicles across different age groups.

---

## 💡 Key Business Insights

1. **Vehicle age is an important factor when evaluating used cars.** Converting model year into `Car Age` makes it easier to analyse how vehicle value changes as cars become older.

2. **Mileage should be considered together with vehicle age.** The `Mileage per Year` feature provides more context than total mileage alone, since two vehicles with the same mileage may have reached it over very different periods.

3. **Price per KM provides a useful value comparison between vehicles.** It combines price and usage into a single measure that can help identify differences between similarly priced vehicles with different mileage.

4. **Transmission type can be represented more simply for predictive analysis.** The `Is Automatic` feature converts transmission information into a machine-learning-friendly binary variable and allows automatic and non-automatic vehicles to be compared more easily.

5. **Price per Year provides an additional perspective on vehicle value and depreciation.** Comparing price relative to vehicle age can help distinguish newer high-value vehicles from older vehicles and may provide useful information for future price prediction models.

---

## 📊 Final Dataset

After completing data cleaning and feature engineering, the processed dataset was saved as:

```text
cleaned_used_cars.csv
```

The cleaned dataset contains the original relevant attributes along with the five engineered features and is prepared for future Machine Learning model development.

---

## 🛠️ Tech Stack

### Libraries

- Python 3
- Pandas
- NumPy
- Matplotlib
- Google Colab

---

## 📂 Project Structure

```text
Day03/
├── task-3.ipynb
├── cleaned_used_cars.csv
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/milansijo/Epochs-Data-Science-Bootcamp.git
```

Navigate to the project:

```bash
cd Epochs-Data-Science-Bootcamp/Day03
```

Install the required Python libraries:

```bash
pip install pandas numpy matplotlib
```

---

## ▶️ Run Locally

1. Open `task-3.ipynb` using Google Colab or Jupyter Notebook.

2. Run all notebook cells to reproduce the EDA, data cleaning, and feature engineering process.

3. The final processed dataset is exported as `cleaned_used_cars.csv`.

---

## 🎯 Learning Outcomes

This project demonstrates:

- Exploratory Data Analysis (EDA)
- Data Cleaning and Preprocessing
- Feature Engineering
- Handling Missing Values and Outliers
- Data Export for Machine Learning

---

## 👨‍💻 Author

**Milan Sijo**

**MUID:** milansijo@mulearn

---

## 📄 License

This project was developed as part of the **Epochs Data Science Bootcamp – Day 03 Assignment** for educational purposes.
