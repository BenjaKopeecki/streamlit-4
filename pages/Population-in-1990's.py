import streamlit as st
import pandas as pd

st.title(page_title="2022 Population Area Chart")
df = pd.read_csv("world_population.csv")
df.columns = df.columns.str.strip()
st.write(
    """This Area Chart shows you the highest 20 Countries Population"""
)
sorted_df = df.sort_values(by='1990 Population', ascending=False).head(20)
st.area_chart(sorted_df.set_index('Country')[['1990 Population']])
