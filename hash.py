my_arr = ["hello", "world", "how", "are", "you"]

#0(1) with an array?
#append, pop, push
#look up from index

my_arr[4]

#hashing or has function: that will give is the indest of the word we are looking for
## "you" --> 4

#to make a hash of something
#Hash takes a string and returns a number

def my_hash(s):
    return len(s)
my_hash("you") # returns 3. This is a bad hash because ALL three letter words return a 3

my_alphabet = {'a':0, 'b':1}
def my_hash2(s):
    total = 0
    for char in s:
        total += my_alphabet[char]
    return total #this is a slightly better solution, but here you are creating your own ASCII

#ASCII => American Standard Code for Information Exchange --> assigns letters to numbers
#uses ord()

#UTF-8 => Unicode Transformation Format --> Replaced ASCII
#uses encode()
#how to make the output more unique??
# could use a random number? How to make sure we get the same index every time?


def my_hash3(s):
    s_utf8 = s.encode()
    
    for c in s_utf8:
        print(c)


#how do we use THIS FUNCTION with the array?
def my_hash4(s):
    s_utf8 = s.encode()
    
    total = 0
    for c in s_utf8:
        total += c
    return total

print(my_hash4("hello"))

hello_index = my_hash4("hello") #returns 532

my_arr = [None] * 5

#this takes the large number and trims it down to size to give us the index
hello_index = hello_index % len(my_arr)

my_arr[hello_index] = "hello"

print(my_arr)
#my_hash4 is not good because TOO MANY COLLISIONS

#hash table, dictionary, object, hash map: array paired up with a hash function

#inserted into a hash map
key = "key"
key_index = my_hash4(key) % len(my_arr)
my_arr[key_index] = "value"

print(my_arr)


#access the value
key_index = my_hash4(key) % len(my_arr)
print(my_arr[key_index])

#steps to put into hash
# have a hash function, have an array and key-value to put into the array

## 1. hash the word - get some number back from the hash function
## 2. modulo the returned number with array length to find the index
## 3. use index to insert word

#steps to get the value
## 1. hash the key/word, get number back from hash function
## 2. modulo the returned number with array length to find the index
## 3. look up value at that index, return it

#uses of hash tables
## dynamic programming
## searching

#hash function ideal speeds
## in a hash table: fast! we want to look up stuff FAST
## to hash passwords and store hashes instead of plaintext passwords: relatively SLOW

# output of hash functions: hash or digest

#hashlib.sha256('hello'.encode()) => another hashing function

# a good hash function like SHA256 gives a totally unique output
# can use as id aka fingerprint of a document (document == big string)

# can you reverse the output of a hash function? Can you go from 532 => "hello"
# a good hash function is NON - REVERSIBLE