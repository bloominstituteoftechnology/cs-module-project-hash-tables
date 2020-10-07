def no_dups(s):
    # Your code here
    cache = {}
    for dup in s.split():
        if dup not in cache:
            cache[dup] = dup
    return ' '.join(cache.values())


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))