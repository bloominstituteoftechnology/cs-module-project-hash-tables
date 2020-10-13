def word_count(s):
    # Your code here
    stop_char = """:;",.-+=/|[]{|}()*^\&"""
    s_clean = "".join([_ for _ in s if _ not in stop_char])
    word_list = s_clean.lower().split()

    word_count = {}
    for x in word_list:
        if x not in word_count:
            word_count[x] = 0
        word_count[x] += 1
    return word_count




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))