# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

f = open("ciphertext.txt", "r")
badchars = ["1", ":", ";", ",", ".", "\n", "—", "?", "!", "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&", "\"", " ", "'"]

dictionary = {}
for x in f.read():
    if x in badchars:
        continue

    if x in dictionary:
        dictionary[x] += 1
    else:
        dictionary[x] = 1
print(dictionary)

count = 0
for k in dictionary.values():
    count += k
print(count)


a = sorted(dictionary.items(), key=lambda kv: (kv[1], kv[0]))
print(a)
code = ["Z", "X", "J", "Q", "V", "K", "P", "C", "Y", "M", "B", "F", "G", "U", 'W', "L", "D", "S", "I", "R", "N", "H", "O", "A", "T", "E"]

decode_table = {}
counter = 0
for item in a:
    for x in item[-2]:
        decode_table[x] = code[counter]
        counter += 1
print(decode_table)

def decode(s):
    r = ""
    for c in s:
        if c in decode_table:
            r += decode_table[c]
        else:
            r += c
    return r

print()
print()
f.close()

fx = open("ciphertext.txt", "r")
print(decode(fx.read()))
fx.close()