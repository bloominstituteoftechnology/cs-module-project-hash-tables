import random
from collections import defaultdict


# Read in all the words in one go
# with open("input.txt") as f:
with open("applications/markov/input.txt") as f:
    words = f.read().split()

# TODO: analyze which words can follow other words
# Your code here
# print(words)

end_punc = ".?!"
start_w = []
stop_w = []
freq_dict = defaultdict(list)

for index, word in enumerate(words):
    # find  start words, must have first char capitalized
    if word[0].isupper():
        start_w.append(word)

    # end words have either .?! at end, check last char
    if word[-1] in end_punc:
        stop_w.append(word[:-1])  # slice off that punc

    # use enumerate to track index
    if index < len(words) - 1:
        freq_dict[word].append(words[index + 1])

# print(f' >>>>>>>>>> start_w :  {start_w}')
# for k,v in freq_dict.items():
#     print(f' key {k}: {v} \n')


#  print(freq_dict)
# TODO: construct 5 random sentences
# Your code here

for line in range(10):

    s = random.choice(start_w)
    if s not in stop_w:
        # loop up a random word in freq_dict
        next_w = random.choice(freq_dict[s])

        # check if not stop_w
        while next_w not in stop_w:
            s += " " + next_w
            # try another word
            next_w = random.choice(freq_dict[next_w])
        s += " " + next_w
    s += s + random.choice(end_punc)
    print(f' Sentence: {s}')    