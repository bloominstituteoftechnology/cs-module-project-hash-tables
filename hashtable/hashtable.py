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
        self.capacity = capacity
        self.table = [[HashTableEntry(x, None)] for x in range(self.capacity)]

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """

        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """

        return len([y
                    for x in self.table
                    for y in x
                    if y.value is not None]) / len(self.table)

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    @staticmethod
    def djb2(key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """

        hsh = 5381

        for character in key:
            hsh = (hsh * 33) + ord(character)

        return hsh

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

        hash_key = self.hash_index(key)

        is_key = False

        hsh = self.table[hash_key]

        for x in range(len(hsh)):
            if key == hsh[x].key:
                is_key = True

        self.table[hash_key] = [HashTableEntry(key, value)]

        # if is_key:
        #     hsh.append(HashTableEntry(key, value))
        #
        # else:
        #     self.table[hash_key] = [HashTableEntry(key, value)]

        # if self.get_load_factor() > .7:
        #     self.resize(self.capacity * 2)
        #
        # if self.get_load_factor() < .2:
        #     self.resize(self.capacity // 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

        hash_key = self.hash_index(key)
        hsh = self.table[hash_key]

        is_key = False

        for x in range(len(hsh)):
            if key == hsh[x].key:
                is_key = True
            if is_key:
                del hsh[x]
                f"Key {key} Deleted"
            else:
                return f"Key {key} Not Found"

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """

        hash_key = self.hash_index(key)

        hsh = self.table[hash_key]

        for x in range(len(hsh)):
            if key == hsh[x].key:
                return hsh[x].value

        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """

        self.capacity = new_capacity
        temp = self.table.copy()

        for x in range(len(temp)):
            y = temp[x]
            for z in y:
                if z.key is str:
                    self.put(z.key, z.value)

        self.table.extend(temp)


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
    new = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
