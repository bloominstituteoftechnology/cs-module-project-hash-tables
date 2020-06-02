import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

words = words.split(' ')
# TODO: analyze which words can follow other words
markov = {}
# List implementation
for i, word in enumerate(words):
    if i < len(words) - 1:
        print
        if word in markov:
            markov[word].append(words[i + 1])
        else:
            markov[word] = [words[i + 1]]
# Set implementation
# for i, word in enumerate(words):
#     if word in markov:
#         markov[word].add(words[i + 1])
#     else:
#         markov[word] = set()

# TODO: construct 5 random sentences
# Your code here
# print(markov)
start_words = {word for word in markov if word[0].isupper()}
stop_words = {word for word in markov if word[-1] in ['.', '?', '!']}
for _ in range(5):
    sentence = ""
    word = start_words.pop()
    start_words.add(word)
    sentence += word + ' '
    while word not in stop_words:
        word = random.choice(markov[word])
        sentence += word + ' '
    print(sentence)