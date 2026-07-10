import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

os.makedirs("models", exist_ok=True)
df = pd.read_csv("Data/processed/heart_disease_cleaned.csv")

print("Dataset Loaded Successfully!")
print("Dataset Shape:", df.shape)

X = df.drop("Heart_Disease", axis=1)
y = df["Heart_Disease"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTrain-Test Split Completed")
print("Training Samples :", X_train.shape)
print("Testing Samples  :", X_test.shape)


# Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
joblib.dump(scaler, "models/scaler.pkl")
print("Scaler Saved Successfully!")


# Logistic Regression
lr_model = LogisticRegression(max_iter=1000)
lr_model.fit(X_train_scaled, y_train)
joblib.dump(
    lr_model,
    "models/logistic_regression.pkl"
)
print("Logistic Regression Model Saved!")


# Support Vector Machine
svm_model = SVC(probability=True)
svm_model.fit(X_train_scaled, y_train)
joblib.dump(
    svm_model,
    "models/support_vector_machine.pkl"
)
print("Support Vector Machine Model Saved!")


# Random Forest
rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
rf_model.fit(X_train, y_train)
joblib.dump(
    rf_model,
    "models/random_forest.pkl"
)
print("Random Forest Model Saved!")

# XGBoost
xgb_model = XGBClassifier(
    eval_metric="logloss",
    random_state=42
)
xgb_model.fit(X_train, y_train)
joblib.dump(
    xgb_model,
    "models/xgboost.pkl"
)
print("XGBoost Model Saved!")

# Training Completed
print("\n")
print("All Models Trained Successfully!")
print("Models saved inside the 'models' folder.")
