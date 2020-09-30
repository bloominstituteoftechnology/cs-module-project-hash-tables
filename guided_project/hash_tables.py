my_arr = ["hi", "world", "hello", "are", "you", "lorem", "ipsum", "set"]

# Search for an element in this arr


## O(n) -- linear search
def find_element(arr, el):
    for thing in arr:
        if thing == el:
            return True

    return False

## Or if we sorted, binary search!
## O(log n)

# Which Big O complexity are faster than log n?
## Constant time! O(1)
### if we increase the input, we still take the number of steps to find what we're looking for

def magic_fun_finder_index(arr, el):
    return el_index

# idx = magic_fun_finder_index(my_arr, "set") ## 7
# my_arr[idx] 

## hash tables == arrays + hashing function

## Write a function that will take a string adn return a number
def len_hash(str):
    return len(str)
len("sad") == len("sad")
len("ball") == len("hats")

# Fast
# Deterministic

# add up the ASCII or unicode
## UTF-8
# use .encode()

## a: 1
## b: 2

## We could map letters to numbers, but that's already been done!
# ASCII was the first mapping of letters to numbers
## UTF-8 is ASCII on steroids, designed to work with ASCII but be universal
# use .encode()


def UTF8_hash(str):
    uft8_bytes = str.encode()
    total = 0
    for byte in uft8_bytes:
        total += byte 

    return total

print(UTF8_hash('sad'))
print(UTF8_hash('was'))

# but we will still have collisions
UTF8_hash('dad')
UTF8_hash('add')

print(UTF8_hash('supercalifragilisticexpialidocious'))

# A hash function: takes string, gives back number
## operate on the bytes that make up the string
## Deterministic

## To improve our hash functions, make output more unique
## SHA256

## Hash function + array!!
## hash function gives us back some big number
### how to map the output of our has fuction to an index in an array?

my_arr2 = [None] * 20

our_hash = UTF8_hash('supercalifragilisticexpialidocious') #3364
idx = our_hash % 20

my_arr2[idx] = 'Mary Poppins'

print(my_arr2)

val = my_arr2[idx]
print(val)

## Key Value store
# 'supercalifragilisticexpialidocious' is the key
# 'Mary Poppins' is the value

# Hash table in programming language
## Python: dictionary
## JS: object
## Hash map
## Map

## Pseudocode for put
### 1. Hash the key
### 2. Take the hash and mod it with len of array
### 3. Go to index and put in value

## Pseudocode for get
### 1. Hash the key
### 2. Take the has and mod it with len of array
### 3. Go to index and get out the value

## Time complexity?
### Same for get and put
### Linear in length of string/key
### Constant time in length of array O(1)


