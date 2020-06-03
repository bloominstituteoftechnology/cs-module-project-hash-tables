# Your code here
cache = {}
def exps(x, y, z):
    # Your code here

    key = (x, y, z)
    if key in cache:
        return cache[key]
    else:
        if x <= 0:
            return y + z
        if x >  0:
            a = exps(x-1,y+1,z)
            key_a = (x-1,y+1,z)
            cache[key_a] = a

            b = exps(x-2,y+2,z*2)
            key_b = (x-2,y+2,z*2)
            cache[key_b] = b

            c = exps(x-3,y+3,z*3)
            key_c = (x-3,y+3,z*3)
            cache[key_c] = c

            return a + b + c


if __name__ == "__main__":
    for i in range(10):
        x = exps(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(exps(150, 400, 800))
