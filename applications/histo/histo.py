# Open and the file
with open('robin.txt') as f:
    texts= f.read()
#split the text
words = texts.lower().split()
#create a dictionary for the word count
histogram ={}
#ignore character
ignore_char = ' " : ; , . - + = / \ | [ ] { } ( ) * ^ & '
for word in words:
    for char in word:
        if char in ignore_char:
            word = word.replace(char, '')
    if word not in histogram:
        histogram[word] = '#'
    else:
        histogram[word] += '#'
for key, value in sorted(histogram.items(), key = lambda item: (item[1]), reverse =True):
    print(f'{key} :{value}')



