def no_dups(s):
    # no_dup = set()
    # result = ''
    # s = s.split()
    # for i in s:
    #     no_dup.add(i)
    # a = ' '.join(no_dup)
    # a = a.strip()
    # return a

    no_dup = {}
    result = ''
    s = s.split()
    for i in s:
        if i not in no_dup:
            no_dup[i] = i
            result += i + ' '

    return result.strip()


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
