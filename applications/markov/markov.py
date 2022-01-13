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
    i = 0
    start = None
    while i < len(lst):
        searched = re.findall(r'^"[A-Z][a-z]*|^[A-Z][a-z]*', lst[i][1])
        print(searched, 'searched')
        if searched:
            start = searched[0]
            break
        i += 1
    print(re.findall(r'^"[A-Z][a-z\,"]*|^[A-Z][a-z\,"]*', '"Hello"'))
# TODO: analyze which words can follow other words
# Your code here


# TODO: construct 5 random sentences
# Your code here
