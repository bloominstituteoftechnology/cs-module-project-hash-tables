from collections import defaultdict


def word_count(s):
    ignore_chars = ',":;,.-+=/\\|[]{}()*^&'
    counts = defaultdict(int)

    s_clean = s.translate(str.maketrans('', '', ignore_chars))

    for word in s_clean.lower().split():
        counts[word] += 1

    return counts


with open('robin.txt') as file:
    s = file.read()

counts = word_count(s)
width = max([len(word) for word in counts.keys()]) + 2

counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

for count in counts:
    print(f'{count[0].ljust(width)}' + '#' * count[1])
