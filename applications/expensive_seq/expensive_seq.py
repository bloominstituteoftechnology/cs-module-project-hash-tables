# Your code here

cache = {}

def expensive_seq(x, y, z):
    first = (x-1,y+1,z)
    second = (x-2,y+2,z*2)
    third = (x-3,y+3,z*3)
    
    if x <= 0:
        return y + z
    if x >  0:
        if first not in cache.keys():
            cache[first] = expensive_seq(x-1,y+1,z)
        if second not in cache.keys():
            cache[second] = expensive_seq(x-2,y+2,z*2)
        if third not in cache.keys():
            cache[third] = expensive_seq(x-3,y+3,z*3)

                
        return cache[first] + cache[second] + cache[third]


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))