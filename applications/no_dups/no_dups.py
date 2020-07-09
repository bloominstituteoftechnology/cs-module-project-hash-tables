def no_dups(s):
    """
    Input: a string of words separated by spaces. Only the letters a-z are
    utilized.

    Output: the string in the same order, but with subsequent duplicate words
    removed.

    There must be no extra spaces at the end of your returned string.

    The solution must be O(n).
    """

    # Initialize dictionary to track words previously encountered.
    words_seen = {}

    def dupe(word):
        """
        Helper function; returns True for previously seen words, False for new
        words.
        """
        nonlocal words_seen
        if word in words_seen:
            return True
        else:
            words_seen[word] = True
            return False

    # Special case to handle empty string.
    if s == '':
        return s

    # Return list in order but without duplicate words.
    else:
        return ' '.join([word for word in s.split() if not dupe(word)])


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
