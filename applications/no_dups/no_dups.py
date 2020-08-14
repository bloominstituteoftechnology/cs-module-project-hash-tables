def no_dups(s):
    # Your code here
    string_list = s.split()
    no_dupe_dict = {}

    for word in string_list:
        if word not in no_dupe_dict:
            no_dupe_dict[word] = word

    string_list = ' '.join(list(no_dupe_dict.keys()))      
    print (string_list)

    return string_list  

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))