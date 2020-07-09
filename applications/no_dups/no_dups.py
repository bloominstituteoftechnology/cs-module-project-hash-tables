
def no_dups(s):
    cache = {}
    s = s.split()
    for i in s:
        if i not in cache:
            cache[i] = 1
    return list(cache.keys())


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))