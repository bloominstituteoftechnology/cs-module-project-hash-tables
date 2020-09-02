

my_arr = ['hi', 'world', 'how', 'are', 'you', 'lorem', 'ipsum', 'set']

# search for an element in this array

##O(n) -- linear search
def find_element(arr, el):
    for thing in arr:
        if thing == el:
            return True

        return False

## or if we sorted, binary search
## O(log n)

## which big 0 complexities are fasted than log n?
## constant time! O(1)
### if we increase the input, we still take number of steps to find what we're looking for

def magic_function_find_index(arr, el):
    return el_index


id = magic_funtion_find_index(my_arr, "set") ## 7
my_arr[idx] # ta-da

##hash tables == array + hashing function


## write a function that will take a string and return a number
def len_hash(str):
    return len(str)
## a lot of collisions
print (len("sad") == len("was"))
len("ball") == len("hats")

#fast
#deterministic

## we could map ltter to numbers, but thats been done
# add up the ASCII or unicode
## UTF-8 is ASCII on steroids
# use .encode()

## a: 1
## b: 2

def UTF8_hash(str):
    for letter in str:
        val = ord(letter)
        total += val

    return total

# or

total = 0
def UTF8_hash(str):
    utf_bytes = str.encode()
        for byte in utf_bytes:
            total += byte
    

    return total

print(UTF8_hash('sad'))
print(UTF8_hash('was'))

# but we will still have collisions 
UTF8_hash('dad')
UTF8_hash('add')
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

my_arr2 = [None] * 20

our_hash = utf8_hash('supercalifragilisticexpialidocious') ## 3643
idx = our_hash % len(my_arr2)

my_arr2[idx] = 'Mary Poppins'

print(my_arr2)


# 'get'
our_hash = UTF8_hash('supercalifragilisticexpialidocious')
idx = our_hash % len(my_arr2)

#print(my_arr2[3])
val = my_arr2[idx]
print(val)

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
key1 ='dad'
key2 = 'add'

hash_1 = UTF8_hash(key1)
idx1 = hash1 % len(my_arr2)
my_arr2[idx1] = 'howdy'

hash2 = UTF8_hash(key2)
idx2 = hash2 % len(my_arr2)
my_arr2[idx2] = 'whats up yall'

###get
get_hash = UTF8_hash(key1)
idx3 = get_hash % len(my_arr2)

print(my_arr2[idx3])

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


my_string = " Dear everybody, how are? I write to you ..."