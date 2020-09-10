def word_count(s):
    # Your code here
    dict = {}
    ignoreCharacters = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split()
    lower_s = s.lower()
    for i in ignoreCharacters:
        lower_s = lower_s.replace(i, " ")

    for x in lower_s.split():
        if x not in dict:
            dict[x] = 1
        else:
            dict[x] += 1
    # print(lower_s)
    return dict
    

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))