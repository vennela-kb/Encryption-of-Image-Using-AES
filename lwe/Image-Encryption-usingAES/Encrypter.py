# Import the base64 module for encoding and decoding binary data
import base64

# Import the hashlib module for secure hash and message digest algorithms
import hashlib

# Import the AESCipher class from the AESCipher module
from AESCipher import AESCipher

# Import the Image class from the PIL (Python Imaging Library) module
from PIL import Image

# Import the randint function from the random module for generating random integers
from random import randint

# Define a class called Encrypter for encrypting text and images
class Encrypter:
    def __init__(self, text, key):
        self.text = text
        self.key = key

    # Method to encrypt an image using AES encryption
    def encrypt_image(self):
        # Create an instance of AESCipher with the provided key
        aes = AESCipher(self.key)
        
        # Encrypt the text using AES encryption
        cipher = aes.encrypt(self.text)
        
        # Uncomment the following line if decryption is required
        # message = aes.decrypt(cipher)
        
        # Return the encrypted text
        return cipher
