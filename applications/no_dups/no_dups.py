def no_dups(s):
    
    # will make a cache that will hold each string as a key
    my_cache = {}
    returnString = ""
    separateString = ""
    first = True # this flag is used just in case there are more than one 
                        # space in the string in a row. After the fisrst space, 
                        # it will not put the second space as part of the variable 
           
    if not s:
        return returnString             # separateString
    for i in range(len(s)):
        # looping through after we have the full string and putting it in the cache
        if s[i] != " ":
            separateString += s[i]
        if s[i] == " " or i == len(s)-1: # this is to check at the end of the string
            if separateString not in my_cache:
                my_cache[separateString] = ""
                if first: # Will do this for the first time and do the else for all others
                          # this is to get the spaces in the correct places
                    returnString += separateString
                    first = False
                
                else:    
                    returnString +=  " " + separateString 
            separateString = ""
    return returnString




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))