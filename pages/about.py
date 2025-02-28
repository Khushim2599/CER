import streamlit as st

# Add a button at the top to go back to Home Page
if st.button("🏠 Go to Home Page"):
    st.switch_page("app.py")

st.set_page_config(page_title="About Us", page_icon="📢")

st.title("📢 About Us")
st.write("Our mission is to support Hispanic immigrants in Atlanta by providing job training, education, and legal resources.")

st.subheader("Our Mission")
st.write("To empower individuals with the tools needed for success in the workforce and education.")

