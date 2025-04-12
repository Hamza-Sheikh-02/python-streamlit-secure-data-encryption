import hashlib

import streamlit as st
from cryptography.fernet import Fernet


# Initialize session state
if "ENCRYPTION_KEY" not in st.session_state:
    st.session_state["ENCRYPTION_KEY"] = Fernet.generate_key()
if "stored_data" not in st.session_state:
    st.session_state["stored_data"] = {}
if "failed_attempts" not in st.session_state:
    st.session_state["failed_attempts"] = 0


# Helper functions
def get_cipher_suite():
    """Return the Fernet cipher suite using the session's encryption key."""
    return Fernet(st.session_state["ENCRYPTION_KEY"])


def encrypt_text(input_text: str) -> str:
    """Encrypt the given text using Fernet encryption."""
    cipher_suite = get_cipher_suite()
    return cipher_suite.encrypt(input_text.encode()).decode()


def decrypt_text(encrypted_input: str) -> str:
    """Decrypt the given encrypted text using Fernet decryption."""
    cipher_suite = get_cipher_suite()
    return cipher_suite.decrypt(encrypted_input.encode()).decode()


def hash_passkey(input_passkey: str) -> str:
    """Hash the provided passkey using SHA-256."""
    return hashlib.sha256(input_passkey.encode()).hexdigest()


# Streamlit UI
st.set_page_config(
    page_title="Secure Data Encryption System",
    page_icon="🔒",
    layout="wide",
)

st.markdown(
    """
    <style>
    #MainMenu, footer {visibility: hidden;}
    .main-title {
        font-size: 36px;
        font-weight: bold;
        color: #2E86C1;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<h1 class="main-title">🔒 Secure Data Encryption System</h1>',
    unsafe_allow_html=True,
)

tab1, tab2, tab3, tab4 = st.tabs(
    ["Home", "Store Data", "Retrieve Data", "Login"])

with tab1:
    st.subheader("🏠 Welcome to the Secure Data System")
    st.write("Securely store and retrieve data with unique passkeys.")

with tab2:
    st.subheader("🔐 Store Data")
    identifier = st.text_input("Identifier", key="store_identifier")
    text = st.text_area("Text to encrypt", key="store_text")
    passkey = st.text_input("Passkey", type="password", key="store_passkey")
    if st.button("Store", key="store_button"):
        if identifier and text and passkey:
            encrypted_text = encrypt_text(text)
            hashed_passkey = hash_passkey(passkey)
            st.session_state["stored_data"][identifier] = {
                "encrypted_text": encrypted_text,
                "passkey": hashed_passkey,
            }
            st.success("Data stored successfully!")
            st.write("Encrypted text:")
            st.code(encrypted_text)
        else:
            st.error("Please fill in all fields.")

with tab3:
    st.write(f"Failed attempts: {st.session_state['failed_attempts']}")
    if st.session_state["failed_attempts"] < 3:
        st.subheader("🔓 Retrieve Data")
        encrypted_text = st.text_input(
            "Encrypted Text",
            key="retrieve_encrypted_text",
        )
        passkey = st.text_input(
            "Passkey",
            type="password",
            key="retrieve_passkey",
        )
        if st.button("Retrieve", key="retrieve_button"):
            if encrypted_text and passkey:
                hashed_passkey = hash_passkey(passkey)
                for data in st.session_state["stored_data"].values():
                    if (data["encrypted_text"] == encrypted_text and
                            data["passkey"] == hashed_passkey):
                        try:
                            decrypted_text = decrypt_text(encrypted_text)
                            st.success("Data retrieved successfully!")
                            st.write("Retrieved")
                            st.info(decrypted_text)
                            st.session_state["failed_attempts"] = 0
                            break
                        except Exception as e:
                            st.error(f"Decryption failed: {e}")
                            st.session_state["failed_attempts"] += 1
                else:
                    st.error("Invalid encrypted text or passkey.")
                    st.session_state["failed_attempts"] += 1
            else:
                st.error("Please provide encrypted text and passkey.")
    else:
        st.warning("Too many failed attempts. Please login to continue.")

with tab4:
    st.subheader("🔑 Login")
    master_password = st.text_input(
        "Master Password",
        type="password",
        key="login_password",
    )
    if st.button("Login", key="login_button"):
        if master_password == "admin123":
            st.session_state["failed_attempts"] = 0
            st.success("Login successful. You can now retrieve data.")
        else:
            st.error("Invalid master password.")
