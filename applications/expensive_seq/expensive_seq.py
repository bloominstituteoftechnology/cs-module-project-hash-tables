
def expensive_seq(x, y, z, cache = dict()):
    if x <= 0: #guard early exit
        return y + z
        
    if (x, y, z) not in cache:
        addend1 = expensive_seq(x - 1, y + 1, z, cache)
        addend2 = expensive_seq(x - 2, y + 2, z * 2, cache)
        addend3 = expensive_seq(x - 3, y + 3, z * 3, cache)
        cache[(x, y, z)] = addend1 + addend2 + addend3
        return cache[(x, y, z)]
    else:
        return cache[(x, y, z)]

if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
