# Reverse numbers (123 -> 321) quickly​

class NumReverser:
    def __init__(self):
	self.cache = {} ​

	# Build a lookup table
	for i in range(1000):
	    self.cache[i] = self.num_reverse(i)​

    def num_reverse(self, n):
	if n in self.cache:
	    print("Cache hit")
	    return self.cache[n]​

	print("Cache miss")
	n2 = list(str(n))
	n2.reverse()
	n2 = ''.join(n2)​

	self.cache[n] = int(n2)​

	return self.cache[n]​

nr = NumReverser()
print(nr.num_reverse(123))
print(nr.num_reverse(1234))