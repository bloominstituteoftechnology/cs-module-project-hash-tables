# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

# Use the frequency key to create a decode cache that changes each letter
frequency_cache = {
  'E': 11.53,
  'T': 9.75,
  'A': 8.46,
  'O': 8.08,
  'H': 7.71,
  'N': 6.73,
  'R': 6.29,
  'I': 5.84,
  'S': 5.56,
  'D': 4.74,
  'L': 3.92,
  'W': 3.08,
  'U': 2.59,
  'G': 2.48,
  'F': 2.42,
  'B': 2.19,
  'M': 2.18,
  'Y': 2.02,
  'C': 1.58,
  'P': 1.08,
  'K': 0.84,
  'V': 0.59,
  'Q': 0.17,
  'J': 0.07,
  'X': 0.07,
  'Z': 0.03
}

def crack_caesar(file):
  with open(file) as f:
    words = f.read()
  
  letter_cache = {}
  decode_cache = {}
  letter_list = list(words)

  # Get the count of each letter and store it in a cache
  for letter in letter_list:
    if letter >= 'A' and letter <= 'Z':
      if letter in letter_cache:
        letter_cache[letter] += 1
      else:
        letter_cache[letter] = 1
  
  # For each letter, find the frequency analysis
  sorted_letter_cache = sorted(letter_cache.items(), key = lambda x: x[1], reverse = True)
  sorted_frequency_cache = sorted(frequency_cache.items(), key = lambda x: x[1], reverse = True)

  for i in range(len(sorted_letter_cache)):
    decode_cache[sorted_letter_cache[i][0]] = sorted_frequency_cache[i][0]

  # Decode each letter and store it in a string
  decoded_text = []
  for char in letter_list:
    if char in decode_cache:
      decoded_text.append(decode_cache[char])
    else:
      decoded_text.append(char)

  # Return the decoded string
  return ''.join(decoded_text)

print(crack_caesar('ciphertext.txt'))