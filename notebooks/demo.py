def expensive_function(x, y):

    # tuple
    # you can use any mutuble key
    key = (x, y)

    if key not in cache:  # if n is not a key in the cache
        cache[key] = whatever_expensive_thing_here()

    return cache[key]
