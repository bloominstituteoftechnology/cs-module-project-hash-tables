def no_dups(s):
    # Your code here
    if s == "":
        return ""
    d = {}
    i = 0
    for word in s.split():
        if word in d:
            continue
        else:
            d[word] = i
            i += 1
    d = {v: k for k, v in d.items()}
    l = [None] * i
    for j in range(0, i):
        l[j] = d[j]
    return " ".join(l)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
    print(no_dups("banana apple banana app banan taco banan ban banana tac taco taco app apple banana ban taco"))