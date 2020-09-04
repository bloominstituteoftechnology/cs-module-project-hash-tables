def no_dups(s):
    # Your code here
    ht = set()
    s = s.split(" ")
    res = ""
    for word in s:
        if word not in ht:
            ht.add(word)
            res += f'{word} '
    return res[:-1]



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))