# fernet module is imported from the crptography package

from cryptography.fernet import Fernet

# key is generated

k= Fernet.generate_key()

# value of the key is saved to the variable

f = Fernet(k)

# the plaintext is converted to ciphertext

token = f.encrypt(b"Python is run away programming language for hackers")

# display the ciphertext

print(token)

# decrypting the ciphertext

d= f.decrypt(token)

# display the plaintext and the decode() method 
# converts it from byte to the string

print(d.decode())