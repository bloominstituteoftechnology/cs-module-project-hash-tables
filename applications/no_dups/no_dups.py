def no_dups(s):
    # Your code here

    words_dict = {}
    words = s.split()

    new_string = ""
    if len(words) > 0:
        count = len(words)
        is_first = True
        for word in words:
            count += 1
            if word in words_dict:
                # the word is already been seen by the program
                words_dict[word] += 1
            else:
                # the word has not yet been seen by the program
                words_dict[word] = 1

                if count + 1 == len(words):
                    new_string += word
                else:
                    if is_first:
                        new_string += word
                        is_first = False
                    else:
                        new_string += " "
                        new_string += word
    

    return new_string



if __name__ == "__main__":
    # print(no_dups(""))
    print(no_dups("hello"))
    # print(no_dups("hello hello"))
    # print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))