from collections import Counter

with open("applications/histo/robin.txt", "r") as f:
    content = f.read()

s = content.translate(str.maketrans(content, content, ':,;.-+=/\|[]{}()*^&"'))

backslash_strings = ["\n", "\t", "\r"]
for bs in backslash_strings:
    s = s.replace(bs, " ") 

if len(s) == 0:
    print("Text not found")

words = [es.lower() for es in s.split(" ") if es is not ""]

counts = Counter(words)
indentation = len(max(words, key=len)) + 2
sorted_list_of_words = sorted(counts, key=lambda k: (-counts[k], k))

for word in sorted_list_of_words:
    spacing = (indentation - len(word)) * " "
    pound_signs = counts[word] * "#"
    print(f"{word}{spacing}{pound_signs}")

