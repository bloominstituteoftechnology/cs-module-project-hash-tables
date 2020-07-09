from collections import defaultdict


def word_count(s):
    """
    Input: This function takes a single string as an argument.

    Output: It returns a dictionary of words and their counts.
    Case should be ignored. Output keys must be lowercase.
    Key order in the dictionary doesn't matter.
    Split the strings into words on any whitespace.
    Ignore each of the following characters:
        " : ; , . - + = / \\ | [ ] { } ( ) * ^ &
    """

    ignore_chars = ',":;,.-+=/\\|[]{}()*^&'

    # Initialize dictionary to track word counts.
    counts = defaultdict(int)

    # Remove characters to be ignored.
    s_clean = s.translate(str.maketrans('', '', ignore_chars))

    # Calculate case-insensitve word counts.
    for word in s_clean.lower().split():
        counts[word] += 1

    return counts


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. '
                     'This is only a test.'))
