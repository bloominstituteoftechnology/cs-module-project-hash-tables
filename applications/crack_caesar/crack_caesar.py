# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
from collections import defaultdict


# List of letters in order of expected frequency, from greatest to least.
freq_list = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
             'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

# Read ciphertext from file.
with open('ciphertext.txt') as file:
    ciphertext = file.read()

# Initialize dictionary to store character counts from ciphertext.
counts = defaultdict(int)

# Update dictionary with running counts for all uppercase letters in
# ciphertext.
for c in ciphertext:
    if c.isupper():
        counts[c] += 1

# Convert count dictionary to frequency list of letters in ciphertext, in
# order from most to least frequent.
cipher_freq = [item[0] for item in sorted(counts.items(),
                                          key=lambda x: x[1],
                                          reverse=True)]

# Generate translation table, matching letters by frequency rank.
lookup = {cipher: plain for cipher, plain in zip(cipher_freq, freq_list)}

# Output predicted plain text.
print(ciphertext.translate(str.maketrans(lookup)))
