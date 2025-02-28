import streamlit as st
import json
import os

st.set_page_config(page_title="Login", page_icon="👤")

# Hide sidebar completely
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        .welcome-text {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            font-family: 'Georgia', serif;
            color: #333;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# File for storing user credentials
USER_DATA_FILE = "users.json"

# Load user data from file
def load_users():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as f:
            return json.load(f)
    return {}

# Save user data to file
def save_users(users):
    with open(USER_DATA_FILE, "w") as f:
        json.dump(users, f)

# Initialize session state variables
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "current_user" not in st.session_state:
    st.session_state["current_user"] = ""

users = load_users()  # Load existing users

# If already logged in, go to home page
if st.session_state["logged_in"]:
    st.switch_page("app.py")

# Welcome Message
st.markdown('<h1 class="welcome-text">Welcome to CER | Bienvenido a CER</h1>', unsafe_allow_html=True)

st.title("👤 User Login / Sign Up")

# Tabs for Sign-up & Login
tab1, tab2 = st.tabs(["Sign Up", "Login"])

# Sign-up Section
with tab1:
    st.subheader("Create an Account")
    new_username = st.text_input("Choose a username:")
    new_password = st.text_input("Choose a password:", type="password")
    
    if st.button("Sign Up"):
        if new_username and new_password:
            if new_username in users:
                st.warning("Username already exists! Try a different one.")
            else:
                users[new_username] = new_password
                save_users(users)  # Save to file
                st.success("Account created successfully! You can now log in.")
        else:
            st.warning("Please fill in both fields.")

# Login Section
with tab2:
    st.subheader("Log In")
    username = st.text_input("Username:", key="login_username")
    password = st.text_input("Password:", type="password", key="login_password")
    
    if st.button("Log In"):
        if username in users and users[username] == password:
            st.session_state["logged_in"] = True
            st.session_state["current_user"] = username
            st.success(f"Welcome back, {username}!")
            st.switch_page("app.py")  # Redirect to home page
        else:
            st.error("Invalid username or password!")
