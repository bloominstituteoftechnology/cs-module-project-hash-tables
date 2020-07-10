# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
# Your code her
cache = {}
f = open('ciphertext.txt','r')
for letter in f.read():
    if letter.isalpha():
        if letter not in cache:
            cache[letter] = 1
        else:
            cache[letter] += 1
listLetters = list(cache.items())
def keyfunc(e):
    return e[1]
listLetters.sort(key=keyfunc, reverse=True)
print(listLetters)
translate = {
    "E": None,
    "T": None,
    "A": None,
    "O": None,
    "H": None,
    "N": None,
    "R": None,
    "I": None,
    "S": None,
    "D": None,
    "L": None,
    "W": None,
    "U": None,
    "G": None,
    "F": None,
    "B": None,
    "M": None,
    "Y": None,
    "C": None,
    "P": None,
    "K": None,
    "V": None,
    "Q": None,
    "J": None,
    "X": None,
    "Z": None
}
print(translate)   
#for index in range(0, len(listLetters)): "   print(index)
