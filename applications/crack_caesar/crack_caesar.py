# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
# Read in all the words in one go
with open("applications/crack_caesar/ciphertext.txt") as f:
    words = f.read()


def letter_count(s):
    # Your code here
    cache = {}

    for c in s:
        if c in cache:
            cache[c] += 1
        else:
            cache[c] = 1

    letters_only = []

    for k, v in cache.items():
        if k.isalpha():
            letters_only.append((k, v))

    letters_only.sort(key=lambda e: e[1], reverse=True)

    # letters_only = dict(letters_only[:26])

    return letters_only


cipher_letters = letter_count(words)

encode_table = {
    'E': cipher_letters[0][0],
    'T': cipher_letters[1][0],
    'A': cipher_letters[2][0],
    'O': cipher_letters[3][0],
    'H': cipher_letters[4][0],
    'N': cipher_letters[5][0],
    'R': cipher_letters[6][0],
    'I': cipher_letters[7][0],
    'S': cipher_letters[8][0],
    'D': cipher_letters[9][0],
    'L': cipher_letters[10][0],
    'W': cipher_letters[11][0],
    'U': cipher_letters[12][0],
    'G': cipher_letters[13][0],
    'F': cipher_letters[14][0],
    'B': cipher_letters[15][0],
    'M': cipher_letters[16][0],
    'Y': cipher_letters[17][0],
    'C': cipher_letters[18][0],
    'P': cipher_letters[19][0],
    'K': cipher_letters[20][0],
    'V': cipher_letters[21][0],
    'Q': cipher_letters[22][0],
    'J': cipher_letters[23][0],
    'X': cipher_letters[24][0],
    'Z': cipher_letters[25][0]
}

decode_table = {

}


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

print(decode(words))
