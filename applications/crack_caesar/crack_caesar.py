# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
with open('ciphertext.txt','r') as f_open:
    data = f_open.read()

myKey = {
    "H": "A",
    "R": "F",
    "I": "K",
    "X": "P",
    "A": "U",
    "S": "Z",
    "Z": "B",
    "J": "G",
    "G": "L",
    "K": "Q",
    "M": "V",
    "Y": "C",
    "D": "H",
    "L": "M",
    "U": "R",
    "B": "W",
    "W": "D",
    "P": "I",
    "C": "N",
    "N": "S",
    "Q": "X",
    "O": "E",
    "T": "J",
    "E": "O",
    "F": "T",
    "V": "Y"
}

def decoder(textFile):
    for i in range(0, len(textFile)):
        for each in myKey:
            if each in textFile[i]:
                textFile = textFile[i].replace(each, myKey[each])
    return textFile

print(decoder(data))