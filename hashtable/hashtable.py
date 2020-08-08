

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
        # Your code here
        self.storage = [None] * capacity
        self.capacity = capacity if capacity >= 8 else 8
        self.weight = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.storage)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.weight / self.capacity

    # def fnv1(self, key):
    #     """
    #     FNV-1 Hash, 64-bit

    #     Implement this, and/or DJB2.
    #     """

    #     # Your code here
        


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hashNum = 5381
        for x in key:
            hashNum = ( ( hashNum << 5 ) + hashNum ) + ord(x)
        return hashNum & 0xFFFFFFFF



    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        self.weight += 1
        idx = self.hash_index(key)
        if self.storage[idx] is not None:
            cur = self.storage[idx]
            while cur.key != key and cur.next is not None:
                cur = cur.next

            # so either cur.key == key or cur.next is None
            if cur.key == key:
                cur.value = value
                self.weight -= 1
                return
            elif cur.next is None:
                cur.next = HashTableEntry(key, value)
        else:
            self.storage[idx] = HashTableEntry(key, value)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        idx = self.hash_index(key)

        if self.storage[idx] is None: return None

        cur = self.storage[idx]
        prev = None
        while cur is not None:
            if cur.key == key: break
            prev = cur
            cur = cur.next
# if None, no removal necessary
        if cur is None: return None
        if prev is None:
            self.storage[idx] = self.storage[idx].next
        else: 
            prev.next = cur.next
# resize logic
        self.weight -= 1
        if self.get_load_factor() < 0.2:
            newCapacity = self.capacity // 2
            if newCapacity < MIN_CAPACITY:
                newCapacity = MIN_CAPACITY
            self.resize(newCapacity)

# for some reason it returns the value, but it's not properly deleting

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        idx = self.hash_index(key)
        if self.storage[idx] is None: return None

        cur = self.storage[idx]
        while cur is not None and cur.key != key:
            cur = cur.next
        if cur is None: return None
        return cur.value


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        self.capacity = new_capacity if new_capacity >= 8 else 8
        oldStorage = self.storage
        self.storage = [None] * self.capacity
        for i in oldStorage:
            if i is not None:
                self.put(i.key, i.value)




if __name__ == "__main__":
#     ht = HashTable(8)

#     ht.put("line_1", "'Twas brillig, and the slithy toves")
#     ht.put("line_2", "Did gyre and gimble in the wabe:")
#     ht.put("line_3", "All mimsy were the borogoves,")
#     ht.put("line_4", "And the mome raths outgrabe.")
#     ht.put("line_5", '"Beware the Jabberwock, my son!')
#     ht.put("line_6", "The jaws that bite, the claws that catch!")
#     ht.put("line_7", "Beware the Jubjub bird, and shun")
#     ht.put("line_8", 'The frumious Bandersnatch!"')
#     ht.put("line_9", "He took his vorpal sword in hand;")
#     ht.put("line_10", "Long time the manxome foe he sought--")
#     ht.put("line_11", "So rested he by the Tumtum tree")
#     ht.put("line_12", "And stood awhile in thought.")

#     print("")

#     # Test storing beyond capacity
#     for i in range(1, 13):
#         print(ht.get(f"line_{i}"))

#     # Test resizing
#     old_capacity = ht.get_num_slots()
#     ht.resize(ht.capacity * 2)
#     new_capacity = ht.get_num_slots()

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     for i in range(1, 13):
#         print(ht.get(f"line_{i}"))

#     print("")
        ht = HashTable(8)
# 
        ht.put("key-0", "val-0")
        ht.put("key-1", "val-1")
        ht.put("key-2", "val-2")
        ht.put("key-3", "val-3")
        ht.put("key-4", "val-4")
        ht.put("key-5", "val-5")
        ht.put("key-6", "val-6")
        ht.put("key-7", "val-7")
        ht.put("key-8", "val-8")
        ht.put("key-9", "val-9")

        ht.delete("key-7")
        ht.delete("key-6")
        ht.delete("key-5")
        ht.delete("key-4")
        ht.delete("key-3")
        ht.delete("key-2")
        ht.delete("key-1")
        print(ht.delete("key-0"))

        return_value = ht.get("key-0")
        print(return_value)