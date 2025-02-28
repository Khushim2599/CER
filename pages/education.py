import streamlit as st

# ✅ Ensure this is the first command
st.set_page_config(page_title="Education Resources", page_icon="📚")

# Redirect users to login page if not logged in
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.switch_page("pages/profile.py")

# ✅ Language Toggle (Switch-style button)
if "language" not in st.session_state:
    st.session_state["language"] = "English"

toggle_col1, toggle_col2 = st.columns([0.8, 0.2])
with toggle_col2:
    language_toggle = st.toggle("🌍 English / Español", value=(st.session_state["language"] == "Español"))
    st.session_state["language"] = "Español" if language_toggle else "English"

# ✅ Hide sidebar
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

# ✅ Navigation Bar
st.markdown('<div class="navbar">', unsafe_allow_html=True)
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("🏠 Home" if st.session_state["language"] == "English" else "🏠 Inicio"):
        st.switch_page("app.py")

with col2:
    if st.button("🔹 Job & Career Help" if st.session_state["language"] == "English" else "🔹 Ayuda para el empleo"):
        st.switch_page("pages/jobs.py")

with col3:
    if st.button("⚖️ Legal & Immigration Help" if st.session_state["language"] == "English" else "⚖️ Ayuda legal e inmigración"):
        st.switch_page("pages/legal.py")

with col4:
    if st.button("📢 About Us" if st.session_state["language"] == "English" else "📢 Sobre Nosotros"):
        st.switch_page("pages/about.py")

with col5:
    if st.button("🤝 Support Your Community" if st.session_state["language"] == "English" else "🤝 Apoya a tu comunidad"):
        st.switch_page("pages/support.py")

st.markdown('</div>', unsafe_allow_html=True)

# ✅ Page Title
st.title("📚 Education Resources" if st.session_state["language"] == "English" else "📚 Recursos educativos")

# ✅ Content with Dynamic Language Switching
st.write("""
Find free ESL classes, GED programs, and college scholarships.
""" if st.session_state["language"] == "English" else """
Encuentra clases gratuitas de inglés, programas GED y becas universitarias.
""")

st.header("📖 Free ESL (English as a Second Language) Classes" if st.session_state["language"] == "English" else "📖 Clases gratuitas de inglés (ESL)")
st.markdown("""
- [Atlanta Technical College ESL](https://www.atlantatech.edu/) – Free English classes for adults.
- [Goodwill of North Georgia ESL Classes](https://www.goodwillng.org/) – Learn English for work and daily life.
""" if st.session_state["language"] == "English" else """
- [Clases de Inglés en Atlanta Technical College](https://www.atlantatech.edu/) – Clases gratuitas de inglés para adultos.
- [Clases de ESL en Goodwill de North Georgia](https://www.goodwillng.org/) – Aprende inglés para el trabajo y la vida diaria.
""")

st.header("🎓 GED & High School Diploma Programs" if st.session_state["language"] == "English" else "🎓 Programas de GED y Diploma de Secundaria")
st.markdown("""
- [GED Classes in Atlanta](https://www.ged.com/) – Find local programs to earn your GED.
- [Adult Education Programs (GA)](https://tcsg.edu/adult-education/) – Free resources to prepare for the GED exam.
""" if st.session_state["language"] == "English" else """
- [Clases de GED en Atlanta](https://www.ged.com/) – Encuentra programas locales para obtener tu GED.
- [Programas de Educación para Adultos (GA)](https://tcsg.edu/adult-education/) – Recursos gratuitos para prepararse para el examen de GED.
""")

st.header("🎓 College Scholarships & Financial Aid" if st.session_state["language"] == "English" else "🎓 Becas Universitarias y Ayuda Financiera")
st.markdown("""
- [TheDream.US Scholarship](https://www.thedream.us/) – Scholarships for undocumented students.
- [Hispanic Scholarship Fund](https://www.hsf.net/) – College funding for Hispanic students.
""" if st.session_state["language"] == "English" else """
- [Beca TheDream.US](https://www.thedream.us/) – Becas para estudiantes indocumentados.
- [Fondo de Becas para Hispanos](https://www.hsf.net/) – Ayuda financiera para estudiantes hispanos.
""")
