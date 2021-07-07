def no_dups(s):
    # Your code here
    """
    Input: a string of words separated by spaces. Only the letters `a`-`z`
    are utilized.

    Output: the string in the same order, but with subsequent duplicate
    words removed.

    There must be no extra spaces at the end of your returned string.

    The solution must be `O(n)`.
    """

    cache = set()

    words = s.split()

    # hold words in order they came
    out_string = []

    # special case: if input is ""
    if len(s) == 0:
        return ""

    for s in words:

        if s not in cache:
            # add it to set
            cache.add(s)

            # add it to the out_string
            out_string.append(s)

    # ensure return is formatted as single string to pass test
    return " ".join(out_string)



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))