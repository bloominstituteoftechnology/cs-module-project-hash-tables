# Your code here

# create a cache to store expensive computations
cache = {}


def expensive_seq(x, y, z):
    if x <= 0:
        # base case for ending recursion
        return y + z
    else:
        # check if the current iteration of x, y, z has already been calculated
        if (x, y, z) not in cache:
            # if it hasn't, store the calculation in the cache
            cache[(x, y, z)] = expensive_seq(x - 1, y + 1, z) + \
                expensive_seq(x - 2, y + 2, z * 2) + \
                expensive_seq(x - 3, y + 3, z * 3)

        # return calculation from the cache
        return cache[(x, y, z)]


if __name__ == "__main__":
    # run the function ten times
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
