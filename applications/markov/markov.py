import random
import re


# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
words = words.split(" ")

def build_index(words):
    index = {}
    start_words = []
    #loop through the split word list
    #add the next word to the list of that index
    for i in range(len(words) - 1):
        #check if word is in the index already
        if words[i] in index:
            index[words[i]].append(words[i + 1])
            #if not will add key and append to the next word
        else:
            index[words[i]] = []
            index[words[i]].append(words[i + 1])
    return index


# TODO: construct 5 random sentences
# Your code here
i = build_index(words)
s = random.choice(words)
print(" ".join(i[s]), end=" ")
