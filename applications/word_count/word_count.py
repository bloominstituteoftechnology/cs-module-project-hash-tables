def word_count(s):
    counts = {}

    nonos = ('"', ':', ';', ',', '.', '-', '+', '=', '/', "|", '[', ']', '{', '}', "(", ')', "*", '^', '&', "\\")
    r = ""

    for c in s:
        if (c not in nonos):
            # When the alg hits a space it adds the characters before to the hashtable 
            if c == ' ':
                if r.lower() in counts:
                    counts[r.lower()] += 1
                    r = ""
                else:
                    counts[r.lower()] = 1
                    r = ""            
            # Otherwise, adds the character to the current string.
            else:
                r += c


        elif c is s[-1]:
            if c in nonos:
                if r.lower() in counts:
                    counts[r.lower()] += 1
                else:
                    counts[r.lower()] = 1
            else:
                r += c
                if r.lower() in counts:
                    counts[r.lower()] += 1
                else:
                    counts[r.lower()] = 1

    # Gets the final word because my logic above does not. 
    # if r is not None:
    #     if r is not '':
    #         if r.lower() in counts:
    #             counts[r.lower()] += 1
    #         else:
    #             counts[r.lower()] = 1

    try:
        del counts['']
    except KeyError:
        pass

    return counts

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello      hello"))
    print('~~~~~~~')
    print(word_count('Hello, my cat.  And my cat doesn\'t say "hello" back.'))
    print('~~~~~~~')
    print(word_count('This is a test of the  Emergency  Broadcast  Network. This is only a test.'))
    print('~~~~~~~')
    print(word_count('":;,.-+=/\\|[]{}()*^&'))
    print('~~~~~~~')
    print(word_count('a a\ra\na\ta \t\r\n')) # {"a": 5})
