# Your code here
with open("robin.txt") as f:
    words = f.read() # put words into an array
    word_split = words.split() # split array into words

cache = {}

for word in word_split: # check word and see if it is in cache.
    if word not in cache:
        cache[word] = '#'
    else:
        cache[word] += '#'
  
items = list(cache.items())

items.sort(key=lambda x: x[1], reverse=True) # sort frequency descending

for key, value in items:
    print(f'{key:<18} {value}')




# Understand
# given a string
## return every letter and how many times it occurs in this string
## sorted by frequence of occurrence​
  
# Planning
# iterate through our string
# tally the count using a dictionary
# sort our dictionary by the value (i.e. the count of each letter)
# ​
# upper- or lower-case everything
# handle spaces
# ​
# should we turn the string into a list first?
# ​
# Execute
# def print_letter_count(s):
#     tally = {}
# ​
#     s = s.lower()
#     for character in s:
#         # if not char.isspace():
#         # if char != " ":
#         if character >= 'a' and character <= 'z':
#             if character not in tally:
#                 tally[character] = 1
#             else:
#                 tally[character] += 1
# ​
#     # print(sorted(tally.items(), key=lambda x: x[1], reverse=True))
#     # sorted gives back a new function
# ​
#     # sort works in place
#     tally_list = list(tally.items())
#     tally_list.sort(key=lambda x: x[1], reverse=True)
# ​
#     # alternate way to reverse sort
#     # tally_list.sort(key = lambda x: (-(x[1]))
# ​
#     for pair in tally_list:
#         print(f'Count: {pair[1]}, letter: {pair[0]}')
# ​
# ​
# ​
# print_letter_count("bunny hop")
# print_letter_count("The quick brown fox jumps over the lazy dog")
# ​
# # Review
# ## Well we could handle more char