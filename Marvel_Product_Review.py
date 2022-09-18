import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

if st.checkbox("Click here to see the report"):
    df=pd.read_csv("D:/Karthikraj_data/OneDrive - Course5 Intelligence Pvt Ltd/Desktop/DRP_data/mcu_box_office.csv")
    phase1=df[df.mcu_phase==1]
    phase2=df[df.mcu_phase==2]
    phase3=df[df.mcu_phase==3]

st.title("Raw data report")
st.title("Highest box office product of marvel")    

highest=df.iloc[:,[0,6,9]] 

high=highest.sort_values(by=["worldwide_box_office"],ascending=False)
high
st.title("Highest opening product of marvel")
opend=df.iloc[:,[0,7,9]] 

opens=opend.sort_values(by=["opening_weekend"],ascending=False)
opens

st.title("best review product of marvel")
pro=df.iloc[:,[0,4,9]] 

product=pro.sort_values(by=["audience_score"],ascending=False)
product