import math
sqrt_table = {}

def compute_inverse_sqaure(n):
    #fairly expensive
    result = 1/math.sqrt(n)
    #cache the result right her
    return  result

def build_look_table():

    for index in range(1, 1001):
        sqrt_table[index] = compute_inverse_sqaure(index)

def faster_compute_square(n):
    return sqrt_table[n]

build_look_table()
print(sqrt_table)