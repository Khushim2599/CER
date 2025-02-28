import streamlit as st

st.set_page_config(page_title="Job & Career Help", page_icon="💼")

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
    if st.button("📚 Education Resources"):
        st.switch_page("pages/education.py")

with col3:
    if st.button("⚖️ Legal & Immigration Help"):
        st.switch_page("pages/legal.py")

with col4:
    if st.button("📢 About Us"):
        st.switch_page("pages/about.py")

st.markdown('</div>', unsafe_allow_html=True)

st.title("🔹 Job & Career Help")

st.write("""
Finding a job can be challenging, but there are many resources available to help you get started. Below are links to job training programs, resume assistance, and job search platforms specifically for Hispanic immigrants in Atlanta.
""")

st.markdown("""
### 📌 **Job Training Programs**
- [Goodwill Job Training](https://www.goodwillng.org/job-training) – Free job training in IT, customer service, healthcare, and more.
- [Georgia WorkSource](https://www.worksourceatlanta.org/) – Career coaching, resume building, and job placement assistance.

### 📝 **Resume Assistance**
- [Resume Templates (Canva)](https://www.canva.com/resumes/templates/) – Free professional resume templates.
- [Atlanta Public Library Resume Help](https://www.fulcolibrary.org/) – Free workshops on resume building.

### 💼 **Job Search Websites**
- [Indeed - Atlanta Jobs](https://www.indeed.com/q-Atlanta-jobs.html) – Search for jobs in Atlanta.
- [Glassdoor - Bilingual Jobs](https://www.glassdoor.com/Job/atlanta-bilingual-jobs-SRCH_IL.0,7_IC1155583_KO8,17.htm) – Find bilingual jobs in Atlanta.
- [Latino Jobs Network](https://latinojobsnetwork.com/) – Job board for Hispanic job seekers.
""")
