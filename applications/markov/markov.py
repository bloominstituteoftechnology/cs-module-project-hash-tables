import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
wordsArray = words.split(" ")
cache = {}
for index in range(len(wordsArray)):
    if index < len(wordsArray)-1:
        if wordsArray[index] not in cache:
            cache[wordsArray[index]] = [wordsArray[index+1]]
        else:
            cache[wordsArray[index]].append(wordsArray[index+1])



# TODO: construct 5 random sentences
# Your code here
def make_sentence(word):
    sentence = []
    while word in cache:
        sentence.append(word)
        if word[-1] in [".","?","!"]:
            # break
            return " ".join(sentence)
        else:
            word = random.choice(cache[word])

    return "Three can keep a secret if two of them are dead."

print(make_sentence("One"))
