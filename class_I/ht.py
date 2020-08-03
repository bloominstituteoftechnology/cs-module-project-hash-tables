# Hash Tables

# What they solve
    # Standard Array Search

# Main hash table operations:
    # GET
    # PUT
    # DELETE

HASH_DATA_SIZE = 8

hash_data = [None] * HASH_DATA_SIZE

def hash_function(s):
    """Take in a string, return sequence of bytes"""

    # O(n) over the key length
    # O(1) over the HASH_DATA_SIZE
    
    bytes_list = s.encode()

    total = 0

    for b in bytes_list: # O(n) over the length of the key
        total += b
    
    return total

def get_index(s):
    hash_value = hash_function(s)

    return hash_value % HASH_DATA_SIZE

def put(k, v):
    """For a given key, store a value in the hash table"""
    index = get_index(k)
    hash_data[index] = v

def get(k):
    """For a given key, return its value from hash table"""
    index = get_index(k)

    return hash_data[index]



print(hash_data)
# index = get_index("Aaron")
# hash_data[index] = "Hello, world!"

put("Aaron", "Hello, world!")
# put("Goats", 3490)


print(hash_data)

print(get("Aaron"))
print(get("Goats"))

