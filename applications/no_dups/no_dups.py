def no_dups(s):
    count = {'hello', 'cat', 'dogs', 'fish', 'spam', 'sausage'}
    res = s.split()
    for word in res:
        if word in count:
            print(word)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
