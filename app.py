import streamlit as st

# Set up the page
st.set_page_config(page_title="Hispanic Career & Education Hub", page_icon="🌍", layout="wide")

# Custom CSS for styling 
st.markdown("""
    <style>'
    body {
        background-color: #f8f9fa;
    }
    .main{
        background-color: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.1);
    }


# Language selection
lang = st.radio("Choose Language / Elige el idioma", ["English", "Español"])

# Content dictionary
content = {
    "English": {
        "title": "Welcome to the Hispanic Career & Education Hub",
        "intro": "Find free resources for jobs, education, and legal support in Atlanta.",
        "job_title": "🔹 Job & Career Help",
        "edu_title": "📚 Education Resources",
        "legal_title": "⚖️ Legal & Immigration Help",
    },
    "Español": {
        "title": "Bienvenido al Centro de Carreras y Educación Hispano",
        "intro": "Encuentra recursos gratuitos para empleos, educación y apoyo legal en Atlanta.",
        "job_title": "🔹 Ayuda para el empleo y la carrera",
        "edu_title": "📚 Recursos educativos",
        "legal_title": "⚖️ Ayuda legal e inmigración",
    }
}

# Display main content
st.title(content[lang]["title"])
st.write(content[lang]["intro"])

# Job & Career Section
st.header(content[lang]["job_title"])
st.markdown("""
- [Goodwill Job Training](https://www.goodwillng.org/job-training)
- [Georgia WorkSource](https://www.worksourceatlanta.org/)
- [Resume Templates (Canva)](https://www.canva.com/resumes/templates/)
- [Latino Jobs Network](https://latinojobsnetwork.com/)
""")

# Education Section
st.header(content[lang]["edu_title"])
st.markdown("""
- [Atlanta Technical College ESL](https://www.atlantatech.edu/)
- [GED Classes in Atlanta](https://www.ged.com/)
- [Free English Classes in GA](https://www.esl.com/resources/georgia/)
""")

# Legal & Immigration Help Section
st.header(content[lang]["legal_title"])
st.markdown("""
- [Georgia Latino Alliance for Human Rights](https://glahr.org/)
- [Atlanta Legal Aid](https://atlantalegalaid.org/)
- [USCIS Work Authorization](https://www.uscis.gov/working-in-the-united-states)
""")
