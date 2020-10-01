import re


def word_count(s):
    # Your code here

    # char_list = ('":;.-+=/\|[]{}()*^&')
    d = dict()

    char_list = '"":;.,-+=/\|[]{}()*^&'

    new_s = s.lower().replace("\r", " ").replace(
        "\t", " ").replace("\n", " ").split(" ")

    print(new_s)

    for word in new_s:
        new_word = word.strip(char_list)
        print(new_word)

        if new_word not in d and new_word != "":
            d[new_word] = 1
        elif new_word != "":
            d[new_word] += 1

    return d

    # char_list = {'"', ':', ';', ',', '.', '-', '+', '=', '/',
    #              '|', '[', ']', '{', '}', '(', ')', '*', '^', '&'}

    # new_s = s.split(" ")
    # print(new_s)

    # chars = [word for word in new_s if word[0:] not in char_list]
    # print("Chars", chars)


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
