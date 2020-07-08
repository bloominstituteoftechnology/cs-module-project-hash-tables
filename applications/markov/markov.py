import random

# Read in all the words in one go
with open("applications/markov/input.txt") as f:
    words = f.read()
    inp = words.split() # splits input text into words
    

# TODO: analyze which words can follow other words
# Your code here
def make_pairs(arr):
    for i in range(len(arr) - 1):
        yield (arr[i], arr[i + 1]) # loops through the entire array and gives the word and word following it.
pairs = make_pairs(inp)
word_dict = {}
for word_1, word_2 in pairs: # adds the word pairs to the dictionary
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]
f_word = random.choice(inp)
l_word = random.choice(inp)
while f_word.islower() and f_word[0] != '"': # stop word
    f_word = random.choice(inp)
while l_word[-1] not in ['.', '!', '?']: # these are stops words
    l_word = random.choice(inp)
first = [f_word]
last = [l_word]
num_words = 150
for i in range(num_words):
    first.append(random.choice(word_dict[first[-1]]))
print(' '.join(first + last))
# TODO: construct 5 random sentences
# Your code here

