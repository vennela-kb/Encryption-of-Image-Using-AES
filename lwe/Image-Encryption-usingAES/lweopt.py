import random, math, hashlib
import psutil
import time
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Initialize variables for tracking performance
start_time = time.time()
process = psutil.Process()
cpu_times_before = process.cpu_times()
memory_usage_before = process.memory_info().rss

# Learning with Errors (LWE) Post Quantum Encryption.
# Python implemented by Justin Newman,
# original lesson from Bill Buchanan OBE.

# We will define a public and private key.
# Define a secret value s:
s = 5

# Generate public key. Made up of two vectors A and B
# First we will look at vector A:
# random numbers up to a given prime. We will use 97.
q = 97  
list_length = 20 # using 20 in this case.  

# Generate a random vector of numbers
A = [80,86,19,62,2,83,25,47,20,58,45,15,30,68,4,13,8,6,42,92]
print('A = ', A)

# Define a number of error values.
e = [3,3,4,1,3,3,4,4,1,4,3,3,2,2,3,2,4,4,1,3]

# Define B such that B_i = A_i x (s + e) (mod q)
def compute_b(A, e):
    B = []
    for i in range(list_length):
        B.append((A[i] * s + e[i]) % q)
    return B

B = compute_b(A, e)

print("B = ", B)
print("e = ", e)

# The public key is now (A, B)
# Read the message from cipher.txt
with open('cipher.txt', 'r') as file:
    content = file.read().strip()

try:
    M = int(content)
except ValueError:
    M = int(hashlib.md5(content.encode()).hexdigest(), 16) % q

n_samples = 4
sample_indexes = set()
while len(sample_indexes) < n_samples:
    sample_indexes.add(random.randint(0, list_length-1))
sample_indexes = list(sample_indexes)

print("Sample indexes: ", sample_indexes)

samples = []
# Display the sampled pairs
for x in range(n_samples):
    samples.append((A[sample_indexes[x]], B[sample_indexes[x]]))
print("Samples: ", samples)

# Compute u and v
u = sum(sample[0] for sample in samples) % q
v = (sum(sample[1] for sample in samples) + math.floor(q // 2) * M) % q

# Encrypt with AES (using u and v as part of the message)
key = get_random_bytes(16)  # AES key
cipher = AES.new(key, AES.MODE_EAX)
nonce = cipher.nonce
encrypted_text, tag = cipher.encrypt_and_digest(f"{u},{v}".encode())

# Get the size of the encrypted text
encrypted_text_size = len(encrypted_text)

# Performance tracking after script execution
cpu_times_after = process.cpu_times()
end_time = time.time()

execution_time = end_time - start_time
cpu_usage = (cpu_times_after.user - cpu_times_before.user) + (cpu_times_after.system - cpu_times_before.system)
memory_usage_after = process.memory_info().rss
memory_usage = (memory_usage_after - memory_usage_before) / 1024  # Convert to KB

print("Encrypted value: ", u, v)
dec = (v - s * u) % q
if dec > q / 2:  # if Dec is greater than q/2, the message is 1
    print("Decrypted Bit: 1")
else:  # if Dec is less than q/2, the message is 0
    print("Decrypted Bit: 0")

print(f"Execution Time: {execution_time} seconds")
print(f"CPU Usage: {cpu_usage} seconds (user + system)")
print(f"Memory Usage: {memory_usage} KB")
print(f"AES Encrypted Text Size: {encrypted_text_size} bytes")
