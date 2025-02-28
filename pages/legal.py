import streamlit as st

st.set_page_config(page_title="Legal & Immigration Help", page_icon="⚖️")

# Redirect users to login page if not logged in
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.switch_page("pages/profile.py")

# Go to Home Page button
if st.button("🏠 Go to Home Page"):
    st.switch_page("app.py")

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
