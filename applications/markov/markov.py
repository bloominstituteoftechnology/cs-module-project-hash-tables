import random

dictionary = {}
l = []
previousWord = ""
begin = False
with open('input.txt', 'r') as f:
    for line in f:
        for word in line.split():
            if begin == True:
                # print("Previous word:", previousWord)
                # print("Current word:", word)

                if previousWord in dictionary:
                    # print("---HIT---")
                    l = dictionary[previousWord]
                    l.append(word)
                    # print(l)
                    dictionary[previousWord] = l
                    l = []
                else:
                    # print("---MISS---")
                    dictionary[previousWord] = l
                # print()
                previousWord = word
            else:
                previousWord = word
                begin = True

punc = [".", "!", "?", "\""]
# print(dictionary)

def print_sentence():
    x = dictionary.keys()
    # print(x)
    startWords = []
    middleWords = []
    for item in x:
        if item[0].isupper():
            startWords.append(item)
        if item[0].islower():
            middleWords.append(item)

    newSentence = True
    counter = 0
    while counter < 5:
        if newSentence:
            word = random.choice(startWords)
            print(word, end= " ")
            newSentence = False
        else:
            l = dictionary[word]
            if len(l) == 0:
                word = random.choice(middleWords)
            else:
                word = random.choice(l)
            print(word, end= " ")


            if word[-1] in punc:
                newSentence = True
                counter += 1

        # l = dictionary[word]
        # word = random.choice(l)
        # print(word, end= " ")
        #
        # l = dictionary[word]
        # word = random.choice(l)
        # print(word, end=" ")


print_sentence()
