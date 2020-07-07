from collections import Counter

# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
common = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
          'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

with open("./ciphertext.txt", "r") as f:
    content = f.read()


c = Counter(filter(str.isalnum, content))

mapping = {k:v for (k,v) in zip([i[0] for i in c.most_common()], common)}
output = ""
for char in content:
    output_char =  char
    if char in mapping.keys():
        output_char = mapping[char]
    output += output_char

print(output)
