import re
def word_count(s):
    # Your code here
    special_characters = ['\"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
    filtered_string = ''.join(filter(lambda c: c not in special_characters, s))
    lower_string = filtered_string.lower()
    array_word = lower_string.split()

    dictionary = {}

    for word in array_word:
        if word not in dictionary:
            dictionary[word] = 0
            
        dictionary[word] += 1

    return dictionary

if __name__ == "__main__":    
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))