def word_count(s):
    # Your code here
    char_exclude = r'" : ; , . - + = / \ | [ ] { } ( ) * ^ &'
    words = s.lower()
    name = s.translate({ord(c): " " for c in char_exclude})
    if name == "":
        return {}
    seperate = name.lower().split()
    words = {i: seperate.count(i) for i in seperate}
    return words


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
