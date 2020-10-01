# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
import string


'''
|   E    |    11.53   |
|   T    |     9.75   |
|   A    |     8.46   |
|   O    |     8.08   |
|   H    |     7.71   |
|   N    |     6.73   |
|   R    |     6.29   |
|   I    |     5.84   |
|   S    |     5.56   |
|   D    |     4.74   |
|   L    |     3.92   |
|   W    |     3.08   |
|   U    |     2.59   |
|   G    |     2.48   |
|   F    |     2.42   |
|   B    |     2.19   |
|   M    |     2.18   |
|   Y    |     2.02   |
|   C    |     1.58   |
|   P    |     1.08   |
|   K    |     0.84   |
|   V    |     0.59   |
|   Q    |     0.17   |
|   J    |     0.07   |
|   X    |     0.07   |
|   Z    |     0.03   |
'''

# Your code here
def decode_cipher(input_file: str):
    known_frequency = ["E", "T", "A", "O", "H", "N", "R", "I", "S", "D", "L", "W", "U", "G", "F", "B", "M", "Y", 
    "C", "P", "K", "V", "Q", "J", "X", "Z"]
    within = string.ascii_uppercase
    counted_set = {}
    letter_percentages = {}
    cipher_map = {}
    with open(input_file) as f:
        cipher_text = f.read()
    for char in cipher_text:
        if char in within:
            if counted_set.__contains__(char):
                counted_set[char] += 1
            else:
                counted_set[char] = 1
        
    for letter in within:
        percentage = (counted_set[letter] / len(cipher_text)) * 100
        letter_percentages[letter] = percentage
    items = list(letter_percentages.items())
    items.sort(key = lambda x: -x[1])
    index = 0
    for (key, value) in items:
        cipher_map[key] = known_frequency[index]
        index += 1
    decoded = ""
    for char in cipher_text:
        if char in within:
            char = cipher_map[char]
        decoded += char
    return decoded

print(decode_cipher("ciphertext.txt"))