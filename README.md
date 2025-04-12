# 🔒 Secure Data Encryption System

A Streamlit-based application for securely storing and retrieving data using unique passkeys and symmetric encryption.

---

## 🌟 Features

- **Secure Storage**: Store data encrypted with a unique passkey
- **Encryption**: Uses Fernet (symmetric encryption) for robust security
- **Decryption**: Retrieve and decrypt data with the correct passkey
- **Failed Attempts Limit**: After three failed decryption attempts, reauthorization is required via a login page
- **Simple Login**: Reauthorize using a master password to reset failed attempts

---

## 🛠️ Installation and Setup

### Prerequisites

- Python 3.x
- Streamlit
- Cryptography library

### Installation

Install the required dependencies:

```bash
pip install streamlit cryptography
```

---

## 🚀 Usage

### Running the App

Start the Streamlit app with:

```bash
streamlit run app.py
```

### How to Use

1. **Home Tab**: Welcome message and overview
2. **Store Data Tab**:
   - Enter an identifier, text to encrypt, and a passkey
   - Click "Store" to encrypt and save the data
3. **Retrieve Data Tab**:
   - Enter the encrypted text and the passkey
   - Click "Retrieve" to decrypt and view the data
   - After three failed attempts, you'll be prompted to login
4. **Login Tab**:
   - Enter the master password (admin123 for demo) to reset failed attempts

---

## 📬 Contact and Credits

**Author**: [Hamza Sheikh](https://github.com/Hamza-Sheikh-02)

**Libraries Used**:

- [Streamlit](https://streamlit.io/)
- [Cryptography](https://cryptography.io/)
