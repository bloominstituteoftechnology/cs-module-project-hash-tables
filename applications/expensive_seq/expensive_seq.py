# Your code here
cache = {}

def expensive_seq(x, y, z):
    # Will do memoization with a dictionary
    if x <= 0:
        return y +z

    elif cach





if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
