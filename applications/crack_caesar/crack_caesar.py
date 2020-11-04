import os

input_text = os.path.join(os.path.dirname(__file__), 'cyphertext.txt')

# Read in all the words in one go
with open(input_text) as f:
    words = f.read()

lowercase_words = words.lower()
encrypted_dict = {}

for char in lowercase_words:
  if char.isalpha() != True:
    continue
  if char in encrypted_dict:
    encrypted_dict[char] += 1
  else:
    encrypted_dict[char] = 1

sorted_encrypted_dict = {k: v for k, v in sorted(encrypted_dict.items(), key=lambda item: item[1], reverse=True)}
