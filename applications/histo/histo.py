# Your code here
import re

def histogram(filename):
    with open(filename) as f:
        words = f.read()

    words1 = re.sub('":;,.-+=/\[|]\{\}()*^&', "", words.replace("\n", " "))
    word_list = words1.split() # no punct list

    longest = "" # loop to find longest word
    word_counts = {} # add all words to dict
    for word in word_list:

        if len(word) > len(longest):
            longest = word

        if word not in word_counts:
            word_counts[word] = ""
        word_counts[word] += "#"
    
    num_left_chars = len(longest) + 2

    count_list = list(word_counts.items()) # turn dictionary into list
    count_list.sort() # sort by word
    count_list.sort(key=lambda x: x[1], reverse=True) # sort by hashes
    for w, c in count_list:
        # print the word, number of spaces, hashes
        print(w, " " * (num_left_chars- len(w)), c)


print(histogram("robin.txt"))