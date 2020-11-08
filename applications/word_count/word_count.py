def word_count(s):
    new_list = s.lower().split()
    # forbidden characters
    forbidden = '":;,.-+=/\|[]}{()*^&'
    storage = {}
    for word in new_list:
        for letter in word:
            if letter in forbidden:
                word = word.replace(letter, "")
        if word == "":
            return {}
        if word in storage:
            storage[word] += 1
        if word not in storage:
            storage[word] = 1

    return storage


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
