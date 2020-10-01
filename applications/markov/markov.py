import random
import string
from collections import defaultdict

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
starting_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ"'
ending_chars = '.?!'
word_dict = {}
index = -1
words_array = words.split()
start = "starting_words"
previous_word = words_array[0]
word_dict[start] = []
for word in words_array:
    if word[-1] is '"':
        word = word.replace('"', "")
    if word[-1] is ':':
        word = word.replace(':', "")
    if word[0] is '(':
        word = word.replace('(', "")
    if word[-1] is ')':
        word = word.replace(')', "")
    if word[0] is '"' and word[1] in starting_chars:
        word_dict[start].append(word)
    elif word[0] in starting_chars:
        word_dict[start].append(word)
    if word_dict.__contains__(word) is False:
        word_dict.setdefault(word, [])
    if index >= 0:
        word_dict[previous_word].append(word)
        previous_word = word
    index += 1

# TODO: construct 5 random sentences
# Your code here
sentences = []
while len(sentences) is not 5:
    starting_word = random.choice(word_dict[start])
    word = starting_word
    sentence = f"{starting_word} "
    while word[-1] not in ending_chars:
        word = random.choice(word_dict[word])
        if word in word_dict[start]:
            while word in word_dict[start]:
                word = random.choice(word_dict[word])
        sentence += f"{word} "
    sentences.append(sentence.rstrip())
    
for sentence in sentences:
    if sentence[0] is '"' and sentence[-1] is not '"':
        sentence += '"'
    print(sentence, end= "\n\n")

