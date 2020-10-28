def word_count(s):
    counts = {}
    avoid = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']

    for character in avoid:
        s = s.replace(character, "")

    each_word = s.split()

    for word in each_word:
        word = word.lower()

        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))