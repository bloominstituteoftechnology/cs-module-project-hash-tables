# make it run, make it right, make it fast

# UPER

# Understand


# Plan

# 1. Read the file input.txt and split it into words
# already read in
# split into words

# 2. Analyze the text, building up the dataset of which words can follow
# which words can follow a word? any word that actually does
# any word at index - 1
# How to build a dataset??

# Use a hashtable
# good way to to relate one piece of info, with other info. relational
# Frequent lookups
# Key: word, value: list of all the words that can follow this word

# 3. Choose a random start word to begin
# What is a start word??
# First or second character is capitalized

# Make a list of start words

# 4. Loop through, choose a randow following word, if it is a stop word stop
# What is a stop word?
# Ends with a .?! or second to last character is punctuation


# Split into words
split_words = words.split()
# if you do not give .split() a parameter then it will split the entire string on spaces

# Create hashtable
dataset = {}

for i in range(len(split_words) - 1):
    word = split_words[i]
    next_word = split_words[i + 1]

    if word not in dataset:
        dataset[word] = [next_word]

    else:
        dataset[word].append(next_word)

# Choose a random start word to begin
# Make a list of start words
# If first or second character is capitalized, put into list
# Loop over our split_words and put any start word into a list

start_words = []

for key in dataset.keys():
    if key[0].isupper() or len(key) > 1 or key[1].isupper():
        start_words.append(key)

word = random.choice(start_words)

stopped = False

stop_signs = "?.!"

while not stopped:
    print(word, end=" ")

    if word[-1] in stop_signs or len(word) > 1 and word[-2] in stop_signs:
        stopped = True

    # Choose a random following word
    following_words = dataset[word]

    word = random.choice(following_words)
