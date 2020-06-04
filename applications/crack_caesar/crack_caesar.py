# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

def split(word): 
    return [char for char in word]

f = open("ciphertext.txt", "r")
text = f.read()

frequency_cache = {}

letters = []
splitLetter = text.split()
for word in splitLetter:
    for char in word:
        if char not in frequency_cache and ord(char) >= 65 and ord(char) <= 90:
            frequency_cache[char] = 1
        elif char in frequency_cache:
            frequency_cache[char] += 1
        else:
            continue

percentages = ["E","T","A","O","H","N","R","I","S","D","L","W","U","G","F","B","M","Y","C","P","K","V","Q","J","X","Z"]

sortedDict = sorted(frequency_cache.items(), key=lambda x: x[1], reverse=True)
cipher = {}

for i in range(len(percentages) -1):
    cipher[sortedDict[i][0]] = percentages[i]

decoded = []
for word in splitLetter:
    decoded.append(' ')
    for char in word:
        if char in cipher:
            decoded.append(cipher[char])
        else:
            decoded.append(char)


print("".join(decoded))