def word_count(s):
    # Your code here
    s = (s.lower().translate({ord(c): None for c in '":;,.-+=/\\|[]{}()*^&'})).split()
    dict_of_elems = dict()

    if not s:
        return {}

    for elem in s:
        # If element exists in dict then increment its value else add it in dict
        if elem in dict_of_elems:
            dict_of_elems[elem] += 1
        else:
            dict_of_elems[elem] = 1  

    return dict_of_elems
    


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))