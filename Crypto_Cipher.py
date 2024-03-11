from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import random

def generate_random_key():
    key = get_random_bytes(16)  # для AES-128
    key = tuple(random.sample(key, len(key)))  # перемішуємо значення ключа
    return key

def encrypt(plain_text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    cipher_text = cipher.encrypt(pad(plain_text.encode('utf-8'), AES.block_size))
    return cipher.iv + cipher_text

def decrypt(cipher_text, key):
    iv = cipher_text[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(cipher_text[AES.block_size:]), AES.block_size)
    return decrypted_text.decode('utf-8')

# Приклад використання
key = generate_random_key()
text_to_encrypt = "Hello, AES!"
cipher_text = encrypt(text_to_encrypt, key)
decrypted_text = decrypt(cipher_text, key)

print("Original Text:", text_to_encrypt)
print("Encrypted Text:", cipher_text)
print("Decrypted Text:", decrypted_text)
