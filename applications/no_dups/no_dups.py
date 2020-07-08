def no_dups(s):
    # Your code here
    non_dup_keys = []
    if s == '':
        return '' #returns an empty string if given
    l = s.split(' ') #splits string into a list
    a = dict.fromkeys(l)
    for key in a.keys():
        non_dup_keys.append(key)
    return ' '.join(non_dup_keys)

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))