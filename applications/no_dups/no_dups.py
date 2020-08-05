def no_dups(s):
    used = []

    for letter in s.split():
        if not used.__contains__(letter):
            used.append(letter)

    return " ".join(used)





if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))