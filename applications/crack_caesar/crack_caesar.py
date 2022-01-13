# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
import re
import os
cache = dict()
f = open(f'{os.getcwd()}/applications/crack_caesar/ciphertext.txt')
r = f.read()
frequencies = {'E': 11.53, 'T': 9.75, 'A': 8.46,
               "O": 8.08, 'H': 7.71, 'N': 6.73, 'R': 6.29, 'I': 5.84, 'S': 5.56, 'D': 4.74,
               'L': 3.92, 'W': 3.08, 'U': 2.59, 'G': 2.48, 'F': 2.42, 'B': 2.19, 'M': 2.18,
               'Y': 2.02, 'C': 1.58, 'P': 1.08, 'K': 0.84, 'V': 0.59, 'Q': 0.17, 'J': 0.07, 'X': 0.07,
               'Z': 0.03}


def crack_caesar():
    s = "".join(re.findall(r'[A-Z]', r))
    total = 0
    percentages = []
    lookup = {}
    output = ''
    for char in s:
        if char in cache:
            cache[char] += 1
        else:
            cache[char] = 1
        total += 1

    for key, val in cache.items():
        percentages.append([key, val / total * 100])

    for p in percentages:
        # print("key:", p[0], 'val:', p[1])
        for f in frequencies.items():
            if round(p[1], 2) == f[1]:
                if p[0] not in lookup:
                    lookup[p[0]] = f[0]

    for char in r:
        try:
            output += lookup[str(char)]
        except KeyError:
            output += char
    print(output)


crack_caesar()
