# Imports
from re import sub

def word_count(s):
    # Copy the inbound string (lowercase)
    tmp_map = {}
    tmp_s   = s.lower()

    # Strip special characters
    tmp_s = sub("[\"\:\;\,\.\-\+\=\/\\\|\[\]\{\}\(\)\*\^\&]", "", tmp_s)

    # Split the updated string into word segments
    tmp_wds = tmp_s.split()

    # Iterate through the list of words and count
    for wd in tmp_wds:
        # Iterating over a new word?
        if wd not in tmp_map:
            tmp_map[wd] = 1
            continue

        # Increment word count
        tmp_map[wd] = tmp_map[wd] + 1

    return tmp_map

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))