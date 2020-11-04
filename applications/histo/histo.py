import os
import collections

input_text = os.path.join(os.path.dirname(__file__), 'robin.txt')

# Read in all the words in one go
with open(input_text) as f:
    words = f.read()

lower_case_words = words.lower()
split_words = lower_case_words.split()
dictionary = {}
largest_word = 0

for word in split_words:
  if len(word) > largest_word:
    largest_word = len(word)
  if word not in dictionary:
    dictionary[word] = 1
  elif word in dictionary:
    dictionary[word] += 1

sorted_dictionary = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1], reverse=True)}

for key, value in sorted_dictionary.items():
  hash_number = "#" * value
  space = largest_word + 2
  print(f"{key:{space}} {hash_number}")
