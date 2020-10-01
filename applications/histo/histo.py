# Your code here
ignore = ['\"', ':', ';', ',', '.', '-', '+', '=', '/', "\\", '|', '[', ']', '{', '}', '(', ')', '*', '^', '&', '!', '?']


with open('robin.txt') as f:
    text = f.read().lower()

for char in ignore:
    text = text.replace(char, "")

word_dict = {}

for word in text.split():
    if word in word_dict:
        word_dict[word] += "#"
    else:
        word_dict[word] = "#"

for word in sorted(word_dict, key=lambda x: len(word_dict[x]), reverse=True):
    print(word, (' ' * (15 - len(word))), word_dict[word])