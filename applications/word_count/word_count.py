def word_count(s):
    # Your code here
    filters = ['"', ':', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&', ';','\r','\n','\t','\t','\r','\n']

    for i in filters:
        s = s.replace(i, ' ')
    # print(s)
    s = s.lower().split(' ')
    count = {}
    for i in s:
        if i not in count:
            count[i] = 0
        count[i] += 1
    if '' in count:
        del count['']
    return count



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))