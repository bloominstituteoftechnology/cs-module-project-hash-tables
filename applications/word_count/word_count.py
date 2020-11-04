def word_count(s):
    dictionary = {}
    special_characters = ['"', ":", ";", ",", ".", "-", "+", "=", "/", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&", "\\"]

    lower_case = s.lower()

    for i in special_characters:
        lower_case = lower_case.replace(i, "")

    split_string = lower_case.split()
    if split_string.count == 0:
        return dictionary

    for word in split_string:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))