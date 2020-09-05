"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

def sum(a,b): return str(a + b)
def dif(a,b): return str(a - b)
def product(a,b): return str(a / b)
#def quot(a,b): return str(a / b)

def find(arr):
    d = dict(zip(arr, [{},{},{}]))
    for a in arr:
        for b in arr:
            if b != a:
                d[a][0] = {b:a + b}
                d[a][1] = {b:a - b}
                d[a][2] = {b:a * b}
    


#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here

