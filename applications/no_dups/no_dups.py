def no_dups(s):
    # Your code here
    duplicates = {}
    duplicates_removed = ""

    for (idx, word) in enumerate(s.split()):
        word = word.lower()
        if word not in duplicates:
            if idx == 0:
                duplicates_removed += word
            else:
                duplicates_removed += " " + word
        duplicates[word] = word
    return duplicates_removed


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))