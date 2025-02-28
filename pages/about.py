import streamlit as st

st.set_page_config(page_title="About Us", page_icon="📢")

# Redirect users to login page if not logged in
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.switch_page("pages/profile.py")

# Apply custom CSS for navigation bar
st.markdown("""
    <style>
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
    if st.button("🏠 Home"):
        st.switch_page("app.py")

with col2:
    if st.button("🔹 Job & Career Help"):
        st.switch_page("pages/jobs.py")

with col3:
    if st.button("📚 Education Resources"):
        st.switch_page("pages/education.py")

with col4:
    if st.button("⚖️ Legal & Immigration Help"):
        st.switch_page("pages/legal.py")

st.markdown('</div>', unsafe_allow_html=True)

st.title("📢 About Us")

st.write("""
The **Hispanic Career & Education Hub** is dedicated to empowering Hispanic immigrants in Atlanta by providing free access to career resources, job training, educational opportunities, and legal assistance.

We understand that navigating a new country can be challenging, and our goal is to bridge the gap by offering **bilingual support** and **easy-to-access information** that helps individuals build stable and successful futures.

### 🌍 **Our Mission**
Our mission is to support Hispanic immigrants in Atlanta by:
- Connecting them to **job opportunities** and **resume-building resources**.
- Providing access to **English learning programs** and **GED certifications**.
- Offering guidance on **legal aid**, **immigration services**, and **worker rights**.
- Ensuring that **language barriers** do not limit access to opportunities.
""")
