#Password encryption program
import base64
def encrypt_password(password):
    global encoded_bytes
    encoded_bytes=base64.b64encode(password.encode())
    print(encoded_bytes)
password=input("Enter the password: ")
encrypt_password(password)
def decrypt_password(encoded_bytes):
    decoded_bytes=base64.b64decode(encoded_bytes)
    decoded_bytes=decoded_bytes.decode()
    print(decoded_bytes)
decrypt_password(encoded_bytes)