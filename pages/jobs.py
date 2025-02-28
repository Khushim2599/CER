import streamlit as st

# Go to Home Page button
if st.button("🏠 Go to Home Page"):
    st.switch_page("app.py")

st.set_page_config(page_title="Job & Career Help", page_icon="💼")

st.title("🔹 Job & Career Help")
st.markdown("""
- [Goodwill Job Training](https://www.goodwillng.org/job-training)
- [Georgia WorkSource](https://www.worksourceatlanta.org/)
- [Resume Templates (Canva)](https://www.canva.com/resumes/templates/)
- [Latino Jobs Network](https://latinojobsnetwork.com/)
""")

