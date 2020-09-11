# Your code here
from hashtable import HashTable
import time

table = HashTable(150)
#table = {}

def expensive_seq(x, y, z):
    key = f'{x}, {y}, {z}'
    entry = table.get(key)
    if x <= 0:
        return y + z
    elif entry:
        return entry
    else:
        val = expensive_seq(x - 1, y + 1, z) + expensive_seq(x - 2, y + 2, z * 2) + expensive_seq(x - 3, y + 3, z * 3)
        table.put(key, val)
        #table[key] = val
        return val




if __name__ == "__main__":
    start = time.time()
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
    end = time.time()
    print('Runtime: ', end - start)
    # 2.59 with my hashtable 8 capacity, probably slowed by table resizing
    # 2.15 with an appropriate capacity, still slow
    # 0.1367 with dicts

