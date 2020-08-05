# Your code here
import os
import re
f = open(f'{os.getcwd()}/applications/histo/robin.txt')
r = f.read()


def histo(s):
    cache = dict()
    words = re.findall('[A-Za-z\']+(?:\`[A-Za-z]+)?', r)
    for word in words:
        if word.lower() not in cache:
            cache[word.lower()] = 1
        else:
            cache[word.lower()] += 1
    words = sorted(cache.items(), key=lambda x: x[1], reverse=True)
    longest = len(sorted(cache.keys(), key=lambda x: len(x))[-1])
    for key, val in words:
        tower = ' ' * (longest - len(key)) + val * '#'
        print(f'{key}  {tower}')


histo(r)
