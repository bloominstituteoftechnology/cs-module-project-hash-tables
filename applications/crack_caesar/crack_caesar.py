# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
import os.path

# get the file path relative to the current script
input_txt = os.path.join(os.path.dirname(__file__), 'ciphertext.txt')

# Read in all the words in one go
with open(input_txt) as f:
    cipherText = f.read()

def letterCount(s):
    dict = {}
    letters = [l.upper() for l in s if l.isalpha()]
    for letter in letters:
        dict[letter] = dict[letter] + 1 if letter in dict else 1
    return dict

def caesarCipherKey(cipherText):
    letters = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 
               'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
    cipherLettersSorted = sorted(letterCount(cipherText).items(), key=lambda x: x[1], reverse=True)
    key = {}
    for (i, l) in enumerate(cipherLettersSorted):
        key[l[0]] = letters[i]
    return key

def crackCaesarCipher(cipherText):
    key = caesarCipherKey(cipherText)
    decodedText = ""
    for c in cipherText:
        decodedText += key[c] if c in key else c
    print(decodedText)

crackCaesarCipher(cipherText)