# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

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

decode_table = {v: k for k, v in encode_table.items()}

ignore = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split()


def decode(s):
    r = ''
    for c in s:
        if c in ignore:
            words = words.replace(c, '')
        if c == ' ':
            r += ' '
        else:
            r += decode_table[c]

    return r


with open("ciphertext.txt") as f:
    r = ''
    words = f.read()
    # for i in words:
    #     if i in ignore:
    #         words = words.replace(i, '')
    #     if i == ' ':
    #         r += ' '
    #     else:
    #         r += decode_table[i]
    print(decode(words))
