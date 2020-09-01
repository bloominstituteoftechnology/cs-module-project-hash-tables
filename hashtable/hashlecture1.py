"""
Hash Tables
-----------

What problem are we solving with this data structure?

Quick O(1) searches!


[ "Lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit" ]
   0        1        2        3      4       5              6             7

Hashing function:

f("dolor") -> 2
f("dolor") -> 2
f("dolor") -> 2
f("dolor") -> 2
f("consectetur") -> 5
f("beej") -> 5


Hash table: key-value store with a particular structure, and O(1) time complexity
Python dict: basically is a hash table
General "Dictionary" equivalent to a "key-value store"
Key-value store is a data structure that returns a value for a given key

"""
table = [None] * 8192

def hashf(s):
	"""Super-naive hashing function--do not use."""

	b = s.encode()  # Get the bytes of the string

	total = 0
	
	for i in b:  # O(n) over the size of the key, O(1) over the size of the hash table
		total += i

	return total

def get_index(key):
	index_value = hashf(key)
	index_value %= len(table)

	return index_value

def put(key, value):   # O(1) over the size of the hash table
	# Which slot (aka index) in the table is the value going?
	index = get_index(key)

	# Store the value at that slot
	table[index] = value

def get(key):
	index = get_index(key)

	return table[index]

def delete(key):
	index = get_index(key)

	table[index] = None

#print(table)

put("Beej", 3490)
#put("eBej", "foo")  # Collision! This would be bad. We'll fix tomorrow.
print(get("Beej"))  # 3490

delete("Beej")
print(get("Beej"))  # None

#print(table)
