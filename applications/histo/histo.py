def print_hist(l, max_length=10):
    """
    @params l is a list of tuples with a word and a count, 
        sorted by count: [("the", 17), ("was", 10), ...]
    @oarams max_length is an optional parameter specifying the
        length of the longest word in the list

    print_hist creates a text string that iterates over a list and
    adds lines for every tuple in the following format: 
        word    ###### (number of hashes based on count)
        the     ####
        in      #
        end     #
        nightly #
    prints that text string, no return value
    """
    text = ""
    for i in l:
        text += f"{i[0]:{max_length}s} " + "#" * i[1] + "\n"
    print(text)


def histo(s):
    """
    @params s is a string of any length
    """

    # initialize dictionary of word counts
    frequency_dict = {}
    # keep track of the length of the longest word in the string
    current_max = 0

    # ignores the following characters and converts string to lowercase
    ignore = '" : ; , . - + = / \ | [ ] { } ( ) * ^ & ? !'.split(" ")
    for char in ignore:
        s = s.replace(char, "")
        s = s.lower()

    # split the string into an array of words
    words = s.split()
    # iterate over every word
    for word in words:
        # if this is first occurence of the word, initialize it ot 0 in dict
        if word not in frequency_dict:
            frequency_dict[word] = 0
            # check if the word is longer than our current longest word
            current_max = len(word) if len(word) > current_max else current_max
        # increment the word count by 1
        frequency_dict[word] += 1
    # convert the dictionary into a list of tuples and sort it based on
    # word count from high to low
    frequency_list = [x for x in frequency_dict.items()]
    frequency_list.sort(key=lambda e: e[1], reverse=True)

    # call the function to print the relevant histogram of word frequencies
    print_hist(frequency_list, current_max)


def file_word_count_histo(filename):
    """
    reads in a file with the express purpose of printing out a 
    histogram of its word count
    """
    with open(filename) as f:
        text = f.read()
    histo(text)


if __name__ == "__main__":
    file_word_count_histo("applications/histo/robin.txt")
