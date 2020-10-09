def word_count(s):
    # Your code here
    out = {}
    # strip ignored characters and bullshit non-space whitespace characters
    IGNORED = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
    words = ''.join(filter(lambda i: i not in IGNORED, s)).translate({ord(c): ' ' for c in '\n\t\r'})
    print(words)


    for word in words.split(' '):
        word = word.lower()
        if len(word) > 0:
            if word not in out:
                out[word] = 1
            else:
                out[word] += 1

    print(out)
    return out


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))