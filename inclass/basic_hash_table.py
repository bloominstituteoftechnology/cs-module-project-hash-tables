class HashTableEntry:
    """
    Linked List hash table key/value pair.
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f'HashTableEntry({repr(self.key)},{repr(self.value)})'

data = [None] * 8

def my_hashing_function(s):
    string_bytes = s.encode()

    total = 0

    for b in string_bytes:
        total += b

    return total

def get_slot(s):
    hash_val = my_hashing_function(s)
    return hash_val % len(data)

def get(key):
    slot = get_slot(key)
    hash_entry = data[slot]

    if hash_entry is not None:
        return hash_entry.value

    return None

def put(key, value):
    slot = get_slot(key)
    data[slot] = HashTableEntry(key, value)

def delete(key):
    put(key, None)

#print(get_slot("☠ arr"))
#print(get_slot("beej"))
#print(get_slot("foo"))
#print(get_slot("bar"))

put("beej", 3490)
put("foo", 999)

#print(data)

print(get("beej"))
#print(get("foo"))
print(get("bar"))
