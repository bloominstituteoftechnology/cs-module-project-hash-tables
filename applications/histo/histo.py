"""
Print a histogram showing the word count for each word, one hash mark for
every occurrence of the word. Output will be first ordered by the number of
words, then by the word (alphabetically). The hash marks should be left
justified two spaces after the longest word. Case should be ignored, and all
output forced to lowercase. Split the strings into words on any whitespace.

Ignore each of the following characters:
   " : ; , . - + = / \\ | [ ] { } ( ) * ^ &
"""

from collections import defaultdict


def word_count(s):
    """
    Helper function that returns word counts for a given string.
    """
    ignore_chars = ',":;,.-+=/\\|[]{}()*^&'

    # Initialize dictionary to store word counts.
    counts = defaultdict(int)

    # Strip characters to ignore from input string.
    s_clean = s.translate(str.maketrans('', '', ignore_chars))

    # Calculate and store case-insensitive word counts.
    for word in s_clean.lower().split():
        counts[word] += 1

    return counts


# Read text from file.
with open('robin.txt') as file:
    s = file.read()

# Get word counts and sort them first by frequency (decreasing), second
# alphabetically (increasing).
counts = word_count(s)
counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

# Calculate offset for left justification of hask marks. (Two more than the
# length of the longest word found.)
width = max([len(word[0]) for word in counts]) + 2

# Print histogram.
for count in counts:
    print(f'{count[0].ljust(width)}' + '#' * count[1])
