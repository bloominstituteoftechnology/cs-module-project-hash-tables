# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
f = open("ciphertext.txt", "r")
badchars = ["1", ":", ";", ",", ".", "\n", "—", "?", "!", "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&", "\"", " ", "'"]

cache = {}
for x in f.read():
	if x in badchars:
		continue
	if x in cache:
		cache[x] += 1
	else:
		cache[x] = 1

count = 0
for k in cache.values():
	count += k

a = sorted(cache.items(), key=lambda kv: (kv[1], kv[0]))
code = ["Z", "X", "J", "Q", "V", "K", "P", "C", "Y", "M", "B", "F", "G", "U", 'W', "L", "D", "S", "I", "R", "N", "H", "O", "A", "T", "E"]

decode_table = {}
counter = 0
for item in a:
	for x in item[-2]:
		decode_table[x] = code[counter]
		counter += 1

def decode(s):
	r = ""
	for c in s:
		if c in decode_table:
			r += decode_table[c]
		else:
			r += c
	return r

f.close()

fx = open("ciphertext.txt", "r")
print(decode(fx.read()))
fx.close()
