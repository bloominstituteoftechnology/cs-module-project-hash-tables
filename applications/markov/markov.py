import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# words.replace("\n", " ")
split_words = words.split()

word_bank = {}
starting_words = []
stopping_words = []

# TODO: analyze which words can follow other words
def build_word_bank():
    for index, word in enumerate(split_words):
        if index < len(split_words) - 1:
            if isStarting(word):
                starting_words.append(word)
            if isStopped(word):
                stopping_words.append(word)
            if word not in word_bank:
                word_bank[word] = []
            word_bank[word].append(split_words[index + 1])

def isStarting(word):
    if word[0].isupper():
        return True
    elif word[0] == '"' and word[1].isupper():
        return True
    else:
        return False

def isStopped(word):
    if word.endswith(("!", "?", ".")):
        return True
    elif word.endswith('"') and word[:-1].endswith(("!", "?", ".")):
        return True
    else:
        return False


# TODO: construct 5 random sentences
build_word_bank()
for i in range(5):
    print(f"Sentence #{i + 1}:")
    word = random.choice(starting_words)
    print(word, end = " ")
    while not isStopped(word):
        word = random.choice(word_bank[word])
        print(word, end = " ")
    print("\n")
