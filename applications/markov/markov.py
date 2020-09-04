import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    
texts = words.split(' ')   
# TODO: analyze which words can follow other words
word_dic ={}
for i  in range(len(texts)-1):
    if texts[i] not in word_dic:
       word_dic[texts[i]] = [texts[i+1]]
    else:
        word_dic[texts[i]].append(texts[i+1])

start_words =[]
stop_words =[]
for word in word_dic:
    if word[0].isupper() or word[0] == '"':
        start_words.append(word)
    if word[-1] in '.?!':
        stop_words.append(word)
    if len(word)>2:
        if (word[-2] in '.?!') and word[-1] =='"':
            stop_words.append(word)

       

#  start with capital letter or "
# for key in word_dic:

# # start_words 
start = random.choice(list(word_dic))

for i in range(5):
    if start in stop_words:
        continue
    else:
       start =  random.choice(word_dic[start])
       for value in word_dic[start]:
           print(value, end = ' ')
    



# TODO: construct 5 random sentences
# Your code here

