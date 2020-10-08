# Your code here
import os.path
input_txt = os.path.join(os.path.dirname(__file__), 'robin.txt')

with open(input_txt) as f:
    words = f.read()
    # print(words)

def word_count(s):
    # Your code here
    dict = {}
    special_char = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split()
    ss = "".join(c.lower() for c in s if not c in special_char).split()
    for word in ss:
        dict[word] = dict[word] + 1 if word in dict else 1
    return dict 

def print_histogram(dict):
    sortedItems = sorted(dict.items(), key=lambda x: (-x[1], x[0]))
    for item in sortedItems:
        print(f"{item[0]:<20} {'#'*item[1]}") 


wordCountDict = word_count(words)
print_histogram(wordCountDict)