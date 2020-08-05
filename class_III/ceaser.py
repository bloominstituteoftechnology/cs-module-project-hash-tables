# Ceaser Cipher

# Hash tables as a map between data values

"""
GOATS
JEHFN
"""

encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S'
}

decode_table = {}

for k,v in encode_table.items():
    decode_table[v] = k

def encode(s):
    r = ""

    for c in s:
        r += encode_table[c]

    return r

def decode(s):
    r = ""

    for c in s:
        r += decode_table[c]

    return r

e = encode("GOATS")
print(e)
print(decode(e))