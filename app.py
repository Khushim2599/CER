import streamlit as st

st.set_page_config(page_title="Avanza", page_icon="🌍", layout="wide")

# Ensure login before accessing any page
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.switch_page("pages/profile.py")

# Language Toggle in Session State
if "language" not in st.session_state:
    st.session_state["language"] = "English"

# Language Selection Button
lang_col1, lang_col2 = st.columns([0.8, 0.2])
with lang_col2:
    if st.button("🇪🇸 Español" if st.session_state["language"] == "English" else "🇺🇸 English"):
        st.session_state["language"] = "Español" if st.session_state["language"] == "English" else "English"
        st.experimental_rerun()

# Hide sidebar completely
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        .title {
            text-align: center;
            font-size: 50px;
            font-weight: bold;
            font-family: 'Arial', sans-serif;
        }
        .subtitle {
            text-align: center;
            font-size: 22px;
            font-family: 'Arial', sans-serif;
            color: #777;
            margin-bottom: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# Page Content
st.markdown('<h1 class="title">Avanza</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subtitle">Hispanic Career & Education Hub</h2>', unsafe_allow_html=True)

st.write("Welcome! This website provides free resources for jobs, education, and legal support for Hispanic immigrants in Atlanta." if st.session_state["language"] == "English" else
         "¡Bienvenido! Este sitio web proporciona recursos gratuitos para empleo, educación y apoyo legal para inmigrantes hispanos en Atlanta.")

st.image("https://source.unsplash.com/1600x500/?community", use_container_width=True)

# Navigation Bar
st.markdown('<div class="navbar">', unsafe_allow_html=True)
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("🔹 Job & Career Help" if st.session_state["language"] == "English" else "🔹 Ayuda para el empleo"):
        st.switch_page("pages/jobs.py")

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
