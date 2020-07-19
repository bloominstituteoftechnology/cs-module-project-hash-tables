# write a function that takes a string
# returns each letter, along with how many times it occurs in the string

def letter_count(s):
    counts = {}
    
    for character in s:
        if character in counts:
            counts[character] += 1
        else:
            counts[character] = 1
    return counts

# Part 2
def print_sorted_letter_count(s):
    letter = letter_count(s)
    
    letters_list = list(letters.items())
    
    letters_list.sort(key= lambda pair: pair[1], reverse=True)
    
    for pair in letters_list:
        print(f'Letter: {pair[0]}, count: {pair[1]}')