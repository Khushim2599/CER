import streamlit as st

st.set_page_config(page_title="Education Resources", page_icon="📚")

# Redirect users to login page if not logged in
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.switch_page("pages/profile.py")

# Go to Home Page button
if st.button("🏠 Go to Home Page"):
    st.switch_page("app.py")

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
