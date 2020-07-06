def my_hash(s):
    sb = s.encode()

    sum = 0
    for b in sb:
        sum += b

    return sum % 8


i = my_hash('steve')


hash_table = [None]*8

hash_table[i] = '8 months'


def get_length_of_time_at_lambda(e):
    curr_hash = my_hash(e)
    return hash_table[curr_hash]


length_steve = get_length_of_time_at_lambda('steve')

print('Steve has been attending Lambda school for ' + length_steve)


# first we hash value -> constant
# index into the list based on the hash -> constant
