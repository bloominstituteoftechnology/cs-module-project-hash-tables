import re
import string
def word_count(s):
    # Your code here
    d = {}
    sp = re.sub('['+'":;,.+=\\-/\\\|{}()\\[\\]*^&'+']', '', s).split()
    for i in sp:
        
        jstring = i.lower()
        
        if(jstring not in d):
            d[jstring] = 1
        else:
            d[jstring] += 1
    return d
    



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))