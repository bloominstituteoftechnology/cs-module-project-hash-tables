def no_dups(s):
    # Your code here

    result = []
    spaces = ' '
    length = len(s)
    i = 0
    while i < length:
        if s[i] not in spaces:
            word_start = i
            while i < length and s[i] not in spaces:
                i += 1
            result.append(s[word_start:i])
        i += 1
    words_stack = []
    for val in result:
        if val not in words_stack:
            words_stack.append(val)
    return ' '.join(words_stack)









if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))


    # result = []
    # words = set()
    # for word in s.split():
    #     if word not in words:
    #         result.append(word)
    #         words.add(word)
    # return ' '.join(result)