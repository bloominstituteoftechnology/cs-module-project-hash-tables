def word_count(s):
    # Your code here
    dict = {}
    special_char = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split()
    ss = "".join(c.lower() for c in s if not c in special_char).split()
    print(ss)
    for word in ss:
        dict[word] = dict[word] + 1 if word in dict else 1
    return dict 

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))