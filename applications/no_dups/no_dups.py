def no_dups(s):
    r = ""
    returns = ""
    counts = {}
    for c in s:
        # When the alg hits a space it adds the characters before to the hashtable 
        if c == ' ':
            counts[r] = True
            r = ""            
        # Otherwise, adds the character to the current string.
        else:
            r += c
    counts[r] = 1

    for key in counts:
        returns += ' ' + key

    return returns[1:]


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))