import random

# Read in all the words in one go
ends = { '?', '!', '"', '.' }
start_words = {}
words = {}


with open("input.txt") as f:
    text = f.read()
    text = text.replace('\n', ' ').replace('\\', '')
    # print(text)
    curr_ht = words
    prev_ht = {}
    curr_word = ''
    prev_word = ''
    for char in text:
        if (ord(char) >= 65 and ord(char) <= 90) or (not curr_word and char == '"'):
            curr_ht = start_words
        if char == ' ':
            if curr_word not in curr_ht and curr_word != '':
                curr_ht[curr_word] = []
            if prev_word:
                prev_ht[prev_word].append(curr_word)
            prev_word = curr_word
            prev_ht = curr_ht
            curr_word = ''
            curr_ht = words
        else:
            curr_word += char


def gobbledegook(length, start_words, words):
    # for i in range(length):
    start = True
    quote = 0
    word = ''
    for i in range(length):
        if start:
            word = random.choice(list(start_words.keys()))
            print(word, end=" ")
            print(random.choice(start_words[word]), end=" ")
            start = False
        else:
            word = random.choice(list(words.keys()))
            print(word, end=" ")
        if word[0] == '"':
            quote += 1
        if word[-1] in ends:
            if quote > 0:
                print('"', end="")
                quote -= 1
            start = True

gobbledegook(100, start_words, words)
# for word in words.keys(b ):
#     print(word)
    # print(word[0])
# TODO: analyze which words can follow other words
# Your code here


# TODO: construct 5 random sentences
# Your code here

