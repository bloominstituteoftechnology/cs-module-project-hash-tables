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

decode_table = {}

for key, value in encode_table.items():
    decode_table[value] = key


def decode(old_string):
    new_letter = ""
    for i in old_string:
        if i in decode_table:
            new_letter = new_letter + decode_table[i]
        else:
            new_letter = new_letter + i
    return new_letter


print(decode(words))
