import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read().strip().split().replace("\n", " ")
    print(words)

# TODO: analyze which words can follow other words
# Your code here

d = dict()

for word, index in enumerate(words):

    # TODO: construct 5 random sentences
    # Your code here
