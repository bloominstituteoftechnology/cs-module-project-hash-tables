def word_count(s):
    # Your code here
    string_count = {}
    split_string = s.split()
    temp_word = ''
    banned_characters = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'

    for index, word in enumerate(split_string):
        temp_word = ''
        for char in word:
            if char not in banned_characters:
                temp_word += char
            if len(temp_word) > 0:
                if temp_word.lower() in string_count:
                    string_count[temp_word.lower()] += 1
                else:
                    string_count[temp_word.lower()] = 1

    return string_count                      


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))