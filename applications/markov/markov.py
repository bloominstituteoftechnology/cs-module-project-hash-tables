import random

# Read in all the words in one go
with open("applications/markov/input.txt") as f:
    words = f.read()
words = words.split(' ')

# TODO: analyze which words can follow other words
# Your code here
follow = {}
for i in range(len(words)):
    if words[i] not in follow:
        if i == len(words) - 1:
            follow[words[i]] = [words[0]]
        else:
            follow[words[i]] = [words[i+1]]
    else:
        follow[words[i]].append(words[i+1])
# print(follow)
# TODO: construct 5 random sentences
# Your code here

def make_sentence(length=False):
    current = random.choice(words)
    curlen = 0
    STARTS_WITH_CAP = current[0].islower() or (current[0] == '"' and current[1].islower())
    ENDS_WITH_PUNC = current.endswith(('.','?','!','".','"?','"!'))
    IS_OF_DESIRED_LENGTH = curlen >= length if length else True
    while STARTS_WITH_CAP:
        current = random.choice(words)
        STARTS_WITH_CAP = current[0].islower() or (current[0] == '"' and current[1].islower())
    while not (ENDS_WITH_PUNC and IS_OF_DESIRED_LENGTH):
        print(current, end=' ')
        curlen += len(current)
        current = random.choice(follow[current])
        ENDS_WITH_PUNC = current.endswith(('.','?','!','".','"?','"!'))
        IS_OF_DESIRED_LENGTH = curlen >= length if length else True
    print(current)
    print(f'\n\n------- End of sentence {curlen}------\n\n')
    return curlen

for i in range(5):
    make_sentence()