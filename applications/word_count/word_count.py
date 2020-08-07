import string


def word_count(s):
    char_list = ' " : , ; . - + = / \ | [] {} () * ^ &'

    newStr = s.lower().split()
    new_list = []

    for string in newStr:
        new_list.append(string.strip(char_list))
    if s == '' or new_list == [""]:
        return {}
    else:
        cache = {}
        for string in new_list:
            cache[string] = new_list.count(string)
    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
