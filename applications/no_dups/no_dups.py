def no_dups(s):
    keys_list = []
    if s == '':
        return ''
    lst = s.split(' ')
    a = dict.fromkeys(lst)
    for key in a.keys():
        keys_list.append(key)
    return ' '.join(keys_list)



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))