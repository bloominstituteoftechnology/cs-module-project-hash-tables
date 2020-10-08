def no_dups(s):
    # Your code here
    if s == "":
        return ""

    word_hash = {}

    sArr = s.split(" ")

    for word in sArr:
        if word.lower() in word_hash:
            word_hash[word.lower()] += 1
        else:
            word_hash[word.lower()] = 1

    single_string = list(word_hash.keys())
    single_string = ' '.join(single_string)

    return single_string



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))