import random

# Read in all the words in one go
with open("/home/ubuntu/Github/CS/cs-module-project-hash-tables/applications/markov/input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words

words = words.split()

this_that = dict()

for i in range(len(words)-1):
    word = words[i]
    if words[i] not in this_that:
        this_that[word] = []
        this_that[word].append(words[i + 1])

    else:
        this_that[word].append(words[i + 1])
    
startwords = []
stopwords = []
stoppunct = ['.', '?', '!']
stopquote = ['."', '?"', '!"']

startwords = []
stopwords = []
stoppunct = ['.', '?', '!']
stopquote = ['."', '?"', '!"']

for word in words:
    if word[0].isupper():
        startwords.append(word)
    
    if word[0] == '"' and word[1].isupper():
        startwords.append(word)
    
    if word[-1] in stoppunct:
        stopwords.append(word)

    if word[-2:] in stopquote:
        stopwords.append(word)

# TODO: construct 5 random sentences
def gibberish(n):

    for i in range(n):
        sentence = []
        sentence.append(random.choice(startwords))
        
        while sentence[-1] not in stopwords:
            sentence.append(random.choice(this_that[sentence[-1]]))
        
        sentence = " ".join(sentence)
        print(sentence)

gibberish(5)

