import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read().strip().replace("\n", " ").split(" ")
    # print(words)

# TODO: analyze which words can follow other words
# Your code here

d = dict()

for i in range(len(words) - 1):
    word = words[i]
    next_word = words[i + 1]

    if word not in d:
        d[word] = [next_word]

    else:
        d[word].append(next_word)

# print(d)


# TODO: construct 5 random sentences
# Your code here

start_list = []

for key in d.keys():
    if key[0].isupper() and len(key) > 1 or key[1].isupper():
        start_list.append(key)

random_word = random.choice(start_list)

stopped = False

stop_list = '.?!'

while not stopped:
    print(random_word, end=" ")

    if random_word[-1] in stop_list and len(random_word) > 1 or random_word[-2] in stop_list:
        stopped = True

    words_to_follow = d[random_word]

    follow_word = random.choice(words_to_follow)
