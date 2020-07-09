# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

from collections import Counter


letter_frequency_order = [
    'E', 'T', 'A', 'O', 'H', 'N', 
    'R', 'I', 'S', 'D', 'L', 'W', 
    'U', 'G', 'F', 'B', 'M', 'Y', 
    'C', 'P', 'K', 'V', 'Q', 'J', 
    'X', 'Z'
    ]

with open("applications/crack_caesar/ciphertext.txt", "r") as f:
    content = f.read()

alpha_counter = Counter(filter(str.isalnum, content))
mapping = {k:v for (k,v) in zip([i[0] for i in alpha_counter.most_common()], letter_frequency_order)}
output = ""

for char in content:
    output_char =  char
    if char in mapping.keys():
        output_char = mapping[char]
    output += output_char

if __name__ == "__main__":
    print(output) 

