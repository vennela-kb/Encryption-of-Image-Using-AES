from Crypto.Cipher import AES
import base64
import hashlib

class AESCipher:
    def __init__(self, key):
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = AES.new(self.key, AES.MODE_CBC).iv
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[16:]))

    def _pad(self, s):
        block_size = AES.block_size
        padding = block_size - len(s) % block_size
        return s + bytes([padding] * padding)

    @staticmethod
    def _unpad(s):
        return s[:-s[-1]]
