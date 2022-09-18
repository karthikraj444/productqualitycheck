import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
if st.checkbox("Click here to see the report"):
    df=pd.read_csv("D:/Karthikraj_data/OneDrive - Course5 Intelligence Pvt Ltd/Desktop/DRP_data/mcu_box_office.csv")
    phase1=df[df.mcu_phase==1]
    phase2=df[df.mcu_phase==2]
    phase3=df[df.mcu_phase==3]
st.title("Biggest_opening of phase1")
fig10=plt.figure(figsize=(10,5))
plt.bar(phase1.movie_title,phase1.opening_weekend)
st.pyplot(fig10)
st.title("Biggest_opening of phase2")
fig11=plt.figure(figsize=(20,12))
plt.bar(phase2.movie_title,phase2.opening_weekend)
st.pyplot(fig11)
st.title("Biggest_opening of phase3")
fig11=plt.figure(figsize=(20,12))
plt.bar(phase3.movie_title,phase3.opening_weekend)
st.pyplot(fig11)