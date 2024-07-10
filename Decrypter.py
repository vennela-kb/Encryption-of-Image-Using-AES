# Decrypter.py
import pickle
from AESCipher import AESCipher

def decrypt(encrypted_data, key):
    cipher = AESCipher(key)
    return pickle.loads(cipher.decrypt(encrypted_data))
