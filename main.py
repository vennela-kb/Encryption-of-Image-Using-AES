import numpy as np
import pywt
import pickle
import cv2
from Encrypter import encrypt
from Decrypter import decrypt

# png image upload
image_path = 'dsu.png'  # Path to your uploaded image
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# upload correct one
if image is None:
    raise ValueError("Image not loaded. Please check the path.")

#  DWT execute
coeffs = pywt.dwt2(image, 'haar')
cA, (cH, cV, cD) = coeffs

# Main image coeff
print("Original Coefficients:")
print("cA shape:", cA.shape)
print("cH shape:", cH.shape)
print("cV shape:", cV.shape)
print("cD shape:", cD.shape)

# Encrypting cH
key = 'password'  # key
cH_encrypted = encrypt(cH, key)

# Store the encrypted value as a string in a text file named cipher.txt
with open('cipher.txt', 'w') as file:
    file.write(str(cH_encrypted))

print(f"Encrypted value has been written to cipher.txt")

# Decrypting cH
cH_decrypted = decrypt(cH_encrypted, key)

#  DWT with decrypted cH executing
coeffs_decrypted = cA, (cH_decrypted, cV, cD)
image_reconstructed = pywt.idwt2(coeffs_decrypted, 'haar')

# Adjust values to stay within the acceptable range
image_reconstructed = np.clip(image_reconstructed, 0, 255).astype(np.uint8)

# reconstructed image
reconstructed_image_path = 'reconstructed_image.png'
cv2.imwrite(reconstructed_image_path, image_reconstructed)

# output
print("\ncH (Encrypted):stored in cipher.txt")

print("\nOriginal Image Shape:", image.shape)
print("Reconstructed Image Shape:", image_reconstructed.shape)
print("\ncH (Original):")
print(cH)
print("\ncH (Decrypted):")
print(cH_decrypted)
