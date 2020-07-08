def no_dups(input_string):
    # Your code here
    # Let's utilize a set to check for duplicates
    # We will loop through the string once and build our set of unique words
    # Then we will loop through again and only add a word to our string if it is in our unique words set
    # Once a word is used, it will be removed from the unique words set

    split_words = input_string.split()
    unique_words = set(split_words)
    result_string = ""

    for word in split_words:
        if word in unique_words:
            result_string += word + " "
            unique_words.remove(word)

    result_string = result_string[:-1] # Remove last trailing space

    return result_string



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))