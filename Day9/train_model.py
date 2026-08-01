import os
import joblib
import kagglehub
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression

print("========================================")
print("Customer Churn Model Training")
print("========================================")

# ---------------------------------------------------
# Create models folder
# ---------------------------------------------------
os.makedirs("models", exist_ok=True)

# ---------------------------------------------------
# Download dataset
# ---------------------------------------------------
path = kagglehub.dataset_download(
    "muhammadshahidazeem/customer-churn-dataset"
)

print("\nDataset Path:")
print(path)

print("\nFiles:")
print(os.listdir(path))

# ---------------------------------------------------
# Load training data
# ---------------------------------------------------
train = pd.read_csv(
    os.path.join(
        path,
        "customer_churn_dataset-training-master.csv"
    )
)

print("\nDataset Loaded Successfully")
print(train.head())

# ---------------------------------------------------
# Remove rows with missing target
# ---------------------------------------------------
train = train.dropna(subset=["Churn"])

train["Churn"] = train["Churn"].astype(int)

# ---------------------------------------------------
# Remove CustomerID
# ---------------------------------------------------
train = train.drop(columns=["CustomerID"])

# ---------------------------------------------------
# Split Features & Target
# ---------------------------------------------------
X = train.drop(columns=["Churn"])
y = train["Churn"]

print("\nTarget Distribution")
print(y.value_counts())

# ---------------------------------------------------
# Feature Lists
# ---------------------------------------------------
categorical_features = [
    "Gender",
    "Subscription Type",
    "Contract Length"
]

numerical_features = [
    "Age",
    "Tenure",
    "Usage Frequency",
    "Support Calls",
    "Payment Delay",
    "Total Spend",
    "Last Interaction"
]

print("\nCategorical Features")
print(categorical_features)

print("\nNumerical Features")
print(numerical_features)

# ---------------------------------------------------
# Numerical Pipeline
# ---------------------------------------------------
numeric_transformer = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(strategy="median")
        ),
        (
            "scaler",
            StandardScaler()
        )
    ]
)

# ---------------------------------------------------
# Categorical Pipeline
# ---------------------------------------------------
categorical_transformer = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(strategy="most_frequent")
        ),
        (
            "encoder",
            OneHotEncoder(handle_unknown="ignore")
        )
    ]
)

# ---------------------------------------------------
# Preprocessor
# ---------------------------------------------------
preprocessor = ColumnTransformer(
    transformers=[
        (
            "num",
            numeric_transformer,
            numerical_features
        ),
        (
            "cat",
            categorical_transformer,
            categorical_features
        )
    ]
)

# ---------------------------------------------------
# Logistic Regression Model
# ---------------------------------------------------
model = LogisticRegression(
    max_iter=1000,
    random_state=42
)

# ---------------------------------------------------
# Complete Pipeline
# ---------------------------------------------------
pipeline = Pipeline(
    steps=[
        (
            "preprocessor",
            preprocessor
        ),
        (
            "classifier",
            model
        )
    ]
)

# ---------------------------------------------------
# Train
# ---------------------------------------------------
print("\nTraining Model...")

pipeline.fit(X, y)

print("Training Completed!")

# ---------------------------------------------------
# Save Model
# ---------------------------------------------------
joblib.dump(
    pipeline,
    "models/model.pkl"
)

print("\n========================================")
print("MODEL SAVED SUCCESSFULLY")
print("========================================")

print("\nSaved File")

print("models/model.pkl")

print("\nProject Structure")
