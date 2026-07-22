# 📊 Northwind Database SQL Analysis & Business Insights

## 📖 Overview

This project is submitted as part of the **Epochs: Data Science Bootcamp '26 - Day 02 Assignment**. The objective is to analyze the Northwind database using SQL to answer real-world business questions and perform exploratory data analysis using Pandas.

The Northwind database is a sample business database containing information about customers, orders, products, suppliers, employees, and shipping details. It provides a realistic environment for practicing SQL queries and business analytics.

---

## 📂 Dataset

**Dataset:** Northwind SQLite Database

**Source:** https://github.com/jpwhite3/northwind-SQLite3

---

## 🎯 Business Questions

The following business questions were addressed using SQL:

* What are the top 10 best-selling products?
* Who are the top 10 customers based on total revenue?
* How have sales changed over time (monthly sales trends)?
* Which product categories generate the highest sales?
* How frequently do customers make purchases?

---

## 🛠 SQL Analysis

The required SQL queries were written to answer each business question and stored in the **queries.sql** file.

The query results were then imported into Pandas for further analysis and visualization.

---

## 📊 Data Analysis

Using Pandas, the SQL query outputs were analyzed to identify trends and business insights through exploratory data analysis.

The notebook includes:

* Loading SQL query results
* Data inspection
* Summary statistics
* Trend analysis
* Business insights

---

## 💡 Key Business Insights

1. The top-selling products contribute a significant share of total sales.
2. A small group of customers generates a large portion of overall revenue.
3. Monthly sales exhibit seasonal fluctuations, with certain months consistently outperforming others.
4. Some product categories contribute substantially more revenue than others.
5. Customer purchasing behavior varies, with a mix of frequent repeat customers and one-time buyers.

---

## 🛠 Technologies Used

* SQL (SQLite)
* Python 3
* Pandas
* SQLite3
* Jupyter Notebook

---

## 📁 Repository Structure

```text
├── queries.sql
├── analysis.ipynb
├── README.md
└── northwind.db
```

---

## 🚀 How to Run

1. Clone this repository.

```bash
git clone <repository-url>
cd <repository-name>
```

2. Install the required libraries.

```bash
pip install pandas jupyter
```

3. Download the Northwind SQLite database from the provided GitHub repository and place **northwind.db** in the project directory.

4. Open **analysis.ipynb** and execute all cells to run the SQL queries, import the results into Pandas, and perform the analysis.

---

## 📸 SQL Output Screenshots

Screenshots of the SQL query outputs are included in this repository to demonstrate the results obtained for each business question.

---

## 📌 Assignment

**Epochs: Data Science Bootcamp '26' – Day 02**
