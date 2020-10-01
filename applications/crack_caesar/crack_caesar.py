# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

letters_tally = {}
cipher_key = {}
deciphered_text = ""

with open("Coding/ComputerScience/HashTables/cs-module-project-hash-tables/applications/crack_caesar/ciphertext.txt", encoding="utf-8") as ciphered_text:
    cipher = ciphered_text.read()

frequency_sorted_alphabet = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

for letter in cipher:
    if letter.isalpha():
        if letter not in letters_tally:
            letters_tally[letter] = 1
        else:
            letters_tally[letter] += 1

sort_cipher = list(letters_tally.items())
sort_cipher.sort(reverse=True, key=lambda item: item[1])

for index, letter in enumerate(frequency_sorted_alphabet):
    cipher_key[sort_cipher[index][0]] = frequency_sorted_alphabet[index]

for letter in cipher:
    if letter.isalpha():
        deciphered_text += cipher_key[letter]
    else:
        deciphered_text += letter

print(deciphered_text)
