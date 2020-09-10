# Imports
from re import sub

# proc_file takes a filename and produces a word histogram based
#   on the file text contents
def proc_file(fname):
    map_words = {}
    arr_words = []

    # Open and read the file contents
    fle  = open(fname)
    cnts = fle.read()
    fle.close()
    print(type(cnts))

    # Apply transformations to the file contents
    tmp_str = cnts.lower() # lowercase words
    tmp_str = sub("[\"\:\;\,\.\-\+\=\/\\\|\[\]\{\}\(\)\*\^\&]",
                    "", 
                    tmp_str)

    # Split the string by whitespace
    arr_words = tmp_str.split()

    # Iterate through the words and produce a word count
    for wrd in arr_words:





proc_file("robin.txt")


