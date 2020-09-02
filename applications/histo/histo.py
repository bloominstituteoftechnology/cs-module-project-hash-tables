with open("robin.txt") as f:
    s = f.read()

counts = dict()

punc = ":;,.-+= /\\|[]{}()*^&\""
for ele in s:
    if ele in punc:
        s = s.replace(ele, " ")

words = s.lower().split()

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

sort_counts = sorted(counts.items(), key=lambda x: (x[1] * -1, x[0]))

if sort_counts:
    list_len = len(sort_counts)
    for i in range(list_len):
        word_len = len(sort_counts[i][0])
        word_str = sort_counts[i][0] + (" " * (20 - word_len))
        print(word_str, end=' ')
        for i in range(sort_counts[i][1]):
            print('', end='#')
        print('')
