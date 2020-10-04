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
def insert_to_hash_table(key,value):
  hash_value = hash_fn(key)
  index = hash_value % len(hash_array)
  print(index)
  hash_array[index] = (key,value)



# Look up Banana in hash_array
def get_from_hash_table(key):
  hash_value = hash_fn(key)
  index = hash_value % len(hash_array)
  print(hash_array[index])


insert_to_hash_table('mango', 'mangoes are available in india')
insert_to_hash_table('apple', 'I love apples')
# print(hash_array)
get_from_hash_table('mango')



