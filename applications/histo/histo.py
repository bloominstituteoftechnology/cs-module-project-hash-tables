# QUESTIONS FOR ANDREW:
# Q: Why is there a blank character '' in the dictionary?

f = open("robin.txt", "r")
badchars = ["\"", ":", ";", ",", ".", "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&", '', "!", "?"]
space = " "

dictionary = {}
word = ""

for x in f.read().lower():
    if x in badchars:
        continue

    if x == space or x == "\n":
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
        word = ""
    else:
        word += x


print(dictionary)

a = sorted(dictionary.items(), key=lambda kv: (kv[1], kv[0]))
print()
a = a[::-1]
# print(a)
str = ""
numberOfSpaces = 20

for item in a:
    str += item[0]

    for i in range(0, numberOfSpaces - len(str)):
        str += " "

    for i in range(0, item[1]):
        str += "#"
    print(str)
    str = ""