def word_count(s):
    # Your code here
    word_dict = {}

    special_chars = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
    s2 = ''.join(c.lower() for c in s if not c in special_chars)
    word_list = s2.split()

    for word in word_list:
        if word == " ":
            continue
        elif word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))