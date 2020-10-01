data = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

def getSumMin(arr):
    sum = 0
    for i in arr:
        min = i[0]
        for x in i:
            if min > x:
                min = x
        sum += min
    return sum
    

cache = {}
def fib(n):
    if n <= 1:
        return n
    else:
        if n not in cache:
            cache[n] = fib(n-1) + fib(n-2)
        return cache[n]

for i in range(100):
    print(f"{i}: {fib(i)}")
# print(fib(1000))