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

    # Extract coefficients for the first level
    coeffs_single_level = pywt.dwt2(image, 'haar')
    cA, (cH, cV, cD) = coeffs_single_level

    # Output the approximation and detail coefficients for the first level
    print("Approximation Coefficients (Single Level):\n", cA)
    print("Horizontal Detail Coefficients (Single Level):\n", cH)
    print("Vertical Detail Coefficients (Single Level):\n", cV)
    print("Diagonal Detail Coefficients (Single Level):\n", cD)

    # Reconstruct the original data from the multilevel DWT coefficients
    reconstructed_image_multilevel = pywt.waverec2(coeffs_multilevel, 'db1')

    # Convert reconstructed image to uint8 (8-bit) for saving
    reconstructed_image_multilevel_uint8 = np.uint8(reconstructed_image_multilevel)

    # Save the reconstructed image
    cv2.imwrite("reconstructed_DSULogo_multilevel.jpg", reconstructed_image_multilevel_uint8)

    # Display the reconstructed image
    cv2.imshow("Reconstructed Image (Multilevel)", reconstructed_image_multilevel_uint8)
    cv2.waitKey(0)
    cv2.destroyAllWindows()