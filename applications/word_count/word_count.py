from collections import defaultdict


def word_count(s):
    ignore_chars = ',":;,.-+=/\\|[]{}()*^&'
    counts = defaultdict(int)

    s_clean = s.translate(str.maketrans('', '', ignore_chars))

    for word in s_clean.lower().split():
        counts[word] += 1

    return counts


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. '
                     'This is only a test.'))
