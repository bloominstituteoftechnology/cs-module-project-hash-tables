def no_dups(s):
    # Your code here
    words = s.split()
    word_count = {}
    unique_words = ""
    for word in words:
        if word_count.__contains__(word) is False:
            word_count[word] = 1
            unique_words += f"{word} "
        
    return unique_words.rstrip()


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
    x = no_dups("hello")
    print(f"This is X: {x}")