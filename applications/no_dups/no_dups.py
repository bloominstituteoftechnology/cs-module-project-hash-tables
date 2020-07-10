def no_dups(s):
    # Your code here
    dup = {}
    string = ""
    for (index, word) in enumerate(s.split()):
        word = word.lower()
        
        if word not in dup:
            if index == 0:
                string += word
            else:
                string += " " + word
            dup[word] = word
    return string

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))