
def no_dups(s):
    # Your code here
    lookup = {}
    words = s.split()
    result = ""

    for word in words:
        if lookup.get(word) is None:
            lookup[word] = word
            if result == "":
                result = word
            else:
                result += f" {word}"

    return result




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))