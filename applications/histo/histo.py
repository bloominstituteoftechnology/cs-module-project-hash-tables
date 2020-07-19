import re

# Your code here
#import the text
with open("robin.txt") as f:
    words = f.read()

#convert to lower, strip the special chars and split the list   
lower_case = words.lower()
new_list = re.sub('["\\:\\;\\,\\.\\-\\+\\=\\/\\\\|\\[\\]\\{\\}\\(\\)\\*\\^\\&]', '', lower_case)
new_words = new_list.split()

#set the histogram dict
histogram = {}
    
for word in new_words:
    #if word is not in histogram, add it
    if words not in histogram:
        histogram[word] = "#"
    #if it is, add one
    else:
        histogram[word] += "#"

#list the items in histogram dict
word_occurrence = list(histogram.items())
#using lambda expression, sort by key and list in reverse
word_occurrence.sort(key=lambda x: x[1], reverse=True)

#print here
for (key, value) in word_occurrence:
    print(f'{key} : {value}')