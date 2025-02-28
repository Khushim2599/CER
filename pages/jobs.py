import streamlit as st

st.set_page_config(page_title="Job & Career Help", page_icon="💼")

# Redirect users to login page if not logged in
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.switch_page("pages/profile.py")

# Language Toggle
if "language" not in st.session_state:
    st.session_state["language"] = "English"

# Language Selection Button
lang_col1, lang_col2 = st.columns([0.8, 0.2])
with lang_col2:
    if st.button("🇪🇸 Español" if st.session_state["language"] == "English" else "🇺🇸 English"):
        st.session_state["language"] = "Español" if st.session_state["language"] == "English" else "English"
        st.experimental_rerun()

# Hide sidebar
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

# Navigation Bar
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

st.title("🔹 Job & Career Help" if st.session_state["language"] == "English" else "🔹 Ayuda para el empleo")

st.write("""
Here you can find job resources, resume assistance, and training programs.
""" if st.session_state["language"] == "English" else """
Aquí puedes encontrar recursos laborales, asistencia con currículums y programas de capacitación.
""")
