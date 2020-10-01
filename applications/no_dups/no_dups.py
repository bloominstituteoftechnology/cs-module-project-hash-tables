def no_dups(s):
    result = ""
    words = {}

    for word in s.split():
        if word not in words and word != "":
            result += f'{word} '
            words[word] = 1
    
    return result.rstrip()



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))