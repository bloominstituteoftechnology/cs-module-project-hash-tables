# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

with open("ciphertext.txt") as f:
    words = f.read()

# create decode table based off of frequency of letters in file 

decode_table = {
    'A': 'C',
    'B': 'F',
    'C': 'H',
    'D': 'N',
    'E': 'M',
    'F': 'Y',
    'G': 'U',
    'H': 'V',
    'I': 'I',
    'J': 'T',
    'K': 'R',
    'L': 'X',
    'M': 'A',
    'N': 'S',
    'O': 'W',
    'P': 'K',
    'Q': 'G',
    'R': 'Z',
    'S': 'L',
    'T': 'J',
    'U': 'D',
    'V': 'Q',
    'W': 'E',
    'X': 'O',
    'Y': 'B',
    'Z': 'P'
}
letter_count = {}

for c in words:

    if not c.isalpha():
        continue
    # count up all occurrences of each of each letter and add to letter_count 
    if c not in letter_count:
        letter_count[c] = 1
    else:
        letter_count[c] += 1


    # assign each cipherletter its actual letter 

# use decode table to decrypt file 

# i = list(letter_count.items())
# i.sort(key=lambda e: -e[1])
# print(i)

# print(letter_count)

def decrypt(s):
	result = ''

	for c in s:
		c = c.upper()

		if c.isalpha():
			result += decode_table[c]
		else:
			result += c

	return result

print(decrypt(words))