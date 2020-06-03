import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
words_list = words.split()
words_list

cache = {}

# Create cursor length of words_list, i
for i in range(len(words_list) - 1):
    
    # if word at words_list[cursor] is in the cache
    if words_list[i] in cache:
        # append next word from word_list to values
        cache[words_list[i]].append(words_list[i+1])
        
    # if word at words_list[cursor] is not in the cache    
    else:
        # add next word from word_list to values
        cache[words_list[i]] = [words_list[i+1]]

# TODO: construct 5 random sentences
# Your code here

# Pick random start word: Capital letter, or capital letter with leading quote sign <">

start_words = []
stop_words = []

punctuation = ['.', '?', '!']

# Creating start and stop words lists
for word in list(cache.keys()):
    
    # Logic for adding words to start words
    if (word[0].isupper() == True) or (word[0] == '"' and word[1].isupper() == True):
        start_words.append(word)
        
    # Logic for adding words to stop words
    if word[-1] in punctuation or word[-1] == '"':
        if (word[-1] in punctuation) or (word[-2] in punctuation and word[-1] == '"'):
            stop_words.append(word)

five_sentences = []

for _ in range(5):
    sentence = []

    start = random.choice(start_words)
    sentence.append(start)

    running = True
    while running:
        next_word = random.choice(cache[sentence[-1]])
        sentence.append(next_word)
        if next_word in stop_words:
            running = False
    five_sentences.append(' '.join(sentence))

print(five_sentences)
