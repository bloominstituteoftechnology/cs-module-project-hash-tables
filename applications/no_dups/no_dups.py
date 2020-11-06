def no_dups(s):
    # split string into list of words
    words = s.split()
    # create an empty dict
    word_dict = {}
    # create an empty list for unique words
    unique_words = []
    # for each word in list
    for word in words:
        # if it isn't in our dict
        if word not in word_dict:
            # add key/value pair
            word_dict[word] = '_'
            # append the new word to the list of unique ones
            unique_words.append(word)
    # return a str output of the unique words 
    return ' '.join(unique_words)



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))