import re

def word_count(s):
    count = dict() 
    words = re.sub("[^w'a-z]+", " ", s.lower()).split()

    for i in words: 
        if i in count: 
            count[i] += 1 
        else: 
            count[i] = 1 
        
    return count



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))