import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

words = words.replace("\n", " ")
words = words.replace("\t", " ")
words = words.replace("\r", " ")

# TODO: analyze which words can follow other words
words = [w for w in words.split(" ") if w is not ""]
starts = []
d = {}

def is_start(word):
    if word[0].isupper():
        return True
    if word[0] == '"' and word[1].isupper():
        return True
    return False

def is_stop(word):
    if word.endswith(("!", "?", ".")):
        return True
    if word.endswith('"'):
        if word[:-1].endswith(("!", "?", ".")):
            return True
    return False

for index, word in enumerate(words):
    if index < len(words) - 1:
        if is_start(word):
            starts.append(word)
        if word in d.keys():
            d[word].append(words[index + 1])
        else:
            d[word] = [words[index + 1]]

# for k, v in d.items():
#     print(f"{k}: {v}")
for i in range(5):
    selected_word = random.choice(starts)
    print(selected_word, end=" ")
    while not is_stop(selected_word):
        selected_word = random.choice(d[selected_word])
        print(selected_word, end=" ")
    print()
    print()



