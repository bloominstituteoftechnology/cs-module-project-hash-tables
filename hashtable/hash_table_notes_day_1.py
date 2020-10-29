
# lorem ipsum
my_arr = ["Lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit" ]

# search for an element, for example consectetur

# O(n)
# for word in my_arr:
#     if word == 'consectetur':
#         return True

# if 'elit' in my_arr:
#     return True 

# O(log n)
# sort array, then run binary search on it

# what if we could find the index of the element in O(1) time?
# then we could take 1 more step to access the element: my_arr[5]

# we would have O(1) search

# we would like a function that returns the index

# Hash function or hashing function

## do you have to track where you've put things in the underlying array?


# Hash functions
# Write a function that takes a string and turns it into a number

# hash the string with a hashing function....and you get back a hash

my_arr = [None] * 8

# it's fast
# deterministic
# can't get the input from the output

def len_hash(s):
    return len(s) # for this example, we will use the length of the word as the index

# Use the hashing function to put the word 'hello' into the array
hello_number = len_hash('hello') # use hashing function to get an index
my_arr[hello_number] = 'hello'


## some time passes...
hello_number = len_hash('hello') # use hashing function to find the index
my_arr[hello_number]  # pull out the word we want

# what about words of the same length?
world_number = len_hash('world')
my_arr[world_number] = 'world'


world_number = len_hash('world')
my_arr[world_number]

# what about long words?
long_word = 'supercalifragilisticexpialidocious'
long_word_hash = len_hash(long_word)

long_word_idx = long_word_hash % len(my_arr)

my_arr[long_word_idx] = long_word

## how to fix this?
### dynamic array?

### use modulo, aka 'mod the number'


# the problem with arrays: search is slow
# How to get faster?
# To reach O(1), make a magic function to return the index of the target word in O(1) time
# made simple hash function
# make the hash function and array play nice together

# Let's improve our hash function, by making it more unique

## add up the letters
### assign a number to every letter
### ASCII has already done this

def add_hash(s):
    total = 0
    for letter in s:
        total += ord(letter)
    return total

### won't work for anagrams!
#### dad vs add

# UTF-8, ASCII on steroids
# encode
def utf8_hash(s):
    total = 0
    string_bytes = s.encode()

    for b in string_bytes:
        total += b
    return total

# we can do math on the bytes of the string!

my_arr = [None] * 10000

def put(key, value):
    # turn the key into an index
    hashed_string = utf8_hash(key)
    idx = hashed_string % len(my_arr)

    # put the value at that index in our array
    my_arr[idx] = value

put('hello', 'hello world')

# what is the time complexity here?
## if you measure by the length of the key, O(n)
## if you measure by the number of slots / length of array, then it's O(1)

def get(s):
    hashed_string = utf8_hash(s) # turn string into number

    idx = hashed_string % len(my_arr) # turn number into index

    value = my_arr[idx] # go and access element at that index

    return value

get('hello') ## get the key


# Delete: find the value, then set to None

# Put
## 1. Hash our string/key, get out a number
## 2. Take this number and modulo it by the length of the array
## 3. This new number can be used as an index, so put the value at that index in our array

# Get
## 1. Hash our string/key, string --> number
## 2. Mod this number by length of array
## 3. Use this modded number / index to get the value there




## Common use-cases?
### hashing functions: encryption
### Fast O(1) lookup of values using a key to find it

## Easy to think about time complexity for arrays vs objects/dictionaries

# if x in my_data_structure: ## O(n) for an array, runs get() --> O(1) for a hash table

# look up user profile from username, 1billion users

    
    
    
 # Couldn't we end up with the wrong modulo if we've increased the size of the array between put and get?
 # Increasing the size of the array which we're using with our hash table?
 # Solving collisions??
 ### TO BE CONTINUED....

"""Notes with Beej

what they solve - look at each item in an index, first, second, third - Linear searching - that's O(n) - Standard array search
if we double the list - twice as long to search, triple = 3 times as long

