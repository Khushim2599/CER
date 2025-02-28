import streamlit as st

st.set_page_config(page_title="Profile", page_icon="👤")

st.title("👤 User Profile")

name = st.text_input("Enter your name:")
email = st.text_input("Enter your email:")

if st.button("Save Profile"):
    st.success(f"Profile saved! Welcome, {name}!")

