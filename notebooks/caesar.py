# big subsitution table
# encryption

# design an encryption app for inventory!!!!
"""
BEEJ
ZOOT
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

# writing our encoder


def encode(s):
    r = ""  # empty and add on to it

    for c in s:
        r += encode_table[c]

    return r


print(f' Our encoder for Hello World:', encode("HELLOWORLD"))

print("+------------------+")


# def decode(s):
#     r = ""
#
#     for c in s:
#         r += decode_table[c]

decode_table = {}


def build_decode_table():
    # this will go through all of our keys
    for key in encode_table.itmes:
        # for key, value in encode_table.items():
            decode_table[value] = key

        # now we can pull our value out:
        value = encode_table[key]
print(decode("DOGGEBEUGW"))
