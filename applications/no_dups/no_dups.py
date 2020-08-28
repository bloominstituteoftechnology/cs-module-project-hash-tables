def no_dups(s):
    counts = dict()

    words = s.lower().split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    results = {k: v for k, v in counts.items()}
    if results:
        keys = " ".join(list(results.keys()))
    else:
        keys = ''
    return keys


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
