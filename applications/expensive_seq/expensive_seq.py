# Your code here


def expensive_seq(x, y, z):
    # Your code here
    #  ROT13 -> In Python, a dict key can be any immutable type... including a tuple.
    hashTable = {}
    inputTup = (x, y, z)
    if inputTup not in hashTable:
        if x <= 0: 
            hashTable[inputTup] = y + z
        if x >  0: 
            hashTable[inputTup] = expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3)
    return hashTable[inputTup]

if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
