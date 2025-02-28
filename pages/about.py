import streamlit as st

st.set_page_config(page_title="About Us", page_icon="📢")

# Go to Home Page button
if st.button("🏠 Go to Home Page"):
    st.switch_page("app.py")

st.title("📢 About Us")

st.write("""
The **Hispanic Career & Education Hub** is dedicated to empowering Hispanic immigrants in Atlanta by providing free access to career resources, job training, educational opportunities, and legal assistance. 

We understand that navigating a new country can be challenging, and our goal is to bridge the gap by offering **bilingual support** and **easy-to-access information** that helps individuals build stable and successful futures.

### 🌍 **Our Mission**
Our mission is to support Hispanic immigrants in Atlanta by:
- Connecting them to **job opportunities** and **resume-building resources**.
- Providing access to **English learning programs** and **GED certifications**.
- Offering guidance on **legal aid**, **immigration services**, and **worker rights**.
- Ensuring that **language barriers** do not limit access to opportunities.

### 🤝 **Get Involved**
If you know someone who could benefit from these resources, please **share this platform with them**! 
""")
