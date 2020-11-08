import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# words = "Cats and dogs and birds and fish dogs birds."

# TODO: analyze which words can follow other words
dictionary = {}
word_list = words.split()

for index, word in enumerate(word_list):
    if word in dictionary:
        if index < len(word_list)-1:
            dictionary[word].append(word_list[index+1])
        else:
            continue
    else:
        if index < len(word_list)-1:
            dictionary[word] = [word_list[index+1]]


# print(dictionary)

# TODO: construct 5 random sentences
start_list = []
end_list = []
for word in word_list:
    if word[len(word)-2] in '.?!' or word[-1] in '.?!':
        end_list.append(word)
    elif (word[0] == '"' and word[1].isupper()) or word[0].isupper():
        start_list.append(word)


def createSentence():
    start = random.choice(start_list)
    print(start, end=" ")
    for s in dictionary[start]:
        print(s, end=" ")
        new_word = random.choice(dictionary[s])
        while new_word not in end_list:
            print(new_word, end=" ")
            new_word = random.choice(dictionary[new_word])
    print(new_word, end=" ")
    print("\n")


for i in range(5):
    print(f"SENTENCE {i+1} \n")
    createSentence()
# Your code here
# need to keep working on this.

# print(dictionary["King"])
