import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
markdict = {}
startwords = []
wordlist = words.split()
prevword = None
for word in wordlist:
    # first word
    if prevword == None:
        prevword = word
        continue
    # stop words, don't add anything to em
    if prevword.endswith(('.', '?', '!')):
        markdict[prevword] = []
        prevword = word
        continue
    # add words
    if prevword not in markdict:
        # start words
        if prevword[0].isupper():
            startwords.append(prevword)
        markdict[prevword] = [word]
    # already in, just append
    else:
        markdict[prevword].append(word)
    prevword = word

# TODO: construct 5 random sentences
# Your code here
import random as rand
for _ in range(5):
    sentence = [rand.choice(startwords)]
    for i in range(100):
        sentence.append(rand.choice(markdict[sentence[i]]))
        if sentence[i+1].endswith(('.', '?', '!')):
            break
    print(' '.join(sentence))