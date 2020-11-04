# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
f = open('ciphertext.txt', 'r')
ciphertext = f.read()
f.close()

cipher_dict = { }
for x in ciphertext:
    if x in cipher_dict:
        cipher_dict[x] += 1
    else:
        cipher_dict[x] = 0

print(cipher_dict)
print(" - - -- - -")
ok = {k: v for k, v in sorted(cipher_dict.items(), key=lambda item: item[1])}
print(ok)


for item in list(ok):
    if ok[item] == 0:
        del ok[item]

for item in list(ok):
    if item == ':' or item == '—' or item == '?' or item == '!' or item == ';' or item == '.'  or item == '\n' or item == '"' or item == "'" or item == '"' or item == ',' or item == ' ':
        ok.pop(item)
ok.pop('-')

print(" - - -- - -")
print(ok)

# new_string = ""
# count = 0
# for x in ciphertext:
#     if x == 'X':
#         x = 'E'
#         new_string += x
    
#     if x == ''

#     if count == 50:
#         break
    
#     # ciphertext[0] == "+"
#     # print(ciphertext[0])
#     # break

# print(new_string)
# print(ciphertext)


        

