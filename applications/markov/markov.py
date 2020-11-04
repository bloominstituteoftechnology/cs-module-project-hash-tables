import random
import os.path

input_text = os.path.join(os.path.dirname(__file__), 'input.txt')

# Read in all the words in one go
with open(input_text) as f:
    words = f.read()

# print(words)
# TODO: analyze which words can follow other words
split_words = words.split()
word_dictionary = {}

for index, word in enumerate(split_words):
  if word not in word_dictionary and index != len(split_words) - 1:
    word_dictionary[word] = [split_words[index + 1]]
  elif word in word_dictionary:
    word_dictionary[word] += [split_words[index + 1]]

# print(word_dictionary)

# TODO: construct 5 random sentences
stop_chars = [".", "?", "!"]

for _ in range(5):
    begin_word = random.choice(list(word_dictionary.keys()))
    curr_word = begin_word
    sentence = ""

    while curr_word[-1] not in stop_chars:
        sentence += curr_word + " "
        word = word_dictionary[curr_word]
        curr_word = random.choice(list(word))

    print(sentence)
