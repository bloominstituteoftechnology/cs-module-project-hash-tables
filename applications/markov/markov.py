import random

# Read in all the words in one go

starts = { '"' }
ends = { '?', '!', '"', '.' }
start_words = {}
words = {}


with open("input.txt") as f:
    words = f.read()
    curr_ht = words
    curr_word = ''
    prev_word = ''
    for char in words:
        if ord(char) >= 65 and ord(char) <= 90:
            curr_ht = start_words
        if letter == ' ':
            if curr_word not in curr_ht:
                curr_ht[curr_word] = []
            if prev_word:
                prev_word.append(curr_word)
            prev_word = curr_ht[curr_word]
            curr_word = ''
        curr_word += char
    



# TODO: analyze which words can follow other words
# Your code here


# TODO: construct 5 random sentences
# Your code here

