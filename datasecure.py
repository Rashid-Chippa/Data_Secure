# import streamlit as st
# import hashlib
# import json
# import os
# import time
# from cryptography.fernet import Fernet
# from base64 import urlsafe_b64encode
# from hashlib import pbkdf2_hmac

# # === data information of user ===
# DATA_FILE ="secure_data.joson"
# SALT = b"secure_salt_value"
# LOCKOUT_DURATION = 60

# # === section login details ===
# if "authenticated_user" not in st.session_state:
#     st.session_state.authenticated_user = None
    
# if "failed_attempts" not in st.session_state:
#     st.session_state.failed_attempts = 0
    
# if "locked_time" not in st.session_state:
#     st.session_state.locked_time = 0
    
# # === if data is load ===
# def load_data():
#     if os.path.exists(DATA_FILE):
#         with open(DATA_FILE< "r") as f:
#             return json.load(f)
#     return{}

# def save_data(data):
#     with open(DATA_FILE, "w") as f:
#         json.dump(data ,f)
        
# def generate_key(passkey):
#     key = pbkdf2_hmac('sha256', passkey.encode(), SALT, 100000)
#     return urlsafe_b64encode(key)

# def hash_password(password):
#     return hashlib.pbkdf2_hmac('sha256', password.encode(), SALT, 100000).hex()

# # ===cryptography.fernet used ===

# def encrypt_text(text, key):
#     cipher = Fernet(generate_key(key))
#     return cipher.encrypt(text.encode()).decode()

# def decrypt_text(encrypt_text, key):
#     try:
#         cipher = Fernet(generate_key(key))
#         return cipher.decrypt(encrypt_text.encode()).decode()
#     except:
#         return None
    
# store_data = load_data()

# #=== navigation bar ===
# st.title("🔒 Secure Data Encryption System")
# menu = [ "Home", "Login", "Register", "Store Data", "Retrieve Data"]
# choice = st.sidebar.selectbox("Navigation", menu)
# if choice == "Home":
#     st.subheader("Welcome to the 🔒 Secure Data Encryption System. Please login or register to access the system.")   
#     st.markdown("Develop a Streamlit-based secure data storage and retrieval system where: Users store data with a unique passkey.Users decrypt data by providing the correct passkey.Multiple failed attempts result in a forced reauthorization (login page).The system operates entirely in memory without external databases.")

# # === user registration ===
# elif choice == "Register":
#     st.subheader("✏️ Register New User")
#     new_username = st.text_input("Enter a new username:")
#     new_password = st.text_input("Enter a new password:", type="password")
   
#     if st.button("Register"):
#         if new_username and new_password:
#             if new_username in store_data:
#                 st.warning("⚠️ Use Already Exists")
#             else:
#                 store_data[new_username] = {"password": hash_password(new_password), "data": {}}
#                 "data" []
#                 save_data(store_data)
#                 st.success("✔️ Registration successfully")
#         else:
#             st.error("Username already exists. Please choose a different username & password.")
    
#     elif choice == "Login":
#         st.subheader("🔐 User Login")
#         if time.time() <st.session_state.locked_time:
#             remaining = int(st.session_state.locked_time - time.time())
#             st.error(f"⚠️ To many failed attempts. Please wait {remaining} seconds before trying again.")
#             st.stop()
            
#         new_username = st.text_input("Enter your username:")
#         new_password = st.text_input("Enter your password:", type="password")
#         if st.button("Login"):
#             if new_username and new_password:
#                 if new_username in store_data and store_data[new_username]["password"] == hash_password(new_password):
#                     st.session_state.authenticated_user = new_username
#                     st.session_state.failed_attempts = 0
#                     st.success(f"✔️ Login successfully Welcome {new_username}")
#                 else:
#                     st.session_state.failed_attempts += 1
#                     remaining = 3 - st.session_state.failed_attempts 
#                     st.error(f"⚠️ Invalid username or password. '❌Please try again. Attempts remaining: {remaining}")    
                        
#                     if  st.session_state.failed_attempts >= 3:
#                         st.session_state.locked_time = time.time() + LOCKOUT_DURATION
#                     st.error("🛑 To many failed attempts. 🔏Locked down for 60 seconds.")
#                     st.stop()

# # === data store section ===
# elif choice == "Store Data":
#     if  not st.session_state.authenticated_user :
#         st.warning("🔐please log in first")
#     else :
#         st.subheader("📦 Store Encrypted Data")
#         data = st.text_area("Enter data to encrypt:")
#         passkey = st.text_input("Enter passkey for encryption:", type="password")
        
#         if st.button("Store Encrypted Data"):
#             if data and passkey:
#                 encrypted_data = encrypt_text(data, passkey)
#                 store_data[st.session_state.authenticated_user]["data"].append(encrypted_data)
#                 save_data(store_data)
#                 st.success("✔️ Data stored successfully")
#             else:
#                 st.error("⚠️ Please enter data and passkey for encryption.")
# # === Data retrieve Data Section ===
# elif choice == "Retrieve data":
#     if not st.session_state.authenticated_user:
#         st.warning("🔐 Please log in first.")
#     else:
#         st.subheader("🔍 Retrieve Encrypted Data")
#         user_data = store_data. get(st.session_state.authenticated_user, {}).get("data", [])
#         if not user_data:
#             st.info("No data found for the user.")
#         else:
#             st.write("Encrypted Data Entries:")
#             for i, item in enumerate(user_data): 
#                  st.code(item,language="text")
                 
#             encrypted_input = st.text_area("Enter the encrypted text")
#             passkey = st.text_input("Enter passkey for decryption:", type="password")
#             if st.button("Decrypt Data"):
#                 result = decrypt_text(encrypted_input, passkey)
#                 if result :
#                     st.success(f"✔️ Decrypted Data: {result}")
#                 else:
#                     st.error("❌ Invalid passkey or encrypted text.")    


import streamlit as st
import hashlib
import json
import os
import time
from cryptography.fernet import Fernet
from base64 import urlsafe_b64encode
from hashlib import pbkdf2_hmac

# === data information of user ===
DATA_FILE = "secure_data.json"  # Fixed typo
SALT = b"secure_salt_value"
LOCKOUT_DURATION = 60

# === section login details ===
if "authenticated_user" not in st.session_state:
    st.session_state.authenticated_user = None
    
if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0
    
if "locked_time" not in st.session_state:
    st.session_state.locked_time = 0
    
# === if data is load ===
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:  # Fixed typo
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)
        
def generate_key(passkey):
    key = pbkdf2_hmac('sha256', passkey.encode(), SALT, 100000)
    return urlsafe_b64encode(key)

def hash_password(password):
    return hashlib.pbkdf2_hmac('sha256', password.encode(), SALT, 100000).hex()

# ===cryptography.fernet used ===
def encrypt_text(text, key):
    cipher = Fernet(generate_key(key))
    return cipher.encrypt(text.encode()).decode()

def decrypt_text(encrypt_text, key):
    try:
        cipher = Fernet(generate_key(key))
        return cipher.decrypt(encrypt_text.encode()).decode()
    except:
        return None
    
store_data = load_data()

#=== navigation bar ===
st.title("🔒 Secure Data Encryption System")
menu = ["Home", "Login", "Register", "Store Data", "Retrieve Data"]  # Fixed typo
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.subheader("Welcome to the 🔒 Secure Data Encryption System. Please login or register to access the system.")   
    st.markdown("Develop a Streamlit-based secure data storage and retrieval system where: Users store data with a unique passkey.Users decrypt data by providing the correct passkey.Multiple failed attempts result in a forced reauthorization (login page).The system operates entirely in memory without external databases.")

# === user registration ===
elif choice == "Register":
    st.subheader("✏️ Register New User")
    new_username = st.text_input("Enter a new username:")
    new_password = st.text_input("Enter a new password:", type="password")
   
    if st.button("Register"):
        if new_username and new_password:
            if new_username in store_data:
                st.warning("⚠️ User Already Exists")
            else:
                store_data[new_username] = {
                    "password": hash_password(new_password), 
                    "data": []  # Changed to list to match your usage
                }
                save_data(store_data)
                st.success("✔️ Registration successful")
        else:
            st.error("Please enter both username and password.")

elif choice == "Login":  # Changed from elif to if
    st.subheader("🔐 User Login")
    if time.time() < st.session_state.locked_time:
        remaining = int(st.session_state.locked_time - time.time())
        st.error(f"⚠️ Too many failed attempts. Please wait {remaining} seconds before trying again.")
        st.stop()
            
    username = st.text_input("Enter your username:")  # Changed variable name
    password = st.text_input("Enter your password:", type="password")
    
    if st.button("Login"):
        if username and password:
            if username in store_data and store_data[username]["password"] == hash_password(password):
                st.session_state.authenticated_user = username
                st.session_state.failed_attempts = 0
                st.success(f"✔️ Login successful. Welcome {username}")
            else:
                st.session_state.failed_attempts += 1
                remaining = 3 - st.session_state.failed_attempts 
                st.error(f"⚠️ Invalid username or password. Please try again. Attempts remaining: {remaining}")    
                    
                if st.session_state.failed_attempts >= 3:
                    st.session_state.locked_time = time.time() + LOCKOUT_DURATION
                    st.error("🛑 Too many failed attempts. 🔏Locked down for 60 seconds.")
        else:
            st.error("Please enter both username and password.")

# === data store section ===
elif choice == "Store Data":
    if not st.session_state.authenticated_user:
        st.warning("🔐 Please log in first")
    else:
        st.subheader("📦 Store Encrypted Data")
        data = st.text_area("Enter data to encrypt:")
        passkey = st.text_input("Enter passkey for encryption:", type="password")
        
        if st.button("Store Encrypted Data"):
            if data and passkey:
                encrypted_data = encrypt_text(data, passkey)
                if "data" not in store_data[st.session_state.authenticated_user]:
                    store_data[st.session_state.authenticated_user]["data"] = []
                store_data[st.session_state.authenticated_user]["data"].append(encrypted_data)
                save_data(store_data)
                st.success("✔️ Data stored successfully")
            else:
                st.error("⚠️ Please enter data and passkey for encryption.")

# === Data retrieve Data Section ===
elif choice == "Retrieve Data":
    if not st.session_state.authenticated_user:
        st.warning("🔐 Please log in first.")
    else:
        st.subheader("🔍 Retrieve Encrypted Data")
        user_data = store_data.get(st.session_state.authenticated_user, {}).get("data", [])
        if not user_data:
            st.info("No data found for the user.")
        else:
            st.write("Encrypted Data Entries:")
            for i, item in enumerate(user_data): 
                st.code(item, language="text")
                 
            encrypted_input = st.text_area("Enter the encrypted text")
            passkey = st.text_input("Enter passkey for decryption:", type="password")
            if st.button("Decrypt Data"):
                if encrypted_input and passkey:
                    result = decrypt_text(encrypted_input, passkey)
                    if result:
                        st.success(f"✔️ Decrypted Data: {result}")
                    else:
                        st.error("❌ Invalid passkey or encrypted text.")
                else:
                    st.error("Please enter both encrypted text and passkey")
                    