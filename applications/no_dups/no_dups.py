def no_dups(s):
    # Your code here
    inputString = s.split(" ")

    newArr = []
    for word in inputString:
        if word not in newArr:
            newArr.append(word)

    return " ".join(newArr)




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))