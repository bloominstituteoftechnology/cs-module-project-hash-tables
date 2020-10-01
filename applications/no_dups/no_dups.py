def no_dups(s):

    # input may contain duplicate words
    # output cannot have duplicate words
    # output must be in same order
    # output cannot have extra spaces at the end
    # Your code here


    cache = {}




    for word in s.split():
        if word not in cache:
            cache[word] = 1

    return ' '.join(cache.keys())





if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))\


