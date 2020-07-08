def no_dups(s):
    # Your code here
    # List to hold non duplicates
    lst_of_keys = []
    if s == '':
        # return empty string if it is given
        return ''
    # split string input into a list
    l = s.split(' ')
    # Turning array into dict as keys removes duplicates
    a = dict.fromkeys(l)
    for key in a.keys():
        # Loops array into dict as keys removes duplicates
        lst_of_keys.append(key)
        # join it all for the return with a space between '' in order to maintain space distance
    return ' ' .join(lst_of_keys)



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))