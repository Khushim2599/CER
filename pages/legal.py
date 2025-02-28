import streamlit as st

# Language Toggle
if "language" not in st.session_state:
    st.session_state["language"] = "English"

# Language Selection Button
lang_col1, lang_col2 = st.columns([0.8, 0.2])
with lang_col2:
    if st.button("🇪🇸 Español" if st.session_state["language"] == "English" else "🇺🇸 English"):
        st.session_state["language"] = "Español" if st.session_state["language"] == "English" else "English"
        st.experimental_rerun()

st.set_page_config(page_title="Legal & Immigration Help", page_icon="⚖️")

# Redirect users to login page if not logged in
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.switch_page("pages/profile.py")

# Navigation Bar
st.markdown("""
    <style>
        .navbar {
            display: flex;
            justify-content: center;
            background-color: #f0f0f0;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .nav-button {
            margin: 0 15px;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            background-color: #d9d9d9;
            border: none;
            padding: 10px 20px;
            border-radius: 8px;
        }
        .nav-button:hover {
            background-color: #b3b3b3;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="navbar">', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🏠 Home"):
        st.switch_page("app.py")

with col2:
    if st.button("🔹 Job & Career Help"):
        st.switch_page("pages/jobs.py")

with col3:
    if st.button("📚 Education Resources"):
        st.switch_page("pages/education.py")

with col4:
    if st.button("📢 About Us"):
        st.switch_page("pages/about.py")

st.markdown('</div>', unsafe_allow_html=True)

st.title("⚖️ Legal & Immigration Help")

st.write("""
Understanding your rights as an immigrant is crucial. Below are resources for legal assistance, immigration help, and work permit applications.
""")

st.markdown("""
### ⚖️ **Free Legal Assistance**
- [Georgia Latino Alliance for Human Rights](https://glahr.org/) – Provides legal support for Hispanic immigrants.
- [Atlanta Legal Aid](https://atlantalegalaid.org/) – Free legal help for low-income individuals.

### 🛂 **Immigration & Work Permits**
- [USCIS Work Authorization](https://www.uscis.gov/working-in-the-united-states) – How to apply for a work permit.
- [RAICES](https://www.raicestexas.org/) – Help with immigration and asylum applications.

### 📞 **Emergency & Hotline Numbers**
- Immigration Help Hotline: **1-888-839-8682**
- Georgia Domestic Workers Hotline: **1-888-987-7011**
""")
