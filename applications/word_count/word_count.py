
badchars = [":", ";", ",", ".", "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&", "\""]

def word_count(s):
    dictionary = {}
    res = s.lower()

    for item in badchars:
        res = res.replace(item, "")

    res = res.split()

    for item in res:
        if item in dictionary:
            x = dictionary[item]
            x += 1
            dictionary[item] = x
        else:
            dictionary[item] = 1

    return dictionary



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))