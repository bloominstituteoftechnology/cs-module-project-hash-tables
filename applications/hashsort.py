d = {
	"foo": 12,
	"bar": 17,
	"qux": 2,
	#34: 3,
	"^%#": 99
}

i = list(d.items())

i.sort()   # Sort by key, then value

# If keys are different types, force them to be the same type
# Beej doesn't yet know why this is sorting out of order, but must find out!
#i.sort(key=lambda e: str(e))

#print(i)


"""
def comp(e):
	return e[1]

i.sort(key=comp)
"""
i.sort(key=lambda e: e[1])

print(i)


