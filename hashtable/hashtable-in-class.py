class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        
        self.capacity = max(capacity, MIN_CAPACITY)
        self.storage = [None] * self.capacity

        self.load = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.storage)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here

# hashing functions used in:
# git
# cryptocurrencies
# hash tables
# store passwords

# choose between hashing functions
## some are fast, some are slow

# "Can a hash be reversed?"
# "How/Why not?"

## What's reversing a hash mean?
## take a hash number and try to get back to the string it was made from

## p@$$w0rd
## 0x23283287ad878f983efc

# deterministic
# irreversible

# an attacker can't reverse, but could try hashing common passwords

## for a hash table, you want a fast function --> O(1)
## for passwords, you want a slow function




# Different strategies to handle collisions?
## chaining: array of linked lists, with one LL per index, each node.next points to the second element
## Array of arrays, with one array per index, just append
## Disallow collisions?
## Open addressing. Linear probing, quadratic probing. [None, 'hello', 'world', None]





    def fnv1(self, key):
        """
        set hash to 0?
        maintain a total?

        - start hash at some large number(FNV_offset_basis)
        - the hashed variable maintains our total

        some_big_prime * some_other_big_prime = some_mysterious_number

        
        Comp Arch - bitwise operations, including XOR

        0101010101010
     ^  1101101011001
        -------------
        1000111110011


        """
        FNV_offset_basis = 14695981039346656037 
        FNV_prime = 1099511628211
        hashed = FNV_offset_basis

        bytes_to_hash = key.encode()

        for byte in bytes_to_hash:
            hashed = hashed * FNV_prime

            hashed = hashed ^ byte

        return hashed

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.

        unsigned long
        hash(unsigned char *str)
        {
            unsigned long hash = 5381;
            int c;

            while (c = *str++)
                hash = ((hash << 5) + hash) + c; /* hash * 33 + c */

            return hash;
        }
        Left bitshifting
        Left shift
                   |
   0101010101000000
                   |
       
       Why 5381 and * 33? because they work!

       What's "work" - what makes these good?
       - irreversible
       - nice distribution, spreads them out over the array --> minimizes collisions
        
        """
        hashed = 5381

        bytes_to_hash = key.encode()

        for byte in bytes_to_hash:
            hashed = ((hashed << 5) + byte)
            # hashed = ((hashed * 33) + byte)

        return hashed


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        self.put(key, None)
        -- will break our count!!

        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # hash the key - self.hash_index will modulo it
        idx = self.hash_index(key)

        # check for a collision
        if self.storage[idx] != None:
            print('warning! collision!!!')

        # insert the value at that location
        self.storage[idx] = value

        self.load += 1


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.

        """
        # hash the key to find index
        idx = self.hash_index(key)

        if self.storage[idx] == None:
            print('Warning! no key!!!')

        else:
            self.storage[idx] = None

            self.load -= 1


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")