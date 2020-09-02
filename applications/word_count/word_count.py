import re

def word_count(s):
    # Your code here
    words = {}
    special_characters = r"""!"#$%&"()*+,-./:;<=>?@[\]^_`{|}~"""
    word_list = re.split(' |\t|\n|\r', s)
    # word_list = s.split("' '|\t|\n|\r")

    for word in word_list:
        word = word.lower()
        word = ''.join([c for c in word if c not in special_characters])
        if len(word) < 1:
            continue
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1

    return words



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))