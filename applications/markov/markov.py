import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

wordList = words.split()
#test = ['One', 'thing', 'was','the', 'certain,', 'that', 'the', 'white', 'kitten!', 'had', 'had', 'nothing', 'to', 'do', 'with', 'it:']
cache = {}
# TODO: analyze which words can follow other words
# Your code here
for (index, word) in enumerate(wordList):
    if index < len(wordList)-1:
        if word not in cache:
            cache[word] = wordList[index+1]
        elif word in cache:
            cache[word] +=  f' {wordList[index+1]}'

# TODO: construct 5 random sentences
# Your code here
stopWord = '\n'

sentence = []
start = 'the'
sentence.append(start)
eachword = list(cache[start].split(' '))
ranNum = random.randrange(0, len(eachword))
sentence.append(eachword[ranNum])
while True:
    eachword = list(cache[eachword[ranNum]].split(' '))
    ranNum = random.randrange(0, len(eachword))
    sentence.append(eachword[ranNum])
    if '!' in eachword[ranNum] or '?' in eachword[ranNum] or '.' in eachword[ranNum]:
        break

print(' '.join(sentence))