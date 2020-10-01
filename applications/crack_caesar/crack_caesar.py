# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Your code here
f = open("ciphertext.txt", "r")
s = f.read()

d = {}

for c in s:
    # isalpha() method returns True if all the characters are alphabet letters (a-z)
    if c.isalpha():
        d[c] += 1
    else:
        d[c] = 1


# for key in range(len(letters)):
#     translated = ''
#     for symbol in s:
#         if symbol in letters:
#             num = letters.find(symbol)
#             num = num - key
#             if num < 0:
#                 num = num + len(letters)
#             translated = translated + letters[num]
#         else:
#             translated = translated + symbol
# print('Hacking key #%s: %s' % (key, translated))