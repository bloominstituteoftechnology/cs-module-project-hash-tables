# Your code here
import codecs

# hint = "Va Clguba, n qvpg xrl pna or nal vzzhgnoyr glcr... vapyhqvat nghcyr"
# codecs.encode(hint, 'rot_13')

# can use cache again
cache = {}


def expensive_seq(x, y, z):
    """
    exps(x, y, z) =
        if x <= 0: y + z
        if x >  0: exps(x-1,y+1,z) + exps(x-2,y+2,z*2) + exps(x-3,y+3,z*3)
    """
    # Your code here
    if (x, y, z) in cache:
        return cache[(x, y, z)]

    # otherwise, incorporate algorithm rules
    if x <= 0:
        cache[(x, y, z)] = y + z
        return cache[(x, y, z)]

    if x > 0:
        cache[(x, y, z)] = expensive_seq(x - 1, y + 1, z) + \
            expensive_seq(x - 2, y + 2, z * 2) + \
            expensive_seq(x - 3, y + 3, z * 3)

    # set return for recursion above
    return cache[(x, y, z)]


# if __name__ == "__main__":
#     # for i in range(10):
#     #     x = expensive_seq(i*2, i*3, i*4)
#     #     print(f"{i*2} {i*3} {i*4} = {x}")

#     # print(expensive_seq(150, 400, 800))

#     # hint = "Va Clguba, n qvpg xrl pna or nal vzzhgnoyr glcr... vapyhqvat nghcyr"
#     # print(codecs.encode(hint, 'rot_13'))

#     # In Python, a dict key can be any immutable type... including a tuple
