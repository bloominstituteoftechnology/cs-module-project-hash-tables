def word_count(s):
    # Your code here
    """
    This function takes a single string as an argument.

    Ex. Hello, my cat. And my cat doesn't say "hello" back.

    It returns a dictionary of words and their counts:

    Ex. {'hello': 2, 'my': 2, 'cat': 2, 'and': 1, "doesn't": 1, 'say': 1, 'back': 1}

    Case should be ignored. Output keys must be lowercase. Key order in the dictionary doesn't matter.

    Split the strings into words on any whitespace. Ignore each of the following characters:

    " : ; , . - + = / \ | [ ] { } ( ) * ^ &

    If the input contains no ignored characters, return an empty dictionary.
    """

    stop_char = """:;",.-+=/|[]{|}()*^\&"""
    
    # Make sure special characters arent in string
    s_clean = "".join([x for x in s if x not in stop_char])

    # Lower case and remove trailing space
    word_list = s_clean.lower().split()

    # use cache to hold memory
    word_count = {}

    for x in word_list:

        if x not in word_count:
            # if not there, start it at 0
            word_count[x] = 0

        # if seen again, increase count
        word_count[x] += 1

    return word_count



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))