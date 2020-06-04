def no_dups(s):
    # Your code here

    # dict
    cache = {}
    text = ""
    words = s.split()

    for word in words:
        # case insensitive
        # check and see if our key is in our dictionary, if so will add 1
        # if not will initilize it
        word = word.lower()
        if word in cache:
            cache[word] += 1
        else:
            cache[word] = 1

    for i in list(cache):
        text += i + " "

        # return rstrip() removed characters
    return text.rstrip()


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
