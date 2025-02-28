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
        .banner-container {
            position: relative;
            text-align: center;
            color: white;
        }
        .banner-image {
            width: 100%;
            height: 300px;
            object-fit: cover;
        }
        .navbar {
            position: absolute;
            top: 10px;
            width: 100%;
            display: flex;
            justify-content: center;
        }
        .navbar button {
            margin: 5px;
            font-size: 16px;
            font-weight: bold;
            background: rgba(0, 0, 0, 0.6);
            color: white;
            border-radius: 10px;
            padding: 10px;
        }
        .navbar button:hover {
            background: rgba(255, 255, 255, 0.4);
            color: black;
        }
        .title-container {
            position: absolute;
            top: 35%;
            width: 100%;
            text-align: center;
        }
        .title {
            font-size: 50px;
            font-weight: bold;
            font-family: 'Arial', sans-serif;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
        }
        .subtitle {
            font-size: 22px;
            font-family: 'Arial', sans-serif;
            color: #ddd;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.7);
        }
    </style>
""", unsafe_allow_html=True)

# ✅ Banner Image with Navigation Overlay
st.markdown("""
    <div class="banner-container">
        <img src="https://www.morganlewis.com/-/media/images/supplemental/we-are-ml/2021/oct---hispanic-heritage-month/abstraction-floral_1166067862_edit_largetile.jpg?rev=baf85c15d2ee4c07898c4170b6ac85d7&hash=A7A8AE243E1D45BA0C4A6D462D25182C" class="banner-image">
        <div class="navbar">
            <button onclick="location.href='pages/jobs.py'">🔹 Job & Career Help</button>
            <button onclick="location.href='pages/education.py'">📚 Education Resources</button>
            <button onclick="location.href='pages/legal.py'">⚖️ Legal & Immigration Help</button>
            <button onclick="location.href='pages/about.py'">📢 About Us</button>
            <button onclick="location.href='pages/support.py'">🤝 Support Your Community</button>
        </div>
        <div class="title-container">
            <h1 class="title">Avanza</h1>
            <h2 class="subtitle">Hispanic Career & Education Hub</h2>
        </div>
    </div>
""", unsafe_allow_html=True)

# ✅ Main Content Below the Banner
st.write("Welcome! This website provides free resources for jobs, education, and legal support for Hispanic immigrants in Atlanta." if st.session_state["language"] == "English" else
         "¡Bienvenido! Este sitio web proporciona recursos gratuitos para empleo, educación y apoyo legal para inmigrantes hispanos en Atlanta.")
