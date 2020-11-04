import os

input_text = os.path.join(os.path.dirname(__file__), 'cyphertext.txt')

# Read in all the words in one go
with open(input_text) as f:
    words = f.read()

lowercase_words = words.lower()
encrypted_dict = {}

# Get frequency of characters in encryption
for char in lowercase_words:
  if char.isalpha() != True:
    continue
  if char in encrypted_dict:
    encrypted_dict[char] += 1
  else:
    encrypted_dict[char] = 1

# Sort characters by frequency
sorted_encrypted_dict = {k: v for k, v in sorted(encrypted_dict.items(), key=lambda item: item[1], reverse=True)}

# Use sorted encryption dictionary to replace characters
encryption_key = ['e', 't', 'a', 'o', 'h', 'n', 'r', 'i', 's', 'd', 'l', 'w', 'u', 'g', 'f', 'b', 'm', 'y', 'c', 'p', 'k', 'v', 'q', 'j', 'x', 'z']
transfer_dict = {}
result = ""

# Create a tranfer Dictionary
for index, key in enumerate(sorted_encrypted_dict):
  transfer_dict[key] = encryption_key[index]

# Use Transfer dictionary to replace characters in CypherText.txt
for char in lowercase_words:
  if char.isalpha() != True:
    result += char
  if char in transfer_dict:
    result += transfer_dict[char]

print(result)
