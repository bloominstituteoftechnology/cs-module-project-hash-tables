# my_arr = ['hi', "how", "are", "you","lorem","ipsum","set"]



for i in "AB".encode():
    print(i)
    
def UTF8_hash(str) :
    total =0
    utf_bytes = str.encode()  
    for b in utf_bytes:
        total += b
        
    return total


print(UTF8_hash('dam'))
print(UTF8_hash('mad'))

my_arr = [None] *20
ourHash= UTF8_hash('supercali')
idx = ourHash % len(my_arr)

my_arr[idx]= "Mary Poppins" 
print(my_arr)
val = my_arr[idx]
print(val)

## PUT
##1. hash the key
##2. mod with leng of array
##3. Go to index and put in the value.

##GET
##1. hash the key
##2. mod with len of arr
##3. Go to index and get out the value.

##Time Complexity

##collision
key1 = "add"
key2 = "dad"
##GET  
hash1 = UTF8_hash(key1)
idx1 = hash1 % len(my_arr)
my_arr[idx] = "howday"
##PUT1
hash2 = UTF8_hash(key2)
idx2 = hash2 % len(my_arr)
my_arr[idx2]= "whats up"

##PUT2
get_hash = UTF8_hash(key1)
idx3 = get_hash % len(my_arr)
print(my_arr)

##SHA-256
