import random

# Read in all the words in one go
# with open("input.txt") as f:
#     words = f.read()
with open("/Users/ekselan/Desktop/LAMBDA/CS-2/hash_tables/applications/markov/input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here

# Make list out of the words
word_list = words.split()

# can use dict with val being a list
cache = {}

# enumerate word list to get index
for i, v in enumerate(word_list):

    # if not in cache, update cache with empty list to hold vals
    if v not in cache:
        cache[v] = []

    # as long as there are items left in list, add them to cache
    if i < len(word_list) - 1:
        cache[v].append(word_list[i+1])


# TODO: construct 5 random sentences
# Your code here

# can write function to generate sentences
def write_sentence():

    # start words are all capital words, regardless of punct
    start_word = random.choice([x.strip('"') for x in word_list if x[0].isupper()])

    # can add start making sentences with start word (sent += something)
    sent = start_word

    # get next word from cache
    next_word = random.choice(cache[start_word])

    # add condition to ensure next word isn't stop word
    while not next_word.endswith(tuple('.?!')):

        # keep generating next words until stop word is reached
        next_word = random.choice(cache[next_word])
        sent += f" {next_word}"

    return sent

# print(words)

if __name__ == "__main__":
    
    print("---" * 5 + "BEGIN" + "---" * 5)
    print(write_sentence())
    print("---" * 10)
    print(write_sentence())
    print("---" * 10)
    print(write_sentence())
    print("---" * 10)
    print(write_sentence())
    print("---" * 10)