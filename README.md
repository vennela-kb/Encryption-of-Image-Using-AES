 LWE Encryption using Python

Objectives:

❖ To study the working of the Learning with Errors (LWE) post-quantum encryption algorithm.
❖ To encrypt and then decrypt a message using the LWE algorithm with Python modules.
❖ To observe and analyze the encryption and decryption process of the LWE algorithm.

Steps to Run the Code:

1. Python IDE:
   - You can use any Python IDE such as PyCharm, Jupyter Notebook, or Google Colab to run the code.

2. Required Libraries:
   - The following libraries need to be installed before running the Python code:
     - `numpy`

3. Python Version:
   - Ensure you are using Python version 3.6 or above.

 Detailed Description of `lwe.py`

The `lwe.py` script demonstrates a simple implementation of the Learning with Errors (LWE) post-quantum encryption algorithm. This script covers key generation, message encryption, and message decryption, providing a practical example of LWE in action.

Key Components:

1. Key Generation:
   - The script defines a secret value `s` and uses a prime number `q` to generate the public key. The public key consists of two vectors, `A` and `B`, along with an error vector `e`. These vectors are generated using random numbers, ensuring the public key is unique and secure.

2. Message Handling:
   - The script reads a message from a file named `cipher.txt`. If the content is not an integer, the script hashes the content to create a consistent integer value. This ensures that any type of content can be processed for encryption.

3. Sampling and Encryption:
   - To encrypt the message, the script randomly selects a subset of indices from the generated vectors. Using these indices, it computes the encrypted values `u` and `v`, which form the encrypted message.

4. Decryption:
   - The script decrypts the message by computing a value `dec` from the encrypted values `u` and `v`, and the secret value `s`. Depending on whether `dec` is greater than half of `q`, the script determines the original message bit.

 Benefits of LWE:

- Post-Quantum Security: LWE is considered secure against quantum attacks, making it a strong candidate for future encryption standards.
- Simplicity and Efficiency: The algorithm is relatively simple to implement and can be efficiently executed on modern hardware.
- Versatility: LWE can be used in various cryptographic protocols, including key exchange, encryption, and digital signatures.

This example demonstrates the practical implementation of LWE encryption, providing a foundation for understanding and utilizing post-quantum cryptographic algorithms.
