import streamlit as st
import pandas as pd
import joblib

# Load your saved model
model = joblib.load('heart_disease_model.pkl')

st.title("Heart Disease Prediction")

# Create input fields for user data
age = st.number_input('Age', min_value=1, max_value=120, value=50)
sex = st.selectbox('Sex', options=[0, 1], format_func=lambda x: 'Female' if x==0 else 'Male')
cp = st.selectbox('Chest Pain Type (cp)', options=[0,1,2,3])
trestbps = st.number_input('Resting Blood Pressure', min_value=80, max_value=200, value=120)
chol = st.number_input('Cholesterol', min_value=100, max_value=600, value=200)
fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl (fbs)', options=[0, 1])
restecg = st.selectbox('Resting ECG results', options=[0,1,2])
thalach = st.number_input('Max Heart Rate Achieved', min_value=60, max_value=220, value=150)
exang = st.selectbox('Exercise Induced Angina (exang)', options=[0, 1])
oldpeak = st.number_input('ST Depression (oldpeak)', min_value=0.0, max_value=10.0, value=1.0, step=0.1)
slope = st.selectbox('Slope of the Peak Exercise ST segment', options=[0, 1, 2])
ca = st.selectbox('Number of Major Vessels Colored by Fluoroscopy (ca)', options=[0, 1, 2, 3, 4])
thal = st.selectbox('Thalassemia (thal)', options=[0, 1, 2, 3])

# When user clicks the button
if st.button('Predict'):
    input_data = pd.DataFrame({
        'age': [age],
        'sex': [sex],
        'cp': [cp],
        'trestbps': [trestbps],
        'chol': [chol],
        'fbs': [fbs],
        'restecg': [restecg],
        'thalach': [thalach],
        'exang': [exang],
        'oldpeak': [oldpeak],
        'slope': [slope],
        'ca': [ca],
        'thal': [thal]
    })

    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("Warning: This patient is predicted to have heart disease.")
    else:
        st.success("Good news: This patient is predicted NOT to have heart disease.")

