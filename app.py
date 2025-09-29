import streamlit as st
import PyPDF2
import io
import firebase_admin
from firebase_admin import credentials, auth, firestore

# --- Firebase Initialization ---
def init_firebase():
    """Initializes the Firebase app, checking if it's already initialized."""
    try:
        # Check if the app is already initialized
        firebase_admin.get_app()
    except ValueError:
        # If not initialized, initialize it
        try:
            cred = credentials.Certificate("firebase_credentials.json")
            firebase_admin.initialize_app(cred)
        except FileNotFoundError:
            st.error("El archivo de credenciales de Firebase (firebase_credentials.json) no se encontró.")
            st.stop()

init_firebase()

# --- Session State Management ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_info' not in st.session_state:
    st.session_state.user_info = None

# --- Authentication Functions ---
def signup(email, password, display_name):
    """Signs up a new user."""
    try:
        user = auth.create_user(
            email=email,
            password=password,
            display_name=display_name
        )
        st.success("¡Cuenta creada exitosamente! Por favor, inicia sesión.")
        return True
    except Exception as e:
        st.error(f"Error al crear la cuenta: {e}")
        return False

def login(email, password):
    """Logs in an existing user."""
    try:
        # This is a workaround for the absence of a direct sign-in method in the Admin SDK
        user = auth.get_user_by_email(email)
        # In a real app, you'd verify the password here, often by calling a custom cloud function
        # or by using the client-side SDK to sign in and then passing the ID token to the backend.
        # For this example, we'll assume if the user exists, the login is successful.
        # A more secure approach is highly recommended for production.
        st.session_state.logged_in = True
        st.session_state.user_info = {
            "uid": user.uid,
            "email": user.email,
            "display_name": user.display_name
        }
        st.rerun()
    except Exception as e:
        st.error(f"Error al iniciar sesión: {e}")

def logout():
    """Logs out the current user."""
    st.session_state.logged_in = False
    st.session_state.user_info = None
    st.rerun()

# --- Main App for Logged-in Users ---
def main_app():
    """The main application shown to logged-in users."""
    st.sidebar.write(f"Bienvenido, {st.session_state.user_info['display_name']}!")
    if st.sidebar.button("Cerrar Sesión"):
        logout()

    st.title("Extractor de Texto de PDF")

    uploaded_file = st.file_uploader("Sube un archivo PDF", type="pdf")

    if uploaded_file is not None:
        st.write("Archivo subido exitosamente.")
        
        try:
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            
            st.text_area("Texto extraído", text, height=300)
            
            # Create a text file in memory
            text_file = io.StringIO(text)
            
            # Provide a download button
            st.download_button(
                label="Descargar texto como .txt",
                data=text_file.getvalue(),
                file_name="texto_extraido.txt",
                mime="text/plain"
            )
            
        except Exception as e:
            st.error(f"Error al procesar el archivo: {e}")

# --- UI for Login/Signup ---
if not st.session_state.logged_in:
    st.sidebar.title("Autenticación")
    choice = st.sidebar.radio("Navegación", ["Iniciar Sesión", "Registrarse"])

    if choice == "Iniciar Sesión":
        st.header("Iniciar Sesión")
        with st.form("login_form"):
            email = st.text_input("Email")
            password = st.text_input("Contraseña", type="password")
            submit = st.form_submit_button("Iniciar Sesión")
            if submit:
                login(email, password)

    elif choice == "Registrarse":
        st.header("Crear una Cuenta")
        with st.form("signup_form"):
            display_name = st.text_input("Nombre")
            email = st.text_input("Email")
            password = st.text_input("Contraseña", type="password")
            submit = st.form_submit_button("Registrarse")
            if submit:
                signup(email, password, display_name)
else:
    main_app()