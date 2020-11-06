import random
import re

start_condition = re.compile('^"?[A-Z]')
end_condition = re.compile('[.?!]"?$')

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

word_list = words.split()    

# TODO: analyze which words can follow other words
# Your code here
markov_dict = {}

for index, word in enumerate(word_list):
    if word not in markov_dict:
        if index + 1 < len(word_list):
            markov_dict[word] = [word_list[index + 1]]
        else:
            markov_dict[word] = [word_list[0]] 
    else:
        if index + 1 < len(word_list):
            markov_dict[word].append(word_list[index + 1])         

# TODO: construct 5 random sentencese
# Your code here
def markov_generator():
    start = False
    stop = False
    starts_with_apos = False
    ends_with_apos = False
    key_word = ''
    markov_sentence = ''

    while start == False:
        story_time = random.choice(list(markov_dict.keys()))
        if start_condition.search(story_time):
            key_word = story_time
            if key_word[0] == ' " ':
                starts_with_apos = True
            else:
                starts_with_apos = False    
                start = True

    current_word = key_word

    while stop == False:
        if end_condition.search(current_word):
            if current_word[len(current_word) - 1] == ' " ':
                ends_with_apos = True
            else:
                ends_with_apos = False
            markov_sentence += current_word + ' " ' if starts_with_apos and not ends_with_apos else current_word
            stop = True
        else:
            markov_sentence += current_word + ' ' 
            current_word = random.choice(markov_dict[current_word])     

    return markov_sentence

for i in range(5):
    print("")
    print(markov_generator())  
    print(" ")           

            



