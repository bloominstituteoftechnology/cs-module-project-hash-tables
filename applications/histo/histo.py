ignored_characters = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']

def histogram():
    counts = {}
    with open("robin.txt") as f:
        words = f.read()
        split_words = words.split()

    for word in split_words:
        histo = ""
        for char in word:
            if char not in ignored_characters:
                histo += char
        word = histo.lower()

        if word in counts:
            counts[word] += 1
        elif word == "" or word == " ":
            break
        else:
            counts[word] = 1

    items = list(counts.items())
    items.sort(key = lambda e: (-e[1], e[0]))
    counts = (dict(items))
    for (string, value) in counts.items():
        max_len = len(max(string, key=len))
        print(f'{string} {" " * max_len} {"#" * value}')


print(histogram())