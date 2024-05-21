import streamlit as st

st.set_page_config(
    page_title="Home Page",
)

st.write("# Welcome to BenjaKopecki's Streamlit Multi-Page. 👋")

st.sidebar.success("Select a chart above.")

st.markdown(
    """
This website is gonna have 4 charts (containing two bar charts, one pie chart, and an area chart) of world population from different countries. Hope you enjoy.
"""
)
