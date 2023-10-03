from Crypto.Cipher import Playfair
from Crypto.Random import get_random_bytes

def encrypt(plaintext, key):
    cipher = Playfair.new(key.encode(), Playfair.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext.encode())
    return ciphertext

def decrypt(ciphertext, key):
    cipher = Playfair.new(key.encode(), Playfair.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext).decode()
    return plaintext

# Example usage
key = "KEYWORD"
plaintext = "HELLO WORLD"

# Encrypt
ciphertext = encrypt(plaintext, key)
print("Encrypted:", ciphertext.hex())

# Decrypt
decrypted_text = decrypt(ciphertext, key)
print("Decrypted:", decrypted_text)
