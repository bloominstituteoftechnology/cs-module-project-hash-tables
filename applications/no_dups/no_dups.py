def no_dups(s):
    if s == "": return ""
    
    results = ''
    wordDict = dict.fromkeys(s.split(' '), False)

    for word in s.split(' '):
        if wordDict[word] == False:
            wordDict[word] = True
            results += f'{word} '

    return results[:-1]



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))