from lm import generate_next_character
import streamlit as st

st.title("Random Name Generator")

if st.button("Generate"):
    name=generate_next_character()
    st.text_area("Name Generated",name)