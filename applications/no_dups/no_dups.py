def no_dups(s):
    word_dict = {}
    for word in s.split():
        word_dict[word] = 0

    string_stuff = ""
    for word in word_dict.keys():
        string_stuff += word + " "
    return string_stuff.strip()




    # Your code here



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))