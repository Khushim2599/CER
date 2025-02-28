import streamlit as st
import json
import os

st.set_page_config(page_title="Login", page_icon="👤")

# Hide sidebar completely
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        .welcome-text {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            font-family: 'Georgia', serif;
            color: #333;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# ✅ Language Toggle at the Top of the Page
if "language" not in st.session_state:
    st.session_state["language"] = "English"

toggle_col1, toggle_col2 = st.columns([0.8, 0.2])
with toggle_col2:
    language_toggle = st.toggle("English / Español", value=(st.session_state["language"] == "Español"))
    st.session_state["language"] = "Español" if language_toggle else "English"

# ✅ Welcome Message
st.markdown('<h1 class="welcome-text">Welcome to Avanza | Bienvenido a Avanza</h1>', unsafe_allow_html=True)

st.title("👤 User Login / Sign Up")

# File for storing user credentials
USER_DATA_FILE = "users.json"

# Load user data from file
def load_users():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as f:
            return json.load(f)
    return {}

# Save user data to file
def save_users(users):
    with open(USER_DATA_FILE, "w") as f:
        json.dump(users, f)

# Initialize session state variables
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "current_user" not in st.session_state:
    st.session_state["current_user"] = ""

users = load_users()  # Load existing users

# If already logged in, go to home page
if st.session_state["logged_in"]:
    st.switch_page("app.py")

# Tabs for Sign-up & Login
tab1, tab2 = st.tabs(["Sign Up" if st.session_state["language"] == "English" else "Regístrate",
                       "Login" if st.session_state["language"] == "English" else "Iniciar sesión"])

# ✅ Sign-up Section
with tab1:
    st.subheader("Create an Account" if st.session_state["language"] == "English" else "Crea una cuenta")
    new_username = st.text_input("Choose a username:" if st.session_state["language"] == "English" else "Elige un nombre de usuario:")
    new_password = st.text_input("Choose a password:" if st.session_state["language"] == "English" else "Elige una contraseña:", type="password")

    if st.button("Sign Up" if st.session_state["language"] == "English" else "Regístrate"):
        if new_username and new_password:
            if new_username in users:
                st.warning("Username already exists! Try a different one." if st.session_state["language"] == "English" else "¡El nombre de usuario ya existe! Prueba con otro.")
            else:
                users[new_username] = new_password
                save_users(users)  # Save to file
                st.success("Account created successfully! You can now log in." if st.session_state["language"] == "English" else "¡Cuenta creada con éxito! Ahora puedes iniciar sesión.")
        else:
            st.warning("Please fill in both fields." if st.session_state["language"] == "English" else "Por favor, completa ambos campos.")

# ✅ Login Section
with tab2:
    st.subheader("Log In" if st.session_state["language"] == "English" else "Iniciar sesión")
    username = st.text_input("Username:" if st.session_state["language"] == "English" else "Nombre de usuario:", key="login_username")
    password = st.text_input("Password:" if st.session_state["language"] == "English" else "Contraseña:", type="password", key="login_password")

    if st.button("Log In" if st.session_state["language"] == "English" else "Iniciar sesión"):
        if username in users and users[username] == password:
            st.session_state["logged_in"] = True
            st.session_state["current_user"] = username
            st.success(f"Welcome back, {username}!" if st.session_state["language"] == "English" else f"¡Bienvenido de nuevo, {username}!")
            st.switch_page("app.py")  # Redirect to home page
        else:
            st.error("Invalid username or password!" if st.session_state["language"] == "English" else "¡Usuario o contraseña inválidos!")
