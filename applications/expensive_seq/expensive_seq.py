# Your code here
# exps(x, y, z) =
#    if x <= 0: y + z
#   if x >  0: exps(x-1,y+1,z) + exps(x-2,y+2,z*2) + exps(x-3,y+3,z*3)


def expensive_seq(x, y, z, cache=dict()):
    # print(cache)
    # print((x, y, z))
    if x <= 0:
        return y + z
    if (x, y, z) not in cache:
        cache[(x, y, z)] = expensive_seq(x - 1, y + 1, z, cache) + expensive_seq(
            x - 2, y + 2, z * 2, cache) + expensive_seq(x - 3, y + 3, z * 3, cache)
        return cache[(x, y, z)]
    else:
        return cache[(x, y, z)]


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i * 2, i * 3, i * 4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
