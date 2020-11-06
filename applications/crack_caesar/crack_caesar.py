# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.


# Your code here
# U -  make a table with letter frequency in it ?
# use the table to iderate through the ciphertext.text
# the most fequent letter in the ciphertext will == the most common letter in the alphabel
# to create a new table of common code .

# p
# E
# R
from csv import reader
with open("ciphertext.txt") as file:
    csv_reader = reader(file)
    for letter in csv_reader:
        print(letter)

text_letter = letter


def frequencyLetter():
    pass
