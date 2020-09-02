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