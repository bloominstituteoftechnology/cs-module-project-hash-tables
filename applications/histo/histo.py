# Your code here
import re

with open("robin.txt") as histo:
    words = histo.read()#opens the file

cache = {}
low = words.lower()#makes words lower case
word_list = re.sub('["\\:\\;\\,\\.\\-\\+\\=\\/\\\\|\\[\\]\\{\\}\\(\\)\\*\\^\\&\\\'\\!]', '', low)#ignore list
new_words = word_list.split()
#print(new_words)
#print(word_list)
for word in new_words:
    if word in cache:
        cache[word] += '#'#gives # to the words
    else:
        cache[word] = '#'
word_count = list(cache.items())
word_count.sort (key=lambda  item:item[1], reverse=True)#reverses

#print(word_count)

for (key, value) in word_count:
    print(f'{key:18} {value}')#18 spaces

