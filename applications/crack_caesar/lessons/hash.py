def my_hash(s):
    sb = s.encode()

    total = 0
    for b in sb:
        total += b


    return total%8 
    #the number 8 was a random number chosen to set its own limits

i = my_hash("derek")

hash_table = [None]*8
hash_table[i] = "8 months"

# hash derek
# retreive value at that hash

def get_length(e):
    curr_hash = my_hash(e)
    return hash_table[curr_hash]

length_derek = get_length("derek")

print("Derek has worked at Lambda for " + length_derek)

employees = {}

### In the end this is taking too long ###





