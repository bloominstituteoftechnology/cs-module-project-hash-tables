import random

# Read in all the words in one go

starts = { '"' }
ends = { '?', '!', '"', '.' }
start_words = {}
words = {}


with open("input.txt") as f:
    text = f.read()
    text = text.replace('\n', ' ')
    curr_ht = words
    prev_ht = {}
    curr_word = ''
    prev_word = ''
    for char in text:
        if ord(char) >= 65 and ord(char) <= 90:
            curr_ht = start_words
        if char == ' ':
            if curr_word not in curr_ht:
                curr_ht[curr_word] = []
            if prev_word:
                prev_ht[prev_word].append(curr_word)
            prev_word = curr_word
            prev_ht = curr_ht
            curr_word = ''
            curr_ht = words
        else:
            curr_word += char

def gobbledegook(length, start_words, words):
    # for i in range(length):
    starting_word = random.choice(list(start_words.keys()))
    
    print(starting_word)

gobbledegook(100, start_words, words)


# TODO: analyze which words can follow other words
# Your code here


# TODO: construct 5 random sentences
# Your code here

