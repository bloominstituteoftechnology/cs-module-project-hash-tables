def word_count(s):
    # Your code here
    cache = {}
    words_lowercased = s.lower()
    ignored_chars = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(" ")

    for chars in ignored_chars:
        words_lowercased = words_lowercased.replace(chars, "")

    for words in words_lowercased.split():
        print(words)
        if words == "":
            continue
        if words not in cache:
            cache[words] = 1
        else:
            cache[words] += 1
    return cache





if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))