import random

# Read in all the words in one go
# with open("input.txt") as f:
# the following "applications/markov/input.txt" is the only way
#  I could get code to read the input.txt file
with open("applications/markov/input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
split_words = words.split()
dict = {}

for i, word in enumerate(split_words):
    if i+1 < len(split_words):
        if word not in dict:
            dict[word] = [split_words[i+1]]
        else:
            dict[word].append(split_words[i+1])


# TODO: construct 5 random sentences
# Your code here
def generate():
    sentence = []
    while True:
        starter = random.choice(list(dict.keys()))
        # tried to shorten follwoing line but kept getting syntax errors at end of )
        if str(starter[0]).isupper() and not str(starter).endswith(".") and not str(starter).endswith("?") and not str(starter).endswith("!") and not str(starter).endswith("\""):
            sentence.append(starter)
            break
    while True:
        sentence_word = random.choice(dict[sentence[len(sentence)-1]])
        # tried to shorten follwoing line but kept getting syntax errors at end of )
        if str(sentence_word).endswith(".") or str(sentence_word).endswith("?") or str(sentence_word).endswith("!") or str(sentence_word).endswith(".\"") or str(sentence_word).endswith("?\"") or str(sentence_word).endswith("!\""):
            sentence.append(sentence_word)
            break
        sentence.append(sentence_word)
    return ' '.join(sentence)

for i in range(5):
    print(generate())




 