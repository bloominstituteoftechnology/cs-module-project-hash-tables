def no_dups(s):
    array = []
    result_string = ""
    split_string = s.split()
    
    if s == "":
        return result_string

    for word in split_string:
        if word not in array:
            array.append(word)
            result_string += word + " "

    if result_string.endswith(" "):
        return result_string[:-1]

    return result_string


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))