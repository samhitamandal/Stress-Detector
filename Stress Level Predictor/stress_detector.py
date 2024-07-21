# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.3
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
from sklearn.model_selection import train_test_split
## ================================ ##

import warnings
warnings.filterwarnings("ignore")
# -
st.write("""
# Stress Level Predictor

This app predicts your stress level as Low Medium or High!!
""")
st.write('---')
df = pd.read_csv("stress_dataset.csv")


dict1= {"Normal Weight": 0,
        'Overweight': 1,
        'Normal': 0,
        'Obese': 2
}
df['BMI Category']=df['BMI Category'].map(dict1)
df=df.drop(columns=['Person ID'], axis=1)
str = df.loc[:, 'Stress Level']

str[ str<4 ] = 0
str[ (3<str) & (str<=6) ] = 1
str[ (6<str) & (str<=10) ] = 2


df=pd.get_dummies(df, columns=["Occupation"],dtype=int)
dict={"Male":1,
         "Female":0
       }
df['Gender']=df['Gender'].map(dict)
df=pd.get_dummies(df, columns=["Sleep Disorder"],dtype=int)
df[['Systolic Pressure', 'Diastolic Pressure']] = df['Blood Pressure'].str.split('/', expand = True)
df=df.drop(columns=['Blood Pressure'],axis=1)
df['Stress Level'].unique()
df=df.drop(columns=['Sleep Disorder_Insomnia','Sleep Disorder_Sleep Apnea','Occupation_Salesperson'],axis=1)
X = df.drop(columns=['Stress Level'],axis=1)
y = df['Stress Level']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.40, random_state=42)

X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)


from xgboost import XGBClassifier

xg_clf = XGBClassifier( n_estimators=100, max_depth=5, learning_rate= 0.01)
xg_clf.fit(X_train_scaled, y_train)
print(xg_clf)


st.write('Please specify the following information to get started with your prediction!')

def user_input_features():
        gender=st.slider('Gender(Put in 1 if you are male and 0 if you are female!)',0,1)
        age=st.slider('Age',1,100)
        sleepd=st.slider('Sleep Duration',0,12)
        sleepq=st.slider('Quality of sleep',0,10)
        pactivity=st.slider('Physical Activity Level',0,100)
        bmi=st.slider('BMI Category(Normal=0,Overweight=1,Obese=2)',0,2)
        heart=st.slider('Heart Rate',40,150)
        step=st.slider('Daily Steps',500,20000)
        st.write('Pressure is usually in the form of A/B.Example: 120/80 Here 120 is Systolic and 80 is Diastolic!')
        syspr=st.slider('Systolic Pressure',80,200)
        diasp=st.slider('Diastolic Pressure',40,120)
        st.write('Please select your occupation')
        oacc=bool(st.button('Accountant'))
        od=st.button('Doctor')
        oen=st.button('Engineer')
        om=st.button('Manager')
        on=st.button('Nurse')
        osr=st.button('Sales Representative')
        osct=st.button('Scientist')
        osfe=st.button('Software Engineer')
        ot=st.button('Teacher')
        ol=st.button('Lawyer')
        data = {'Gender':  gender ,
             'Age': age,
             'Sleep Duration': sleepd,
             'Quality of Sleep': sleepq,
             'Physical Activity Level': pactivity,
             'BMI Category': bmi,
             'Heart Rate':heart ,
             'Daily Steps': step,
             'Occupation_Accountant': oacc,
             'Occupation_Doctor': od,
             'Occupation_Engineer': oen,
             'Occupation_Lawyer' : ol,
             'Occupation_Manager': om,
             'Occupation_Nurse': on,
            
             'Occupation_Sales Representative': osr,
             'Occupation_Scientist': osct,
             'Occupation_Software Engineer': osfe,
             'Occupation_Teacher': ot,
           
             'Systolic Pressure': syspr,
             'Diastolic Pressure': diasp
        }
        features = pd.DataFrame(data, index=[0])
        return features

user = user_input_features()

user_scaled=scaler.transform(user)
col1, col2, col3 , col4, col5 = st.columns(5)

with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3 :
    predict=st.button('**PREDICT**')

if predict:
   value=xg_clf.predict(user_scaled)
   if value==0:
         st.write('# You have LOW stress levels!')
   elif value==1:
         st.write('#  You have MEDIUM stress levels!')
   else:
         st.write('# You have HIGH stress levels!')
