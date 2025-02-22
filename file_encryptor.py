from cryptography.fernet import Fernet
import os

def generate_key():
    """Generates and saves a key to 'secret.key'."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("[+] Secret key generated and saved as 'secret.key'")

def load_key():
    """Loads the secret key from 'secret.key'."""
    if not os.path.exists("secret.key"):
        print("[-] No key found. Generating a new key.")
        generate_key()
    with open("secret.key", "rb") as key_file:
        return key_file.read()

def encrypt_file(input_file, output_file, key):
    """Encrypts the input_file and saves it as output_file."""
    fernet = Fernet(key)
    try:
        with open(input_file, "rb") as file:
            original = file.read()
        encrypted = fernet.encrypt(original)
        with open(output_file, "wb") as file:
            file.write(encrypted)
        print(f"[+] File '{input_file}' encrypted and saved as '{output_file}'")
    except Exception as e:
        print(f"[-] Error encrypting file: {e}")

def decrypt_file(input_file, output_file, key):
    """Decrypts the input_file and saves it as output_file."""
    fernet = Fernet(key)
    try:
        with open(input_file, "rb") as file:
            encrypted = file.read()
        decrypted = fernet.decrypt(encrypted)
        with open(output_file, "wb") as file:
            file.write(decrypted)
        print(f"[+] File '{input_file}' decrypted and saved as '{output_file}'")
    except Exception as e:
        print(f"[-] Error decrypting file: {e}")

def main():
    print("\nFile Encryption/Decryption Tool\n--------------------------------")
    print("1. Generate Secret Key")
    print("2. Encrypt a File")
    print("3. Decrypt a File")
    choice = input("\nSelect an option (1/2/3): ").strip()

    if choice == "1":
        generate_key()
    elif choice in ["2", "3"]:
        key = load_key()
        input_file = input("Enter the path of the file: ").strip()
        output_file = input("Enter the output file name: ").strip()
        if choice == "2":
            encrypt_file(input_file, output_file, key)
        else:
            decrypt_file(input_file, output_file, key)
    else:
        print("[-] Invalid choice. Exiting.")

if __name__ == "__main__":
    main()

