

# transposition table

# you have data to transform from one form into another

# transposition cipher
# Caesar cipher --> 'rotate' the letter

# given a string, build a new string by looking up each letter

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

# make a function to encode a string
# iterate through the string we're given
# for every letter, look up its encoding (its transformation)
# build a new string

first_string = 'hello'

def encode(old_string):
    new_string = ''

    for letter in old_string.upper():
        new_string = new_string + encode_table[letter]

    return new_string

herrow = encode(first_string)
print(herrow)

# make a decode table so we can also decode our super secret messages
# with encode table, keys --> values, values --> keys

## iterate through encode table
### for each key, value, add to a new dictionary with value, key
decode_table = {}
for key, value in encode_table.items():
    decode_table[value] = key


def decode(old_string):
    new_string = ''

    for letter in old_string.upper():
        new_string = new_string + decode_table[letter]

    return new_string


decoded = decode(herrow)
print(decoded)