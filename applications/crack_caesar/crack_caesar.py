# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# In other words, ordered from most frequently used to least, the letters
# are:

# ```
# 'E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
# 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z'
# ```
# Write a program that automatically finds the key for the ciphertext in
# the file[`ciphertext.txt`](ciphertext.txt), then decodes it and shows
# the plaintext.

# (All non-letters should pass through the decoding as- is, i.e. spaces and
#  punctuation should be preserved. The input will not contain any
#  lowercase letters.)

# No tests are provided for this one, but the result should be readable,
# with at most a handful of incorrect letters.
import re

with open("ciphertext.txt") as f:
    cipher = f.read()
letter_frequency = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
                    'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
# wow well made that simpler


def crack(data):
    cache = {}
    data = re.sub('[^a-zA-Z]', '', data)

    for el in data:
        if el in cache:
            cache[el] += 1
        else:
            cache[el] = 1
    key = sorted(cache.items(), key=lambda x: x[1], reverse=True)
    for el in range(len(key)):
        key[el] = key[el][0]
    return key


code = dict(zip(crack(cipher), letter_frequency))
print(cipher.translate(str.maketrans(code)))


# def crack_code(encoded_data):
#     # map ea element of the sorted array frequencies of chara in encoded data
#     # loop through creating a hash tbl encoding the key encoded_data[i] and value =lettter_frequency[i]
#     letter_frequency = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L',
#                         'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

#     decode_key = {}

#     for i in range(len(letter_frequency)):
#         # 0 index selects chara as the key - frequency
#         k = encoded_data[i][0]
#         v = letter_frequency[i]
#         if k not in decode_key:
#             # swaps key/value
#             decode_key[k] = v

#     for l in decode_key:
#         print(f'key: {l}, value: {decode_key[l]}')
#     return decode_key


# def decode(data):
#     total_count = 0
#     encoded_letters = {}

#     ignore = ['\t', '\r', '\n']

#     for item in ignore:
#         string = data.replace(item, ' ')

#     newstr = re.sub(r'[a-zA-Z]', '', string)
#     # add all letters in the cipher and how many times they are present
#     # Get the frequency, convert to array and sort it
#     for char in newstr:
#         if char not in encoded_letters and len(char) > 0:
#             encoded_letters[char] = 1
#             total_count += 1
#         elif len(char) > 0:
#             encoded_letters[char] += 1
#             total_count += 1

#     for letter in encoded_letters:
#         encoded_letters[letter] = encoded_letters[letter] / total_count

#     encoded_letters = list(encoded_letters.items())
#     encoded_letters.sort(key=lambda l: l[1], reverse=True)

#     decode_key = crack_code(encoded_letters)

#     # Decode text
#     decoded_txt = ''

#     for thing in data:
#         if thing in decode_key:
#             decode_char = thing.replace(thing, decode_key[thing])
#             decoded_txt = decoded_txt + decode_char
#         else:
#             decoded_txt = decoded_txt + thing
#     print(decoded_txt)
#     return decoded_txt


# # read from file
# with open("ciphertext.txt") as f:
#     words = f.read()
#     decode(words)
