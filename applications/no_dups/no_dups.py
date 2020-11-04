def no_dups(s):
    # edge case of empty string
    if s == "":
        return ""
    # separate the list of words into an array
    word_array = s.split(" ")

    # create an empty list
    no_dups_array = []
    # check to see if the word was already in the array 
    for word in word_array:
        # if not then add 
        if word not in no_dups_array:
            no_dups_array.append(word)
    
    # put the array back into a string and return
    return " ".join(no_dups_array)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))