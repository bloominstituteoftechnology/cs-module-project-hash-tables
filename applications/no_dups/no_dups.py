

def no_dups(s):
    #List to hold non duplicates 
    lst_of_keys = []
    if s == '':
        # Return empty string if it is given
        return ''
    # Split string input into a list
    l = s.split(' ')
    # Turning array into dict as keys removes duplicates
    a = dict.fromkeys(l)
    for key in a.keys():
        # Loops keys and appends them to List of keys
        lst_of_keys.append(key)
        #Join it all for the return with a space between ' ' in order to maintain space distance
    return ' '.join(lst_of_keys)
        



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))