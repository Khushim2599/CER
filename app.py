import streamlit as st

# Set up the page
st.set_page_config(page_title="Hispanic Career & Education Hub", page_icon="🌍", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About Us", "Job & Career Help", "Education Resources", "Legal & Immigration Help", "Profile"])

# Language selection
lang = st.sidebar.radio("Choose Language / Elige el idioma", ["English", "Español"])

# Home Page
if page == "Home":
    st.title("🌍 Hispanic Career & Education Hub")
    st.write("Welcome! This website provides free resources for jobs, education, and legal support for Hispanic immigrants in Atlanta.")
    st.image("https://source.unsplash.com/1600x500/?community", use_column_width=True)

# About Us Page
elif page == "About Us":
    st.title("📢 About Us")
    st.write("Our mission is to support Hispanic immigrants in Atlanta by providing job training, education, and legal resources.")
    st.subheader("Our Mission")
    st.write("To empower individuals with the tools needed for success in the workforce and education.")

# Job & Career Help Page
elif page == "Job & Career Help":
    st.title("🔹 Job & Career Help")
    st.markdown("""
    - [Goodwill Job Training](https://www.goodwillng.org/job-training)
    - [Georgia WorkSource](https://www.worksourceatlanta.org/)
    - [Resume Templates (Canva)](https://www.canva.com/resumes/templates/)
    - [Latino Jobs Network](https://latinojobsnetwork.com/)
    """)

# Education Resources Page
elif page == "Education Resources":
    st.title("📚 Education Resources")
    st.markdown("""
    - [Atlanta Technical College ESL](https://www.atlantatech.edu/)
    - [GED Classes in Atlanta](https://www.ged.com/)
    - [Free English Classes in GA](https://www.esl.com/resources/georgia/)
    """)

# Legal & Immigration Help Page
elif page == "Legal & Immigration Help":
    st.title("⚖️ Legal & Immigration Help")
    st.markdown("""
    - [Georgia Latino Alliance for Human Rights](https://glahr.org/)
    - [Atlanta Legal Aid](https://atlantalegalaid.org/)
    - [USCIS Work Authorization](https://www.uscis.gov/working-in-the-united-states)
    """)

# Profile Page
elif page == "Profile":
    st.title("👤 User Profile")
    name = st.text_input("Enter your name:")
    email = st.text_input("Enter your email:")
    if st.button("Save Profile"):
        st.success(f"Profile saved! Welcome, {name}!")
