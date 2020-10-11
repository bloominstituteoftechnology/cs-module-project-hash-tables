def no_dups(s):
    # Your code here
    str = s.split()
    str_list = []
    str_dict = {}
    for word in str:
        if word not in str_dict:
            str_dict[word] = 1
            str_list.append(word)
    result = ' '.join(str_list)        
    print(result)
    return result





if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))