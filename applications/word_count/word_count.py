def word_count(s):
    # we need to first clean the sentence of any of the markings
    forbidden = '":;,.-+=/\|[]{}()*^&"'
    new_string = ""
    for word in s:
        if word in forbidden:
            print(word)
        else:
            new_string += word.lower()

    print("- - - - ")
    print(new_string)

    words_dict = {}
    words = new_string.split()

    if len(words) > 0: 
        for word in words:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1
    
    return words_dict
        



    # listWords = []

    
    # for word in words:
    #     listWords.append(word)
    #     return listWords
    # return words

    

    # for word in s:
    #     if words_dict[word]:
    #         words_dict[word] += 1
    #     else:
    #         words_dict[word] = 1

    # ignore these characters
    # : ; , . - + = / \ | [ ] { } ( ) * ^ & 


    # return a dictioany of words and their counts

if __name__ == "__main__":
    # print(word_count(""))
    # print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))