# Your code here

values = {}

def expensive_seq(x, y, z):

    if (x, y, z) not in values:
        if x <= 0 and (y, z) not in values and (z, y) not in values:
            new_value = y + z
            values[(x, y, z)] = new_value
            values[(x, z, y)] = new_value
        else:
            new_value = expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3)
            values[(x, y, z)] = new_value
    return values[(x, y, z)] 

    # exps(x, y, z) =
    #  if x <= 0: y + z
    #  if x >  0: exps(x-1,y+1,z) + exps(x-2,y+2,z*2) + exps(x-3,y+3,z*3)



if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
