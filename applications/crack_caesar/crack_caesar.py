# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

cipher = {x: 0 for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}

with open('ciphertext.txt', 'r') as f:
    while 1:
        char = f.read(1)
        if char in cipher.keys():
            cipher[char] += 1
        if not char:
            break

    f.close()

char_max = sum(cipher.values())

freq = {char: val/char_max for char, val in cipher.items()}

freq_sorted = sorted(freq.items(), key=lambda x: x[1], reverse=True)

most_frequent = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D',
                 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P',
                 'K', 'V', 'Q', 'J', 'X', 'Z']

freq_mapped = {char1[0]: char2 for char1, char2
               in zip(freq_sorted, most_frequent)}

translation = str.maketrans(freq_mapped)

with open('ciphertext.txt', 'r') as f:

    file = f.read()
    file = file.translate(translation)

    print(file)
    f.close()

with open('ciphertext.txt', 'w') as f:

    f.write(file)

    f.close()
