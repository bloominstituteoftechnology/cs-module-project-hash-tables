def no_dups(s):
    words_already_seen = set()
    result = ''
    words = s.split()
    for word in words:
        if word not in words_already_seen:
            result += word + ' '
            words_already_seen.add(word)
    
    if result.endswith(' '):
        result = result[:-1]
    return result



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))