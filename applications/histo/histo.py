def histo(filename):
    # open file
    with open(filename, 'r') as f:
        # set string text to variable
        s = f.read()
    # list of characters to ignore
    characters_to_ignore = ['"', ":", ";" , ".", "-", "+", "=", "/", "[", "]",
    "{", "}", "(", ")", ",", "*", "^", "&", "|", '\\']
    # for each character in input string
    for character in s:
        # if it's in the ignored characters
        if character in characters_to_ignore:
            # replace the value with whitepsace
            s = s.replace(character, ' ')
    # now, ready to make string a list by splitting string on whitespace
    words = s.split()
    # make all words in list lowercase
    words = [word.lower() for word in words]
    # create an empty dict
    word_dict = {}
    # for each word in our list of words 
    for word in words:
        # if not already in dict
        if word not in word_dict:
            # add new key/value pair
            word_dict[word] = 1
        # if word in dict
        else:
            # increase the counter
            word_dict[word] += 1
    # sort the list of tuples by the second key first (counts, descending)
    # then by the first key (alphabetical order)
    for tup in sorted(word_dict.items(), key=lambda x: (-x[1], x[0])):
        # print our word and it's associated word count as a histogram
        print(tup[0].ljust(20) + "  " + ("#" * tup[1]))


if __name__ == '__main__':

    histo('robin.txt')

