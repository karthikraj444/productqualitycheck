import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
if st.checkbox("Click here to see the report"):
    df=pd.read_csv("D:/Karthikraj_data/OneDrive - Course5 Intelligence Pvt Ltd/Desktop/DRP_data/mcu_box_office.csv")
    phase1=df[df.mcu_phase==1]
    phase2=df[df.mcu_phase==2]
    phase3=df[df.mcu_phase==3]

st.title("Production budget of phase1 film")

fig = plt.figure(figsize = (20, 12))
plt.bar(phase1.movie_title,phase1.production_budget)
st.pyplot(fig)
st.title("Worldwide box office of phase1 film")
fig2=plt.figure(figsize=(20,12))
plt.bar(phase1.movie_title,phase1.worldwide_box_office)
st.pyplot(fig2)

st.title("Production budget of phase2 film")
fig3 = plt.figure(figsize = (20, 12))
plt.bar(phase2.movie_title,phase2.production_budget)
st.pyplot(fig3)
st.title("Worldwide box office of phase2 film")
fig4=plt.figure(figsize=(20,12))
plt.bar(phase2.movie_title,phase2.worldwide_box_office)
st.pyplot(fig4)

st.title("Production budget of phase3 film")
fig5 = plt.figure(figsize = (20, 12))
plt.bar(phase3.movie_title,phase3.production_budget)
st.pyplot(fig5)
st.title("Worldwide box office of phase3 film")
fig6=plt.figure(figsize=(20,12))
plt.bar(phase3.movie_title,phase3.worldwide_box_office)
st.pyplot(fig6)