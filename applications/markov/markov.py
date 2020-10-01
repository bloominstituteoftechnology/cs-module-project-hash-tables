import random

# Read in all the words in one go
with open("applications/markov/input.txt") as f:
    words = f.read()

# This handles some strange occurences of "--" in the text to make the
# resulting sentences that have been created more consistent
words = words.replace("\"--", "\"")
words = words.replace("--\"", "\"")
words = words.replace("--", " ")

# split the words into an array
words = words.split()

# dictionary of possible next words with the current word as the key
# for example in the sentence "Well, a cat saw a goat"
# d = {"a": ["cat", "goat"], "Well": ["a"], ... "goat": []}
d = {}
# list of possible starting words based on relevant criteria ie capital letters
# ex from above: s = ["Well"]
s = []

# iterate over every word from the read-in file
for i in range(len(words)):
    current_word = words[i]
    # flag to check if the word is a start word
    start = False
    # checks if word is a start word if the first letter is a capital or is
    # a quotation mark followed by a capital letter
    if current_word[0].isupper() or (current_word[0] == "\"" and current_word[1].isupper()):
        start = True
    # initialize an empty array for the first occurenc eof each word
    if current_word not in d:
        d[current_word] = []
    # if the word is a start word we haven't seen yet, add it to start word array
    if start and current_word not in s:
        s.append(current_word)
    # as long as the current word is not the last letter, append the next word
    # to correct the current word's array in the dictionary
    if i < len(words) - 1:
        next_word = words[i + 1]
        d[current_word].append(next_word)

# print the dictionary of possible next words and the list of start
# words, useful for debugging
# print(d, "\n\n=====\n\n=====\n\n", s)

# possible sentence endings
endings = [".", "!", "?", ".\"", "!\"", "?\""]


def make_sentence():
    # pick a random word from start word array s to begin the sentence
    text = random.choice(s)
    # declare that word as the "previous" word to get into the loop
    prev = text
    # while the previous word (prev) is NOT an ending word
    # (calculated based on the last character or the last 2 characters)
    while text[-1:] not in endings and text[-2:] not in endings:
        # pick a word to follow it from our next word dictionary, d
        cur = random.choice(d[prev])
        # add that word to the sentence
        text += " " + cur
        # overwrite the previous word
        prev = cur
    return text


# make 5 random sentences
for i in range(5):
    print(make_sentence())
