from collections import Counter

def no_dups(s):
    words = s.split()
    count = {}

    count = Counter(words)
    count = list(count)
    count = ' '.join(count)

    return count


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))