# Your code here
import os.path

# get the file path relative to the current script
input_txt = os.path.join(os.path.dirname(__file__), 'robin.txt')

# Read in all the words in one go
with open(input_txt) as f:
    words = f.read()

def word_count(s):
    dict = {}
    special_chars = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split()
    s2 = ''.join(c.lower() for c in s if not c in special_chars)
    for word in s2.split():
        dict[word] = dict[word] + 1 if word in dict else 1
    return dict

def print_histogram(dict):
    sortedItems = sorted(dict.items(), key=lambda x: (-x[1], x[0]), reverse=False)
    for item in sortedItems:
        print(f"{item[0]:<20} {'#'*item[1]}")

wordCountDict = word_count(words)
print_histogram(wordCountDict)
