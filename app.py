import streamlit as st

# Set up the main page
st.set_page_config(page_title="Hispanic Career & Education Hub", page_icon="🌍", layout="wide")

# Redirect users to the login page if not logged in
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.switch_page("pages/profile.py")

# Sidebar greeting for logged-in users
st.sidebar.title("Navigation")
st.sidebar.write(f"👋 Welcome, **{st.session_state['current_user']}**")
if st.sidebar.button("Log Out"):
    st.session_state["logged_in"] = False
    st.session_state["current_user"] = ""
    st.experimental_rerun()

# Home Page Content
st.title("🌍 Hispanic Career & Education Hub")
st.write("Welcome! This website provides free resources for jobs, education, and legal support for Hispanic immigrants in Atlanta.")

st.image("https://source.unsplash.com/1600x500/?community", use_column_width=True)

st.markdown("### Explore Our Resources")
st.write("Click on any category below to learn more.")

# Create a 2-column layout for the navigation cards
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔹 Job & Career Help"):
        st.switch_page("pages/jobs.py")

with col2:
    if st.button("📚 Education Resources"):
        st.switch_page("pages/education.py")

with col3:
    if st.button("⚖️ Legal & Immigration Help"):
        st.switch_page("pages/legal.py")

st.markdown("---")

# About Us Section
if st.button("📢 About Us"):
    st.switch_page("pages/about.py")
