# Your code here
# set cache to track computations already completed
cache = {}


def expensive_seq(x, y, z):
    # search for item in cache if not present and x is >=0 add to cache
    if(x, y, z) not in cache:
        if x <= 0:
            cache[(x, y, z)] = y + z
        else:
            cache[x, y, z] = expensive_seq(
                x-1, y+1, z) + expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)
    return cache[(x, y, z)]


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))

# Research:
# ROT13 (rotate by 13 places) replaces a letter with the letter 13 letters after it in the alphabet. It has been described as the "Usenet equivalent printing an answer to a quiz upside down" as it provides virtually no cryptographic security.

# Decoded hint:
# In Python, a dict key can be any immutable type... including a tuple.
# Seems like the problem is similar to the last problem with different math.
