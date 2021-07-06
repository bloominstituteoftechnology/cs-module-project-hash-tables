import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    wordy = words.split()

    dic = {}

# TODO: analyze which words can follow other words
# Your code here
# need to look at the index, and then for all of the indexed items to the right of it, randomly print from there
# can't look to the left
# how do I write that:

# if it is index[0] than all are viable for the randomizer to choose from
# if it is index[1] than all are viable from :1 + range on
# if it is index[n] than all are vialbe from :n + length(index)
# what do I need to make this happen:
# I need a dictionary/hashtable

# example assuming there are 4 spots in total
# do they include the one at the index itself?
# INDEX     STORAGE SPOT
#   0   ->  [0?, 1, 2, 3, 4]
#   1   ->  [1?, 2, 3, 4]
#   2   ->  [2?, 3, 4]
#   3   ->  [3?, 4]
#   4   ->  [4?]

# need to think about if duplicates should be ignored -> that'd fuck up the probability of the chances of random words
#


# TODO: construct 5 random sentences
# Your code here

