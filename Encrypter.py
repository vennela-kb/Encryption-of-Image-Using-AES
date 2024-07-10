# Encrypter.py
import pickle
from AESCipher import AESCipher

def encrypt(data, key):
    cipher = AESCipher(key)
    return cipher.encrypt(pickle.dumps(data))
