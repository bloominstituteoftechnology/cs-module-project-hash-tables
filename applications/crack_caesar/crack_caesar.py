# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
from collections import defaultdict

counts = defaultdict(int)

with open('ciphertext.txt') as file:
    ciphertext = file.read()

for c in ciphertext:
    if c.isupper():
        counts[c] += 1

freq_list = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
             'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

cipher_freq = [item[0] for item in sorted(counts.items(),
                                          key=lambda x: x[1],
                                          reverse=True)]

lookup = {cipher: plain for cipher, plain in zip(cipher_freq, freq_list)}

print(ciphertext.translate(str.maketrans(lookup)))
