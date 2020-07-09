def word_count(s):
    cache = {}
    s = s.lower()
    for i in s:
        if i >= 'a' and i <='z':
            if i not in cache:
                cache[i] = 1
            else:
                cache[i] += 1
    for i in cache:
        print(f'Letter: {i[0]}, Count: {cache[i]}')


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))