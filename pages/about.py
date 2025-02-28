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


st.set_page_config(page_title="About Us", page_icon="📢")

# Hide sidebar completely
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

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
    if st.button("⚖️ Legal & Immigration Help"):
        st.switch_page("pages/legal.py")

st.markdown('</div>', unsafe_allow_html=True)

st.title("📢 About Us")

st.write("""
The **Hispanic Career & Education Hub** is dedicated to empowering Hispanic immigrants in Atlanta by providing free access to career resources, job training, educational opportunities, and legal assistance.
""")
