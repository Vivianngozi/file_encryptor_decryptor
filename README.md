<h3>Python program that encrypt and decrypt text files using a secret key with the cryptography library, including options to save the output as a new file.</h3>

<h3>Code explaination:</h3>
1. Key Generation & Management</br>
- generate_key(): Creates a strong encryption key using the cryptography library and saves it to a file named secret.key. </br>
- load_key(): Loads the key from secret.key. If it doesn't exist, it auto-generates a new one.
2. Encryption Process<br>
  -encrypt_file(): <br>
    a. Reads the content of the file you want to encrypt. <br>
    b. Uses Fernet (from cryptography) to encrypt the data.<br>
    c. Saves the encrypted content as a new file.
  
3. Decryption Process <br>
- decrypt_file():<br>
a. Reads the encrypted file.<br>
b. Decrypts it using the same secret.key.<br>
c. Saves the decrypted content into a new file.
4. User Interaction <br>
- When you run the script, it gives you three options:<br>
a. Generate Secret Key – To create a new encryption key.<br>
b. Encrypt a File – Encrypt any file of your choice.<br>
c. Decrypt a File – Decrypt an encrypted file using the key.
5. Error Handling <br>
- Handles cases like: <br>
a. Missing files.<br>
b. Incorrect keys (for decryption).<br>
c. Invalid menu options.
