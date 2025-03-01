import streamlit as st

# ✅ Ensure this is the first command
st.set_page_config(page_title="Job & Career Help", page_icon="💼")

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

# ✅ Hide Sidebar
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        .navbar {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-bottom: 15px;
        }
        .navbar button {
            font-size: 16px;
            font-weight: bold;
            padding: 8px 15px;
            background: #004080;
            color: white;
            border-radius: 10px;
            border: none;
            cursor: pointer;
        }
        .navbar button:hover {
            background: #0059b3;
        }
        .banner-container {
            width: 100%;
            height: 250px; /* Increased height */
            position: relative;
            overflow: hidden;
            margin-bottom: 20px;
        }
        .banner-image {
            width: 100%;
            height: 100%;
            object-fit: cover;
            border-radius: 0;
        }
        .banner-text {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 24px;
            font-weight: bold;
            color: white;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
            background: rgba(0, 0, 0, 0.5);
            padding: 12px 20px;
            border-radius: 10px;
            text-align: center;
            width: 80%;
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
    if st.button("📚 Education Resources" if st.session_state["language"] == "English" else "📚 Recursos educativos"):
        st.switch_page("pages/education.py")

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

# ✅ Bigger Banner Image with Text Overlay
st.markdown('<div class="banner-container">', unsafe_allow_html=True)
st.markdown(
    f"""
    <div class="banner-container">
        <img src="https://www.morganlewis.com/-/media/images/supplemental/we-are-ml/2021/oct---hispanic-heritage-month/abstraction-floral_1166067862_edit_largetile.jpg?rev=baf85c15d2ee4c07898c4170b6ac85d7&hash=A7A8AE243E1D45BA0C4A6D462D25182C" class="banner-image">
        <div class="banner-text">
            {"🔹 Job & Career Help <br> Find job resources, resume assistance, and training programs." if st.session_state["language"] == "English" else "🔹 Ayuda para el empleo <br> Encuentra recursos laborales, asistencia con currículums y programas de capacitación."}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ✅ Job Training Programs
st.header("📌 Job Training Programs" if st.session_state["language"] == "English" else "📌 Programas de capacitación laboral")
st.markdown("""
- [Goodwill Job Training](https://goodwillng.org/putting-people-to-work/get-job-training/) – Free job training in IT, customer service, healthcare, and more.
- [Georgia WorkSource](https://www.worksourceatlanta.org/) – Career coaching, resume building, and job placement assistance.
""" if st.session_state["language"] == "English" else """
- [Capacitación Laboral de Goodwill](https://www.goodwillng.org/job-training) – Capacitación gratuita en TI, servicio al cliente, salud y más.
- [Georgia WorkSource](https://www.worksourceatlanta.org/) – Coaching profesional, creación de currículums y asistencia en colocación laboral.
""")

# ✅ Resume Assistance
st.header("📝 Resume Assistance" if st.session_state["language"] == "English" else "📝 Asistencia con currículums")
st.markdown("""
- [Resume Templates (Canva)](https://www.canva.com/resumes/templates/) – Free professional resume templates.
- [Atlanta Public Library Resume Help](https://www.fulcolibrary.org/) – Free workshops on resume building.
""" if st.session_state["language"] == "English" else """
- [Plantillas de Currículum (Canva)](https://www.canva.com/resumes/templates/) – Plantillas de currículum gratuitas y profesionales.
- [Ayuda con Currículums en la Biblioteca de Atlanta](https://www.fulcolibrary.org/) – Talleres gratuitos sobre creación de currículums.
""")

# ✅ Job Search Websites
st.header("💼 Job Search Websites" if st.session_state["language"] == "English" else "💼 Sitios web de búsqueda de empleo")
st.markdown("""
- [Indeed - Atlanta Jobs](https://www.indeed.com/q-Atlanta-jobs.html) – Search for jobs in Atlanta.
- [Glassdoor - Bilingual Jobs](https://www.glassdoor.com/Job/atlanta-bilingual-jobs-SRCH_IL.0,7_IC1155583_KO8,17.htm) – Find bilingual jobs in Atlanta.
- [Latino Jobs Network](https://latinojobsnetwork.com/) – Job board for Hispanic job seekers.
""" if st.session_state["language"] == "English" else """
- [Indeed - Trabajos en Atlanta](https://www.indeed.com/q-Atlanta-jobs.html) – Busca empleos en Atlanta.
- [Glassdoor - Trabajos Bilingües](https://www.glassdoor.com/Job/atlanta-bilingual-jobs-SRCH_IL.0,7_IC1155583_KO8,17.htm) – Encuentra trabajos bilingües en Atlanta.
- [Latino Jobs Network](https://latinojobsnetwork.com/) – Bolsa de trabajo para buscadores de empleo hispanos.
""")
