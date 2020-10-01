import random

# markov_me is function that returns a Markov Chain "sentence" given a initial word
def markov_me(wrd):
    # Initialize the return string source array
    ret_arr = []

    # Capitalize the first word
    ret_arr.append(wrd)

    while True:
        # Have we encountered a stop word?
        if (ret_arr[-1][-1] in [".", "?", "!"]) or (ret_arr[-1][-2:] in ['."', '?"', '!"']):
            # Encountered a stop word... break out of processing loop
            break

        # Grab a word that can follow the last word in our sentence array
        tmp_list = word2words[ret_arr[-1]]
        # Randomly pick a "next" word
        ret_arr.append(random.choice(tmp_list))

    return " ".join(ret_arr).capitalize()

#* Main Processing
# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# Define a word analysis map ("<string>": "<list>")
word2words = {}

# Iterate through the input string
arr_words = words.split()
for idx, wrd in enumerate(arr_words):
    # Are we a the end of the word list?
    if idx == len(arr_words)-1:
        # At the end of the list, break the loop
        break

    # Is the word in our analysis map?
    if wrd not in word2words:
        # Encountered a new word, add to our map
        word2words[wrd] = []

    # Grab the next word
    wrd_next = arr_words[idx+1]
    # Associate the next word with the word being iterated on
    word2words[wrd].append(wrd_next)

# Generate Markov Chains given a random input word
print("")
for i in range(5):
    lne = i + 1
    print(f'Chain-{lne}: {markov_me(random.choice(arr_words))}\n')

