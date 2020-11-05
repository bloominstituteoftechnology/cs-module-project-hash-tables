import random

markov = {}

with open("input.txt", encoding="utf8") as f:
    words = f.read().strip().replace("\n", " ").split(" ")


for idx, word in enumerate(words):
    if idx < len(words)-1:
        # prevent completely empty strings which will throw out of bounds if you access their [-1]
        if word == "":
            word = " "
        elif words[idx+1] == "":
            markov[word] = " "
        else:
            markov[word] = words[idx+1]


def make_sentence():
    try:
        start = get_starting_word()
        sentence = start
        nxt = start
        last = words[-1]

        while nxt[-1] != "." or nxt[-1] != "?" or nxt[-1] != "!":
            if nxt == last:
                break

            nxt = markov[nxt]
            sentence += f" {nxt}"

            if sentence[-1] == "." or sentence[-1] == "?" or sentence[-1] == "!":
                break

        return sentence
    except: 
        pass


def get_starting_word():
    word = " "
    while word != "" and word[0] != '"' and word[0].isupper() == False:
        word = random.choice(words)

    return word


for i in range(100):
    print("")
    print(make_sentence())
