def no_dups(s):
    # We'll use a set to filter out duplicate values
    words = set()
    # Split so we can split the repeated runs of whitespace
    wordList = s.split()
    # This is going to be what our program outputs
    output = ""

    for word in wordList:
        # if the word is not already in our set
        if word not in words:
            # We add the word to our set
            words.add(word)
            output += word + " "
    # Strip so we can remove spaces at the beginning and end of a string
    return output.strip()




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))