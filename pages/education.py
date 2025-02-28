import streamlit as st

st.set_page_config(page_title="Education Resources", page_icon="📚")

# Redirect users to login page if not logged in
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.switch_page("pages/profile.py")

# Navigation Bar
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

st.markdown('<div class="navbar">', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🏠 Home"):
        st.switch_page("app.py")

with col2:
    if st.button("🔹 Job & Career Help"):
        st.switch_page("pages/jobs.py")

with col3:
    if st.button("⚖️ Legal & Immigration Help"):
        st.switch_page("pages/legal.py")

with col4:
    if st.button("📢 About Us"):
        st.switch_page("pages/about.py")

st.markdown('</div>', unsafe_allow_html=True)

st.title("📚 Education Resources")

st.write("""
Education is a key to success. Here, you will find free English learning resources, GED programs, and scholarship opportunities.
""")

st.markdown("""
### 🏫 **English as a Second Language (ESL) Classes**
- [Atlanta Technical College ESL](https://www.atlantatech.edu/) – Free and low-cost English classes.
- [Free English Classes in GA](https://www.esl.com/resources/georgia/) – Find ESL programs near you.

### 🎓 **GED (High School Equivalency) Programs**
- [GED Classes in Atlanta](https://www.ged.com/) – Online and in-person GED programs.
- [Goodwill GED Assistance](https://www.goodwillng.org/education) – Free GED prep courses.

### 🎓 **College & Scholarship Help**
- [TheDream.US Scholarship](https://www.thedream.us/) – Scholarships for undocumented students.
- [Hispanic Scholarship Fund](https://www.hsf.net/) – Scholarships for Hispanic students.
""")
