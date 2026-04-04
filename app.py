import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("Diabetes Prediction App")

st.write("Enter patient details below:")

# Inputs

pregnancies = st.number_input("Pregnancies", min_value=0)

glucose = st.number_input("Glucose Level")

blood_pressure = st.number_input("Blood Pressure")

skin_thickness = st.number_input("Skin Thickness")

insulin = st.number_input("Insulin Level")

bmi = st.number_input("BMI")

dpf = st.number_input("Diabetes Pedigree Function")

age = st.number_input("Age")

# Prediction

if st.button("Predict"):

    input_data = np.array([
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        dpf,
        age
    ]).reshape(1, -1)

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.error("Patient is Diabetic")
    else:
        st.success("Patient is Not Diabetic")