import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    words = words.split()

# TODO: analyze which words can follow other words
def make_pairs(arr):
    for i in range(len(arr) - 1):
        yield (arr[i], arr[i + 1])

pairs = make_pairs(words)
word_dict = {}
for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

first_word = random.choice(words)
last_word = random.choice(words)

while first_word.islower() and first_word[0] != '"':
    first_word = random.choice(words)
while last_word[-1] not in ['.', '!', '?']:
    last_word = random.choice(words)

chain = [first_word]
lword = [last_word]
n_words = 100

for i in range(n_words):
    chain.append(random.choice(word_dict[chain[-1]]))
print(' '.join(chain + lword))


# TODO: construct 5 random sentences
# Your code here
