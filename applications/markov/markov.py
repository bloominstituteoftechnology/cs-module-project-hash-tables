import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
words = words.split()

cache = {}

stop = [".", "?", "!", '"']

for i in range(len(words) - 1):
    if words[i][-1] not in stop:
        # print(words[i])
        # print('last:', words[i][-1])
        if words[i] not in cache:
            cache[words[i]] = [words[i+ 1]]

        else:
            cache[words[i]] += [words[i+ 1]]

# TODO: construct 5 random sentences
# Your code here

#get random word
#use it as a key to print one of its values
#search the database for a key matching that value
#and so on, until reaching given stopping point

for i in range(50):
    starter = cache[words[55].key()]
    print(starter)