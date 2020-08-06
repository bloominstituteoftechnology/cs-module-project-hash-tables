def no_dups(s):
    # split list
    # save cache
    # loop through list if string not in cache add to cache
    #
    newStr = s.split(' ')

    newArr = []
    for char in newStr:
        if char in newArr:
            pass
        elif newStr.count(char) >= 1:
            newArr.append(char)
    finalStr = ' '.join([str(el) for el in newArr])
    return finalStr


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
