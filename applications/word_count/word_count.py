def word_count(s):
    """
    @params s is a string of any length

    word_count iterates over every word in the string, and returns
    a count of occurences of each unique word in the following dictionary
    format: {"word": 5, "word2": 3, ...}
    """

    # initialize a dictionary to store and count words
    d = {}

    # for the sake of consistency, word_count ignores the following symbols
    ignore = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(" ")
    for char in ignore:
        s = s.replace(char, "")

    # iterate over every word in the input string
    for word in s.split():
        # ignore case by converting all words to lowercase
        word = word.lower()
        # if it's the first time we've hit the word, initialize a dictionary entry
        if word not in d:
            d[word] = 0

        # increment the corresponding entry by 1 each time we find the word
        d[word] += 1
    return d


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
