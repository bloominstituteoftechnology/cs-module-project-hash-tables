def no_dups(s):
    # Your code here
    no_dups = {}
    for x in s.split():
        if x not in no_dups:
            no_dups[x] = x
    return ' '.join(no_dups.values())



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))