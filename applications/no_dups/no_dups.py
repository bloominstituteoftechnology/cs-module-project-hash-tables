def no_dups(s):
    word = s.split(" ")
    word_dict = dict()
    no_duplicates = []

    for i in word:
        if i not in word_dict:
            word_dict[i] = 1
            no_duplicates.append(i)
    return " ".join(no_duplicates)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))