# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

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
alphanumeric_counter = Counter(filter(str.isalnum, content))
mapping = {k:v for (k,v) in zip([i[0] for i in alphanumeric_counter.most_common()], letter_frequency_order)}
output = ""
for character in content:
    output_character =  character
    if character in mapping.keys():
        output_character = mapping[character]
    output += output_character

if __name__ == "__main__":
    print(output)