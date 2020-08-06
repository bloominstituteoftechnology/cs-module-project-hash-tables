import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read().strip().replace("\n", " ").split(" ")
    # print(words)

# TODO: analyze which words can follow other words
# Your code here

d = dict()

for index, word in enumerate(words):
    if index < (len(words)-1):
        if word == "":
            word = " "
        elif words[index + 1] == "":
            d[word] = " "
        else:
            d[word] = words[index + 1]
# print(d)


# TODO: construct 5 random sentences
# Your code here

def make_sentence():

    try:
        start = get_starting_word()
