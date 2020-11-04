def no_dups(s):
    # Your code here
    d = {}
    arr = s.split()
    output = []

    for word in arr:
        if word not in d:
            d[word] = 1
            output.append(word)
    
    return " ".join(output)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))