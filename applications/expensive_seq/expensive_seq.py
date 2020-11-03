# Your code here
# exps(x, y, z) =
    #  if x <= 0: y + z
    #  if x >  0: exps(x-1,y+1,z) + exps(x-2,y+2,z*2) + exps(x-3,y+3,z*3) 
    
nums  = {}
def expensive_seq(x, y, z):
    # Your code here
    if (x, y, z) in nums.keys():
        return nums[(x, y, z)]

    if x <= 0:
        return y + z

    if x > 0:
        value = expensive_seq(x-1, y+1, z) + expensive_seq(x-2,
                                                           y+2, z*2) + expensive_seq(x-3, y+3, z*3)

    nums[(x, y, z)] = value
    return value



if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
