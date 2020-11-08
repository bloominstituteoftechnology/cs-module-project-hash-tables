def no_dups(s):
    data = {}
    # Your code here
    s_array = s.split()
    print(s_array)
    for word in s_array:
        if word in data:
            continue
        else:
            data[word] = 1
    return " ".join(data.keys())


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
