import sys
import re

# sys.path.insert(1, '/home/ubuntom/Projects/lambda/cs-module-project-hash-tables')

# from hashtable.hashtable import HashTable
esc = {char for char in ['\t', '\n', '\r']}

def word_count(s):
    # Your code here
    ht = {}
    word = ""
    special = {char for char in '":;,.-+=/\\|[]{}()*^& '}
    s = s.replace('\r', ' ').replace('\n', ' ').replace('\t', ' ')
    def add_word(word):
        if word not in ht:
            ht[word] = 1
        else:
            ht[word] += 1
    for i in range(len(s)):
        if s[i] not in special:
            word += s[i].lower()
        if s[i] == ' ' and word:
            add_word(word)
            word = ''
    if word:
        add_word(word)
    return ht

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count("Hello    hello"))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))
    print(word_count('a a\ra\na\ta \t\r\n'))