def no_dups(s):
    table = {}

    # Loop over every word in the string, and add each word to a table as a key
    for word in s.split():
        if not word in table: 
            table[word] = 1

    # Map over keys in a table, append each to returned string as well as whitespace 
    returnString = ""
    for x in table: 
        returnString += x 
        returnString += " "

    return returnString[:-1] # Remove last element from returnString as it has an extra whitespace





if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))