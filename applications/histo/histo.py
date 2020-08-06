# Your code here
#words = s.translate(str.maketrans('', '', string.punctuation))
import string

with open('robin.txt') as f:
    txt = f.read()
    words = txt.translate(str.maketrans('', '', string.punctuation))
    print(words)

words = words.split()
# print(words)

frequency_dict = {}

for word in words:
    if word in frequency_dict:
        frequency_dict[word] += '#'
    else:
        frequency_dict[word] = '#'

# print(frequency_dict)

for word in sorted(frequency_dict, key=lambda k: len(frequency_dict[k]), reverse=True):
    print(word, (' ' * (15 - len(word))), frequency_dict[word])