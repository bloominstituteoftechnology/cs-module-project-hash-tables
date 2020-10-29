# Takes in inputStr and returns a number

def my_hash(inputStr):
    # 'foo' ~~> [x, y, y] - Byte representations for each byte in UTF-8.
    sb = inputStr.encode()  # the UTF-8 bytes for the string
    total = 0
    for b in sb:
        total += b
    return total


print(my_hash("foo"))

my_table = [None] * 8
# store key "foo" w/ value "bar"

hash_index = my_hash('foo') % len(my_table)
my_table[hash_index] = 'bar'
# print(my_table)

# get value w/ key "foo"

another_hash_index = my_hash('foo') % len(my_table)
print(my_table[another_hash_index])

yet_another_hash_index = my_hash('foo') % len(my_table)
my_table[yet_another_hash_index] = None

