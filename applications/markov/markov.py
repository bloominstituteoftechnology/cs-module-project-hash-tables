import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read().replace("\n", " ")
    f.close()

