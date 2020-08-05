import random
import os
import re

# Read in all the words in one go
d = dict()
with open(f"{os.getcwd()}/applications/markov/input.txt") as f:
    words = re.findall(r'[A-Za-z\']+(?:\`[A-Za-z]+)?', f.read())

    for idx, word in enumerate(words):
        try:
            if word not in d:
                d[word] = words[idx + 1]
            else:
                d[word] += f' {words[idx + 1]}'
        except IndexError:
            pass
    lst = list(d.items())
    while True:
        choice = random.choice(lst)
        print(choice)
        result = None
        while not result:
            searched = re.findall(r'[A-Z]*', choice[1])
            if searched:
                result = searched[1]
            break
        print(result)
# TODO: analyze which words can follow other words
# Your code here


# TODO: construct 5 random sentences
# Your code here
