import streamlit as st

st.set_page_config(page_title="Job & Career Help", page_icon="💼")

# Redirect users to login page if not logged in
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.switch_page("pages/profile.py")

# Go to Home Page button
if st.button("🏠 Go to Home Page"):
    st.switch_page("app.py")

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
