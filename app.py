import streamlit as st

# Set up the main page
st.set_page_config(page_title="Hispanic Career & Education Hub", page_icon="🌍", layout="wide")

# Initialize session state for authentication
if "users" not in st.session_state:
    st.session_state["users"] = {}  # Stores usernames & passwords
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "current_user" not in st.session_state:
    st.session_state["current_user"] = ""

# Redirect users to the login page if not logged in
if not st.session_state["logged_in"]:
    st.switch_page("pages/profile.py")

# Once logged in, show the main content
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About Us", "Job & Career Help", "Education Resources", "Legal & Immigration Help"])

# Sidebar greeting for logged-in users
st.sidebar.write(f"👋 Welcome, **{st.session_state['current_user']}**")
if st.sidebar.button("Log Out"):
    st.session_state["logged_in"] = False
    st.session_state["current_user"] = ""
    st.experimental_rerun()

# Home Page
if page == "Home":
    st.title("🌍 Hispanic Career & Education Hub")
    st.write("Welcome! This website provides free resources for jobs, education, and legal support for Hispanic immigrants in Atlanta.")
    st.image("https://source.unsplash.com/1600x500/?community", use_column_width=True)

# About Us Page
elif page == "About Us":
    st.switch_page("pages/about.py")

# Job & Career Help Page
elif page == "Job & Career Help":
    st.switch_page("pages/jobs.py")

# Education Resources Page
elif page == "Education Resources":
    st.switch_page("pages/education.py")

# Legal & Immigration Help Page
elif page == "Legal & Immigration Help":
    st.switch_page("pages/legal.py")
