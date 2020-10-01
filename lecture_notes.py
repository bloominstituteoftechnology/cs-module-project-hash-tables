# collision
'''
What happens when you store values that have the same index?

btyecodes summing up to the same basically

You would have to overwrite it somehow

Use linked list, chain the values at the end of the linked list for each array spot

This can slow stuff down, you will have O(n), iterating through a list.

'''



# naive hash tabling

list_size = 8

my_list = [None] * list_size

def naive_hash(str, list_size):
    bytes_representation = "hello".encode()

    sum = 0
    for byte in bytes_representation:
        sum += byte

    return sum % list_size


# def swap(a, b):
#     for i in range(len(a)):
#         for j in range(len(b)):
#             a[i], b[j] = b[j], a[i]
#             if sum(a) == sum(b):
#                 return [b[j], a[i]]
#             a[i], b[j] = b[j], a[i]


def swap(a, b):
    a_sum = sum(a)
    b_sum = sum(b)
    b = set(b)
    for i in a:
        diff = ((b_sum - a_sum) // 2) + i
        if diff in b:
            return [i, diff]

print(swap([1], [2,3]))
