def print_letter_count(s):
    counts = {}

    for c in s:
        # c = c.lower()  # case insensitive
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1

    items = list(counts.items())
    items.sort(key=lambda e: e[1])

    print(items)


print_letter_count("aaabbcbcaAA!")
