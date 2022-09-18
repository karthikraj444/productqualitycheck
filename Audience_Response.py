import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
if st.checkbox("Click here to see the report"):
    df=pd.read_csv("D:/Karthikraj_data/OneDrive - Course5 Intelligence Pvt Ltd/Desktop/DRP_data/mcu_box_office.csv")
    phase1=df[df.mcu_phase==1]
    phase2=df[df.mcu_phase==2]
    phase3=df[df.mcu_phase==3]
st.title("Audience_Score for phase1")

fig7=plt.figure(figsize=(20,12))
plt.pie(phase1.audience_score,labels=phase1.movie_title)
st.pyplot(fig7)

st.title("Audience_Score for phase2")
fig8=plt.figure(figsize=(20,12))
plt.pie(phase2.audience_score,labels=phase2.movie_title)
st.pyplot(fig8)

st.title("Audience_Score for phase3")
fig9=plt.figure(figsize=(20,12))
plt.pie(phase3.audience_score,labels=phase3.movie_title)
st.pyplot(fig9)