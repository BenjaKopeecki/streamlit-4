import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv("world_population.csv") 
st.set_page_config(page_title="1970's Population Pie Chart")
st.write(
    """This Pie Chart shows you the lowest 10 1970's Population"""
)
df.columns = df.columns.str.strip()
sorted_df = df.sort_values(by='1970 Population').head(10)
value_counts = df['1970 Population'].value_counts()
st.write("### 1970's Population Pie Chart")
fig, ax = plt.subplots()
ax.pie(sorted_df['1970 Population'], labels=sorted_df['Country'], autopct='%1.1f%%')
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig)