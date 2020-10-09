# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
import os.path

input_txt = os.path.join(os.path.dirname(__file__), 'ciphertext.txt')

# with open(input_txt) as f:
#     cipherText = f.read()

# def letterCount(s):
#     dict = {}
#     letters = [l.upper() for l in s if l.isalpha()]
#     for letter in letters:
#         dict[letter] = dict[letter] + 1 if letter in dict else 1
#     return dict

# def caesarCipherKey(cipherText):
#     letters = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
#                'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
#     cipherLettersSorted = sorted(letterCount(cipherText).items(), key=lambda x: x[1], reverse=True)
#     key = {}
#     for (i, l) in enumerate(cipherLettersSorted):
#         key[l[0]] = letters[i]
#     return key

# def crackCaesarCipher(cipherText):
#     key = caesarCipherKey(cipherText)
#     decodedText = ""
#     for c in cipherText:
#         decodedText += key[c] if c in key else c
#     print(decodedText)

# crackCaesarCipher(cipherText)

with open(input_txt) as f:
    text = f.read()
    text = text.replace('\n', ' ').replace('\\', '')
    ht = {}
    count = 0
    for char in text:
        if ord(char) >= 65 and ord(char) <= 90:
            if char not in ht:
                ht[char] = 1
            else:
                ht[char] += 1
            count += 1
    frequent_list = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
                     'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
    ht = {k[0]: frequent_list[i] for i, k in enumerate(
        sorted(ht.items(), key=lambda item: item[1], reverse=True))}
    for char in text:
        if ord(char) >= 65 and ord(char) <= 90:
            print(ht[char], end="")
        else:
            print(char, end="")
