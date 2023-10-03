from pycipher import Caesar as Substitution
plaintext = "Instrument"     
print("Plain text:",plaintext)
shift=int(input("Enter key:"))
cipher = Substitution(shift)
encrypted_text = cipher.encipher(plaintext)
print("Encrypted:", encrypted_text)

decrypted_text = cipher.decipher(encrypted_text)
print("Decrypted:",decrypted_text)
