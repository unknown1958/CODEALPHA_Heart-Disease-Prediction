import streamlit as st
from src.predict import predict_heart_disease

st.set_page_config(
    page_title="Heart Disease Prediction",
    layout="wide"
)

st.markdown("""
<style>

.main{
    background:#f5f7fb;
}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    max-width:1200px;
}

.hero{
    background:white;
    border-radius:20px;
    padding:40px;
    box-shadow:0 6px 20px rgba(0,0,0,.08);
    margin-bottom:25px;
}

.hero h1{
    color:#1e3a8a;
    font-size:48px;
    margin-bottom:10px;
}

.hero p{
    color:#666;
    font-size:20px;
}

.section{
    background:white;
    padding:30px;
    border-radius:18px;
    box-shadow:0 5px 18px rgba(0,0,0,.08);
}

.result{
    background:white;
    padding:25px;
    border-radius:15px;
    margin-top:25px;
    box-shadow:0 5px 18px rgba(0,0,0,.08);
}

.info-card{
    background:white;
    border-radius:15px;
    padding:25px;
    text-align:center;
    box-shadow:0 5px 18px rgba(0,0,0,.08);
}

.stButton>button{
    width:100%;
    background:linear-gradient(90deg,#2563eb,#4f46e5);
    color:white;
    border:none;
    border-radius:12px;
    height:55px;
    font-size:20px;
    font-weight:bold;
}

.stButton>button:hover{
    background:linear-gradient(90deg,#1d4ed8,#4338ca);
    color:white;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='hero'>
<h1>Heart Disease Prediction</h1>
<p>Estimate the likelihood of heart disease using machine learning models.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='section'>", unsafe_allow_html=True)

st.subheader("Patient Details")

model = st.selectbox(
    "Prediction Model",
    [
        "Logistic Regression",
        "Support Vector Machine",
        "Random Forest",
        "XGBoost"
    ]
)

left, right = st.columns(2)

with left:

    age = st.number_input("Age",1,120,45)

    gender = st.selectbox(
        "Gender",
        ["Male","Female"]
    )

    chest = st.selectbox(
        "Chest Pain Type",
        [
            "Typical Angina",
            "Atypical Angina",
            "Non-anginal Pain",
            "Asymptomatic"
        ]
    )

    bp = st.number_input(
        "Resting Blood Pressure",
        80,
        250,
        120
    )

    chol = st.number_input(
        "Cholesterol",
        100,
        600,
        200
    )

    sugar = st.selectbox(
        "Fasting Blood Sugar",
        [
            "Normal",
            "High"
        ]
    )

with right:

    ecg = st.selectbox(
        "Resting ECG",
        [
            "Normal",
            "ST-T Wave Abnormality",
            "Left Ventricular Hypertrophy"
        ]
    )

    hr = st.number_input(
        "Maximum Heart Rate",
        60,
        250,
        150
    )

    angina = st.selectbox(
        "Exercise Induced Angina",
        [
            "No",
            "Yes"
        ]
    )

    oldpeak = st.number_input(
        "ST Depression",
        0.0,
        10.0,
        1.0
    )

    slope = st.selectbox(
        "ST Segment Slope",
        [
            "Upsloping",
            "Flat",
            "Downsloping"
        ]
    )

    vessels = st.selectbox(
        "Major Vessels",
        [0,1,2,3]
    )

    thal = st.selectbox(
        "Thalassemia",
        [
            "Normal",
            "Fixed Defect",
            "Reversible Defect"
        ]
    )

predict = st.button("Predict Risk")

st.markdown("</div>", unsafe_allow_html=True)

if predict:

    gender = 1 if gender=="Male" else 0

    chest = {
        "Typical Angina":0,
        "Atypical Angina":1,
        "Non-anginal Pain":2,
        "Asymptomatic":3
    }[chest]

    sugar = {
        "Normal":0,
        "High":1
    }[sugar]

    ecg = {
        "Normal":0,
        "ST-T Wave Abnormality":1,
        "Left Ventricular Hypertrophy":2
    }[ecg]

    angina = {
        "No":0,
        "Yes":1
    }[angina]

    slope = {
        "Upsloping":0,
        "Flat":1,
        "Downsloping":2
    }[slope]

    thal = {
        "Normal":3,
        "Fixed Defect":6,
        "Reversible Defect":7
    }[thal]

    values = [
        age,
        gender,
        chest,
        bp,
        chol,
        sugar,
        ecg,
        hr,
        angina,
        oldpeak,
        slope,
        vessels,
        thal
    ]

    prediction, probability = predict_heart_disease(
        values,
        model
    )

    st.markdown("<div class='result'>", unsafe_allow_html=True)

    st.subheader("Prediction Result")

    st.write("Selected Model:", model)

    if prediction == 1:
        st.error("High Risk of Heart Disease")
    else:
        st.success("Low Risk of Heart Disease")

    if probability is not None:
        st.progress(float(probability))
        st.metric(
            "Confidence",
            f"{probability*100:.2f}%"
        )

    st.markdown("</div>", unsafe_allow_html=True)

