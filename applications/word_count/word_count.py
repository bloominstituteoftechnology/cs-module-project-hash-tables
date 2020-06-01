def word_count(s):
    # Keys will be words, values will be each word's count
    word_counts = {}
    # Chars we don't want counted
    invalid_chars = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
    # Building list of words to iterate over
    words = s.split(" ")

    for word in words:
        # Ignoring case
        word = word.lower()
        # If word has no content, skip it
        if len(word) == 0:
            continue
        # If invalid char, strip off string
        for char in invalid_chars:
            if char in word:
                # print(char)
                # print(word)
                word = word.strip(char)
        # If word already in counts dict, increment count
        if word in word_counts:
            word_counts[word] += 1
        # Else; set count to 1
        else:
            word_counts[word] = 1

    return word_counts

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello  hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))