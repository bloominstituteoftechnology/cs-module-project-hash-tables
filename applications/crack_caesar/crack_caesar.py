# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
freqs = {}
with open('ciphertext.txt') as f:
    for line in f:
        for char in line:
            if char in freqs:
                freqs[char] += 1
            else:
                freqs[char] = 1

del freqs[' ']
del freqs[',']
del freqs['.']
del freqs["'"]
del freqs["\n"]
del freqs['"']
del freqs[';']
del freqs[':']
del freqs['-']
del freqs['?']
del freqs['!']
del freqs['â']
del freqs['€']
del freqs['”']
del freqs['(']
del freqs['1']
del freqs[')']

# Create a list of sorted letters
freqs = sorted(freqs.items(), key=lambda x: x[1], reverse=True)
print(freqs)

# Building the code
actual_freq = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

# Create a dictionary
decoder = {}

for index, item in enumerate(freqs):
    print(item[0])
    decoder[item[0]] = actual_freq[index]

print(decoder)


# DECODE!
string = ' '

with open('ciphertext.txt') as f:
    for line in f:
        for char in line:
            if char in decoder:
                string += decoder[char]
            else:
                string += char

print(string)