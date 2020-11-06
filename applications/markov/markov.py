import random
import numpy as np

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    corpus = words.split()

def get_current_and_next(word_list):
    # for each word in our word list
    for i in range(len(word_list) - 1):
        # iterate over without storing
        # can produce a sequence of values
        yield (word_list[i], word_list[i+1])

current_and_next = get_current_and_next(corpus)

d = {}

# grab the two values from the gen obj
for current_word, next_word in current_and_next:
    # if current word is already a key
    if current_word in d.keys():
        # add another 'next' word
        d[current_word].append(next_word)
    else:
        # create a key where value is a list of next words 
        d[current_word] = [next_word]

num_of_words = 100

# generate a start word
start_word = np.random.choice(corpus)
# create the first word of the chain
markov_chain = [start_word]
for i in range(num_of_words):
    # access the values from the latest word's key in the dict
    newest_word_choices = d[markov_chain[-1]]
    # add a new word to the chain by grabbing one of the possible values
    markov_chain.append(np.random.choice(newest_word_choices))
print(' '.join(markov_chain))


# sentences:

"""
last to see how she began writing for him, and down on her sister, who was far as our fire in time without fifty dinners at me!" 
she held the black kitten's fault entirely. 
For the window with great curiosity to look as if we were playing just the poor King was in the King, so wide open! 
All the boys getting larger and then she was nearly sure they had got all knots and had
"""

# with 100 words

"""
running after its face this led to know you know, I turned cold to find one. 
"Blew--me--up," panted the King and fields, that there was all your feelings!" 
There was so cold, and Alice said, because the tail just now, as she called out to wind blows--
oh, that's very first thing down among the door of use, and, as different as soon as soon as if you're not been reduced at once! 
Well, I can only two and then she could find that she went on the old nurse by the kitten had been rolling it was--'and if the King took
"""