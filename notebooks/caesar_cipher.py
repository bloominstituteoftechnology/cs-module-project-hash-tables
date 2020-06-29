# Caesar Cipher

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


def build_decode_table():
    for key, value in encode_table.items():
        decode_table[value] = key


def encode(s):
    r = ""

    for c in s:
        if c in encode_table:
            r += encode_table[c]
        else:
            r += c

    return r


def decode(s):
    r = ""

    for c in s:
        if c in decode_table:
            r += decode_table[c]
        else:
            r += c

    return r


build_decode_table()

print(encode("HELLO, WORLD!"))

print(decode("DOGGE, BEUGW!"))
