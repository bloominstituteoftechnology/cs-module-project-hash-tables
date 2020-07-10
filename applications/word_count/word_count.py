def word_count(s):
    # print(s)
    symlist = ['"',':',';',',','.','-','+','=','/','|',
              '\\','[',']','{','}','(',')','*','&','^']
    for symbol in symlist:
        s = s.replace(symbol, '')
    # print(s)

    wordlist = s.lower().split()
    worddict = {}
    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1
    return worddict


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))