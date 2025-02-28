import streamlit as st

# ✅ Ensure this is the first command
st.set_page_config(page_title="Support Your Community", page_icon="🤝")

# Redirect users to login page if not logged in
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.switch_page("pages/profile.py")

# ✅ Language Toggle (Switch-style button)
if "language" not in st.session_state:
    st.session_state["language"] = "English"

toggle_col1, toggle_col2 = st.columns([0.8, 0.2])
with toggle_col2:
    language_toggle = st.toggle("🌍 English / Español", value=(st.session_state["language"] == "Español"))
    st.session_state["language"] = "Español" if language_toggle else "English"

# ✅ Hide sidebar
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

# ✅ Navigation Bar
st.markdown('<div class="navbar">', unsafe_allow_html=True)
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("🏠 Home" if st.session_state["language"] == "English" else "🏠 Inicio"):
        st.switch_page("app.py")

with col2:
    if st.button("🔹 Job & Career Help" if st.session_state["language"] == "English" else "🔹 Ayuda para el empleo"):
        st.switch_page("pages/jobs.py")

with col3:
    if st.button("📚 Education Resources" if st.session_state["language"] == "English" else "📚 Recursos educativos"):
        st.switch_page("pages/education.py")

with col4:
    if st.button("📢 About Us" if st.session_state["language"] == "English" else "📢 Sobre Nosotros"):
        st.switch_page("pages/about.py")

with col5:
    if st.button("⚖️ Legal & Immigration Help" if st.session_state["language"] == "English" else "⚖️ Ayuda legal e inmigración"):
        st.switch_page("pages/legal.py")

st.markdown('</div>', unsafe_allow_html=True)

# ✅ Page Title
st.title("🤝 Support Your Community" if st.session_state["language"] == "English" else "🤝 Apoya a tu comunidad")

# ✅ Content with Dynamic Language Switching
st.write("""
Find and support Hispanic-owned businesses in your area.
""" if st.session_state["language"] == "English" else """
Encuentra y apoya a empresas hispanas en tu comunidad.
""")

st.header("🍽️ Food & Restaurants" if st.session_state["language"] == "English" else "🍽️ Comida y Restaurantes")
st.markdown("""
- [Tacos El Gordo](https://example.com) 🌮 – Authentic Mexican tacos.
- [Cuban Delights Bakery](https://example.com) 🥖 – Fresh Cuban pastries.
- [Peruvian Taste](https://example.com) 🍗 – Traditional Peruvian dishes.
""" if st.session_state["language"] == "English" else """
- [Tacos El Gordo](https://example.com) 🌮 – Auténticos tacos mexicanos.
- [Cuban Delights Bakery](https://example.com) 🥖 – Pasteles cubanos frescos.
- [Peruvian Taste](https://example.com) 🍗 – Platos tradicionales peruanos.
""")

st.header("🛍️ Retail & Shopping" if st.session_state["language"] == "English" else "🛍️ Tiendas y Compras")
st.markdown("""
- [Hispanic Handcrafts](https://example.com) 🏺 – Handmade Latin American crafts.
- [Latina Fashion Store](https://example.com) 👗 – Trendy Hispanic fashion.
""" if st.session_state["language"] == "English" else """
- [Artesanías Hispanas](https://example.com) 🏺 – Artesanías hechas a mano de América Latina.
- [Tienda de Moda Latina](https://example.com) 👗 – Moda hispana a la última tendencia.
""")

st.header("💇‍♀️ Beauty & Salon" if st.session_state["language"] == "English" else "💇‍♀️ Belleza y Salón")
st.markdown("""
- [Maria's Beauty Salon](https://example.com) 💄 – Latina-owned beauty salon.
- [Barbería El Rey](https://example.com) ✂️ – Traditional Hispanic barbershop.
""" if st.session_state["language"] == "English" else """
- [Salón de Belleza de María](https://example.com) 💄 – Salón de belleza de propiedad latina.
- [Barbería El Rey](https://example.com) ✂️ – Barbería hispana tradicional.
""")

st.header("🛠️ Services & Others" if st.session_state["language"] == "English" else "🛠️ Servicios y Otros")
st.markdown("""
- [Hispanic Auto Repair](https://example.com) 🚗 – Affordable car repair services.
- [Legal Aid for Immigrants](https://example.com) ⚖️ – Free legal consultations.
""" if st.session_state["language"] == "English" else """
- [Reparación de Autos Hispana](https://example.com) 🚗 – Servicios de reparación de autos asequibles.
- [Asistencia Legal para Inmigrantes](https://example.com) ⚖️ – Consultas legales gratuitas.
""")
