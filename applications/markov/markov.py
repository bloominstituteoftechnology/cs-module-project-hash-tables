import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

    my_list = []
    words = words.split()
    # print(words)
    for i in range(len(words) - 1):
        my_list.append((words[i], words[i + 1]))


# TODO: analyze which words can follow other words
# Your code here


# TODO: construct 5 random sentences
# Your code here
