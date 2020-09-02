

def no_dups(s):
    d = {}
    wordList = s.split()

    for word in wordList:
        if word in d:
            continue 
        else:
            d[word] = 1
    
    arr = [key for key in d]
    string = " " 

    return string.join(arr)



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))