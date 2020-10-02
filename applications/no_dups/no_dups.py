def no_dups(s):
    # Your code here

    words = s.split(" ")
    print(words)
    # print(words)
    # return " ".join(set(list(words)))
    lst = []
    for word in words:
        if word not in lst:
            lst.append(word)

    return ' '.join(lst)
    # cache = {}
    # words = s.split()
    # for word in words:
    #     if word not in cache:
    #         cache[word] = word

    # return cache


if __name__ == "__main__":
    #print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))