def no_dups(s):
    # Your code here
    duplicates = {}
    sentence = ""
    
    words = s.split()

    for word in words:
        if word not in duplicates.keys():
            duplicates[word] = word
            sentence += word + " "
    sentence = sentence[:-1]
    return sentence



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))