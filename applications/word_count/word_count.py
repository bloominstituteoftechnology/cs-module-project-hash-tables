ignored_characters = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']

def word_count(s):

    counts = {}

    for word in s.split():
        new_word = ""
        for char in word:
            if char not in ignored_characters:
                new_word += char
        word = new_word.lower()

        if word in counts:
            counts[word] += 1
        elif word == "" or word == " ":
            break
        else:
            counts[word] = 1

    if s == "":
        return {}
    else:
        return counts

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))