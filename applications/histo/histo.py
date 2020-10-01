# Imports
from re import sub

# proc_file takes a filename and produces a word histogram based
#   on the file text contents
def proc_file(fname):
    map_words2count = {}  # map [string]:[int]
    map_count2words = {}  # map [int]:[list of words]
    arr_words       = []
    max_wrd_len     = 0

    # Open and read the file contents
    fle  = open(fname)
    cnts = fle.read()
    fle.close()

    # Apply transformations to the file contents
    tmp_str = cnts.lower() # lowercase words
    tmp_str = sub("[\"\:\;\,\.\-\+\=\/\\\|\[\]\{\}\(\)\*\^\&]",
                    "", 
                    tmp_str)

    # Split the string by whitespace
    arr_words = tmp_str.split()

    # Iterate through the words and produce a word count
    for wrd in arr_words:
        # Is this longest word?
        if len(wrd) > max_wrd_len:
            # Yes, store the length value
            max_wrd_len = len(wrd)

        # Newly encountered word?
        if wrd not in map_words2count:
            # Found a new word
            map_words2count[wrd] = 1
            continue

        map_words2count[wrd] = map_words2count[wrd] + 1

    # Iterate through the map of words and construct a 
    #    map of count to list of words
    for wd, ct in map_words2count.items():
        # Encountering a new count value?
        if ct not in map_count2words:
            # Yes, insert new count in map
            map_count2words[ct] = list([wd])
            continue

        map_count2words[ct].append(wd)

    # Iterate through map_count2words and sort the list of words 
    #   for each mapping
    for ct in map_count2words.keys():
        map_count2words[ct].sort()

    # Sort map_count2words (descending) by key value 
    map_count2words_srtd = sorted(map_count2words.items(), key=lambda x: x[0], reverse=True)

    # Iterate through the sorted map of words and print out a rough histogram visual
    for tpl in map_count2words_srtd:
        # Construct a string to print
        hashes_num  = tpl[0]                   # number of hash signs
        hash_signs  = "#" * hashes_num         # string of hashes

        # Iterate through the list of words with this count 
        for wdr in tpl[1]:
            filr_num    = max_wrd_len - len(wdr)   # number of spaces (numeric value)
            filr        = " " * filr_num           # number of spaces (string)
            if filr_num == 0:
                filr = ""

            # Print out a string
            print("{word}{filler}: {hashes}".format(word=wdr, filler=filr, hashes=hash_signs))

proc_file("robin.txt")

