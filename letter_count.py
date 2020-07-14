
# write a function that takes a string
# and return each letter, along with how many times it occurs in the string
def letter_count(s):
    # create a dictionary
    counts = {}

    # iterate through the string
    for character in s:
        # ensure character is a letter
        if character.isalpha():
        # if the character is in the dictionary, increment its count
            if character in counts:
                counts[character] += 1

        # if not, add it, with value 1
            else:
                counts[character] = 1

    # return the dictionary
    return counts


# Stage 2:
## Print them all, but start with the key that occurs most often in our string
## Also: accept only letters, and ensure they are lowercased

def print_sorted_letter_count(s):

    letters = letter_count(s)

    letters_list = list(letters.items())

    letters_list.sort(key=lambda pair: pair[1], reverse=True)

    for pair in letters_list:
        print(f'Letter: {pair[0]}, count: {pair[1]}')

print_sorted_letter_count('Hello!')
print_sorted_letter_count('The quick brown fox jumps over the lazy dog')

# Review