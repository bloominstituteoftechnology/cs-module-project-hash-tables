from linked_list import LinkedList, HashTableEntry


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.dfs
    """

    def __init__(self, capacity=8):
        self.buckets = [None] * capacity
        self.capacity = capacity
        self.used = 0
        self.load = self.get_load_factor()

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.buckets)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        load = self.used/self.capacity
        return load

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        - start hash at some large number(fnv offset_basis)
        - the hash variable maintains our total.
        - xor (looking at number in binary form)
        looks at every pair of bits and treats 1 as true and 0 as false. 
        """
        pass
        # FNV_prime = 1099511628211
        # offset_basis = 14695981039346656037

        # #FNV-1a Hash Function
        # hash = offset_basis
        #bytes_t0_hash = key.encode()
        # what is seed here?
        # for bytes in bytes_to_hash:
        #     hash = hash * FNV_prime
        #     hash = hash ^ byte
        # return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        bytes_to_hash = key.encode()
        for byte in bytes_to_hash:
            hash = (hash * 33) + byte
        return hash & 0xFFFFFFFF

    def simp_hash_fn(self, key, value):
        # key that gets hashed
        byte = key.encode()
        print('simp hash func', byte)
        total = 0

        for char in byte:
            # print(char)
            total += char
            total &= 0xffffffff
            # print("total 32 bit", total)
        print(total % self.capacity)
        return total % self.capacity  # 8

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        if self.buckets[index] == None:
            self.buckets[index] = LinkedList()
            self.buckets[index].add_to_head(key, value)

        elif self.buckets[index].find(key):
            self.buckets[index].delete(key)
            self.buckets[index].add_to_head(key, value)
        else:
            self.buckets[index].add_to_head(key, value)
        self.used += 1
        # index = self.hash_index(key)
        # if self.buckets[index] != None:
        #     print("Something already exists at this index.")
        # self.buckets[index] = value

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.buckets[index] == None:
            return None
        else:
            self.used -= 1
            return self.buckets[index].delete(key)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.buckets[index]:
            if self.buckets[index].find(key):
                answer = self.buckets[index].find(key)
                return answer
            else:
                return None

    def resize(self, new_capacity):
        # Your code here
        # make a new array that is double the current size.
        oldArr = self.buckets
        self.buckets = [None] * new_capacity
        self.capacity = new_capacity
        print(len(self.buckets))
        for i in oldArr:
            if i != None:
                current = i.head
                while current != None:
                    self.put(current.key, current.value)
                    current = current.next
            else:
                continue

        # go through each linked list in the array
        # go through each item and rehash it
        # insert the items into their new locations

    def print_out_hashtable(self):
        for i in self.buckets:
            print(i)


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
    # ht.simp_hash_fn("yodd dyo ma", "black88")

    # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # print(ht.resize(ht.capacity * 2))

    # # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity*2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
    print(ht.get_load_factor())
    ht.print_out_hashtable()
