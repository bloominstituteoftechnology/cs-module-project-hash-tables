"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
from itertools import combinations_with_replacement
# will create a dictionary that has as the keys the ans to the function of each 
# number in the set. The value will be the number in the set


def myFunction(q):
    theList = list(q)
    answers = []
    ans_cache = {}
    combos = [] # This will store those that that make the correct
    cache = {}
    sub_cache = {}
    # making the cache of answers
    for elem in theList:
        ans = f(elem)
        cache[elem] = ans
        #answers.append(ans)

    # will now get all the different combinations of each 
    # and will then put them in the add_cache and put them 
    # in the minus cache
    comboList = list(combinations_with_replacement(q, r=3))
   
    # will now loop through the combo list and find both the 
    # add and substract of each and put it into a hash table
    # there are two different subtract caches for each combo
    # because a - b doesn't equal b-a
    for theTuple in comboList:
        
        if  cache[theTuple[0]] not in ans_cache:
            ans_cache[f(theTuple[0])] =  theTuple[0]
        
        if cache[theTuple[1]] not in ans_cache:
            ans_cache[f(theTuple[1])] = theTuple[1]
        
        if cache[theTuple[2]] not in ans_cache:
            ans_cache[f(theTuple[2])] = theTuple[2]
        # will now do the add_cache and the sub cache
        # when returning the add cache need to return the tuple as is and also 
        # reversed be
        # add_cache[ans_cache[theTuple[0]] + ans_cache[theTuple[1]]] = theTuple
        # using only the subtraction becuase changing the formula to solve for a
        
            
        if (theTuple) not in sub_cache:
            sub_cache[theTuple] =  cache[theTuple[0]] - cache[theTuple[1]] - cache[theTuple[2]]
        if (theTuple[1], theTuple[0], theTuple[2]) not in sub_cache:
            sub_cache[(theTuple[1], theTuple[0], theTuple[2])] =   cache[theTuple[1]] - cache[theTuple[0]] - cache[theTuple[2]]
        if (theTuple[1], theTuple[2], theTuple[0]) not in sub_cache:   
            sub_cache[(theTuple[1], theTuple[2], theTuple[0])] =   cache[theTuple[1]] - cache[theTuple[2]] - cache[theTuple[0]]
        if (theTuple[0], theTuple[2], theTuple[1]) not in sub_cache:
            sub_cache[(theTuple[0], theTuple[2], theTuple[1])] =  cache[theTuple[0]] - cache[theTuple[2]] - cache[theTuple[1]]
        if (theTuple[2], theTuple[0], theTuple[1]) not in sub_cache:
            sub_cache[(theTuple[2], theTuple[0], theTuple[1])] =  cache[theTuple[2]] - cache[theTuple[0]] - cache[theTuple[1]]
        if (theTuple[2], theTuple[1], theTuple[0]) not in sub_cache:
            sub_cache[(theTuple[2], theTuple[1], theTuple[0])] =  cache[theTuple[2]] - cache[theTuple[1]] - cache[theTuple[0]]

    # now need to go through and see if there are any thing in the answer cache that will equal that of the sub cache
    for k , v in sub_cache.items():
        
        if v in ans_cache:
            combos.append((ans_cache[v], k[2], k[0], k[1]))
    
    return combos



if __name__ == "__main__":
    print(myFunction(q))