# Customer Segmentation using K-Means Clustering and PCA

**Participant Name:** Milan Sijo  
**MUID:** milansijo@mulearn

## Business Objective

The objective of this project is to segment mall customers into meaningful groups based on their demographic and spending characteristics.

Using unsupervised machine learning, customers with similar behavior are grouped together so that businesses can better understand their customer base and develop targeted marketing strategies.

---

## Dataset Overview

**Dataset:** Mall Customer Segmentation Dataset  
**Source:** Kaggle

The dataset contains information about mall customers including:

- Customer ID
- Gender
- Age
- Annual Income
- Spending Score

The dataset was analyzed and prepared before applying clustering techniques.

---

## Features Used

The following features were used for customer segmentation:

- `Gender`
- `Age`
- `Annual Income (k$)`
- `Spending Score (1-100)`

`CustomerID` was removed because it is only a unique identifier and does not provide useful information for customer segmentation.

---

## Preprocessing Pipeline

The following preprocessing steps were performed:

### 1. Missing Value Check

The dataset was checked for missing values before clustering.

### 2. Customer ID Removal

`CustomerID` was removed because it is an identifier and should not influence customer clustering.

### 3. Categorical Encoding

The `Gender` column was converted into numerical form:

- Male = 0
- Female = 1

### 4. Feature Scaling

`StandardScaler` was used to standardize the features before applying K-Means.

Scaling was necessary because K-Means uses distance to group customers, and the features have different numerical ranges.

---

## Elbow Method

The Elbow Method was used to determine an appropriate number of clusters.

K-Means was tested for different values of `k`, and inertia was plotted against the number of clusters.

Based on the elbow curve, **4 clusters** were selected for customer segmentation.

---

## K-Means Clustering

K-Means clustering was applied to the scaled dataset using:

```text
Number of Clusters = 4
```

Each customer was assigned to one of four clusters based on similarities in their features.

---

## Cluster Profiling

The four customer segments obtained were:

| Cluster | Avg. Age | Avg. Income (k$) | Avg. Spending Score | Customers | Gender |
|---|---:|---:|---:|---:|---|
| 0 | 47.80 | 58.07 | 34.88 | 56 | Female |
| 1 | 28.00 | 62.24 | 64.83 | 46 | Male |
| 2 | 28.39 | 60.43 | 68.18 | 56 | Female |
| 3 | 52.74 | 62.21 | 30.64 | 42 | Male |

---

## Customer Segment Interpretation

### Cluster 0 – Mature Female Low Spenders

- Average Age: 47.80
- Average Income: 58.07k
- Spending Score: 34.88
- Customers: 56
- Gender: Female

This cluster represents mature female customers with moderate income but relatively low spending.

### Cluster 1 – Young Male Active Spenders

- Average Age: 28.00
- Average Income: 62.24k
- Spending Score: 64.83
- Customers: 46
- Gender: Male

This cluster represents young male customers with moderate-to-high income and relatively high spending activity.

### Cluster 2 – Young Female High Spenders

- Average Age: 28.39
- Average Income: 60.43k
- Spending Score: 68.18
- Customers: 56
- Gender: Female

This cluster represents young female customers with relatively high spending behavior. It has the highest average spending score among the four clusters.

### Cluster 3 – Mature Male Low Spenders

- Average Age: 52.74
- Average Income: 62.21k
- Spending Score: 30.64
- Customers: 42
- Gender: Male

This cluster represents mature male customers with moderate-to-high income but comparatively low spending.

---

## PCA Analysis

Principal Component Analysis (PCA) was used to reduce the scaled feature space into two dimensions for visualization.

The explained variance obtained was:

| Principal Component | Explained Variance |
|---|---:|
| PC1 | 33.69% |
| PC2 | 26.23% |
| **Total** | **59.92%** |

The first two principal components retain approximately **59.92% of the total variance** in the scaled dataset.

The PCA visualization showed four distinguishable customer groups, although some overlap exists between clusters.

PCA was used only for dimensionality reduction and visualization. The K-Means clusters were generated using the original scaled feature set.

---

## Key Observations

1. Four customer segments were identified using K-Means clustering.

2. Younger customers in Clusters 1 and 2 have higher average spending scores.

3. Older customers in Clusters 0 and 3 have lower average spending scores.

4. Cluster 2 has the highest average spending score of **68.18**.

5. Cluster 3 has the lowest average spending score of **30.64**.

6. Annual income is relatively similar across the four clusters, while age, spending behavior, and gender provide stronger separation.

7. PCA retained approximately **59.92%** of the total variance using two principal components.

---

## Business Recommendations

### Cluster 0 – Mature Female Low Spenders

Use personalized promotions, loyalty rewards, and value-oriented offers to encourage greater engagement and spending.

### Cluster 1 – Young Male Active Spenders

Target this segment with new products, premium offers, personalized recommendations, and loyalty programs.

### Cluster 2 – Young Female High Spenders

Focus on premium products, exclusive launches, personalized recommendations, and loyalty rewards to maintain their high engagement.

### Cluster 3 – Mature Male Low Spenders

Use value-focused promotions, targeted discounts, and relevant product recommendations to increase engagement.

---

## Future Improvements

The customer segmentation analysis can be improved by:

- Testing different numbers of clusters
- Using Silhouette Score to evaluate clustering quality
- Comparing K-Means with other clustering algorithms
- Applying hierarchical clustering
- Testing clustering without Gender to study behavioral segments separately
- Using additional customer behavioral features
- Exploring additional PCA components to preserve more variance

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
- Feature Scaling
- Elbow Method
- K-Means Clustering
- Cluster Profiling
- Principal Component Analysis (PCA)
- Customer Segmentation

---

## Repository Structure

```text
Day7/
│
├── customer_segmentation.ipynb
└── README.md
```

The notebook contains the complete workflow:

```text
Dataset Loading
      ↓
Data Exploration
      ↓
Data Preprocessing
      ↓
Feature Scaling
      ↓
Elbow Method
      ↓
K-Means Clustering
      ↓
Cluster Profiling
      ↓
PCA
      ↓
Cluster Visualization
      ↓
Business Interpretation
```

---

## Conclusion

K-Means clustering successfully divided the mall customers into **four distinct segments** based on customer characteristics.

The analysis showed that younger customers generally had higher spending scores, while older customers had lower spending scores. The clustering also produced gender-separated segments because Gender was included as a clustering feature.

PCA reduced the feature space to two components that retained **59.92% of the total variance**, allowing the four customer segments to be visualized in two dimensions.

These customer segments can help businesses create more targeted marketing and engagement strategies.

---

## Assignment Details

**Epochs '26 – Assignment 7**  
**Topic:** Unsupervised Learning – Customer Segmentation

**Participant Name:** Milan Sijo  
**MUID:** milansijo@mulearn