import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

words = ''.join([i for i in words if not i.isdigit()]).replace("\n", " ").split(' ')

# TODO: analyze which words can follow other words
index = 1
chain = {}

for word in words[index:]:
    key = words[index - 1]
    if key in chain:
        chain[key].append(word)
    else:
        chain[key] = [word]
    index += 1


# TODO: construct 5 random sentences

for i in range(5):
    word1 = random.choice(list(chain.keys()))
    while (word1[0].isupper() is False):
        if word1[0] == '\"' and len(word1) > 1:
            if word1[1].isupper() is True:
               break
        word1 = random.choice(list(chain.keys()))
    message = word1

    while (word1.endswith('.') is False) and \
          (word1.endswith('?') is False) and \
          (word1.endswith('!') is False):
        if word1.endswith('\"') is True:
            str_len = len(word1)
            if (word1[str_len - 1] == '.') or \
               (word1[str_len - 1] == '?') or \
               (word1[str_len - 1] == '\"'):
                break
        word2 = random.choice(chain[word1])
        word1 = word2
        message += ' ' + word2

    print(message)
    print(' ')
