data = [0] * 128

def my_hash(s):
    """ Beej's naive hasing function """
    sb = s.encode()
    total = 0

    for b in sb:
        total += b
        total &= 0xffffffff  #32-bit hashing function
        #total &= 0xffffffffffffffff  #64-bit hashing function

    return total

def get_index(s):
    h = my_hash(s)
    i = h % len(data)
    return i

def put(k,v):
    # get the index into 'data' to store 'v'
    i = get_index(k)
    data[i] = v
    
def get(k):
    i = get_index(k)
    return data[i]

put('beej', 3490)
put('goats', 999)

print(data)
print(get('beej'))
#print(my_hash("beej"))
#print(my_hash("goats"))

#print(get_index('beej'))
#print(get_index('goats'))

