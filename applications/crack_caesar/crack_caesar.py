# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
from collections import defaultdict


def crack_c(filename):

    freq_list = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
    'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

    with open(filename) as f:
        cipher_t = f.read()

    counts = defaultdict(int)     # init to defaultdict(<class 'int'>, {})
    # print(counts)

    for ch in cipher_t:
        if ch.isupper():
            counts[ch] += 1

    # sort by value
    print(sorted(counts.items(),  key = lambda x : x[1], reverse = True ))    
    # [('W', 1769), ('J', 1497), ('M', 1299), ('X', 1240),...


    # find items by freq value
    cipher_f = [item[0] for item in sorted(counts.items(), key = lambda x : x[1], reverse = True )]
    print(cipher_f)   # ['W', 'J', 'M', 'X',....

    # values are mapped to decode
    val_map = {cipher: val for cipher, val in zip(cipher_f, freq_list)}
    print(val_map)   # {'W': 'E', 'J': 'T', 'M': 'A', 'X': 'O',..... 


    # The translate() method returns a copy of the string in which all characters have been 
    # translated using table (constructed with the maketrans() function in the string module
    print(cipher_t.translate(str.maketrans(val_map)))



crack_c("applications/crack_caesar/ciphertext.txt")