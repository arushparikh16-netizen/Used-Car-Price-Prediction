import streamlit as st
import pandas as pd
import numpy as np
import joblib

model=joblib.load("car_price_model.pkl")

st.title("Used Car Price Prediction Model")
st.subheader("Enter the car details:")

Name=st.text_input("Enter the brand of your car ")
Location=st.text_input("Enter your Location")
Year=st.selectbox("Enter the Manufacturing Year of your car",list(range(1998,2020)))
Kms=st.number_input("Enter the Kilometers Driven by car")
fuel=st.selectbox("Enter the Fuel type of your car",['Diesel','Petrol','CNG','LPG','Electric'])
trans=st.selectbox("Enter transmision type",['Automatic','Manual'])
owner=st.selectbox("Enter owner type",['First','Second','Third','Fourth & Above'])
mil=st.number_input("Enter the mileage in km/kg")
eng=st.number_input("Enter the CC of Enhgine")
pow=st.number_input("Enter the Power in bhp")
seats=st.slider("Enter the number of seats",min_value=0,max_value=10)

if st.button("Predict",use_container_width=True):
    input_df=pd.DataFrame([{
        "Name":Name,
        "Location":Location,
        "Year":int(Year),
        "Kilometers_Driven":Kms,
        "Fuel_Type":fuel,
        "Transmission":trans,
        "Owner_Type":owner,
        "Mileage":mil,
        "Engine":eng,
        "Power":pow,
        "Seats":seats
    }])

    prediction=model.predict(input_df)
    actual_price=np.expm1(prediction[0])

    st.success(f"Estimated Car Price is {actual_price:.2f} Lakhs")

    st.caption("This model is only for Educational Purpose")
