# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

import os

f = open(f"{os.getcwd()}/applications/crack_caesar/ciphertext.txt")

text = f.read()
# print(text)


letter_frequencies = {'E': 11.53, 'T': 9.75, 'A': 8.46, 'O': 8.08, 'H': 7.71,
                      'N': 6.73, 'R': 6.29, 'I': 5.84, 'S': 5.56, 'D': 4.74,
                      'L': 3.92, 'W': 3.08, 'U': 2.59, 'G': 2.48, 'F': 2.42,
                      'B': 2.19, 'M': 2.18, 'Y': 2.02, 'C': 1.58, 'P': 1.08,
                      'K': 0.84, 'V': 0.59, 'Q': 0.17, 'J': 0.07, 'X': 0.07,
                      'Z': 0.03}
