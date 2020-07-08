def no_dups(s):
    words_seen = {}

    def dupe(word):
        nonlocal words_seen
        if word in words_seen:
            return True
        else:
            words_seen[word] = True
            return False

    if s == '':
        return s
    else:
        return ' '.join([word for word in s.split() if not dupe(word)])


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
