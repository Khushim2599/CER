import streamlit as st

st.set_page_config(page_title="Login", page_icon="👤")

# Initialize session state for authentication
if "users" not in st.session_state:
    st.session_state["users"] = {}  # Stores usernames & passwords
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "current_user" not in st.session_state:
    st.session_state["current_user"] = ""

# Function for user authentication
def authenticate(username, password):
    return st.session_state["users"].get(username) == password

st.title("👤 User Login / Sign Up")

# Tabs for Sign-up & Login
tab1, tab2 = st.tabs(["Sign Up", "Login"])

# Sign-up Section
with tab1:
    st.subheader("Create an Account")
    new_username = st.text_input("Choose a username:")
    new_password = st.text_input("Choose a password:", type="password")
    
    if st.button("Sign Up"):
        if new_username and new_password:
            if new_username in st.session_state["users"]:
                st.warning("Username already exists! Try a different one.")
            else:
                st.session_state["users"][new_username] = new_password
                st.success("Account created successfully! You can now log in.")
        else:
            st.warning("Please fill in both fields.")

# Login Section
with tab2:
    st.subheader("Log In")
    username = st.text_input("Username:", key="login_username")
    password = st.text_input("Password:", type="password", key="login_password")
    
    if st.button("Log In"):
        if authenticate(username, password):
            st.session_state["logged_in"] = True
            st.session_state["current_user"] = username
            st.success(f"Welcome back, {username}!")
            st.switch_page("app.py")  # Redirect to home page
        else:
            st.error("Invalid username or password!")
