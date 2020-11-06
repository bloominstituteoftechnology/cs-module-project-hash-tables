import random

# Read in all the words in one go
with open("applications/markov/input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
    word_list = words.split()

    markov = {}

    last_word = None
    for index in range(1, len(word_list)):
        last_word = word_list[index - 1]
        word = word_list[index]
        if last_word not in markov.keys():
            markov[last_word] = [word]
        else:
            markov[last_word].append(word)

    # print(markov)
# TODO: construct 5 random sentences
    select_word = word_list[random.randint(0, len(word_list)-1)]
    sentence = select_word + " "
    for word in range(20):
        words = markov[select_word]
        select_word = words[random.randint(0, len(words)-1)]
        sentence += select_word + " "

    print("")
    print(sentence)

    select_word = word_list[random.randint(0, len(word_list)-1)]
    sentence = select_word + " "
    for word in range(20):
        words = markov[select_word]
        select_word = words[random.randint(0, len(words)-1)]
        sentence += select_word + " "

    print("")
    print(sentence)

    select_word = word_list[random.randint(0, len(word_list)-1)]
    sentence = select_word + " "
    for word in range(20):
        words = markov[select_word]
        select_word = words[random.randint(0, len(words)-1)]
        sentence += select_word + " "

    print("")
    print(sentence)

    select_word = word_list[random.randint(0, len(word_list)-1)]
    sentence = select_word + " "
    for word in range(20):
        words = markov[select_word]
        select_word = words[random.randint(0, len(words)-1)]
        sentence += select_word + " "

    print("")
    print(sentence)

    select_word = word_list[random.randint(0, len(word_list)-1)]
    sentence = select_word + " "
    for word in range(20):
        words = markov[select_word]
        select_word = words[random.randint(0, len(words)-1)]
        sentence += select_word + " "

    print("")
    print(sentence)
