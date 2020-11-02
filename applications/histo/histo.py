# Your code here
with open("robin.txt") as f:
    words = f.read()


d = {}

    # split the string into list of words
for c in words:
    if not c.isalpha() and not c.isspace():
        words = words.replace(c, '')

wordList = words.split()
maxLength = 0 

    # populate historgram 

    # loop through the words
for word in wordList:
    word = word.lower()

        # keeping track of the longest word length 
    if len(word) > maxLength:
        maxLength = len(word) 

    if word not in d:
        d[word] = 1
    else:
        d[word] += 1


    # sort histogram 

sortedHist = sorted(d.items(), key=lambda kv:  [-kv[1], kv[0]])


# print histogram with desired formatting 


for word in sortedHist:

    width = maxLength + 2

    hashtags = word[1]*'#'

    print(f"{word[0]:{width}} {hashtags}")
