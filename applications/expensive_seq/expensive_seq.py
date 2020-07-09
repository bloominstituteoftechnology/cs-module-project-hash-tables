# Your code here


results = dict()


def expensive_seq(x, y, z):
    if x <= 0:
        return y + z
    else:
        if(x-1, y+1, z) in results:
            append1 = results[(x-1, y+1, z)]
        else:
            append1 = expensive_seq(x-1, y+1, z)
            results[(x-1, y+1, z)] = append1
        if (x-2, y+2, z*2) in results:
            append2 = results[(x-2, y+2, z*2)]
        else:
            append2 = expensive_seq(x-2, y+2, z*2)
            results[(x-2, y+2, z*2)] = append2

        if (x-3, y+3, z*3) in results:
            append3 = results[(x-3, y+3, z*3)]
        else:
            append3 = expensive_seq(x-3, y+3, z*3)
            results[(x-3, y+3, z*3)] = append3

        result = append1 + append2 + append3
        results[(x, y, z)] = result

        return result


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
