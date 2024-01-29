# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 12:59:53 2024

@author: Sahil Chand
"""

import pickle
import streamlit as st

# loading the saved models
diabetes_model = pickle.load(open('trained_model.sav', 'rb'))
heart_disease_model = pickle.load(open('trained_model_for_heart.sav', 'rb'))

# Sidebar
selected = st.sidebar.radio(
    'Multiple Disease Prediction System (Warning: these predictions are not 100% accurate)',
    ['Diabetes Predictor', 'Heart Disease Predictor']
)

# Diabetes Prediction Page
if selected == 'Diabetes Predictor':
    st.title('Diabetes Prediction using Machine Learning')

    Pregnancies = st.text_input('How many times have you been pregnant')
    Glucose = st.text_input('Glucose Level')
    BloodPressure= st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('How old are you?')

    diab_diagnosis = ''

    # creating a button for Prediction
    if st.button('Diabetes Test Result'):
        # Check if all inputs are non-empty
        if all([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]):
            user_input = [float(x) for x in [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
            diab_prediction = diabetes_model.predict([user_input])

            if diab_prediction[0] == 0:
                diab_diagnosis = 'Non-Diabetic'
            else:
                diab_diagnosis = 'Diabetic'
        else:
            st.warning("Please enter values for all input fields.")

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
elif selected == 'Heart Disease Predictor':
    st.title('Heart Disease Prediction using Machine Learning')

    # Input fields...
    age = st.text_input('How old are you?')

    sex = st.text_input('What sex are you?')

    cp = st.text_input('Chest Pain types(0-3 scale)')

    trestbps = st.text_input('Resting Blood Pressure')

    chol = st.text_input('Serum Cholestoral in mg/dl')

    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    restecg = st.text_input('Resting Electrocardiographic results')

    thalach = st.text_input('Maximum Heart Rate')

    exang = st.text_input('Exercise Induced Angina')

    oldpeak = st.text_input('ST depression induced by exercise')

    slope = st.text_input('Slope of the peak exercise ST segment')

    ca = st.text_input('Major vessels colored by flourosopy')

    thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')


    heart_diagnosis = ''

    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        # Check if all inputs are non-empty
        if all([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]):
            user_input = [float(x) for x in [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
            heart_prediction = heart_disease_model.predict([user_input])

            if heart_prediction[0] == 0:
                heart_diagnosis = 'No heart disease'
            else:
                heart_diagnosis = 'Heart Disease'
        else:
            st.warning("Please enter values for all input fields.")

    st.success(heart_diagnosis)
