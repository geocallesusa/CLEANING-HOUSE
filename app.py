import streamlit as st

st.title("My First Streamlit App")
st.write("Welcome to my application published from GitHub!")

name = st.text_input("What is your name?")

if name:
    st.success(f"Hello, {name}!")