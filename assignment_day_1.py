

#my_arr = ['hi', 'world', 'how', 'are', 'you', 'lorem', 'ipsum', 'set']

# search for an element in this array

##O(n) -- linear search
#def find_element(arr, el):
 #   for thing in arr:
  #      if thing == el:
   #         return True

    #    return False

## or if we sorted, binary search
## O(log n)

## which big 0 complexities are fasted than log n?
## constant time! O(1)
### if we increase the input, we still take number of steps to find what we're looking for

#def magic_function_find_index(arr, el):
 #   return el_index


# id = magic_funtion_find_index(my_arr, "set") ## 7
# my_arr[idx] # ta-da

##hash tables == array + hashing function


## write a function that will take a string and return a number
#def len_hash(str):
 #   return len(str)
## a lot of collisions
#print (len("sad") == len("was"))
#len("ball") == len("hats")

#fast
#deterministic

## we could map ltter to numbers, but thats been done
# add up the ASCII or unicode
## UTF-8 is ASCII on steroids
# use .encode()

## a: 1
## b: 2

#def UTF8_hash(str):
    #for letter in str:
        #val = ord(letter)
        #total += val

    #return total

# or

#total = 0
#def UTF8_hash(str):
    #utf_bytes = str.encode()
    #for byte in utf_bytes:
            #total += byte
    

    #return total

#print(UTF8_hash('sad'))
#print(UTF8_hash('was'))

# but we will still have collisions 
#UTF8_hash('dad')
#UTF8_hash('add')
# a hash function: takes string, gives back number
## opersate on the bytes that make up the string
## derterministic 

## to improve our hash functions , make output more unique!

## SHA256

## Hash function + array!!
## hash function gives up back some big number
### how to map the output of our hash function to an index in an array?



## how to turn result of hash function into usable index?
###modulo the hash with len(my_arr)

## modulo demonstration
## modulo returns from 0 to len(list)- 1
#1 % 20 --> 1
#15 % 20 --> 15
#20 % 20 --> 0
#21 % 20 --> 1
#22 % 20 --> 2
#39 % 20 --> 19
#40 % 20 --> 0

#"take it modulo", "modulo it", "mod it"
# "modding"

# use mdulo with hash (output of hashing function) to get usable index

## we can now combine hash function and array

#my_arr2 = [None] * 20

#our_hash = UTF8_hash('supercalifragilisticexpialidocious') ## 3643
#idx = our_hash % len(my_arr2)

#my_arr2[idx] = 'Mary Poppins'

#print(my_arr2)


# 'get'
#our_hash = UTF8_hash('supercalifragilisticexpialidocious')
#idx = our_hash % len(my_arr2)

#print(my_arr2[3])
#val = my_arr2[idx]
#print(val)

## key value pair
# 'supercalifragilisticexpialidocious' is the key
# "Mary Poppins" is the value

# hash table in programming languages?
## python dictionary
## JS: object
## hash map
## map


## psudo code for put
### 1. hash the key
### 2. take the hash and mod it with len of array
### 3. go to index and put in value

#psudo got for get
### 1. hash the key
### 2. take the hash and mod it with len of array
### 3. go to index and get the value

## time complexity?
### the same for get and put
#### Linear in length of string /key
#### constant time in leinght of array < --- this is what we pay attention to
# O(1)

## collision
#key1 ='dad'
#key2 = 'add'

#hash_1 = UTF8_hash(key1)
#idx1 = hash1 % len(my_arr2)
##my_arr2[idx1] = 'howdy'

#hash2 = UTF8_hash(key2)
#idx2 = hash2 % len(my_arr2)
#my_arr2[idx2] = 'whats up yall'

###get
#get_hash = UTF8_hash(key1)
#idx3 = get_hash % len(my_arr2)

#print(my_arr2[idx3])

## even when we use our hash function with modulo we get collisions
### to be solved later


## we wrote our own hash function what about python hash
## many different hash functions! can also use hash()


### when used with hash tables hashing function should be FAST
### why? we want O(1) and a lot of look ups


## other uses of hash functions
### passwords!! EX BYCRPTJS
### encryption/decryption 


## password --> hashing function --> hashed_password

## password --> hashingfunction --> hash === hashed_password ??


### here hash function should be slow
#### 1234mypassword

### SHA-256 has never had a collision
#### can use the output as a fingerprint for your string


#my_string = " Dear everybody, how are? I write to you ..."

country_code = {'25': 'USA', '20': 'India', '10': 'Nepal'}
print (country_code['10'])
print (country_code['20'])

country_code = [('25', 'USA'), ('20', 'India'), ('10', 'Nepal')]
def insert(item_list, key, value):
    item_list.append((key, value))

def search(item_list, key):
    for item in item_list:
        if item[0] == key:
            return item[1]

print (search(country_code, '20'))




hash_table = [None] * 10
print (hash_table)

def hashing_fun(key):
    return key % len(hash_table)

print (hashing_fun(10))
print (hashing_fun(20))
print (hashing_fun(25))

def insert(hash_table, key, value):
    hash_key = hashing_fun(key)
    hash_table[hash_key] = value

insert(hash_table, 10, 'Nepal')
print (hash_table)

insert(hash_table, 25, 'USA')
print (hash_table)

### Collision

insert(hash_table, 20, 'India')
print (hash_table)

### the result of hashing_func for keys 10 and 20 is the same 


### Collision Resolution 
### There are generally two ways to resolve a collision: 1. Linear Probing 2. Chaining

## Linear Probing


## Chaining

hash_table =[[] for _ in range(10)]
print (hash_table)

def hashing_func(key):
    return key % len(hash_table)

print (hashing_func(10))
print (hashing_func(20))
print (hashing_func(25))

def insert(hash_table, key, value):
    hash_key = hashing_func(key)
    hash_table[hash_key].append(value)

insert(hash_table, 10, 'Nepal')
print (hash_table)

insert(hash_table, 25, 'USA')
print (hash_table)

insert(hash_table, 20, 'India')

## Standard implementation

hash_key = hash('xyz')
print(hash_key)

hash_key = hash('10')
print(hash_key)

hash_key = hash(10)
print(hash_key)

hash_key = hash('20')
print(hash_key)

hash_key = hash(10)
print(hash_key)

hash_key = hash('25')
print(hash_key)

hash_key = hash(25)
print(hash_key)

hash_key = hash('10') % len(hash_table)
print(hash_key)

hash_key = hash('20') % len(hash_table)
print(hash_key)

hash_key = hash('25') % len(hash_table)
print(hash_key)

hash_key = hash(10) % len(hash_table)
print(hash_key)

hash_key = hash(20) % len(hash_table)
print(hash_key)

hash_key = hash(25) % len(hash_table)
print(hash_key)


#empty hash table
hash_table = [[] for _ in range(10)]
print(hash_table)

## insert data into table
def insert(hash_table, key, value):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True
            break
    if key_exists:
        bucket[i] = ((key, value))
    else:
        bucket.append((key, value))

insert(hash_table, 10, 'Nepal')
insert(hash_table, 25, 'USA')
insert(hash_table, 20, 'India')
print(hash_table)

#search data from hash table
def search(hash_table, key):
    hash_key = hash(key) % len(hash_table)
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return v

print(search(hash_table, 10))
print(search(hash_table, 20))
print(search(hash_table, 30))


## Delete data from Hash Table

def delete(hash_table, key):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]
    for i, (k, v) in enumerate(bucket):
        if key == k:
            del bucket[i]
            print('Key {} deleted'.format(key))
        else:
            print('key {} not found'.format(key))

delete(hash_table, 10)
print(hash_table)