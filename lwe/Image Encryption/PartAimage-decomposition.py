import pywt
import numpy as np
import cv2

# Read the image
image = cv2.imread("dsu.png", cv2.IMREAD_GRAYSCALE)

# Check if the image was successfully loaded
if image is None:
    print("Error: Unable to load image.")
else:
    # Perform multilevel 2D DWT
    coeffs_multilevel = pywt.wavedec2(image, 'db1', level=2)

    # Reconstruction example
    reconstructed_image_multilevel = pywt.waverec2(coeffs_multilevel, 'db1')
    reconstructed_image_multilevel_uint8 = (255 * (reconstructed_image_multilevel - np.min(reconstructed_image_multilevel)) / 
                                            (np.max(reconstructed_image_multilevel) - np.min(reconstructed_image_multilevel)))
    cv2.imwrite("decomposed_DSULogo_multilevel.jpg", np.uint8(reconstructed_image_multilevel_uint8))
