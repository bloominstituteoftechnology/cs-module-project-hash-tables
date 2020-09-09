def no_dups(s):
    # Define a duplicate map
    map_dupe = {}

    # Split the string into words
    arr_wrds = s.split()
    ret_str  = ""

    # Iterate through the list of words
    for wrd in arr_wrds:
        # Is the word a dupe?
        if wrd not in map_dupe:
            # Not a dupe; add the word to the map and the return string
            map_dupe[wrd] = True
            ret_str       = ret_str + " " + wrd
            continue

        # Word is a dupe... continue processing

    return ret_str.strip()

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))