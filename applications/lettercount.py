# Count the number of occurrences of a letter in a string
# "Hello there!"

d = {}

def letter_count(s):


	for c in s:

		if c.isspace():
			continue

		c = c.upper()

		if c not in d:
			#d[c] = 0
			d[c] = 1
		else:
			d[c] += 1

	return d

letter_count("Hello there!")

for key in d:
	print(key)

array = [key for key in d]

print(array)

