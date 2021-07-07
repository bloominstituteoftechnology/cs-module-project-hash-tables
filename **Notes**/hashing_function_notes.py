
# Making a linked list vs. just iterating down: how do you want to implement your hashtable?
## Option 1: create a LL class, or import it, and HashTable class calls the LL methods
## Option 2: inside your HashTable class, make your put/get/delete iterate down the nodes

# Resizing
## What does the OS do if your array gets filled up?
### Find a new spot in memory - double the size of the old one
### Copy old array into new one
### Return the address in memory of your new array


## if hash table is 70% full, how long does the next put take?
### O(n) where n is number of items in hash table

## put takes constant time, if we amortize out the cost of resizing


## compare to dropping the small terms in big O?
### O(n^2)

def quadratic(array):
    for x in array: # million
        print(x)
    
    for x in array: # million * million
        for y in array:
            print(x, y)
        

# Hashing Functions Uses
## Hash a key and work with a hash table
## Use with a database
## Encryption
### Hashing a password
### authentication
##### We want a slow hash function, to prevent brute force

def my_password_hash_function():
    pass


## Encryption - cryptography
### the output often called digest, the hash
print("The quick brown fox jumped over the lazy dog \n and then went to sleep \n shall i compare thee?")
### 0x1ad4fe598373cb
### MD5, SHA256

### Tweet the hash
#### Proves the document existed at some time
#### Produce a work of art
#### ....or code
#### Scientific discovery, or patent


# What if we used SHA256, which never produces collisions? Does our hash table need to handle collisions?
## Still have collisions, because we modulo the output with our hash table length