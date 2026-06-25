import pandas as pd
import numpy as np
import os

os.makedirs("Data/processed", exist_ok=True)

# Column names
columns = [
    "Age",
    "Gender",
    "Chest_Pain_Type",
    "Resting_Blood_Pressure",
    "Cholesterol",
    "Fasting_Blood_Sugar",
    "Resting_ECG_Result",
    "Maximum_Heart_Rate",
    "Exercise_Induced_Angina",
    "Oldpeak",
    "ST_Segment_Slope",
    "Major_Vessels",
    "Thalassemia",
    "Heart_Disease"
]

# Load dataset
df = pd.read_csv(
    "Data/raw/processed.cleveland.data",
    names=columns
)

# Replace missing values represented by '?'
df.replace("?", np.nan, inplace=True)

# Convert columns to numeric
df["Major_Vessels"] = pd.to_numeric(df["Major_Vessels"])
df["Thalassemia"] = pd.to_numeric(df["Thalassemia"])

# Remove missing values
df.dropna(inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Convert target into binary classification
df["Heart_Disease"] = df["Heart_Disease"].apply(
    lambda x: 0 if x == 0 else 1
)

# Save cleaned dataset
df.to_csv(
    "Data/processed/heart_disease_cleaned.csv",
    index=False
)

print("Cleaned dataset saved successfully!")
print("Dataset Shape:", df.shape)
print(f"Cleaned dataset saved at: Data/processed/heart_disease_cleaned.csv")