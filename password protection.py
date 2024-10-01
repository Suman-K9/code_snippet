from cryptography.fernet import Fernet
import base64

def encrypt_file(file_path, password):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher_suite.encrypt(file_data)
    with open(file_path + '.encrypted', 'wb') as file:
        file.write(encrypted_data)

    # Store the key securely, e.g. in an environment variable or a secure storage
    encrypted_key = base64.b64encode(key)
    with open('key.txt', 'wb') as file:
        file.write(encrypted_key)

encrypt_file('your_python_file.py', 'your_password')
