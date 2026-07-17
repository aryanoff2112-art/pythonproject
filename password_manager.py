import os
import base64
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes


PASSWORD_FILE = "passwords.txt"
SALT_FILE = "salt.key"

def load_salt():
    if not os.path.exists(SALT_FILE):
        salt = os.urandom(16)
        with open(SALT_FILE, "wb") as f:
            f.write(salt)
    else:
        with open(SALT_FILE, "rb") as f:
            salt = f.read()

    return salt

def generate_key(master_password):
    salt = load_salt()

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )

    key = base64.urlsafe_b64encode(
        kdf.derive(master_password.encode())
    )

    return Fernet(key)

master_password = input("Enter Master Password: ")

fer = generate_key(master_password)

def add():
    website = input("Website: ").strip()
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    encrypted_password = fer.encrypt(password.encode()).decode()

    with open(PASSWORD_FILE, "a") as f:
        f.write(f"{website}|{username}|{encrypted_password}\n")

    print("\nPassword stored successfully!\n")

def view():

    if not os.path.exists(PASSWORD_FILE):
        print("\nNo passwords stored yet.\n")
        return
    try:
        with open(PASSWORD_FILE, "r") as f:

            found = False

            for line in f:

                line = line.strip()

                if not line:
                    continue

                parts = line.split("|")

                if len(parts) != 3:
                    continue

                website, username, encrypted = parts

                try:
                    password = fer.decrypt(encrypted.encode()).decode()

                    print("-" * 45)
                    print(f"Website : {website}")
                    print(f"Username: {username}")
                    print(f"Password: {password}")

                    found = True

                except InvalidToken:
                    print("\nWrong Master Password!")
                    return

            if found:
                print("-" * 45)
            else:
                print("No passwords found.")

    except Exception as e:
        print("Error:", e)

while True:

    print("\nPASSWORD MANAGER")
    print("1. Store New Password")
    print("2. View Passwords")
    print("Q. Quit")

    choice = input("\nChoose an option: ").lower().strip()

    if choice == "1":
        add()

    elif choice == "2":
        view()

    elif choice == "q":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")