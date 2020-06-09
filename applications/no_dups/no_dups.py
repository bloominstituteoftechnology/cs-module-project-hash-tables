def no_dups(s):
    words = s.strip().split()
    new = ""
    lex = {}
    for word in words:
        if word not in lex.keys():
            lex[word] = 1
            new += word + ' '
    return new.strip()



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
