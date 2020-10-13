

   

# Decoded hints: 
# Vgrzf: `.items()` method on a dictionary might be useful.

# Fbegvat: it's possible for `.sort()` to sort on multiple keys at once.

# Fbegvat: negatives might help where `reverse` won't.

# Cevagvat: you can print a variable field width in an f-string with
# nested braces, like so `{x:{y}}`

# _______________________________

# Do word count and reuse the code for this problem

# PSEUDOCODE

# Read the file, get string 

# FOR WORD COUNT
# Create a function for word count, pass the string for evaluation
# Lower case the string
# Gather the ignorable symbols
# Cut the ignorable symbols out of the string 
# Split the string into a list of words 
# Create a dict {}
# Iterate through the list of words
# Use this time to find the max length of string for later use
# If the word isn't in the dictionary, create a key for the word, assign value of 1 {the: 1}
# If it exists, increase the value for that key {the: 2}

# FOR HISTO
# If we get a string with only ignored characters, what do we do? 
# Consider what your code outputs - does it already cover this case? If not, make a case to handle it

# Get the count items
# Sort by the counts in descending order, then by the key alphabetically - use the hint above!

# Loop through count items [(word, count)]
# print the word, the spaces, and the #'s 

    # do something to add the right amount of spaces after each word
    # make sure to account for the 2 spaces after the longest word 
      # consider the relationship between the longest word and the current word
    # print out the # symbols based on value ("#" * the count)


# Draw a histogram of words in an input string

This is a variation of the "word count" exercise, with a focus on how to
sort the data in a dictionary.

## Input

This function takes a single filename string as an argument, e.g.

```
robin.txt
```

It should open the file, and work through it to produce the output.

(`robin.txt` is in this directory.)

## Output

Print a histogram showing the word count for each word, one hash mark
for every occurrence of the word.

Output will be first ordered by the number of words, then by the word
(alphabetically).

The hash marks should be left justified two spaces after the longest
word.

Case should be ignored, and all output forced to lowercase.

Split the strings into words on any whitespace.

Ignore each of the following characters:

```
" : ; , . - + = / \ | [ ] { } ( ) * ^ &
```

If the input contains no ignored characters, print nothing.

Sample output (truncated):

```
the              ################################################
and              ####################################
of               ###################################
a                ########################
with             #################
to               ################
robin            #############
he               ############
his              ############
that             ############
in               ###########
at               ##########
good             ##########
i                ##########
as               #########
for              #######
green            #######
thou             #######
upon             #######
ale              ######
all              ######
bow              ######
```

## Hints

Items: `.vgrzf()` zrgubq ba n qvpgvbanel zvtug or hfrshy.

`.items()` method on a dictionary might be useful

Sorting: vg'f cbffvoyr sbe `.fbeg()` gb fbeg ba zhygvcyr xrlf ng bapr.

it's possible for `.sort()` to sort on multiple keys at once.

Sorting: artngvirf zvtug uryc jurer `erirefr` jba'g.

negatives might help where `reverse` won't.

Printing: lbh pna cevag n inevnoyr svryq jvqgu va na s-fgevat jvgu
arfgrq oenprf, yvxr fb `{k:{l}}`

you can print a variable field width in an f-string with
nested braces, like so `{x:{y}}`

(The hints are encrypted with ROT13. Google for `rot13 decoder` to see
them.)