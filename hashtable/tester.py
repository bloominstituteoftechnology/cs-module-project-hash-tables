from hashtable1 import HashTable


ht = HashTable(8)

ht.put("key-0", "val-0")
ht.put("key-1", "val-1")
ht.put("key-2", "val-2")

return_value = ht.get("key-0")
print(return_value)
return_value = ht.get("key-1")
print(return_value)
return_value = ht.get("key-2")
print(return_value)

ht.put("key-0", "new-val-0")
ht.put("key-1", "new-val-1")
ht.put("key-2", "new-val-2")

return_value = ht.get("key-0")
print(return_value)
return_value = ht.get("key-1")
print(return_value)
return_value = ht.get("key-2")
print(return_value)

print('load_factor = ', ht.get_load_factor())

ht.delete("key-2")
ht.delete("key-1")
ht.delete("key-0")

return_value = ht.get("key-0")
print(return_value)
return_value = ht.get("key-1")
print(return_value)
return_value = ht.get("key-2")
print(return_value)
