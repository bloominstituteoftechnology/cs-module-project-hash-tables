def my_hash(s):
    sb = s.encode()
    total = 0
    for c in sb:
        total += c
    return total

my_array = [None] * 8
hash_index = my_hash("hello world") % 8
# print(my_hash("hello world")) # 1116

print(f'my_arrray {my_array}')
print(f'hash index {hash_index}')


