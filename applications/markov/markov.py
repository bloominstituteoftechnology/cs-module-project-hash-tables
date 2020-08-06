import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

    my_list = []
    words = words.split()
    # print(words)
    for i in range(len(words) - 1):
        my_list.append((words[i], words[i + 1]))
    result = ''
    for k, v in my_list:
        if v[-1:] not in '. ? !'.split():
            if str(k[:1]).isupper() or k[:1] == '"':
                result += k + v
        print(result)
        # print(f"{k}: {v}")


# TODO: analyze which words can follow other words
# Your code here


# TODO: construct 5 random sentences
# Your code here
