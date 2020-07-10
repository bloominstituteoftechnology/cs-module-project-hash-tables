# Your code here
cache = {}
ignored = ['"', ':', ';', ',', '.', '-', '+', '=', '\\','/', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
f = open('robin.txt', 'r')

for line in f:
    wordList = line.split()
    for word in wordList:
        word = word.lower()
        for badChar in ignored:
            word = word.replace(badChar, "")
        
        if word in cache:
            cache[word] += 1
        elif word =="" or word ==" ":
            break
        else:
            cache[word] = 1


print(cache)