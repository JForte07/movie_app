import streamlit as st
from app import home_page

st.set_page_config(
    page_title="Movie App",
    page_icon="🎬",
)
# Call the homepage function
st = home_page(st)
