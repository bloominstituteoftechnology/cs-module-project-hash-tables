import re
def word_count(s):
    # make the list all lower case 
    lower_s = s.lower()
    #remove special characters
    special_chars = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
    for special in special_chars:
        lower_s = lower_s.replace(special, '')
    for s in ['\r','\t','\n']:
        lower_s = lower_s.replace(s, " ")
        
    # create an array from the string separating on empty spaces
    word_list = lower_s.split(" ")
    # create an empty dictionary
    word_dic = {}

    #check for edge case of empty string
    if s == "":
        return {}

    # loop through array 
    for word in word_list:
        # ignore if empty space
        if word == "":
            continue
        #if the word is in the dictionary add by 1
        if word in word_dic:
            word_dic[word] += 1
        # else create a new element in the dictionary
        else:
            word_dic[word] = 1

    # return the dictionary
    return word_dic


if __name__ == "__main__":
    print(word_count('a a\ra\na\ta \t\r\n'))
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))