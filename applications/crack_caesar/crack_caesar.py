# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
f = open("ciphertext.txt", "r")
text = f.read()

characters_to_ignore = '" : ; , . - + = / \ | [ ] { } ( ) * ^ & â € 1 ? ” ! '.split(" ")
characters_to_ignore.append("'")
for letter in text:
    if letter in characters_to_ignore:
        text = text.replace(letter, "")

print(text)

most_common = [
    "E",
    "T",
    "A",
    "O",
    "H",
    "N",
    "R",
    "I",
    "S",
    "D",
    "L",
    "W",
    "U",
    "G",
    "F",
    "B",
    "M",
    "Y",
    "C",
    "P",
    "K",
    "V",
    "Q",
    "J",
    "X",
    "Z",
]


def letter_count(s):
    d = {}

    for letter in s:
        if letter.isspace():
            continue
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1
    return d


# print(letter_count(text))


def sort_letter_count(str):
    d = letter_count(str)

    items = list(d.items())
    items.sort(key=lambda e: e[1], reverse=True)
    most_common_encoded = []
    for i in items:
        most_common_encoded.append(i[0])
    return most_common_encoded


most_common_encoded = sort_letter_count(text)

print(most_common)
print(most_common_encoded)

encoded_dict = {}

for i, val in enumerate(most_common):
    encoded_dict[val] = most_common_encoded[i]

decoded_dict = {}
for k, v in encoded_dict.items():
    decoded_dict[v] = k


def decode(str):
    r = ""
    for letter in str:
        if letter not in decoded_dict:
            r += letter
        else:
            r += decoded_dict[letter]
    return r


print(decode(text))
