def no_dups(s):
    # Your code here
    cache = []

    s = s.lower().split()
    space = " "

    if not s:
        return ""
    
    for word in s:
        if word not in cache:
            cache.append(word)

    return space.join(cache)

# Why doesn't this work?
    # s = s.lower().split()
    # no_repeats = set(s)
    # space = " "

    # if not s:
    #     return ""
    
    # # Difference of list including duplicates 
    # left_overs = (list(map(lambda x: s.remove(x)  
    #     if x in s else None, no_repeats))) 
    
    # new_str = s - left_overs

    # return space.join(new_str)
    

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))