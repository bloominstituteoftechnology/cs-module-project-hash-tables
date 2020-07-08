def no_dups(s):
    # Your code here
    l = s.split()
    q = set()
    o = []
    for w in l:
        if w not in q:
            o.append(w)
            q.add(w)
    r =" ".join(o)
    return r


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))