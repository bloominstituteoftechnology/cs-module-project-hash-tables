# Hash table --> Dictionary(python) --> Object(Javascript)--->Hash Map(other languages)
hash_array = [None]*8
def hash_fn(str):
  encoded_string = str.encode()
  # print(encoded_string)
  sum=0
  for byte_char in encoded_string:
    sum += byte_char
  # print(sum)
  return sum

# store banana inside hash_array
hash_value = hash_fn("banana")
print(hash_value)
index = hash_value % len(hash_array)
hash_array[index] = ("banana","is yellow")
print(hash_array)


# Look up Banana in hash_array
hash_value = hash_fn("banana")
index = hash_value % len(hash_array)

print(hash_array[index])




