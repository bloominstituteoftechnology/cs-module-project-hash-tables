
seq = {}

def expensive_seq(x, y, z):
    # if x is less than or equal to 0, then just return the sum of y and z
    if x <= 0:
        return y + z
    else:
        # if (x, y, z) is not already stored in our sequence
        if (x, y, z) not in seq:
            # then we perform the proper calculations
            seq[(x, y, z)] = expensive_seq(x-1, y+1, z) + expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)
        # finally we return our sequence
        return seq[(x ,y, z)]



if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
