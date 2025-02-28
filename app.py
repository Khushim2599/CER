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

# Custom CSS for larger buttons
st.markdown("""
    <style>
    .big-button {
        display: block;
        width: 100%;
        padding: 20px;
        font-size: 18px;
        font-weight: bold;
        text-align: center;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Create a 2-column layout for the navigation cards
col1, col2, col3 = st.columns(3)

with col1:
    if st.markdown('<a href="pages/jobs.py" class="big-button">🔹 Job & Career Help</a>', unsafe_allow_html=True):
        st.switch_page("pages/jobs.py")

with col2:
    if st.markdown('<a href="pages/education.py" class="big-button">📚 Education Resources</a>', unsafe_allow_html=True):
        st.switch_page("pages/education.py")

with col3:
    if st.markdown('<a href="pages/legal.py" class="big-button">⚖️ Legal & Immigration Help</a>', unsafe_allow_html=True):
        st.switch_page("pages/legal.py")

st.markdown("---")

# About Us Section
if st.button("📢 About Us", key="about_us"):
    st.switch_page("pages/about.py")
