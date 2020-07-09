# Your code here


def expensive_seq(x, y, z):
    cache = {}
    def es_inner(x,y,z):

        tup = (x, y, x)

        if tup not in cache:
            if x <= 0:
                y + z
            if x > 0:
                cache[tup] = es_inner(x - 1, y + 1, z) + es_inner(x - 2, y + 2, z * 2) + es_inner(x - 3, y + 3, z * 3)

        return cache[tup]
    return es_inner(x,y,z)


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
