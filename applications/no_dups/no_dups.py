def no_dups(s):
    out = []
    for word in s.split(' '):
        if word not in out:
            out.append(word)
    return ' '.join(out)

# using hashtables for this is kind of a waste yo


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))