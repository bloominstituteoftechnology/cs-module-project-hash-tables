def no_dups(s):
    wordset = set()
    wordlist = s.split()
    str_out = ""
    for word in wordlist:
        if word not in wordset:
            wordset.add(word)
            str_out += word + " "
    return str_out.strip()

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))