import streamlit as st

# ✅ Ensure this is the first command
st.set_page_config(page_title="Avanza", page_icon="🌍", layout="wide")

# Ensure login before accessing any page
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.switch_page("pages/profile.py")

# ✅ Language Toggle in Session State
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
        .title {
            text-align: center;
            font-size: 50px;
            font-weight: bold;
            font-family: 'Arial', sans-serif;
            margin-top: 10px;
        }
        .subtitle {
            text-align: center;
            font-size: 22px;
            font-family: 'Arial', sans-serif;
            color: #777;
            margin-bottom: 20px;
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
        .image-container {
            text-align: center;
        }
        .banner-image {
            width: 90%;
            height: 200px;
            object-fit: cover;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# ✅ Title and Subtitle
st.markdown('<h1 class="title">Avanza</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subtitle">Hispanic Career & Education Hub</h2>', unsafe_allow_html=True)

# ✅ Navigation Bar
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

# ✅ Image Below Navigation
st.markdown('<div class="image-container">', unsafe_allow_html=True)
st.image("https://www.morganlewis.com/-/media/images/supplemental/we-are-ml/2021/oct---hispanic-heritage-month/abstraction-floral_1166067862_edit_largetile.jpg?rev=baf85c15d2ee4c07898c4170b6ac85d7&hash=A7A8AE243E1D45BA0C4A6D462D25182C", 
         use_column_width=False, width=900)
st.markdown('</div>', unsafe_allow_html=True)

# ✅ Main Content Below the Image
st.write("Welcome! This website provides free resources for jobs, education, and legal support for Hispanic immigrants in Atlanta." if st.session_state["language"] == "English" else
         "¡Bienvenido! Este sitio web proporciona recursos gratuitos para empleo, educación y apoyo legal para inmigrantes hispanos en Atlanta.")
