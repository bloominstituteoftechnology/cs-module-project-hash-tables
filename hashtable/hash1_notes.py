data = [None] * 16  # Size should be a power of 2​

def my_hash(s):
	"""Beej's naive hashing function"""​

	sb = s.encode()​

	total = 0​

	for b in sb:
		total += b
		total &= 0xffffffff  # add this for a 32-bit hashing function
		#total &= 0xffffffffffffffff  # add this for a 64-bit hashing function​

	return total​

def get_index(s):
	h = my_hash(s)​

	i = h % len(data)​

	return i​

def put(k, v):
	# Get the index into "data" to store "v"
	i = get_index(k)​

	# Store v there
	data[i] = v​

def get(k):
	i = get_index(k)​

	return data[i]​

def delete(k):
	i = get_index(k)​

	data[i] = None
​

if __name__ == "__main__":​

	put("beej", 3490)
	put("goats", 999)
	put("beej", "hello")​

	print(data)​

	print(get("beej"))​

	#print(my_hash("beej"))
	#print(my_hash("goats"))​

	#print(get_index("beej"))
	#print(get_index("goats"))
	#print(get_index("foo"))
	#print(get_index("bar"))
	#print(get_index("baz"))
	#print(get_index("qux"))