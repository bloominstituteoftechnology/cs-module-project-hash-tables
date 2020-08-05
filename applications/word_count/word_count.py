import re


def word_count(s):
    # Your code here
    d = dict()
    split = re.findall('[A-Za-z\']+(?:\`[A-Za-z]+)?', s)

    split = [x for x in split if x != '']
    print(split)
    for char in split:
        if char.lower() in d and char != '':
            d[char.lower()] += 1
        else:
            d[char.lower()] = 1
    return d


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
