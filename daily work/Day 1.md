# Day 1 - Project Setup, Dataset Collection, Data Cleaning & Exploratory Data Analysis

## Project
**Heart Disease Prediction from Medical Data**

---

## Objective

The objective of this project is to develop a machine learning model that predicts whether a patient has heart disease using clinical and medical attributes. Day 1 focused on setting up the project, collecting the dataset, cleaning the data, and understanding it through exploratory data analysis (EDA).

---

# Project Structure

```text
Heart Disease Prediction/
│
├── daily work/
│   └── Day 1.md
│
├── Data/
│   ├── raw/
│   │   └── processed.cleveland.data
│   │
│   └── processed/
│       └── heart_disease_cleaned.csv
│
├── notebook/
│   └── EDA.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
│
├── models/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Dataset Collection

Downloaded the **Heart Disease (Cleveland)** dataset from the **UCI Machine Learning Repository**.

## Dataset Information

| Property | Value |
|----------|-------|
| Dataset Name | Heart Disease (Cleveland) |
| Problem Type | Classification |
| Original Records | 303 |
| Features | 13 |
| Target Variable | Heart Disease |

The dataset was stored in:

```text
Data/raw/
```

---

# Data Loading

The dataset was loaded into a Pandas DataFrame.

Since the original dataset did not contain column names, meaningful column names were assigned manually.

## Assigned Features

- Age
- Gender
- Chest_Pain_Type
- Resting_Blood_Pressure
- Cholesterol
- Fasting_Blood_Sugar
- Resting_ECG_Result
- Maximum_Heart_Rate
- Exercise_Induced_Angina
- Oldpeak
- ST_Segment_Slope
- Major_Vessels
- Thalassemia
- Heart_Disease

---

# Data Cleaning

The following preprocessing steps were performed:

- Replaced missing values (`?`) with `NaN`
- Converted object columns to numeric format
- Removed rows containing missing values
- Removed duplicate records
- Converted the target variable into binary classes:
  - **0** → No Heart Disease
  - **1** → Heart Disease

## Dataset After Cleaning

| Property | Value |
|----------|-------|
| Records | 297 |
| Columns | 14 |

The cleaned dataset was saved to:

```text
Data/processed/heart_disease_cleaned.csv
```

---

# Exploratory Data Analysis (EDA)

Performed exploratory data analysis to better understand the dataset.

## Analysis Performed

- Dataset information (`info()`)
- Statistical summary (`describe()`)
- Missing value analysis
- Duplicate value check
- Target variable distribution
- Histograms
- Correlation heatmap

These visualizations helped understand the distribution of the medical features and their relationships with the target variable.

---

# Files Created

- `notebook/EDA.ipynb`
- `src/preprocessing.py`
- `Data/processed/heart_disease_cleaned.csv`
- `daily work/Day 1.md`

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- Visual Studio Code

---

# Outcome

Successfully completed the first phase of the project by:

- Setting up the project structure
- Downloading the dataset
- Cleaning the dataset
- Performing exploratory data analysis
- Saving the cleaned dataset for machine learning

---

# Tasks Completed

- ✅ Project structure created
- ✅ Dataset downloaded
- ✅ Dataset loaded into Pandas
- ✅ Feature names assigned
- ✅ Missing values handled
- ✅ Duplicate records removed
- ✅ Target variable converted to binary
- ✅ Exploratory Data Analysis completed
- ✅ Cleaned dataset saved

