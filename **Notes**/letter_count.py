print('\n')
example_string = "The quick brown fox jumps over the lazy dog"
print(example_string)
# The quick brown fox jumps over the lazy dog
print('\n')
string_list = example_string.split()
print(string_list)
# ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
print('\n')
giant_string = "".join(string_list)
print(giant_string)
#Thequickbrownfoxjumpsoverthelazydog
print('\n')
print(len(giant_string))
# 35