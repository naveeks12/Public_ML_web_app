# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 11:53:21 2024

@author: navee
"""



import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import os




#heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))

script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, 'heart_disease_model.sav')

heart_disease_model = pickle.load(open(model_path, 'rb'))


script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, 'diabetes_model.sav')

diabetes_model = pickle.load(open(model_path, 'rb'))

#diabetes_model = pickle.load(open('diabetes_model.sav','rb'))

with st.sidebar:
    selected = option_menu('Precision Cardiovascular Health Prediction using ML Algorithms',
                           ['Heart Disease Prediction',
                            'Diabetes Perdiction'],
                           icons = ['heart','activity'],
                           default_index=0)


#side bar for navigate
if(selected == 'Heart Disease Prediction'):
    st.title('Heart Disease Prediction Using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        Age = st.text_input('Age of person')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        CP = st.text_input('Chest Pain Type')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestrol in mg/dl')
    with col3:
        fbs = st.text_input('Floating Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achived')
      
    with col3:
         exang = st.text_input('Excercise induced angina')  
    with col1:
        oldpeak = st.text_input('ST Deperession induced by exercise relative to rest')
    with col2:
        slope = st.text_input('Slope od the peak excercise st segment')
    with col3:
        ca= st.text_input('Number of major vessels(0-3) colored by flourospy')
    with col1:
        thal = st.text_input('Number of major vessels(0-3) colored by flourosopy')
     
     #printing the prediction model
    heart_dignosis = ''

     
     # creating a button for prediction 
    if st.button('Heart Test Result'):
         
         heart_prediction = heart_disease_model.predict([[Age,sex,CP,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
         if (heart_prediction[0]==1):
             heart_dignosis='The person is having Heart Disease'
         else:
            heart_dignosis='The Preson is not Having HEart Disease'
    st.success(heart_dignosis)
    
    
    
if(selected == 'Diabetes Perdiction'):
    st.title('Diabetes Perdiction Using ML')    
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('BloodPressure Value')
    with col1:
        SkinThickness = st.text_input('SkinThickness value')
    with col2:
        Insulin = st.text_input('Insulin Value')
    with col3:
         BMI= st.text_input('BMI Value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age = st.text_input('Age of Person')
     
     #printing the prediction model
    Diabetes_dignosis = ''
    
    if st.button('Diabetes Test Result'):
        Diabetes_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if (Diabetes_prediction[0]==1):
            Diabetes_dignosis='The person is Diabetic'
        else:
            Diabetes_dignosis='The Preson is not Diabetic'     
        st.success(Diabetes_dignosis) 
    
    
        

            
    
