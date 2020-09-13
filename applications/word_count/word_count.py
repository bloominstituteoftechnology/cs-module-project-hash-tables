def word_count(s):
    # will split the word on spaces and then will add
    # them to the dictionary and will count the number of 
    # time they occur
    my_cache = {}
    separateString = ""
    ignore = {"\"": "",  ":":"",  ";":"", ",":"",  ".":"",  "-":"",  
                "+":"",  "=":"",  "/":"",  "\\":"",  "|":"",  "[":"",  
                "]":"",  "{":"",  "}":"",  "(":"",  ")":"",  "*":"",  
                "^":"",  "&":"", "\r":"", "\n":"", "\t":""}
    hasWord = False

    if not s:
        return my_cache            # separateString
    for i in range(len(s)):
        # looping through after we have the full string and putting it in the cache
        if s[i] != " " and s[i] not in ignore:
            separateString += s[i].lower()
            hasWord = True
        if s[i] == " " or i == len(s)-1 or s[i] in ignore: # this is to check at the end of the string
            if hasWord:
                if separateString not in my_cache:
                    my_cache[separateString] = 0
                my_cache[separateString] +=1

                separateString = ""
                hasWord = False
                
    return my_cache



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))