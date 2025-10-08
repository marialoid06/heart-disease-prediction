import streamlit as st
import pickle
import numpy as np
import pandas as pd # <-- ADD THIS LINE

# Load the trained model
try:
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Model file not found. Please run model.py to train and save the model.")
    st.stop()

# Page configuration
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="centered"
)

# Custom CSS for styling the predict button
st.markdown("""
<style>
    div.stButton > button {
        background-color: #28a745;
        color: white;
        font-size: 18px;
        padding: 10px 24px;
        border-radius: 8px;
        border: none;
        width: 100%;
    }
    div.stButton > button:hover {
        background-color: #218838;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# App title
st.title('❤️ Heart Disease Risk Predictor')
st.write("This app predicts the risk of a patient having heart disease based on their medical data. Please enter the patient's details below.")

st.markdown("---")

# Function to get user input
def user_input_features():
    st.subheader("Patient's Medical Information")
    
    # Using two columns for a cleaner layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("#### Basic Information & Vitals")
        age = st.number_input('Age', min_value=1, max_value=120, value=50, step=1)
        st.caption("Patient's age in years.")

        sex = st.selectbox('Sex', (0, 1), format_func=lambda x: 'Female' if x == 0 else 'Male')
        st.caption("Patient's gender (0: Female, 1: Male).")
        
        cp_options = {0: 'Typical Angina', 1: 'Atypical Angina', 2: 'Non-anginal Pain', 3: 'Asymptomatic'}
        cp = st.selectbox('Chest Pain Type (cp)', options=list(cp_options.keys()), format_func=lambda x: cp_options[x])
        st.caption("Describes the type of chest pain experienced.")

        trestbps = st.number_input('Resting Blood Pressure (trestbps)', min_value=80, max_value=220, value=120)
        st.caption("Blood pressure in mm Hg upon admission to the hospital.")

        chol = st.number_input('Serum Cholesterol (chol)', min_value=100, max_value=600, value=200)
        st.caption("Cholesterol level in mg/dl.")
        
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl (fbs)', (0, 1), format_func=lambda x: 'False' if x == 0 else 'True')
        st.caption("Indicates if fasting blood sugar is higher than 120 mg/dl.")

    with col2:
        st.write("#### Advanced Test Results")
        restecg_options = {0: 'Normal', 1: 'ST-T wave abnormality', 2: 'Probable or definite left ventricular hypertrophy'}
        restecg = st.selectbox('Resting ECG Results (restecg)', options=list(restecg_options.keys()), format_func=lambda x: restecg_options[x])
        st.caption("Results of the resting electrocardiogram.")
        
        thalach = st.number_input('Maximum Heart Rate Achieved (thalach)', min_value=60, max_value=220, value=150)
        st.caption("The highest heart rate achieved during a stress test.")

        exang = st.selectbox('Exercise Induced Angina (exang)', (0, 1), format_func=lambda x: 'No' if x == 0 else 'Yes')
        st.caption("Whether the patient experienced angina (chest pain) during exercise.")
        
        oldpeak = st.number_input('ST Depression (oldpeak)', min_value=0.0, max_value=7.0, value=1.0, step=0.1)
        st.caption("ST depression induced by exercise relative to rest.")

        slope_options = {0: 'Upsloping', 1: 'Flat', 2: 'Downsloping'}
        slope = st.selectbox('Slope of Peak Exercise ST Segment (slope)', options=list(slope_options.keys()), format_func=lambda x: slope_options[x])
        st.caption("The slope of the ST segment during peak exercise.")
        
        ca = st.selectbox('Major Vessels Colored by Flourosopy (ca)', (0, 1, 2, 3, 4))
        st.caption("Number of major vessels (0-4) visualized by fluoroscopy.")
        
        thal_options = {0: 'Normal', 1: 'Fixed Defect', 2: 'Reversible Defect', 3: 'Unknown'}
        thal = st.selectbox('Thalassemia (thal)', options=list(thal_options.keys()), format_func=lambda x: thal_options[x])
        st.caption("A blood disorder called thalassemia.")

    data = {
        'age': age, 'sex': sex, 'cp': cp, 'trestbps': trestbps, 'chol': chol,
        'fbs': fbs, 'restecg': restecg, 'thalach': thalach, 'exang': exang,
        'oldpeak': oldpeak, 'slope': slope, 'ca': ca, 'thal': thal
    }
    features = pd.DataFrame(data, index=[0])
    return features

# Get user input
input_features = user_input_features()

st.markdown("---")

# Prediction button and logic
if st.button('Predict Heart Disease Risk'):
    prediction_proba = model.predict_proba(input_features)
    risk_percentage = prediction_proba[0][1] * 100

    st.subheader('Prediction Result')
    
    # Displaying the risk percentage with a progress bar
    st.progress(int(risk_percentage))
    st.metric(label="Chance of Having Heart Disease", value=f"{risk_percentage:.2f}%")

    # Providing a doctor-like interpretation
    if risk_percentage < 25:
        st.success("The model indicates a Low Risk of heart disease. It's still important to maintain a healthy lifestyle.")
    elif risk_percentage < 50:
        st.info("The model indicates a Moderate Risk of heart disease. Consider consulting a doctor for advice on lifestyle changes.")
    elif risk_percentage < 75:
        st.warning("The model indicates a High Risk of heart disease. It is strongly recommended to consult a doctor.")
    else:
        st.error("The model indicates a Very High Risk of heart disease. Please consult a doctor immediately for a full evaluation.")

