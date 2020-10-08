import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# Analyze which words can follow other words
words = words.replace("\n", " ")
wordArr = words.split(' ')
word_cache = {}

for i in range(len(wordArr)):
    if wordArr[i] is "" or wordArr[i + 1] is "":
        continue

    if wordArr[i] in word_cache:
        word_cache[wordArr[i]].append(wordArr[i + 1])
    else:
        word_cache[wordArr[i]] = [wordArr[i + 1]]

# Construct 5 random sentences
start_words = []
stop_words = []

for word in list(word_cache.keys()):
    if word[0].isupper():
        start_words.append(word)
    
    if len(word) > 1 and word[0] is '"' and word[1].isupper():
        start_words.append(word)
    
    if word[len(word) - 1] in '.?!' or (word[len(word) - 1] is '"' and word[len(word) - 2] in '.?!'):
        stop_words.append(word)

sentence = [random.choice(start_words)]

def create_sentence():
    sentence = [random.choice(start_words)]

    if sentence[0] in stop_words:
        result = ' '.join(sentence)
        return result
      
    while sentence[len(sentence) - 1] not in stop_words:
        try:
            sentence.append(next_word(word_cache[sentence[len(sentence) - 1]]))
        except KeyError:
            result = ' '.join(sentence)
            return result
    
    result = ' '.join(sentence)
    return result

def next_word(word_list):
    random_word = random.choice(word_list)
    return random_word

print(create_sentence())
print(create_sentence())
print(create_sentence())
print(create_sentence())
print(create_sentence())