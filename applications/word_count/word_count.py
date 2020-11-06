
def word_count(s):
    frequency = {}
    ignore = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
    
    clean_string = "".join(ch for ch in s if ch not in ignore)
    for word in clean_string.lower().split():
        if word not in frequency:
            frequency[word] = 1
        else:
            frequency[word] += 1
            
    return frequency


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))