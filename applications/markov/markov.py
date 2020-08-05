import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
words = words.split()
# print(words)

d = {}
s = []

for i in range(len(words)):
    w = words[i]
    start = False
    if w[0].isupper() or (w[0] == "\"" and w[1].isupper()):
        start = True
    if w not in d:
        d[w] = []
    if start and w not in s:
        s.append(w)
    if i < len(words) - 1:
        nextw = words[i + 1]
        d[w].append(nextw)

# print(d, "\n\n=====\n\n=====\n\n", s)


# TODO: construct 5 random sentences
# Your code here
endings = [".", "!", "?", ".\"", "!\"", "?\""]


def make_sentence():
    text = random.choice(s)
    prev = text
    while text[-1:] not in endings and text[-2:] not in endings:
        cur = random.choice(d[prev])
        text += " " + cur
        prev = cur
    return text


for i in range(5):
    print(make_sentence())
