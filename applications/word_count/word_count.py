import string


def word_count(s):
    clean = s.translate(str.maketrans('', '', '\":;,.-+=/\\|[]{}()*^&'))
    words = clean.split()
    words = [x.lower() for x in words]
    words = {x.lower(): words.count(x) for x in words}
    return words


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
