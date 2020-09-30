def no_dups(s):
    # Your code here
    words = s.split(' ')
    no_dups = []
    for word in words: 
        if word not in no_dups:
            no_dups.append(word)
    return ' '.join(no_dups)




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))