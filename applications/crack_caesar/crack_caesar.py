# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

from collections import OrderedDict
# Your code here
def readText():
    letterDict = {}
    cipherArray = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
    decodedDict = {}

    f = open("applications/crack_caesar/ciphertext.txt", "r")
    contents = f.read()

    for x in contents:
        if x in letterDict:
            letterDict[x] += 1
        else:
            if x.isalpha():
                letterDict[x] = 1

    sorted_letterDict = sorted(letterDict.items(), key=lambda x: (x[1], x[0]), reverse=True)

    index = 0
    for x in sorted_letterDict:
        for letter in x[-2]:
            decodedDict[letter] = cipherArray[index]
            index += 1
    print(decodedDict)

    decodedText = ""
    for x in contents:
        if x in decodedDict:
            decodedText += decodedDict[x]
        else:
            decodedText += x
    return print(decodedText)

readText()

