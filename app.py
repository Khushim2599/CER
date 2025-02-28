import streamlit as st
import json
import os

st.set_page_config(page_title="Avanza", page_icon="🌍", layout="wide")

# File for storing user credentials
USER_DATA_FILE = "users.json"

# Load user data from file
def load_users():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as f:
            return json.load(f)
    return {}

users = load_users()

# Ensure login before accessing any page
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.switch_page("pages/profile.py")

# Hide sidebar completely
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

# Apply custom CSS for title and navigation bar
st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 50px;
            font-weight: bold;
            font-family: 'Arial', sans-serif;
        }
        .navbar {
            display: flex;
            justify-content: center;
            background-color: #f0f0f0;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .nav-button {
            margin: 0 15px;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            background-color: #d9d9d9;
            border: none;
            padding: 10px 20px;
            border-radius: 8px;
        }
        .nav-button:hover {
            background-color: #b3b3b3;
        }
    </style>
""", unsafe_allow_html=True)

# Navigation bar at the top
st.markdown('<div class="navbar">', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🔹 Job & Career Help"):
        st.switch_page("pages/jobs.py")

with col2:
    if st.button("📚 Education Resources"):
        st.switch_page("pages/education.py")

with col3:
    if st.button("⚖️ Legal & Immigration Help"):
        st.switch_page("pages/legal.py")

with col4:
    if st.button("📢 About Us"):
        st.switch_page("pages/about.py")

st.markdown('</div>', unsafe_allow_html=True)

# Welcome Section
st.markdown('<h1 class="title">Hispanic Career & Education Hub</h1>', unsafe_allow_html=True)
st.write("Welcome! This website provides free resources for jobs, education, and legal support for Hispanic immigrants in Atlanta.")

st.image("https://source.unsplash.com/1600x500/?community", use_container_width=True)
