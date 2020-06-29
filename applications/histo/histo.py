# Your code here


# Read in all the words in one go
with open("applications/histo/robin.txt") as f:
    words = f.read()


def word_count(s):
    # Your code here
    cache = {}
    text = ""
    punctuation = ['"', ':', ';', ',', '.', '-', '+', '=', '/',
                   '\\', '|', '[', ']', '{', '}', '(', ')', '*',
                   '^', '&']
    for c in s:
        if c in punctuation:
            s.replace(c, '')
        else:
            text += c

    words = text.split()

    for word in words:
        word = word.lower()
        if word in cache:
            cache[word] += 1
        else:
            cache[word] = 1

    items = list(cache.items())
    items.sort(key=lambda e: e[1], reverse=True)

    items = dict(items)

    for k, v in items.items():
        hashtags = []
        for _ in range(v):
            hashtags.append('#')
        print(k + " " + ''.join(map(str, hashtags)))


word_count(words)
