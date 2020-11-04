# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

"""
UPER
Understand
Create a frequency analysis of ciphertext.
Map that text to frequency chart in Readme.md
Create new dictionary that matches letters based on percentage
Use that to decipher

Plan
- iterate and count letters ✓
- use a dictionary to keep track ✓
- discard special characters ✓
- Find the percentage of total text  ✓
- Map to frequency analysis in ReadMe. ✓

"""
from string import ascii_uppercase
import operator

def alpha_length_text(text):
    alphabets = 0
    for i in range(len(text)):
        if text[i].isalpha():
            alphabets = alphabets + 1
    return alphabets

def percentages(text, length):
    letters = {}

    for x in ascii_uppercase:
        letters[x] = round((text.count(x)/length*100),2)

    # sorted_x = sorted(letters.items(), key=operator.itemgetter(1), reverse=True)
    return letters

frequency = {
    "A": 8.46,
    "B": 2.19,
    "C": 1.58,
    "D": 4.74,
    "E": 11.53,
    "F": 2.42,
    "G": 2.48,
    "H": 7.71,
    "I": 5.84,
    "J": 0.07,
    "K": 0.84,
    "L": 3.92,
    "M": 2.18,
    "N": 6.73,
    "O": 8.08,
    "P": 1.08,
    "Q": 0.17,
    "R": 6.29,
    "S": 5.56,
    "T": 9.75,
    "U": 2.59,
    "V": 0.59,
    "W": 3.08,
    "X": 0.07,
    "Y": 2.02,
    "Z": 0.03,
}

file = open('cs-module-project-hash-tables/applications/crack_caesar/ciphertext.txt', 'r+')
cipher = file.read()
cipher_letter_frequency = alpha_length_text(cipher)
cipher_letter_frequency_percentages = percentages(cipher, cipher_letter_frequency)
cipher_letter_frequency_percentages_flipped = dict([(value, key) for key, value in cipher_letter_frequency_percentages.items()])

merged = {}
for key, value in frequency.items():
    merged[key] = cipher_letter_frequency_percentages_flipped[value]

decode_table = {}
for k, v in merged.items():
    decode_table[v] = k

def decode(text):
    r = ""

    for c in text:
        if c not in decode_table:
            r += " "
        else:
            r += decode_table[c]

    return r

print(f"DECODED TEXT: \n {decode(cipher)}")