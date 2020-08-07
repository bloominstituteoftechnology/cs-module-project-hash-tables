import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

split_words = words.split()


dataset = {}
for i in range(len(split_words) - 1):
    word = split_words[i]
    next_word = split_words[i + 1]
    if word not in dataset:
        dataset[word] = [next_word]
    else:
        dataset[word].append(next_word)

start_words = []
for key in dataset.keys():
    if key[0].isupper() or len(key) > 1 and key[1].isupper():
        start_words.append(key)

word = random.choice(start_words)

stopped = False
stop_signs = ".?!"
while not stopped:
    print(word)

    if word[-1] in stop_signs or len(word) > 1 and word[-2] in stop_signs:
        stopped = True
    following_words = dataset[word]

    word = random.choice(following_words)


# loop through split_words, for ea word in split_words:
# split into words
# analyze the text, building up the dataset of which words to follow
# Which words can follow a word? Any word the actually follows a word
#index + 1
# How to build dataset? Hashtable -> good way to relate pairs of data/fast look up.
# key: word, value: list of words that follow the word
# Choose a random "start word" to begin.
# What is a start word?
# 1st of 2nd character is capitalized

# make a list of start words (cache)

# loop through
# print, choose a random following word, if it is a stop word, stop
#    ##What's a stop word?
#      #a word followed by '.?!'or if second to last character is


# TODO: analyze which words can follow other words
# Your code here


# TODO: construct 5 random sentences
# Your code here


# 1. Read the file `input.txt` and split it into words.

# Don't worry about changing punctuation or capitalization. For
# example, a "word" might be `"Hello, `. Just leave it all in there.

# 2. Analyze the text, building up the dataset of which words can follow
# particular words.

# (Hint: leave duplicates in for this part. If a the word `and` is seen
#  following the word `goats` multiple times, include all those `and`s.
#  It'll give more convincing results because it is modelling the
#  _frequency_ of _how often_ a word follows another word.)

# 3. Choose a random "start word" to begin.

# 4. Loop through:

#    * Print the word.
#    * If it's a "stop word", stop.
#    * Else randomly choose a word that can follow this one.

# Start words are words that begin with a capital, or a `"` followed by a
# capital.

# Stop words are words that end in any of the punctuation `.?!`, or that
# punctuation followed by a `"`.

# Hints:

# * `random.choice()` can choose a random word out of a list.
# * `print(s, end=" ")` will print a space after every word instead of a
# newline.

# There is no test file for this. Just see if it makes good nonsense.


# Split all words into an array

# Loop through array of split words, for each element
# cache to track keys that have used
# build a dict using the first word as key and second as value
#
