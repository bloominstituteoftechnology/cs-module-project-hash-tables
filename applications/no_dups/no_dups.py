def no_dups(s):
    # base case for error handling
    # if s == "":
    #     return ""
    # dictionary that maps the unique word order (not the count)
    # against the word, ex: {"we": 0, "are": 1, ...}
    # d = {}
    # # keep a counter of each unique word's order
    # i = 0
    # # iterate over every word
    # for word in s.split():
    #     if word in d:
    #         # if we've already seen the word, DO NOTHING!
    #         continue
    #     else:
    #         # store the relative order, i, into our dictionary
    #         d[word] = i
    #         # increment order counter
    #         i += 1
    # this code was written to handle situations where the list did not
    # come out correctly sorted, but proved to be unnecessary
    # d = {v: k for k, v in d.items()}
    # l = [None] * i
    # for j in range(0, i):
    #     l[j] = d[j]
    # l = [word for word, _ in d.items()]

    # in the end, none of the above code was really necessary, except to utilize
    # a dictionary, which I felt was the pedagogical prupose of the project
    l = []
    for word in s.split():
        if word in l:
            continue
        else:
            l.append(word)
    return " ".join(l)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
    print(no_dups("banana apple banana app banan taco banan ban banana tac taco taco app apple banana ban taco"))
