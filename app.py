import streamlit as st

# Set up the main page
st.set_page_config(page_title="Hispanic Career & Education Hub", page_icon="🌍", layout="wide")

# Ensure login before accessing any page
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.switch_page("pages/profile.py")

# Sidebar greeting for logged-in users
st.sidebar.title("Navigation")
st.sidebar.write(f"👋 Welcome, **{st.session_state['current_user']}**")
if st.sidebar.button("Log Out"):
    st.session_state["logged_in"] = False
    st.session_state["current_user"] = ""
    st.experimental_rerun()

# Apply custom CSS for title styling
st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 50px;
            font-weight: bold;
            font-family: 'Arial', sans-serif;
        }
        .big-button {
            display: block;
            width: 100%;
            padding: 20px;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            border-radius: 10px;
            background-color: #f0f0f0;
            margin-bottom: 10px;
            cursor: pointer;
        }
    </style>
""", unsafe_allow_html=True)

# Home Page Content
st.markdown('<h1 class="title">Hispanic Career & Education Hub</h1>', unsafe_allow_html=True)
st.write("Welcome! This website provides free resources for jobs, education, and legal support for Hispanic immigrants in Atlanta.")

st.image("https://source.unsplash.com/1600x500/?community", use_column_width=True)

st.markdown("### Explore Our Resources")
st.write("Click on any category below to learn more.")

# Create a 2-column layout for navigation buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("🔹 Job & Career Help"):
        st.switch
