# 📊 Google Play Store Apps - Dataset Exploration & Problem Framing

**Name:** Milan Sijo  
**MUID:** milansijo@mulearn

---

## 📖 Project Overview

This project is submitted as part of the **Epochs:Data Science Bootcamp '26 - Day 01 Assignment**. The objective is to explore a real-world dataset, identify a business problem, and determine the most appropriate Machine Learning approach.

The chosen dataset is the **Google Play Store Apps Dataset**, which contains information about Android applications available on the Google Play Store, including ratings, reviews, installs, categories, prices, content ratings, and more.

---

## 📂 Dataset

**Dataset:** Google Play Store Apps

**Source:** https://www.kaggle.com/datasets/lava18/google-play-store-apps

---

## 🎯 Business Problem

Developers and businesses publishing applications on the Google Play Store want to understand the factors that contribute to an app's success.

Some important business questions include:

* What factors influence an app's rating?
* Which app categories perform the best?
* Can we predict the rating of an app before publishing it?
* Which features contribute most to user satisfaction?

Answering these questions can help developers improve app quality, increase user engagement, and make better business decisions.

---

## 🤖 Machine Learning Problem

### Problem Type

**Regression**

### Justification

The target variable is **Rating**, which is a continuous numerical value ranging approximately from 1 to 5. Since the goal is to predict a numerical value, this is a **Regression** problem.

---

## 🎯 Target Variable

* **Rating**

---

## 🔑 Key Features

Some important features that may influence the app rating include:

* Category
* Reviews
* Size
* Installs
* Type (Free/Paid)
* Price
* Content Rating
* Genres

---

## 📊 Dataset Exploration

Basic exploration was performed using **Pandas**, including:

* Dataset shape
* Data types
* Missing value analysis
* Summary statistics
* Preview of the dataset

The dataset was downloaded directly from Kaggle within the notebook using the **`kagglehub`** library, ensuring that the latest version is fetched automatically during execution.

---

## 🔍 Key Observations

1. The dataset contains missing values, especially in the **Rating** column.
2. Most applications on the Google Play Store are **free** rather than paid.
3. Categories such as **Family**, **Games**, and **Tools** contain the largest number of applications.

---

## 🛠️ Tech Stack

### Libraries

* Python 3
* Pandas
* NumPy
* KaggleHub
* Jupyter Notebook

---

## 📂 Project Structure

```text
Day01/
├── analysis.ipynb
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
cd Epochs-Data-Science-Bootcamp/Day01
```

Install the required libraries:

```bash
pip install pandas numpy kagglehub
```

---

## ▶️ Run Locally

Ensure your Kaggle API credentials are configured.

Open **analysis.ipynb** and run all cells. The notebook automatically downloads the latest version of the dataset using:

```python
import kagglehub

path = kagglehub.dataset_download("lava18/google-play-store-apps")
```

No manual dataset download or CSV placement is required.

---

## 🎯 Learning Outcomes

This project demonstrates:

- Real-World Dataset Exploration
- Business Problem Identification
- Machine Learning Problem Framing
- Exploratory Data Analysis using Pandas
- Automated Dataset Downloading using KaggleHub

---

## 👨‍💻 Author

**Milan Sijo**

**MUID:** milansijo@mulearn

---

## 📄 License

This project was developed as part of the **Epochs Data Science Bootcamp – Day 01 Assignment** for educational purposes.
