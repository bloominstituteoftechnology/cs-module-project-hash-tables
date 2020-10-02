# Your code here
#from functools import map

with open('robin.txt', 'r') as f:
    lines = f.readlines()
d = {}
for i in range(len(lines)):
    s = lines[i]
    table = s.maketrans('', '', '":;,.-+=/\|[]{}()*^&')
    s = s.translate(table)
    words = s.split()
    for word in words:
        word = word.lower()
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

word_lst = []
for word in d:
    word_lst.append([word, d[word]])

word_lst.sort(key=lambda x: (-x[1], x[0]))

longest_len = 0
for i in range(len(word_lst)):
    if len(word_lst[i][0]) > longest_len:
        longest_len = len(word_lst[i][0])

for idx in range(len(word_lst)):
    print(f'{word_lst[idx][0]:{longest_len}}', '#' * word_lst[idx][1])

# print(word_lst)

# # Read file into the list - lines
# with open('robin.txt', 'r') as f:
#     lines = f.readlines()

# # Construct dictionary - d - containing frequencies of words
# d = {}
# for s in lines:
#     table = s.maketrans('', '', '":;,.-+=/\|[]{}()*^&')
#     s = s.translate(table)
#     words = s.split()
#     for word in words:
#         word = word.lower()
#         if word in d:
#             d[word] += 1
#         else:
#             d[word] = 1

# # Generate custom sorted list of frequencies
# word_lst = list(d.items())
# word_lst.sort(key=lambda x: (-x[1], x[0]))

# # Compute longest_len, so that we can use it for formatting output
# # longest_len = max(map(lambda x: x[1], word_lst))
# longest_len = max(d.values())

# # Print output as per requirement
# for pair in word_lst:
#     print(f'{pair[0]:{longest_len}}', '#' * pair[1])
