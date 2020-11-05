def no_dups(s):
    counts = {}
    result = ""

    for word in s.split(" "):
        if word not in counts and word != "":
            counts[word] = 1
        elif word != "":
            counts[word] += 1

    for word in counts:
        result += f"{word} "

    return result.strip()



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))