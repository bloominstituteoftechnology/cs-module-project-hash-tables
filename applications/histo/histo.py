# Your code here
import re

with open('robin.txt') as f:
    words = f.read()

histogram = {}

lowered = words.lower()
new_list = re.sub('["\\:\\;\\,\\.\\-\\+\\=\\/\\\\|\\[\\]\\{\\}\\(\\)\\*\\^\\&\\\'\\!]', '', lowered)
new_words = new_list.split()

for word in new_words:
    if word in histogram:
        histogram[word] += "#"
    else:
        histogram[word] = "#"

word_occurrence = list(histogram.items())

word_occurrence.sort(key=lambda x: x[1], reverse=True)

for (key, value) in word_occurrence:
    print(f'{key:18} {value}')