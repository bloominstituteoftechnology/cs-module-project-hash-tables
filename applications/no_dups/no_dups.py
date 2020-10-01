def no_dups(s):
    # Your code here
    d = {}
    string = ""
    sp = s.split(" ")
    if(s == ""):
        return string
    else:
        for i in sp:
            if i not in d:
                d[i] = 0
                string = string + i + " "
        return string.strip()

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))