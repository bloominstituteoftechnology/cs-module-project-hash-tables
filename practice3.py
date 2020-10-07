class LinkedList:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next = None

class HashTable:
  def __init__(self, capacity):
    self.hash_array = [None] * capacity

  def hash_fn(self, str):
    encoded_str = str.encode()
    results = 0
    for byte_character in encoded_str:
      results += byte_character
    return results

  def hash_index(self,key):
    hash_value = self.hash_fn(key)
    index = hash_value % len(self.hash_array)
    print(index)
    return index


  def put(self,key,value):
    index = self.hash_index(key)
    self.hash_array[index] = (key,value)
    print(self.hash_array)

  def get(self,key):
    index = self.hash_index(key)
    return self.hash_array[index]

ht = HashTable(8)
ht.put('apples', 'I like to eat apples sometimes')
ht.put('cakes', 'too much sugar in it')
ht.put('cloths', 'spelled wrong there')
ht.get('apples')