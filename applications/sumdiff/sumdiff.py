"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
	return x * 4 + 6

# Your code here
cache = {}
for w in q:
	for x in q:
		for y in q:
			for z in q:
				if w not in cache:
					l = f(w)
					cache[w] = l
				else:
					l = cache[w]

				if x not in cache:
					l2 = f(x)
					cache[x] = l2
				else:
					l2 = cache[x]

				if y not in cache:
					r = f(y)
					cache[y] = r
				else:
					r = cache[y]

				if z not in cache:
					r2 = f(z)
					cache[z] = r2
				else:
					r2 = cache[z]

				if l + l2 == r - r2:
					print('f({0}) + f({1}) = f({2}) - f({3})\t\t{4} + {5} = {6} - {7}'.format(w, x, y, z, l, l2, r, r2))
