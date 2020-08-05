def no_dups(s):
    # Your code here
    dict1 = {}
    words = s.split()

    for word in words:
        dict1[word] = 0
    return " ".join([x for x in dict1.keys()])




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))