import random
import string
from collections import defaultdict

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read().split()

# Analyze which words can follow other words.
start_words = []
stop_words = []
sequences = defaultdict(list)

for index, word in enumerate(words):

    # Start words are words that begin with a capital, or a " followed by a
    # capital.
    if word.lstrip('"')[0] in string.ascii_uppercase:
        start_words.append(word)

    # Stop words are words that end in any of the punctuation .?!, or that
    # punctuation followed by a ".
    if word.rstrip('"')[-1] in '.?!':
        stop_words.append(word)

    # All words except the last word in the text have a following word which
    # should be added to the bigram list. Duplicates are included by design.
    if index < len(words) - 1:
        sequences[word].append(words[index + 1])

# Construct 5 random sentences.
for i in range(5):

    # Start with a start word.
    s = random.choice(start_words)

    # Continue choosing a random next word from the list of followers until a
    # stop word is reached, separating words with spaces.
    if s not in stop_words:
        next_word = random.choice(sequences[s])
        while next_word not in stop_words:
            s += ' ' + next_word
            next_word = random.choice(sequences[next_word])
        s += ' ' + next_word

    # Ensure double quotation marks appear in matched pairs.
    if s.count('"') % 2 != 0:
        if s[-1] != '"':
            s += '"'
        else:
            s = '"' + s

    # Make sure opening and closing parentheses are balanced (but not
    # necessarily in the conventional order).
    if s.count('(') > s.count(')'):
        s += ')'
    elif s.count(')') > s.count('('):
        s = '(' + s

    print(s + '\n')
