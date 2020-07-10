# # Count the words in an input string

# ## Input

# This function takes a single string as an argument.

# ```
# Hello, my cat. And my cat doesn't say "hello" back.
# ```

# ## Output

# It returns a dictionary of words and their counts:

# ```
# {'hello': 2, 'my': 2, 'cat': 2, 'and': 1, "doesn't": 1, 'say': 1, 'back': 1}
# ```

# Case should be ignored. Output keys must be lowercase.

# Key order in the dictionary doesn't matter.

# Split the strings into words on any whitespace.

# Ignore each of the following characters:

# ```
# " : ; , . - + = / \ | [ ] { } ( ) * ^ &
# ```

# If the input contains no ignored characters, return an empty dictionary.



def word_count(input_string):

    # Let's first remove the special characters
    # Then we need to convert the string to all lowercase
    # Next we should split on whitespace making a list
    # Finally input that list into a dictionary to count the occurances of each word

    special_characters = ['\"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
    filtered_string = ''.join(filter(lambda c: c not in special_characters, input_string))
    lower_string = filtered_string.lower()
    word_array = lower_string.split()

    word_counts = {}

    for word in word_array:
        if word not in word_counts:
            word_counts[word] = 0

        word_counts[word] += 1

    return word_counts




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))