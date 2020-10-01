def word_count(s):
    # need cache consisting of words + amount of times word occurs, must be sorted by freq
    cache = {}
    # case doesn't effect word count, so lowercase all the words
    words_lowercased = s.lower()
    # ignore chars
    ignored_chars = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(" ")
    # iterate through string
    for chars in ignored_chars:
        # replace all non words with space
        words_lowercased = words_lowercased.replace(chars, "")
    for words in words_lowercased.split():
        print(words)
        # continue if iterating through space
        if words == "":
            continue
        if words not in cache:
            cache[words] = 1
        else:
            cache[words] += 1
    return cache
    # only count words, ignore grammar
    # if " " or non-letter than push everything between last " " or non letter into cache
    # return cache



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))

# print(word_count("TESTING TESTING TESTING TESTING"))