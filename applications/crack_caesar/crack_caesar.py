# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

with open('ciphertext.txt') as f:
    text = f.read()

charcount = {}
for char in text:
    # get only characters
    if char in map(chr, range(65, 91)):
        if char not in charcount:
            charcount[char] = 1
        else:
            charcount[char] += 1

# sort list by frequency
charcount = sorted(charcount.items(),
                   reverse=True, key=lambda item: item[1])

# set up rule list
normal_letter_freqs = ['E','T','A','O','H','N','R','I','S',
                       'D','L','W','U','G','F','Y','M','B',
                       'C','P','K','V','Q','J','X','Z']
rules = {}
for n in range(65, 91):
    rules[chr(n)] = chr(n)
l = []
for i, letter in enumerate(normal_letter_freqs):
    if letter in l:
        continue
    print(letter, charcount[i][0])
    rules[letter] = charcount[i][0]
    rules[charcount[i][0]] = letter
    l.append(letter)
    l.append(charcount[i][0])

l = []
# print(rules)
for rule in rules:
    if rule in l:
        continue
    # print(rule, rules[rule])
    text = text.replace(rule, '#')
    text = text.replace(rules[rule], rule)
    text = text.replace('#', rules[rule])
    l.append(rule)
    l.append(rules[rule])

# couldn't get it exactly to work
# I need a better system of generation and editing
# what matches with what
# 
# I think I know what the text is, though
print(text[:100])