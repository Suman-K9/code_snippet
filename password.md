```python
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



##### To run the file

from cryptography.fernet import Fernet
import base64

def decrypt_file(file_path, password):
    with open('key.txt', 'rb') as file:
        encrypted_key = file.read()
    key = base64.b64decode(encrypted_key)
    cipher_suite = Fernet(key)
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    with open(file_path[:-9], 'wb') as file:
        file.write(decrypted_data)

decrypt_file('your_python_file.py.encrypted', 'your_password')
exec(open('your_python_file.py').read())
```
