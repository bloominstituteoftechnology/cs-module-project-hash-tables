def no_dups(s):
    '''
    str -> str

    '''
    cache = ''
    words = s.split()
    for word in words:
        if word not in cache:
           cache = cache + ' ' +word
    return cache.strip()

     

            



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))