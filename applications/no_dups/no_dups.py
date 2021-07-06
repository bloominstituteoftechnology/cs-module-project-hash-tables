def no_dups(s):
    # Your code here
    # the hell do I have to do?
    # remove the duplicates of an inputed string

    # heres what I need to do:
    # 1. take the string thats being put into the function and split it into a list
    words = s.split()
    # give it a new place for the list to live once you've removed the duplicates:
    new_list = []
    # 2. take that list and iterate over it:
    for checking in words:
        #     if the list doesn't have the word append it to the new list
        if checking not in new_list:
            new_list.append(checking)
            #     return the new list
    return " ".join(new_list)

    # thinking hashing, use dictionary, check word in list save it in

    # how do I do that?
    # there must be no extra spaces at the end of your returned string
    # keep it 0(n)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
