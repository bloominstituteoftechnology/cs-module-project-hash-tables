def word_count(s):
    # Your code here
    # {'hello': 2, 'my': 2, 'cat': 2, 'and': 1, "doesn't": 1, 'say': 1, 'back': 1}
    # s = '":;,.-+=/\\|[]{}()*^&'
    table = s.maketrans('', '', '":;,.-+=/\|[]{}()*^&')
    s = s.translate(table)

    d = {}
    words = s.split()
    for word in words:
        word = word.lower()
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

    return d

#print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))