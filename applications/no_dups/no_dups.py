def no_dups(s):
    # Your code here
    words = s.split()
    dictionary = dict()

    if words:
        for word in words:
            if word not in dictionary:
                dictionary[word] = None
    else: # Empty string
        return ""

    print(dictionary)

    return " ".join(list(dictionary.keys()))


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))