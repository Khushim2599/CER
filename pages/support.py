import streamlit as st

st.set_page_config(page_title="Support Your Community", page_icon="🤝")

# Redirect users to login page if not logged in
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.switch_page("pages/profile.py")

# Language Toggle
if "language" not in st.session_state:
    st.session_state["language"] = "English"

# Hide sidebar
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

# Page Title
st.title("🤝 Support Your Community" if st.session_state["language"] == "English" else "🤝 Apoya a tu comunidad")

st.write("Discover and support small Hispanic-owned businesses in your area!" if st.session_state["language"] == "English" else
         "¡Descubre y apoya a pequeñas empresas hispanas en tu comunidad!")

# Business Categories
st.header("🍽️ Food & Restaurants" if st.session_state["language"] == "English" else "🍽️ Comida y Restaurantes")
st.markdown("""
- [Tacos El Gordo](https://example.com) 🌮
- [Cuban Delights Bakery](https://example.com) 🥖
- [Peruvian Taste](https://example.com) 🍗
""")

st.header("🛍️ Retail & Shopping" if st.session_state["language"] == "English" else "🛍️ Tiendas y Compras")
st.markdown("""
- [Hispanic Handcrafts](https://example.com) 🏺
- [Latina Fashion Store](https://example.com) 👗
""")

st.header("💇‍♀️ Beauty & Salon" if st.session_state["language"] == "English" else "💇‍♀️ Belleza y Salón")
st.markdown("""
- [Maria's Beauty Salon](https://example.com) 💄
- [Barbería El Rey](https://example.com) ✂️
""")

st.header("🛠️ Services & Others" if st.session_state["language"] == "English" else "🛠️ Servicios y Otros")
st.markdown("""
- [Hispanic Auto Repair](https://example.com) 🚗
- [Legal Aid for Immigrants](https://example.com) ⚖️
""")
