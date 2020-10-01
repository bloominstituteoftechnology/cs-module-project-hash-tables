# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
ignore = ['\"', ':', ';', ',', '.', '-', '+', '=', '/', "\\", '|', '[', ']', '{', '}', '(', ')', '*', '^', '&', '”', '€', '!', '?', '1', 'â', " ", "\'", "\n"]

with open('ciphertext.txt') as f:
    text = f.read()

char_count = {}
for char in text:
    if char in ignore:
        continue
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

sorted_pre_key = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
freq = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
keys = {}
for ind, tup in enumerate(sorted_pre_key):
    keys[tup[0]] = freq[ind]

new_text = ""
for char in text:
    if char in ignore:
        new_text += char
    else:
        new_text += keys[char]



print(new_text)