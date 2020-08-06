import re
import string

def word_count(s):
    # Your code here
    my_dict = {}

    words = s.translate(str.maketrans('', '', string.punctuation))
    words = [string.lower() for string in words.split()]

    for word in words:
        if word not in my_dict:
            my_dict[word] = 1
        else:
            my_dict[word] += 1

    return my_dict



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))