

func slowfun_too_slow(x, y) {
    v :=  x^y
    v := v!
    v := v // (x + y)
    v := v mod 982451653

    return v
}

Need to make this run faster using a lookup table.

Should the lookup be outside the function scope?
    *yes*
Is skipping the math operations on numbers it's alreay run enough to spped up the overall op?
    *not if you're caching individual x+y queries but if you're using the results of factorial operations the lookup wold be far ahead of the operations at sufficient size*

How do we cache the factorial operation?
    **
    the code is:
    v = math.factorial(v)

    so if we check right before we do that and see if we've computed that factorial before we can just return the previous result istead of sending the processor through a multi-recursive operation it's done before. If not we can let it run the op and cache the result on the way 

    if my_lookup[v] is not None:
        v = my_lookup[v].value
    else:
        my_lookup[v].value = math.factorial(v)
        v = my_lookup[v].value

    This implements a system by which things must always be cached as they are always retrieved from the cache.
    **