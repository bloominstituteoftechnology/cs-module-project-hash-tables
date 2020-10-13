

def word_count(s):
    
    d = {}

    # split the string into list of words
    for c in s:
        if not c.isalpha() and not c.isspace():
            s = s.replace(c, '')

    wordList = s.split()

    # loop through the words
    for word in wordList:
        word = word.lower() 
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
        # if the word is not in the dictionary, add it as a key and set its value to 1
        # else (if it is in the dictionary) add 1 to its value 
    
    return d



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))