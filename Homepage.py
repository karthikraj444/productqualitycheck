import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("D:/Karthikraj_data/OneDrive - Course5 Intelligence Pvt Ltd/Desktop/DRP_data/mcu_box_office.csv")
st.sidebar.subheader("Dataset")
st.sidebar.write(df)
st.title("Product Quality Analysis")
st.write("Upload the dataset")
upload=st.file_uploader(label="upload the file")
fd=pd.read_csv(upload)
fd
phase1=df[df.mcu_phase==1]
phase2=df[df.mcu_phase==2]
phase3=df[df.mcu_phase==3]
audience1=df[df.mcu_phase==1]







