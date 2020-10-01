import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    # print(words)

# TODO: analyze which words can follow other words
# Your code here

split_words = words.split()

d = dict()

for i in range(len(split_words) - 1):
    word = split_words[i]
    next_word = split_words[i + 1]

    if word not in d:
        d[word] = [next_word]

    else:
        d[word].append(next_word)

# print(d)


# TODO: construct 5 random sentences
# Your code here

start_list = []

for key in d.keys():
    # print(key)
    if key[0].isupper() or len(key) > 1 and key[1].isupper():
        start_list.append(key)

random_word = random.choice(start_list)

stopped = False

stop_list = ".?!"

while not stopped:
    print(random_word)

    if random_word[-1] in stop_list or len(random_word) > 1 and random_word[-2] in stop_list:
        stopped = True

    words_to_follow = d[random_word]

    follow_word = random.choice(words_to_follow)
