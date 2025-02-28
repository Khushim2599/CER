import streamlit as st

# ✅ Ensure this is the first command
st.set_page_config(page_title="Legal & Immigration Help", page_icon="⚖️")

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
    if st.button("📚 Education Resources" if st.session_state["language"] == "English" else "📚 Recursos educativos"):
        st.switch_page("pages/education.py")

with col4:
    if st.button("📢 About Us" if st.session_state["language"] == "English" else "📢 Sobre Nosotros"):
        st.switch_page("pages/about.py")

with col5:
    if st.button("🤝 Support Your Community" if st.session_state["language"] == "English" else "🤝 Apoya a tu comunidad"):
        st.switch_page("pages/support.py")

st.markdown('</div>', unsafe_allow_html=True)

# ✅ Page Title
st.title("⚖️ Legal & Immigration Help" if st.session_state["language"] == "English" else "⚖️ Ayuda legal e inmigración")

# ✅ Content with Dynamic Language Switching
st.write("""
Find free legal aid and immigration support resources.
""" if st.session_state["language"] == "English" else """
Encuentra ayuda legal gratuita y recursos de apoyo para inmigración.
""")

st.header("🆘 Free Legal Aid Services" if st.session_state["language"] == "English" else "🆘 Servicios de ayuda legal gratuita")
st.markdown("""
- [Atlanta Legal Aid](https://atlantalegalaid.org/) – Free legal help for low-income families.
- [Georgia Latino Alliance for Human Rights (GLAHR)](https://glahr.org/) – Advocacy and legal assistance for immigrants.
- [Catholic Charities Immigration Legal Services](https://catholiccharitiesatlanta.org/) – Assistance with visas, work permits, and citizenship.
""" if st.session_state["language"] == "English" else """
- [Asistencia Legal de Atlanta](https://atlantalegalaid.org/) – Ayuda legal gratuita para familias de bajos ingresos.
- [Alianza Latina de Georgia por los Derechos Humanos (GLAHR)](https://glahr.org/) – Defensa y asistencia legal para inmigrantes.
- [Servicios Legales de Inmigración de Caridades Católicas](https://catholiccharitiesatlanta.org/) – Asistencia con visas, permisos de trabajo y ciudadanía.
""")

st.header("📑 Immigration Resources" if st.session_state["language"] == "English" else "📑 Recursos de inmigración")
st.markdown("""
- [USCIS Work Authorization](https://www.uscis.gov/working-in-the-united-states) – Check if you qualify for work permits.
- [DACA Information & Renewals](https://www.uscis.gov/DACA) – Apply or renew Deferred Action for Childhood Arrivals.
- [Refugee & Asylum Support](https://www.acf.hhs.gov/orr) – Resources for asylum seekers and refugees.
""" if st.session_state["language"] == "English" else """
- [Autorización de Trabajo de USCIS](https://www.uscis.gov/working-in-the-united-states) – Verifica si calificas para permisos de trabajo.
- [Información y Renovación de DACA](https://www.uscis.gov/DACA) – Solicita o renueva Acción Diferida para los Llegados en la Infancia.
- [Apoyo para Refugiados y Asilo](https://www.acf.hhs.gov/orr) – Recursos para solicitantes de asilo y refugiados.
""")

st.header("📢 Know Your Rights" if st.session_state["language"] == "English" else "📢 Conoce tus derechos")
st.markdown("""
- [ACLU Immigrant Rights](https://www.aclu.org/issues/immigrants-rights) – Learn what to do if approached by ICE.
- [ICE Raids - What to Do](https://www.nilc.org/) – Resources on how to protect yourself and your family.
- [Local Immigration Help Centers](https://www.immigrationadvocates.org/) – Find support centers near you.
""" if st.session_state["language"] == "English" else """
- [Derechos de los Inmigrantes - ACLU](https://www.aclu.org/issues/immigrants-rights) – Aprende qué hacer si ICE se acerca a ti.
- [Redadas de ICE - Qué Hacer](https://www.nilc.org/) – Recursos sobre cómo protegerte a ti y a tu familia.
- [Centros de Ayuda para Inmigrantes](https://www.immigrationadvocates.org/) – Encuentra centros de apoyo cerca de ti.
""")
