import string

# Your code here
def decode_cipher(input_file: str):
    known_frequency = ["E", "T", "A", "O", "H", "N", "R", "I", "S", "D", "L", "W", "U", "G", "F", "B", "M", "Y", 
    "C", "P", "K", "V", "Q", "J", "X", "Z"]
    within = string.ascii_uppercase
    counted_set = {}
    letter_percentages = {}
    cipher_map = {}
    with open(input_file) as f:
        cipher_text = f.read()
    for char in cipher_text:
        if char in within:
            if counted_set.__contains__(char):
                counted_set[char] += 1
            else:
                counted_set[char] = 1
        
    for letter in within:
        percentage = (counted_set[letter] / len(cipher_text)) * 100
        letter_percentages[letter] = percentage
    items = list(letter_percentages.items())
    items.sort(key = lambda x: -x[1])
    index = 0
    for (key, value) in items:
        cipher_map[key] = known_frequency[index]
        index += 1
    decoded = ""
    for char in cipher_text:
        if char in within:
            char = cipher_map[char]
        decoded += char
    return decoded

print(decode_cipher("ciphertext.txt"))