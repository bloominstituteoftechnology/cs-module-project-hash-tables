import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here

#split the words from text and set up word dictonary
split_words = words.split()
word_dict = {}

for i in range(len(split_words)):
    #if the word is not in the word dict - dict is empty
    if split_words[i] not in word_dict:
        word_dict[split_words[i]] = []
    
    #instead of else - we're going to try to append the split words into the dict
    try:
        word_dict[split_words[i]].append(split_words[i + 1])
    except IndexError:
        break    

# TODO: construct 5 random sentences
# Your code here
#punctuation to be aware of
punctuation = (".", "?", "!", '."', '?"', '!"')

def make_sentance(name):
    # print a space after name
    print(name, end=" ")
    
    #if the name ends with the punctuation defined - new line and break out of if statement
    if name.endswith(punctuation):
        print ('\n')
        return 
    else:
        # if not - randomly choose words for the sentance       
        make_sentance(random.choice(word_dict[name]))
    
    

make_sentance("Alice")
make_sentance("Queen")
make_sentance("King")
make_sentance("One")
make_sentance("Dinah")