def word_count(s):
    word_dic = {}
    ignored_char ='":;,.-+=/\\|[]{}()*^&'
    #split the string into words
    words= s.lower().split()

    for word in words:
        for char in word:
            if char in ignored_char:
                word = word.replace(char,'') 
        if word is '':
            return {}    
        if word  not in word_dic:
            word_dic[word] = 1
        else:
            word_dic[word] +=1

    return word_dic

if __name__ == "__main__":
    print(word_count('":;,.-+=/\\|[]{}()*^&'))
    print(word_count(""))
    print(word_count("Hello hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))