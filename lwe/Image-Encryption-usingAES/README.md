 LWE and AES Image Encryption using Python:
Objectives:
	To study the working of the Learning with Errors (LWE) post-quantum encryption algorithm.
	 To encrypt and then decrypt a message using the LWE algorithm with Python modules.
	 To observe and analyze the encryption and decryption process of the LWE algorithm.
	 To implement double encryption by combining AES and LWE algorithms for enhanced security.

Steps to Run the Code:
1. Python IDE:
   - You can use any Python IDE such as PyCharm, Jupyter Notebook, or Google Colab to run the code.

2. Required Libraries:
   - The following libraries need to be installed before running the Python code:
     - pycryptodome (For AES encryption)
     - numpy
     - pywavelets
     - pickle
     - opencv-python

3. Python Version:
   - Ensure you are using Python version 3.6 or above.

 Description of lwe.py

The lwe.py script demonstrates a simple implementation of the Learning with Errors (LWE) post-quantum encryption algorithm. This script covers key generation, message encryption, and message decryption, providing a practical example of LWE in action.

 Description of lwe.py
The lwe.py script demonstrates a simple implementation of the Learning with Errors (LWE) post-quantum encryption algorithm. This script covers key generation, message encryption, and message decryption, providing a practical example of LWE in action.

Key Components:
1. Key Generation:
   - The script defines a secret value s and uses a prime number q to generate the public key. The public key consists of two vectors, A and B, along with an error vector e. These vectors are generated using random numbers, ensuring the public key is unique and secure.

2. Message Handling:
   - The script reads a message from a file named cipher.txt. If the content is not an integer, the script hashes the content to create a consistent integer value. This ensures that any type of content can be processed for encryption.

3. Sampling and Encryption:
   - To encrypt the message, the script randomly selects a subset of indices from the generated vectors. Using these indices, it computes the encrypted values u and v, which form the encrypted message.

4. Decryption:
   - The script decrypts the message by computing a value dec from the encrypted values u and v, and the secret value s. Depending on whether dec is greater than half of q, the script determines the original message bit.

 AES Encryption of Image Coefficient:
I worked on encrypting the cH coefficient from a PNG image using AES encryption, following the method presented by Rachit Goel (available on GitHub). Initially, I converted the image to grayscale to read the cH coefficient from a 2D discrete wavelet transform, stored its original value, and then encrypted this coefficient using a key. I also made some basic changes to the encrypt and decrypt Python files to facilitate this process. The encrypted value was saved in a file named cipher.txt. Subsequently, I decrypted the values and printed them.

 Double Encryption with LWE: 
Next, I modified the code from lwe.py (Learning with Errors by Justin Mathew, available on GitHub) to implement double encryption. This involved using the cipher.txt file, which contained the AES-encrypted cH coefficient, as input for the Learning with Errors algorithm. This double encryption process enhances resistance to quantum computer attacks.
To ensure compatibility, I verified that cipher.txt contained plain text readable by the Learning with Errors repository and matched the input size required by the repository.

 Benefits of LWE and Double Encryption:
- Post-Quantum Security: LWE is considered secure against quantum attacks, making it a strong candidate for future encryption standards.
- Enhanced Security: Combining AES and LWE encryption provides an additional layer of security, making it more resistant to attacks.
- Versatility: LWE can be used in various cryptographic protocols, including key exchange, encryption, and digital signatures.
