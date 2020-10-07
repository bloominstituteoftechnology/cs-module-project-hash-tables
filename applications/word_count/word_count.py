def word_count(s):
    # Your code here
    dict = {}
    lower = s.lower()

    ignore = [":", ";", ",", ".", "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&", "\""]

    for item in ignore:
        lower = lower.replace(item, "")

    words = lower.split()

    for item in words:
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1

    return dict

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))