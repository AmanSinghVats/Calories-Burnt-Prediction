import streamlit as st
import pickle 
import pandas as pd

Gender = ['Male', 'Female']



pipe = pickle.load(open('pipe.pkl','rb'))
st.title("Calroie Burnt Prediction")

col1, col2 = st.columns(2)

with col1:
    Gender = st.selectbox("Select Your Gender", sorted(Gender))

with col2:
    Age = st.number_input("Age",step=1, format="%d")


col3, col4 = st.columns(2)

with col3:
    Height = st.number_input("Heigth in cm",step=1)

with col4:
    Weight = st.number_input("Weigth in kg", step=1)

Duration = st.number_input("Duuration in mins", min_value=1, step=1, format="%d")

col5, col6 = st.columns(2)

with col5:
    Heart_Rate = st.number_input("Heart_Rate",step=1)

with col6:
    Body_Temp = st.number_input("Body_Temp after Workout in C", step=1)

if st.button("Predict Probability"):

    input_df = pd.DataFrame({'Gender':[Gender],
                  'Age':[Age],
                  'Height':[Height],
                  'Weight':[Weight],
                  'Duration':[Duration],
                  'Heart_Rate':[Heart_Rate],
                  'Body_Temp':[Body_Temp]})
    
    result = pipe.predict_proba(input_df)
    st.header("Calories burnt by you - " + str(result))
    