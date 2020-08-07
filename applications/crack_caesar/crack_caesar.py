# Use frequency analysis to find the key to ciphertext.txt,
# and then decode it.

# Your code here
def letter_count(text):
    """
    @params text is string of any length

    letter_count takes a string and returns a dictionary of the count of each specific
    character in the following format: {"A": 54, "B": 12, ...}
    """

    # the count does not include the following characters
    ignore = '" : ; , . - + = / \ | [ ] { } ( ) * ^ & ? ! \''.split(" ")
    ignore.extend([" ", "\n"])

    # counting code
    counts = {}
    for i in text:
        if i not in counts and i not in ignore:
            counts[i] = 0
        if i not in ignore:
            counts[i] += 1

    # return the dictionary
    return counts


def readfile(filename):
    # reads in a file and returns the text as a whole block
    with open(filename) as f:
        text = f.read()
    return text


def file_decode(filename):
    """
    @params filename is a string filename relative to the root of the project,
    or wherever the terminal root is that's runnign the program

    file_decode reads in a file that is encoded with a simple caesar cipher, where
    individual letters are mapped 1:1 to another distinct letter in the alphabet, and
    decodes it, returning a string of the whole decoded file

    this function assumes all letters in the file are uppercase and that symbols
    and spaces in the file are not encoded
    """

    # an array listing the letters of the english language in order of relative frequency
    general_frequency = [
        "E", "T", "A", "O", "H", "N", "R", "I", "S", "D", "L", "W", "U", "G", "F", "B", "M", "Y", "C", "P", "K", "V", "Q", "J", "X", "Z"]

    # read in the file
    text = readfile(filename)
    # store a count of the letters into a dictionary d
    d = letter_count(text)
    # convert dictionary elements into an array of tuples
    input_frequency = [item_tuple for item_tuple in d.items()]
    # sort the array based on frequency (second tuple element) from high to low
    input_frequency.sort(key=lambda e: e[1], reverse=True)
    # map the sorted list of tuples into a sorted array of just the letters (first tuple element)
    input_frequency = [x for x, y in input_frequency]

    """
    This array should, with a *high probability* of correctness, map 1:1 with the
    corresponding *decoded* letter in general_frequency! So to decode, all we have
    to do is convert l[index] -> general_frequency[index]
    """

    # initialize empty return string
    newText = ""
    # iterate over every character in the file
    for cur in range(len(text)):
        # if the character is alphabetical
        if text[cur].isalpha():
            try:
                # attempt to find the index of that letter in our sorted array
                frequency_index = input_frequency.index(text[cur])
                # in our return text, return the *decoded* character with the same index
                newText += general_frequency[frequency_index]
            except:
                # if that fails, the character is either not a letter or there's an issue
                # with the mapping indices, in which case the original character is maintained
                newText += text[cur]
        else:
            # if the character is for sure not a letter, don't change it
            newText += text[cur]

    # return the *mostly or completely* decoded string
    return newText


if __name__ == "__main__":
    print(file_decode("applications/crack_caesar/ciphertext.txt"))
