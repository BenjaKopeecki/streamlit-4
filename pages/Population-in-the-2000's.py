import streamlit as st
import pandas as pd

st.set_page_config(page_title="Bar Chart")
df = pd.read_csv("world_population.csv")
df.columns = df.columns.str.strip()
st.write(
    """This Bar Chart shows you the top 5 2000's Population"""
)
sorted_df = df.sort_values(by='2000 Population', ascending=False).head(5)
st.bar_chart(sorted_df.set_index('Country')[['2000 Population']])
