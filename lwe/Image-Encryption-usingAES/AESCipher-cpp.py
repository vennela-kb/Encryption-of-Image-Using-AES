import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class AESCipher:
    def __init__(self, key):
        self.key = hashlib.sha256(key.encode()).digest()
        self.bs = AES.block_size

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = get_random_bytes(self.bs)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:self.bs]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[self.bs:]))

    def _pad(self, s):
        padding = self.bs - len(s) % self.bs
        return s + padding * chr(padding).encode()

    @staticmethod
    def _unpad(s):
        return s[:-s[-1]]
