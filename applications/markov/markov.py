import random as r
import math as m
# Read in all the words in one go
content = open('applications\markov\input.txt', 'r').read().replace('\n', ' ').replace('"', '').replace('\'', '').replace('(', '').replace(')', '').replace('[', '').replace(']', '').split(' ')
# Create dict of unique word parts
wordDict = { word : [] for word in set(content) }
# For word in content add the words successor to dict
for idx, word in enumerate(content[:-1]): # not the last word
    wordDict[word].append(content[idx + 1].replace(' ', ''))# no spaces

for x, y in wordDict.items():
  print(x, y)


"""
def startSentence():
    return r.choice(list(wordDict.keys())).title()

def randomPredecessor(words):
    print('yeetskeet')
    print(word)
    if (wordDict[word.lower()]): return wordDict[word.lower()]
    else: return startSentence().lower()

def buildSentence(words = []):
    if words == []: words.append(startSentence())
    print(words[-1][-1])
    print(f'current sent: {words}')
    if words[-1][-1] == '.' or words[-1][-1] == '!' or words[-1][-1] == '?':
        sentence = ''
        for word in words:
            sentence += (word + ' ')
        return sentence
    else:
        buildSentence(words.append(randomPredecessor(str(words[-1]))))
"""



"""
def lc(word):
    word = word.lower()
    print(word)
    return word

def startSentenc():
    return r.choice(list(wordDict.keys()))

def randomPredecessor(word):
    word = lc(word)
    if (wordDict[word]): return r.choice(list(wordDict[word]))
    else: return lc(startSentenc())

def speak():
    sent = f'{startSentenc().title()}'
    current = lc(sent)
    x = 5
    while x > 0:
        current = randomPredecessor(lc(current))
        sent += f' {current}'
        x -= 1
    return sent

print(speak())

print(r.choice(str(wordDict.keys())))
print(r.choice(list(wordDict.keys())))
print(speak())

"""





