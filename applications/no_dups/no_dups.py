def no_dups(s):
    cache = {}
    new_string = ""

    for item in s.split():
        if item not in cache:
            new_string += item
            new_string += " "
            cache[item] = True
    new_string = new_string[:-1]

    return new_string



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))