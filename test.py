import  streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('startup_cleaned.csv')
df['date']=pd.to_datetime(df['date'],errors='coerce')
df['year']=df['date'].dt.year
#df.info()

total=round(df['amount'].sum())
max=round(df['amount'].max())
min=round(df['amount'].min())
avg=round(df['amount'].mean())


def load_overall_analysis():
    st.header("Overall Analysis")
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.metric('Toal Investment', str(total) + "Cr")
    with col2:
        st.metric('Max Investment', str(max) + "Cr")
    with col3:
        st.metric('Minimum Investment', str(min) + "Cr")
    with col4:
        st.metric('Average Investment', str(avg) + "Cr")
    y = df.groupby('year')[['amount']].sum()
    fig, ax = plt.subplots()
    ax.plot(y.index, y.values)
    st.pyplot(fig)


def load_startup_analysis():
    st.header("Startup Analysis")

def load_investor_analysis(invester):
    st.title(invester)

options=st.sidebar.selectbox("Select Any One",["Investor","Startup","Overall"])
if options=="Overall":
    load_overall_analysis()
elif options=="Startup":
    load_startup_analysis()
else:
    selected_invester =st.sidebar.selectbox("Investor Name",sorted(set(df["investors"].str.split(",").sum())))
    btn2=st.sidebar.button("Select One")
    if btn2:
        load_investor_analysis(selected_invester)
