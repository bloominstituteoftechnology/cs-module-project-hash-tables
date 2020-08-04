import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    f.close()

words = words.split(' ')

# TODO: analyze which words can follow other words

pairs = []
for x in range(len(words) - 1):
    pairs.append((words[x], words[x+1]))

chains = {}
for x in pairs:
    if x[0] in chains.keys():
        chains[x[0]].append(x[1])
    else:
        chains[x[0]] = [x[1]]

# TODO: construct 5 random sentences

for _ in range(5):
    start = [random.choice(words)]
    print('\n')
    for _ in range(30):
        start.append(random.choice(chains[start[-1]]))
    print(' '.join(start), end=' ')
    print('\n')

