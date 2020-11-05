# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# master_frequency = {
#     "E": 11.53,
#     "T": 9.75,
#     "A": 8.46,
#     "O": 8.08,
#     "H": 7.71,
#     "N": 6.73,
#     "R": 6.29,
#     "I": 5.84,
#     "S": 5.56,
#     "D": 4.74,
#     "L": 3.92,
#     "W": 3.08,
#     "U": 2.59,
#     "G": 2.48,
#     "F": 2.42,
#     "B": 2.19,
#     "M": 2.18,
#     "Y": 2.02,
#     "C": 1.58,
#     "P": 1.08,
#     "K": 0.84,
#     "V": 0.59,
#     "Q": 0.17,
#     "J": 0.07,
#     "X": 0.07,
#     "Z": 0.03,
# }

aaaaaaa = open("ciphertext.txt", 'r')
for line in aaaaaaa.readlines(1):
    print(str(line))
# for line in cipher:
#     print(line)
# cipher.close()
# ? Import text
# ? make it a list

# ? Init a dict of count and a-z keys with vals of 0

# ? loop through text
# ? if letter, increase its count in dict by 1 and val of 'count' by one

# ? Then go through alphabet dict and divide letter count by length count and reassign it

# ? loop again and swap frequency value for corresponding letter

# ? Loop through text and swap each letter
