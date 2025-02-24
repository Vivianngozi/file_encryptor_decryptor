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

4. How to Run the Script<br>
- Install Required Library <br>
a. The script uses the cryptography library.
b. Open your terminal or command prompt and run:<br>
<b>$ pip install cryptography</b>
- Save the Script </br>
a. Open your preferred code editor (VS Code, PyCharm, etc.). </br>
b. Copy and paste the script into a new file named:</br>
<b>file_encryptor.py</b> </br>
c. Save the file in your desired directory. </br>
- Run the Script </br>
a. Open Terminal or Command Prompt. </br>
b. Navigate to the directory where you saved file_encryptor.py: </br>
<b>$ cd /path/to/your/script/ <b> </br>
c. Run the script using Python:
<b>$ python3 file_encryptor.py </b> </br>
- Using the Tool </br>
Once the script is running, you'll see the menu:

File Encryption/Decryption Tool
--------------------------------
1. Generate Secret Key  
2. Encrypt a File  
3. Decrypt a File  
Select an option (1/2/3):
</br>
1. Generate Secret Key: This creates a secret.key file, used for encryption and decryption.
Important: Keep this key safe — without it, you can’t decrypt your files. </br>
2. Encrypt a File: Enter the path to the file you want to encrypt.
Specify the output file name (e.g., encrypted_file.enc).
The file will be encrypted and saved as the new file. <br>
3. Decrypt a File: Enter the path of the encrypted file (e.g., encrypted_file.enc).
Specify an output file (e.g., decrypted_file.txt). <br>

The script will decrypt and save the content to the new file.</br>
<h3>💡 Example Usage </h3>
- Encrypting a File </br>
a. Original file: notes.txt </br>
b. After encryption: notes_encrypted.enc</br>
- Decrypting a File</br>
a. Encrypted file: notes_encrypted.enc </br>
b. After decryption: notes_decrypted.txt (matches the original content)
