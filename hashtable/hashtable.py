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
    """

    def __init__(self, capacity):
        # assign self.capacity to capacity
        # set self.size to 0
        # assign self.buckets to an empty array * self.capacity
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * self.capacity

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
        # set initial count to zero
        count = 0
        # for ea item in buckets set cur to item, while current value is none increment count by 1 and set current value pointer to the next value
        for item in self.buckets:
            cur = item
            while cur != None:
                count += 1
                cur = cur.next
        # if count/self.capacity is > 0.7 then call resize method and multiply original capacity by 2, doubling it in size.
        if count/self.capacity > 0.7:
            self.resize(self.capacity * 2)
        # else if count/self.capacity is < 0.2 and if capacity/2 is less than 8, resize to original size of 8.
        elif count/self.capacity < 0.2:
            if self.capacity/2 < 8:
                self.resize(8)
            # else call resize with self.capacity/2 to shrink the hash table
            else:
                self.resize(self.capacity/2)
        # otherwise return current count/capacity to get new size.
        return count/self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        pass

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # hashing function
        hash = 5381
        for x in key:
            hash = ((hash << 5) + 5) + ord(x)
        return hash & 0xFFFFFFFF

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
        # assign slot to a variable calling hash_index method and passing in key.
        # increment self.size by 1
        # assign each self.buckets[slot] to HashTableEntry class passing in key and value
        if self.buckets[self.hash_index(key)] != None:
            cur = self.buckets[self.hash_index(key)]
            while cur.next != None and cur.key != key:
                cur = cur.next
            if cur.key == key:
                cur.value = value
            else:
                cur.next = HashTableEntry(key, value)
        else:
            self.buckets[self.hash_index(key)] = HashTableEntry(key, value)
        self.get_load_factor()

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        prev = None
        cur = self.buckets[self.hash_index(key)]
        if cur != None:
            while cur.key != key and cur != None:
                prev = cur
                cur = cur.next
            if cur.key == key:
                if prev != None:
                    prev.next = cur.next
                else:
                    self.buckets[self.hash_index(key)] = cur.next
            else:
                print('Not found')
        else:
            print("Item not found")
        self.get_load_factor()

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        cur = self.buckets[self.hash_index(key)]
        if cur != None:
            while cur.key != key and cur.next != None:
                cur = cur.next
            if cur.key == key:
                return cur.value
            else:
                return None
        else:
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        new_bucket = [None] * int(new_capacity)
        for item in self.buckets:
            current = item
            while current != None:
                if new_bucket[self.hash_index(current.key)] != None:
                    cur = new_bucket[self.hash_index(current.key)]
                    while cur.next != None and cur.key != current.key:
                        cur = cur.next
                    if cur.key == current.key:
                        cur.value = current.value
                    else:
                        cur.next = HashTableEntry(current.key, current.value)
                else:
                    new_bucket[self.hash_index(current.key)] = HashTableEntry(
                        current.key, current.value)
                current = current.next
        self.bucket = new_bucket


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
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
