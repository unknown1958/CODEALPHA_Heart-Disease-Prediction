import joblib
import numpy as np

# Load scaler
scaler = joblib.load("models/scaler.pkl")

# Load models
models = {
    "Logistic Regression": joblib.load("models/logistic_regression.pkl"),
    "Support Vector Machine": joblib.load("models/support_vector_machine.pkl"),
    "Random Forest": joblib.load("models/random_forest.pkl"),
    "XGBoost": joblib.load("models/xgboost.pkl")
}

def predict_heart_disease(input_data, model_name):

    data = np.array(input_data).reshape(1, -1)

    # Scale only for LR and SVM
    if model_name in ["Logistic Regression", "Support Vector Machine"]:
        data = scaler.transform(data)

    prediction = models[model_name].predict(data)[0]

    probability = None

    if hasattr(models[model_name], "predict_proba"):
        probability = models[model_name].predict_proba(data)[0][1]

    return prediction, probability
