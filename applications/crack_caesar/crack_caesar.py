# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
with open("ciphertext.txt") as f:
    words = f.read()
# Your code here

encode_table = {
    'A': 'H',   'B': 'Z',   'C': 'Y',   'D': 'W',   'E': 'O',
    'F': 'R',   'G': 'J',   'H': 'D',   'I': 'P',   'J': 'T',
    'K': 'I',   'L': 'G',   'M': 'L',   'N': 'C',   'O': 'E',
    'P': 'X',   'Q': 'K',   'R': 'U',   'S': 'N',   'T': 'F',
    'U': 'A',   'V': 'M',   'W': 'B',   'X': 'Q',   'Y': 'V',
    'Z': 'S',
}


def encode(old_string):
    new_letter = ""
    for i in old_string:
        if i in encode_table:
            new_letter = new_letter + encode_table[i]
        else:
            return i
    return new_letter


print(encode(words))
