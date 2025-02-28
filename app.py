import streamlit as st

# Set up the main page
st.set_page_config(page_title="Hispanic Career & Education Hub", page_icon="🌍", layout="wide")

# Main page content
st.title("🌍 Hispanic Career & Education Hub")
st.write("Welcome! This website provides free resources for jobs, education, and legal support for Hispanic immigrants in Atlanta.")

st.image("https://source.unsplash.com/1600x500/?community", use_column_width=True)

st.sidebar.success("Select a page above to navigate.")
