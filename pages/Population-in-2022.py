import streamlit as st
import pandas as pd

st.set_page_config(page_title="Bar Chart")
df = pd.read_csv("world_population.csv")
df.columns = df.columns.str.strip()
st.write(
    """This Bar Chart shows you the lowest 15 2022 Population"""
)
sorted_df = df.sort_values(by='2022 Population').head(15)
st.bar_chart(sorted_df.set_index('Country')[['2022 Population']])
