"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""
from functools import lru_cache

@lru_cache(maxsize=64)
def f(x):
    return x * 4 + 6

def match(matrixA, matrixB, opperation):
    matches = []
    for i, w in enumerate(matrixA):
        for i2, x in enumerate(w):
            for j, y in enumerate(matrixB):
                for j2, z in enumerate(y):
                    print(f'{x} == {z}?')
                    if z == x:
                        matches.append(f'{i} {opperation} {j} = {z}')
    print(matches)
    return 0


def find(lst):  
    sumMatrix = [[row + col for col in lst] for row in lst]
    difMatrix = [[row - col for col in lst] for row in lst]
    prodMatrix = [[row * col for col in lst] for row in lst]

    for row in sumMatrix: print(row)
    print()
    for row in difMatrix: print(row)
    print()
    for row in prodMatrix: print(row)
    print(0)

    match(sumMatrix, difMatrix, 'x')
    return 0

    """
    diffs = [] 
    for i, x in enumerate(lst): 
        for j, y in enumerate(lst): 
            if i != j:  
                diffs.append(abs(x-y)) 
    """          
    return 0


#q = set(range(1, 10))
#q = set(range(1, 200))
#q = (1, 3, 4, 7, 12)
q = (1,2,3,4)
print(find(q))
"""
def f(x):
    return x * 4 + 6
"""
# Your code here

