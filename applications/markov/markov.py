import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
word_list = words.split()
# TODO: analyze which words can follow other words
# Your code here
# make a dictionary and the value is a list that you can append following words
following = {}
for i, value in enumerate(word_list):
    if value not in following:
        following[value] = []
    if i < len(word_list) - 1:
        following[value].append(word_list[i+1])

# TODO: construct 5 random sentences
# Your code here
def write_sentence():
    # choose between all capital words, regardless of ""
    start_word = random.choice([x.strip('"') for x in word_list if x[0].isupper()])

    # need a while loop to add to a sentence
    sentence = start_word
    # consult dict at random for next word
    next_word = random.choice(following[start_word])

    while not next_word.endswith(tuple('.?!')):
        # take the prev next word and go thru the dict again
        next_word = random.choice(following[next_word])
        sentence += f" {next_word}"
    return sentence

print(write_sentence())
print(write_sentence())
print(write_sentence())
print(write_sentence())