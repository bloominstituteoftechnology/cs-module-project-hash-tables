

def word_count(s):
    ignore = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'
    count = dict()
    for i in s:
        if i in ignore:
            s = s.replace(i, ' ')
            s = s.lower()
    s = s.split()
    for word in s:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
    return count


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
