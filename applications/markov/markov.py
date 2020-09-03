import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
words = words.split(' ')
# TODO: analyze which words can follow other words
# Your code here
follow = []
for i in words:
    current = i
    follow.append((last,current))
    last = current
print(follow)
# TODO: construct 5 random sentences
# Your code here

