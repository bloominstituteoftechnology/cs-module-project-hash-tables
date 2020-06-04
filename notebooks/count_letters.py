"""
How to extract the number of letters:
four a's
Three b's
two c's

we're going to Cache these results as we go.
we're going to make a hashtable
and go through the string once
print_letter_count("aaaabbbcc")
"""


def print_letter_count(s):
    counts = {}

    for c in s:
        # c = c.lower() # case insensitive
        # check and see if our key is in our dictionary, if so will add 1
        # if not will initilize it
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
        # get items from count first
        items = list(counts.items())
        # then sort
        items.sort(key=lambda e: e[1])
        print(items)

        # deceding count
        items.sort(key=lambda e: e[1], reverse=True)
        print(items)

    print(f' Our letters extracted and number amount:', counts)
    # print(c)


print_letter_count("aaaabbbcc")
print_letter_count("aaaabbbccAA!")
