from functools import lru_cache
@lru_cache(maxsize=64)
def expensive_seq(x, y, z):
    if x <= 0: return y + z
    if x > 0: return expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3)

"""
cache = {}
def expensive_seq(x, y, z):
    if x <= 0:
        return y + z
    if (x, y, z) not in cache:
        cache[(x, y, z)] = expensive_seq(x - 1, y + 1, z) + expensive_seq(x - 2, y + 2, z * 2) + expensive_seq(x - 3, y + 3, z * 3)
    return cache[(x, y, z)]
"""




if __name__ == "__main__":
    
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")
    
    print(expensive_seq(150, 400, 800))
    """
    print(f'input: 111 output: {expensive_seq(1, 1, 1)}')
    print(f'input: 222 output: {expensive_seq(2, 2, 2)}')
    print(f'input: 333 output: {expensive_seq(3, 3, 3)}')
    print(f'input: 444 output: {expensive_seq(4, 4, 4)}')
    print(f'input: 555 output: {expensive_seq(5, 5, 5)}')
    print(f'input: 666 output: {expensive_seq(6, 6, 6)}')
    print('')
    print(f'input: 100 output: {expensive_seq(1, 0, 0)}')
    print(f'input: 200 output: {expensive_seq(2, 0, 0)}')
    print(f'input: 300 output: {expensive_seq(3, 0, 0)}')
    print(f'input: 400 output: {expensive_seq(4, 0, 0)}')
    print(f'input: 500 output: {expensive_seq(5, 0, 0)}')
    print(f'input: 600 output: {expensive_seq(6, 0, 0)}')
    print('')
    print(f'input: 110 output: {expensive_seq(1, 1, 0)}')
    print(f'input: 210 output: {expensive_seq(2, 1, 0)}')
    print(f'input: 310 output: {expensive_seq(3, 1, 0)}')
    print(f'input: 410 output: {expensive_seq(4, 1, 0)}')
    print(f'input: 510 output: {expensive_seq(5, 1, 0)}')
    print(f'input: 610 output: {expensive_seq(6, 1, 0)}')
    print('')
    print(f'input: 101 output: {expensive_seq(1, 0, 1)}')
    print(f'input: 201 output: {expensive_seq(2, 0, 1)}')
    print(f'input: 301 output: {expensive_seq(3, 0, 1)}')
    print(f'input: 401 output: {expensive_seq(4, 0, 1)}')
    print(f'input: 501 output: {expensive_seq(5, 0, 1)}')
    print(f'input: 601 output: {expensive_seq(6, 0, 1)}')
    print('')


    print(f'input: 111 output: {expensive_seq(1, 1, 1)}')
    print(f'input: 122 output: {expensive_seq(1, 2, 2)}')
    print(f'input: 133 output: {expensive_seq(1, 3, 3)}')
    print(f'input: 144 output: {expensive_seq(1, 4, 4)}')
    print(f'input: 155 output: {expensive_seq(1, 5, 5)}')
    print(f'input: 166 output: {expensive_seq(1, 6, 6)}')

    print('')
    print(f'input: 011 output: {expensive_seq(0, 1, 1)}')
    print(f'input: 010 output: {expensive_seq(0, 1, 0)}')
    print(f'input: 001 output: {expensive_seq(0, 0, 1)}')
    print(f'input: 022 output: {expensive_seq(0, 2, 2)}')
    print(f'input: 023 output: {expensive_seq(0, 2, 3)}')

    print('')
    print(f'input: 200 output: {expensive_seq(2, 0, 0)}')
    print(f'input: 210 output: {expensive_seq(2, 1, 0)}')
    print(f'input: 201 output: {expensive_seq(2, 0, 1)}')
    print(f'input: 211 output: {expensive_seq(2, 1, 1)}')

    print('')
    print(f'input: 300 output: {expensive_seq(3, 0, 0)}')
    print(f'input: 310 output: {expensive_seq(3, 1, 0)}')
    print(f'input: 301 output: {expensive_seq(3, 0, 1)}')
    print(f'input: 311 output: {expensive_seq(3, 1, 1)}')

    print('')
    print(f'input: 400 output: {expensive_seq(4, 0, 0)}')
    print(f'input: 410 output: {expensive_seq(4, 1, 0)}')
    print(f'input: 401 output: {expensive_seq(4, 0, 1)}')
    print(f'input: 411 output: {expensive_seq(4, 1, 1)}')

    print('')
    print(f'input: 500 output: {expensive_seq(5, 0, 0)}')
    print(f'input: 510 output: {expensive_seq(5, 1, 0)}')
    print(f'input: 501 output: {expensive_seq(5, 0, 1)}')
    print(f'input: 511 output: {expensive_seq(5, 1, 1)}')
    """
