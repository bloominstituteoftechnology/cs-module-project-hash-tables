# Your code here
# starts off with 0:1
# fibonacci sequence
# access information from a dictionary, with a unique key per iteration
cache = {}


def expensive_seq(x, y, z):

    # Your code here
    # base case
    if x <= 0:
        return y + z
    # common case
    # if n is not a key in the cache, will add it
    if (x, y, z) not in cache:
        cache[(x, y, z)] = expensive_seq(x-1, y+1, z) + \
            expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)

    return cache[(x, y, z)]


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
