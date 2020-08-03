# Build a data structure that will let us search for info really fast
## Use array, and a function!

## 'get' and search work out to be the same thing here

## Given a list of a trillion elements, find a string O(1)
## Hack: turn a string into an index
## That way, we can jump there immediately

# we are building a dictionary, {}, from scratch

## To turn a string into an index, we built a hash function
### The hash function takes a string, turns it into a number, scrambles the number, and gives it back to us

## We make sure the number we get back works with our list --> index
## Use our new index!

# Example
# Let's use key-value pair: "hello", "hello world"
## Step 1: hash "hello"
## Step 2: make hash work with list - aka turn into index
## Step 3: put value at that index!

# Let's look it up!
## Step 1: hash "hello"
## Step 2: make result work with list - turn into index
## Step 3: go look at that index

# Note: need to know the string we used!

# new_list[0] = "hello world"
# hello -> 0
# hash(world) --> 4


my_list = ["hi", "how", "are", "you", "hello", "world"]

# time complexity of search?
# Why?
# my_list.contains() --> for loop

# What if we had a function to tell us the index of "hello" in O(1)?
## Time complexity of search? O(1)
## Why?

# def my_func(string_to_search_for):
    # return index_of_string

# my_index = my_func("hello") # 4
# my_list[my_index] # return "hello"

# hashing function, hashes and returns a hash
## Deterministic


# Most take a string
# return an integer
# operate on the bytes of the string
## byte is basically an integer 0-255

# ASCII maps letters to numbers: Latin alphabet, Arabic numerals

# Unicode Transformation Format-8

# Next, transform the bytes into a random-looking number

# We want different strings to come back with different numbers
## as spread out as possible over our array


def my_hash(s):
    string_bytes = s.encode()
    total = 0
    for b in string_bytes:
        total += b

    return total

print(my_hash("hello"))
print(my_hash("world"))

# what would happen if we got back the same number (index!) for different words?
## Example "add" and "dad"
## Collision
## To be continued!


# How to use the number we return (the "hash") to get an index a list?


# my_list[hello_hash]

new_list = [None] * 8




# Put "howdy world" in at index "world"
## Step 1: put "world" through our hashing function
hello_hash = my_hash("hello")
## Step 2: modulo that result with the length of our list
hello_index = hello_hash % len(new_list)
## Step 3: use that modulo - index - with our list
new_list[hello_index] = "hello world"


# PUT again
hashed_world = my_hash("world")

world_index = hashed_world % len(new_list)

new_list[world_index] = "howdy world"

print(new_list)

# key-value store: dictionary, JS: object, Swift also dictionaries

# Search for "hello world" or "howdy world", given "world" or "hello"
## Step 1: get the hash
hashed_string = my_hash("hello")
## Step 2: take the hash modulo length of our array
our_index = hashed_string % len(new_list)
## Step 3: use that index to access the value stored there
print(new_list[our_index])


# Time complexity of get and put?
## Depends whether you measure by the string we put in, or by the list we use as a table/storage
## String/key: O(n) aka linear, because we iterate over the string
## List: O(1), constant

## Hash tables: think of get and put as O(1)

## you made a hash out of that

# Hash table, hash map, map, dictionary, object, set